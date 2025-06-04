FROM python:3.13.3-slim
LABEL authors="shyin.lim"

RUN apt-get update && apt-get install -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY .. /app
WORKDIR /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

ENV TZ=Asia/Taipei