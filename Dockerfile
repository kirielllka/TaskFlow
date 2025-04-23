FROM python:3.11-buster

RUN adduser --disabled-password taskflow-user



WORKDIR /TaskFlow

COPY requirements.txt .
RUN apt-get update && \
    apt install -y python3-dev
RUN pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt || cat requirements.txt

COPY TaskFlow /TaskFlow

ENV PYTHONPATH=/TaskFlow

EXPOSE 8000

USER taskflow-user