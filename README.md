# Mycelial Adapter Network - Proof of Concept

Companion code for the white paper **"The End of AI Rent-Seeking: How Regular Companies Are Building Sovereign AI Empires"**.

## Features
- Working distributed grafting between two nodes
- 4-bit quantized models (Llama-3.2-1B)
- Correct orthogonal SVD projection + low-rank recomposition
- Differential privacy on grafts
- Base64 serialization for network transmission
- Safe PEFT handling for 4-bit models

## Quick Start

1. `pip install -r requirements.txt`
2. `huggingface-cli login` (for Llama models)
3. Terminal 1: `uvicorn server_a:app --port 8000 --reload`
4. Terminal 2: `uvicorn server_b:app --port 8001 --reload`
5. Terminal 3: `python main.py`

## Notes
- Org A proposes grafts
- Org B accepts and merges them
- Ready for extension to Ray, Celery, or full gRPC

## Docker Deployment

```bash
docker compose up --build

## Quick Start
scr
### Option 1: Using the startup ipt (Recommended)

```bash
chmod +x start.sh
./start.sh

This is a living proof-of-concept for the Mycelial Adapter Network described in the paper.
