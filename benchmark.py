import time
import torch
import numpy as np
import requests
from datetime import datetime

print("=== Mycelial Adapter Network - Benchmark Suite ===\n")

def run_benchmark(rounds: int = 10):
    results = {
        "timestamp": datetime.now().isoformat(),
        "rounds": rounds,
        "graft_times": [],
        "privacy_times": [],
        "svd_times": [],
        "total_times": []
    }

    for i in range(rounds):
        print(f"Round {i+1}/{rounds}")
        start_total = time.perf_counter()

        # 1. Propose graft from Org A
        t0 = time.perf_counter()
        proposal = requests.post("http://127.0.0.1:8000/propose_graft").json()
        graft_time = time.perf_counter() - t0
        results["graft_times"].append(graft_time)

        # 2. Accept graft on Org B
        t1 = time.perf_counter()
        result = requests.post("http://127.0.0.1:8001/accept_graft", json=proposal)
        total_time = time.perf_counter() - start_total
        results["total_times"].append(total_time)

        print(f"  Graft proposal: {graft_time:.4f}s | Total round: {total_time:.4f}s")

    # Summary
    print("\n=== BENCHMARK RESULTS ===")
    print(f"Average graft proposal time : {np.mean(results['graft_times']):.4f}s")
    print(f"Average full round time     : {np.mean(results['total_times']):.4f}s")
    print(f"Security Overhead Tax (est) : {np.mean(results['total_times']) * 100 / 0.85 - 100:.1f}% (based on baseline)")

    # Save results
    import json
    with open("benchmark_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Results saved to benchmark_results.json")

if __name__ == "__main__":
    run_benchmark(rounds=20)
