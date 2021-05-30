import psycopg2
from psycopg2 import Error
from request import  order
import datetime as dt
from datetime import datetime, date

def get_footprint_from_db(imageid):
    try:
        conn = psycopg2.connect(user="plandata", password="sejl44skib", host="localhost", port="5432", database="plandata")
        cursor = conn.cursor()
        select_query =f"SELECT imageid, btrim(st_astext(wkb_geometry),'POLYGON()'), cameraid, coneid, direction, centroid_t FROM footprints.footprints WHERE imageid = '{imageid}';"
        cursor.execute(select_query)
        data = cursor.fetchone()
        return data
    except(Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


def get_camera_width_height(cameraid, coneid):
    try:
        conn = psycopg2.connect(user="plandata", password="sejl44skib", host="localhost", port="5432", database="plandata")
        cursor = conn.cursor()
        select_query =f"SELECT imagewidth, imageheight FROM footprints.camera WHERE coneid = '{coneid}' AND camid = '{cameraid}'; " 
        cursor.execute(select_query)
        data = cursor.fetchone()
        width, height = data[0], data[1]
        return width, height
    except(Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(conn):
            conn.commit()
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

def create_order(order):
    created_on = dt.datetime.now()
    location = order.location
    email = order.email
    created_on = str(created_on)
    try:
        conn = psycopg2.connect(user="plandata", password="sejl44skib", host="localhost", port="5432", database="plandata")
        cursor = conn.cursor()
        insert_query =f"INSERT INTO footprints.orders (location, created_on, requester_email) VALUES ('{location}', '{created_on}', '{email}') RETURNING order_id;"
        cursor.execute(insert_query)
        order_id = cursor.fetchone()
        conn.commit()
        order.orderID = order_id[0]
    except(Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")    

def update_order(order):
    orderid = order.orderID
    image_directory = order.image_directory
    finished = str(dt.datetime.now())
   # images_directory = images_directory   
    try:
        conn = psycopg2.connect(user="plandata", password="sejl44skib", host="localhost", port="5432", database="plandata")
        cursor = conn.cursor()
        update_query =f"UPDATE footprints.orders SET image_directory = '{image_directory}', finished = '{finished}' WHERE order_id = {orderid};"
        cursor.execute(update_query)
        conn.commit()
    except(Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")    


 
