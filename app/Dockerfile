FROM python:3.5

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE "8000:8000"

CMD gunicorn -c gunicorn.conf.py app:app
