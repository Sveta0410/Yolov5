FROM python:3.8

RUN mkdir /app/

ADD app_db.py /app/

RUN pip install psycopg2

WORKDIR /app/

CMD ["python", "app_db.py"]