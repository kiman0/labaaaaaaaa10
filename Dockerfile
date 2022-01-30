FROM python:3.9.5-slim-buster

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app/

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "app:app" ]