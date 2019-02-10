FROM python:3.7-slim
RUN apt update && apt install -y \
    python3-dev \
    python3-pip \
    curl
COPY ./requirements.txt /usr/local/src/app/
RUN pip3 install -r /usr/local/src/app/requirements.txt
COPY . /usr/local/src/app/
WORKDIR /usr/local/src/app/