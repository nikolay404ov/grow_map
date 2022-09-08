FROM python:3.8.5

WORKDIR /usr/app

RUN pip install --upgrade pip --no-cache-dir
RUN apt-get update && apt-get -y dist-upgrade

COPY ./src .
RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornH11Worker main:app