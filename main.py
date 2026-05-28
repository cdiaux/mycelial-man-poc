import requests

print("=== Mycelial Adapter Network - Distributed Test ===\n")

proposal = requests.post("http://127.0.0.1:8000/propose_graft").json()
result = requests.post("http://127.0.0.1:8001/accept_graft", json=proposal)
print("Graft result from Org B:", result.json())
