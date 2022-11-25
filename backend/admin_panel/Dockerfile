FROM python:3.9

WORKDIR /code

COPY ./src/requirements.txt ./
RUN python3 -m pip install --upgrade pip \
    && pip3 install -r /code/requirements.txt --no-cache-dir
#COPY ./src .
#RUN python manage.py migrate --noinput

CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000