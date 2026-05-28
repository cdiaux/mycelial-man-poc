import base64
from fastapi import FastAPI
from config import Config
from manifold import MycelialManifold
from privacy import DifferentialPrivacyEngine
from proposal import GraftProposal
from encryption import PayloadEncryptor
from transformers import AutoModelForCausalLM
import uvicorn
import time

app = FastAPI(title="Mycelial Node - Org A")

config = Config()
base_model = AutoModelForCausalLM.from_pretrained(
    config.model_id, 
    load_in_4bit=config.load_in_4bit, 
    device_map="auto"
)
manifold = MycelialManifold(base_model, config)
dp = DifferentialPrivacyEngine()
encryptor = PayloadEncryptor()   # New

manifold.add_adapter("Org_A")

@app.post("/propose_graft")
def propose_graft():
    layer_target = "model.layers.0.self_attn.q_proj"
    
    raw_delta = manifold.get_lora_delta("Org_A", layer_target)
    privatized = dp.privatize(raw_delta)
    
    # ENCRYPT the tensor before sending
    encrypted_b64 = encryptor.encrypt(privatized.cpu().numpy().tobytes())
    
    proposal = GraftProposal(
        source_org="Org_A",
        target_org="Org_B",
        layer_name=layer_target,
        delta_b64=encrypted_b64,
        shape=list(privatized.shape),
        surprise_score=0.08,
        privacy_cost=dp.epsilon,
        graft_id=f"graft_{int(time.time())}"
    )
    return proposal.to_dict()
