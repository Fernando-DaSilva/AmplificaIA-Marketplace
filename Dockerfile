# Multi-stage lightweight Python Dockerfile for AmplificaIA Marketplace Prototype
FROM python:3.12-slim

WORKDIR /app

# Prevent Python from writing pyc files to disk and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install curl for healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose port 8050
EXPOSE 8050

# Run application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8050"]
