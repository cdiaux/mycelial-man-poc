#!/bin/bash

echo "=== Starting Mycelial Adapter Network ==="

# Start Org A in background
echo "Starting Org A on port 8000..."
uvicorn server_a:app --host 0.0.0.0 --port 8000 --reload &

# Start Org B in background
echo "Starting Org B on port 8001..."
uvicorn server_b:app --host 0.0.0.0 --port 8001 --reload &

# Wait a moment for servers to start
sleep 3

echo "Running test client..."
python main.py

echo ""
echo "Both nodes are running."
echo "Org A: http://localhost:8000"
echo "Org B: http://localhost:8001"
echo "Press Ctrl+C to stop all servers."
