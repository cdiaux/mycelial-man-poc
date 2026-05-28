import torch
import base64
import numpy as np
from peft import LoraConfig, get_peft_model, PeftModel
from typing import Dict
from .proposal import GraftProposal

class MycelialManifold:
    def __init__(self, base_model, config):
        self.base_model = base_model
        self.rank = config.lora_rank
        self.alpha = config.lora_alpha
        self.scaling = self.alpha / self.rank
        self.adapters: Dict[str, PeftModel] = {}
        self.config = config

    def add_adapter(self, org_id: str):
        config = LoraConfig(
            r=self.rank,
            lora_alpha=self.alpha,
            target_modules=self.config.target_modules,
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM"
        )
        self.adapters[org_id] = get_peft_model(self.base_model, config)
        print(f"[Manifold] Created adapter for {org_id}")

    def get_lora_delta(self, org_id: str, layer_name: str) -> torch.Tensor:
        model = self.adapters[org_id]
        for name, module in model.named_modules():
            if layer_name in name and hasattr(module, "lora_B"):
                B = module.lora_B.default.weight.data
                A = module.lora_A.default.weight.data
                return (B @ A) * self.scaling
        raise ValueError(f"LoRA module {layer_name} not found in {org_id}")

    def low_rank_recompose(self, full_delta: torch.Tensor) -> tuple:
        """SVD → truncate to rank r → return B' and A'"""
        U, S, Vh = torch.linalg.svd(full_delta.float(), full_matrices=False)
        
        U_r = U[:, :self.rank]
        S_r = S[:self.rank]
        Vh_r = Vh[:self.rank, :]

        S_sqrt = torch.diag(S_r.sqrt())

        B_new = U_r @ S_sqrt
        A_new = S_sqrt @ Vh_r
        return B_new, A_new

    def accept_graft(self, proposal: GraftProposal) -> bool:
        if proposal.target_org not in self.adapters:
            return False

        target_model = self.adapters[proposal.target_org]

        # Decode Base64
        raw_bytes = base64.b64decode(proposal.delta_b64)
        flat = np.frombuffer(raw_bytes, dtype=np.float32)
        delta_tensor = torch.from_numpy(flat).reshape(proposal.shape)

        B_new, A_new = self.low_rank_recompose(delta_tensor)

        temp_name = f"graft_{proposal.graft_id}"
        target_module = proposal.layer_name.split('.')[-1]

        target_model.add_adapter(temp_name, LoraConfig(
            r=self.rank,
            lora_alpha=self.alpha,
            target_modules=[target_module],
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM"
        ))

        # Inject weights
        with torch.no_grad():
            for name, param in target_model.named_parameters():
                if temp_name in name:
                    if "lora_B" in name:
                        param.copy_(B_new)
                    elif "lora_A" in name:
                        param.copy_(A_new)

        # For 4-bit safety, use set_adapter instead of merging
        target_model.set_adapter(temp_name)

        print(f"[GRAFT SUCCESS] {proposal.source_org} → {proposal.target_org} | Layer: {proposal.layer_name}")
        return True
