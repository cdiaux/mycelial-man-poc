FROM pytorch/pytorch:2.4.0-cuda12.4-cudnn9-runtime

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose ports for both nodes
EXPOSE 8000 8001

# Default command (will be overridden in docker-compose)
CMD ["uvicorn", "server_a:app", "--host", "0.0.0.0", "--port", "8000"]
