FROM python:2.7

ADD ./src /src

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE "8000:8000"

CMD gunicorn -c gunicorn.conf.py app:app
