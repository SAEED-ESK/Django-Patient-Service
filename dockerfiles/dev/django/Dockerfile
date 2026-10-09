FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip install debugpy

COPY ./core /app