#!/bin/bash
echo "Stopping all Mycelial servers..."
pkill -f "uvicorn server_a" || true
pkill -f "uvicorn server_b" || true
echo "Servers stopped."
