# Dockerfile.prod

FROM tiangolo/uvicorn-gunicorn:python3.8-slim

WORKDIR /app/

RUN apt-get update && apt-get install -y netcat

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
