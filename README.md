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

2. Hugging Face Login (for Llama models)bash

huggingface-cli login

3. Run the Network (Recommended)bash

chmod +x start.sh
./start.sh

4. Run Benchmarkbash

python benchmark.py

Manual Startbash

# Terminal 1 - Org A
uvicorn server_a:app --port 8000 --reload

# Terminal 2 - Org B
uvicorn server_b:app --port 8001 --reload

# Terminal 3 - Test
python main.py

Docker Deploymentbash

docker compose up --build

Repository StructureFile
Purpose
server_a.py
Org A (graft proposer)
server_b.py
Org B (graft receiver)
manifold.py
Core grafting + SVD logic
privacy.py
Differential Privacy Engine
proposal.py
Serializable GraftProposal
benchmark.py
Measures Security Overhead Tax
start.sh
Easy startup script
docker-compose.yml
Multi-container deployment

SecuritySee `SECURITY.md` (SECURITY.md) for reporting vulnerabilities.Important Notes:This is a proof-of-concept. Do not use in production without additional hardening.
AES encryption key is generated at runtime (for demo). In production, use a shared secret or secrets manager.
4-bit models use safe adapter switching to avoid quantization issues.

Benchmark ResultsRunning benchmark.py will generate benchmark_results.json with real measurements of:Graft proposal latency
Full round-trip time
Estimated Security Overhead Tax

CitationIf you use this code in research or a project, please cite the white paper:Weaver, M. (2026). The End of AI Rent-Seeking: How Regular Companies Are Building Sovereign AI Empires.

LicenseMIT License — see `LICENSE` (LICENSE) file.

---

**Copy and paste the entire content above into your `README.md` file.**

This version is clean, well-structured, professional, and ready for public release.

Would you like me to also generate the final `SECURITY.md`, `.gitignore`, or a sample launch announcement post for X?

