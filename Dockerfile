FROM python:3

RUN pip install pipenv

WORKDIR /opt/local

ENTRYPOINT ./bootstrap.sh