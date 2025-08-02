# -*- coding: utf-8 -*-
import psycopg2


def read_connection() -> dict:
    """Чтение данных из конфигурационного файла для подключения к базе данных."""
    config = dict()
    with open('connections.config') as file:
        for line in file:
            info = line[:-1].split('=')
            config[info[0]] = info[1]
    return config


conn_string = read_connection()
conn = psycopg2.connect(dbname=conn_string['dbname'],
                 host=conn_string['host'],
                 port=int(conn_string['port']),
                 user=conn_string['user'],
                 password=conn_string['password'])
with conn.cursor() as cursor:
    print('Подключение установлено')

print(cursor.closed)
print(conn.closed)
conn.close()
print(conn.closed)
