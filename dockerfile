FROM python:3.8

COPY . /app
WORKDIR /app
#RUN pip install --no-cache-dir pipenv==2018.11.26
RUN pip install --no-cache-dir pipenv

RUN pip install gunicorn flask
RUN pip install Flask-WTF

RUN pipenv install --system

# for heroku
ENV FLASK_RUN_PORT=$PORT

ENV FLASK_APP app.py
CMD ["flask", "run", "--host=0.0.0.0"]
