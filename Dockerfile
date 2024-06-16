FROM python:3.6-slim

RUN mkdir -p /opt/calc

WORKDIR /opt/calc

COPY requires ./
RUN pip install --upgrade pip && pip install --default-timeout=100 -r requires
