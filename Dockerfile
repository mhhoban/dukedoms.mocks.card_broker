FROM python:3.6.5-alpine3.7
RUN apk add --no-cache bash
RUN apk add --no-cache build-base
RUN apk add --no-cache postgresql-dev


COPY requirements.txt /

RUN pip3 install -r /requirements.txt

ARG service
COPY $service/ /$service

ARG service
WORKDIR /$service


CMD ["gunicorn", "main:application", "-b", "0.0.0.0:8080"]
