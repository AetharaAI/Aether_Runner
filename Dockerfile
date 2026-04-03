FROM python:3.11-slim

ARG INSTALL_INFERENCE=false

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements-inference.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN if [ "$INSTALL_INFERENCE" = "true" ]; then pip install --no-cache-dir -r requirements-inference.txt; fi

COPY . .

EXPOSE 8010

CMD ["uvicorn", "aether_runner.main:app", "--host", "0.0.0.0", "--port", "8010"]
