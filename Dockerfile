FROM python:3.11.5

ENV PYTHONUNBUFFERED 1

RUN mkdir code

COPY . /code/

WORKDIR /code

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean


RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY requirements.txt /code/
