from fastapi import FastAPI
from manifold import MycelialManifold
from config import Config
from proposal import GraftProposal
from encryption import PayloadEncryptor
from transformers import AutoModelForCausalLM
import uvicorn

app = FastAPI(title="Mycelial Node - Org B")

config = Config()
base_model = AutoModelForCausalLM.from_pretrained(
    config.model_id, 
    load_in_4bit=config.load_in_4bit, 
    device_map="auto"
)
manifold = MycelialManifold(base_model, config)
manifold.add_adapter("Org_B")

encryptor = PayloadEncryptor()   # Must use same key as Org A in real deployment

@app.post("/accept_graft")
def accept_graft(proposal_dict: dict):
    proposal = GraftProposal(**proposal_dict)
    
    # DECRYPT the tensor
    decrypted_bytes = encryptor.decrypt(proposal.delta_b64)
    # Reconstruct tensor
    flat = np.frombuffer(decrypted_bytes, dtype=np.float32)
    proposal.delta = torch.from_numpy(flat).reshape(proposal.shape)  # Temporary for acceptance

    success = manifold.accept_graft(proposal)
    return {"accepted": success, "org": "Org_B"}
