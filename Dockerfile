
FROM python:3.11-slim

WORKDIR /app_core

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY app_core.py .


CMD ["python", "run", "app_core.py"]
