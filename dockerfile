FROM python:3.6-slim

COPY . /root
WORKDIR /root

RUN pip install --no-cache-dir pipenv
RUN pipenv install --system

ENV FLASK_APP start.py
CMD ["flask", "run", "--host=0.0.0.0"]
