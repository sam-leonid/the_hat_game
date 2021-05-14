FROM python:3.6-slim

COPY . /root
WORKDIR /root


# RUN pip install -U pip && pip install --upgrade setuptools && pip install catboost==0.24.2
# RUN pip install -U nltk
# RUN pip install Flask-WTF
# RUN pip install pickle-mixin
# RUN pip install flask gunicorn numpy sklearn

RUN pip install pipenv
RUN pipenv install --system
RUN python -m nltk.downloader -d /usr/share/nltk_data all

# COPY Pipfile* /tmp/
# RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
# RUN pip install -r /tmp/requirements.txt
