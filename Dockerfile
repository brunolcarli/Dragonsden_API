FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV NAME=dragonsden

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y \
        gcc \
        make \
        python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir --upgrade pip wheel && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . /app/
