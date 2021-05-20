FROM python:3.6-slim

COPY . /root
WORKDIR /root

RUN pip install pipenv
RUN pipenv install --system
