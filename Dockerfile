FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    libatlas-base-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV SYNTHETIC_IMAGES_DIR="/app/ml/v1/datasets/synthetic_images"
ENV SYNTHETIC_LABELS_PATH="/app/ml/v1/datasets"
ENV MODEL_DIR='/app/ml/v1/h5'
ENV MODEL_NAME="text-recognize-model.h5"
ENV VERSION=v1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]
