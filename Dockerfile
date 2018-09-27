FROM python:3.7.0-slim-stretch

LABEL maintainer='James Hibbard'

COPY . /app

RUN pip install /app \
    && rm -rf /var/lib/apt/lists/*
