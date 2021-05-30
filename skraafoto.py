import os
import psycopg2
from shapely import wkb
from psycopg2 import Error
import re
from shapely.geometry import Polygon
from pyproj import Proj, transform
import pyproj
from PIL import Image


import cv2
import numpy as np
import math
#from google.colab.patches import cv2_imshow


conn = psycopg2.connect(user="plandata", password="sejl44skib", host="localhost", port="5432", database="plandata")
def get_coords_of_image(imageid):
    try:
        conn = psycopg2.connect(user="plandata", password="sejl44skib", host="localhost", port="5432", database="plandata")
        cursor = conn.cursor()
        select_query =f"SELECT imageid, northing, easting, height, btrim(st_astext(wkb_geometry),'POLYGON()'), cameraid, coneid, direction FROM footprints.footprints WHERE imageid = '{imageid}';"
        cursor.execute(select_query)
        x = cursor.fetchone()
        points = x[4]
        points = points.split(',')
        print(x)
        return points
    except(Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


def get_lon_lat(coords):
    list_of_coords = []
    lst_coords_in_pairs = coords.split(",")
    for a in lst_coords_in_pairs:
        try:
            split_pairs = a.split()
            x,y = int(split_pairs[0]),int(split_pairs[1])
            p = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')
            lon_lat_coord = p(x,y,inverse=True)
            list_of_coords.append(lon_lat_coord)
        except Exception as err:
            print('Could not convert string-grids to lat and lon', err)
    return list_of_coords

def convert_lon_lat_to_grid(lon, lat):
    grid = []
    p = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')
    lon_lat_coord=p(lon, lat, inverse=False)
    grid.append(lon_lat_coord)
    return grid;

def convert_wkb_to_lat_lon(imgid):
    sql = f"SELECT btrim(st_astext(wkb_geometry),'POLYGON()') from footprints.footprints where imageid like '{imgid}';"
    cursor = conn.cursor()
    cursor.execute(sql)
    list_geom = []
    result = cursor.fetchone()
    for grid_coords in result:
        #print(grid_coords)
        lat_lon_coords = get_lon_lat(grid_coords)
        list_geom.append(lat_lon_coords)
    return list_geom   

def split_x_y(point):
    split_coords = point.split(' ')
    xCoords = int(split_coords[0])
    yCoords = int(split_coords[1])
    return xCoords, yCoords    

def get_distance_between_polygon_corners(maxPoint, minPoint):
    print(maxPoint)
    print(minPoint)
    distance = maxPoint-minPoint
    return abs(distance)

def distance_to_my_point(polygon_point,my_point):
    distance = polygon_point-my_point
    return abs(distance)        
    

def get_distance_to_point_in_percent(imageBbox, point):
    Ax, Ay = split_x_y(imageBbox[0])
    Bx, By = split_x_y(imageBbox[1])
    Cx, Cy = split_x_y(imageBbox[2])
    Px, Py = point[0][0], point[0][1]
    #print(Ax, Ay, Bx, By, Cx, Cy)

    absAB = 1062 #get_distance_between_polygon_corners(By,Ay)
    absCB = get_distance_between_polygon_corners(Cx,Bx)
    absAP = distance_to_my_point(Ay, Py)
    absCP = distance_to_my_point(Cx, Px)
    print('absAB', absAB)
    print('absCB', absCB)
    CP_CB_percent = (1050.692/1052)*100
    AP_AB_percent = (924.500/1062)*100
    print(AP_AB_percent, CP_CB_percent)
    return AP_AB_percent, CP_CB_percent    

def get_image_pixels(img_path):
    with Image.open(img_path) as img:
       width, height = img.size
    print((width/height))
    return width, height

def colour_spot(imageSize, pointDistance, image_path):
    imageWidth = imageSize[0]
    imageHeight = imageSize[1]
    AP_AB = pointDistance[0]
    CP_CB = pointDistance[1]
    y = 6690# math.trunc((imageHeight*AP_AB)/100)
    x = 1997# math.trunc((imageWidth*CP_CB)/100)
    print(x,y)
    image=cv2.imread(f"{image_path}", 1)
   #image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
   #mage = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
    image[y:y+100, x:x+100] = (255,0,0)    
    cv2.imwrite('new_img.jpg', image) 

    return y,x 

## TODO
    ## Set the Coordinates for image bbox into an array so that i can call the X and Y values individually.
    ## Calculate the difference between my given point and the A and C point
    ## Calculate that differnece in %
    ## Move that many pixels in the picture from x,y == 0,0, then paint pixel. 



   

image = '2019_84_41_3_0021_00007489'
img_path =f'../temp/tempdisc/1km_6175_711/{image}.jpg'
points = get_coords_of_image(image)
#p = convert_wkb_to_lat_lon(image)
#g = convert_lon_lat_to_grid(12.36471, 55.67860)
#print('grid', g)
#lol = get_distance_to_point_in_percent(points, g)
#imgsize = get_image_pixels(img_path)
#print('img1',imgsize)
#print(imgsize, lol)
#print(colour_spot(imgsize, lol, img_path))

def calculate(x,y,z):
    a = (10300/7700)
    f = math.atan((19/2))
    Zfar = 2384.0
    Znear = 0.1
    q = (Zfar/(Zfar-Znear))
    newx = (a*f*x)/z
    newy = (f*y)/z
    newz = (z*q) - (Znear*q)
    print(newx, newy, newz)  


x = 711543 - 711118
y = 0 - 1557
z = 6175441 - 6177247

print(x,y,z)
calculate(x,y,z)
