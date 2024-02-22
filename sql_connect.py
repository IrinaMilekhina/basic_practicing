"""
Необходимо установить Docker
Запустить его
Затем через терминал скачать образ с PostgreSQL и запустить контейнер:
https://hub.docker.com/_/postgres
Создать БД

установить библиотеку SQLAlchemy
https://docs.sqlalchemy.org/en/20/intro.html#installation
установить библиотеку psycopg2

В файле уже есть код подключения к БД
Необходимо записать данные в базу
"""
from sqlalchemy import create_engine
import psycopg2
conn_string = "host='0.0.0.0' port='5432' dbname='postgres' user='postgres' password='pss1234'"
conn = psycopg2.connect(conn_string)

engine = create_engine('postgresql+psycopg2://postgres:pss1234@127.0.0.1:5432/test')

print()
