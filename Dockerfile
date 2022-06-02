# syntax=docker/dockerfile:1
FROM python:3.9-alpine AS base
RUN apk update

FROM base AS python-env
ENV PYTHONPATH=$PYTHONPATH:/src
WORKDIR /mnt
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM python-env
WORKDIR /mnt
EXPOSE 9090



