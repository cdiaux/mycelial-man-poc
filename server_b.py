from fastapi import FastAPI
from manifold import MycelialManifold
from config import Config
from proposal import GraftProposal
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

@app.post("/accept_graft")
def accept_graft(proposal_dict: dict):
    proposal = GraftProposal(**proposal_dict)
    success = manifold.accept_graft(proposal)
    return {"accepted": success, "org": "Org_B"}
