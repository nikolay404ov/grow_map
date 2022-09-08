FROM python:3.8.5

WORKDIR /usr/app

RUN pip install --upgrade pip --no-cache-dir
RUN apt-get update && apt-get -y dist-upgrade

COPY ./tests/requirements.txt ./

RUN pip install -r requirements.txt

CMD python -m pytest -vv ./
