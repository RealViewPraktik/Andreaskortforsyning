import psycopg2
from psycopg2 import Error


def create_order_and_camera_table():
    try:
        conn = psycopg2.connect(user="plandata", password="sejl44skib", host="localhost", port="5432", database="plandata")
        cursor = conn.cursor()
        query = open("/home/plandata/Andreas/program/sql/createdb.sql").read()
        cursor.execute(query)
        conn.commit()
        print('Tables Created')
    except(Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(conn):
            cursor.close()


create_order_and_camera_table()
