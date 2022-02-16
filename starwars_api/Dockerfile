FROM python:3.10-alpine

RUN apk update && apk add python3-dev gcc libc-dev
# RUN apt-get update && apt-get install gcc -y && apt install -y build-essential libpq-dev

RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system

COPY . .

RUN pip install -e .
