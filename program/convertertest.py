from pyproj import Proj, transform
import pyproj
import DBfacade as DBF
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import psycopg2
from psycopg2 import Error
import cv2
import numpy as np

import os

from request import order
import DBfacade as DBF

def get_image_list(location):
    images = ['2019_84_41_3_0021_00007488']
    return images

def get_footprint_from_DB(imageid):
    result = DBF.get_footprint_from_db(imageid)
    return result

def homo_to_eucli(coords):
    if coords[2] == 0: return none, none
    return coords[0]/coords[2], coords[1]/coords[2]

def mk_point(x,y):
    return np.array([x, y, 1], dtype='float32')


def get_image_width_height(cameraid, coneid):

    width, height = DBF.get_camera_width_height(cameraid, coneid)
    return width, height


def split_x_y(point):
    split_coords = point.split(' ')
    xCoords = int(split_coords[0])
    yCoords = int(split_coords[1])
    return xCoords, yCoords

def create_polygon_array(polygon):
    polygon = polygon.split(',')
    Ax, Ay = split_x_y(polygon[0])
    Bx, By = split_x_y(polygon[1])
    Cx, Cy = split_x_y(polygon[2])
    Dx, Dy = split_x_y(polygon[3])
    return Polygon([(Ax, Ay),(Bx, By),(Cx, Cy),(Dx, Dy),(Ax, Ay)])

def create_array(polygon):
    polygon = polygon.split(',')
    Ax, Ay = split_x_y(polygon[0])
    Bx, By = split_x_y(polygon[1])
    Cx, Cy = split_x_y(polygon[2])
    Dx, Dy = split_x_y(polygon[3])
    return np.array([[Ax, Ay],[Bx, By],[Cx, Cy],[Dx, Dy]], dtype='float32')


def convert_lon_lat_to_grid(point):
    lon, lat = point[0],point[1]
    grid = []
    p = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')
    lon_lat_coord=p(lon, lat, inverse=False)
    grid.append(lon_lat_coord)
    return grid;


#def run_imagecutcontroller(location, email):
    location = np.array([[location[0]], [location[1]]])
    footprints = [];
    images = get_image_list(location)
    for imageid in images:
        footprint = DBF.get_footprint_from_db(imageid)
        footprints.append(footprint)
       
    valid_images = get_images_for_point(location, footprints)
    find_point_on_image(valid_images,location)
      

def find_point_on_image(images,location):
    point = mk_point(location[0][0], location[1][0])
    for image in images:
        direction = image[4]
        corners = image[1]
        poly = create_array(corners)
        src = poly

        if direction == 'N':
            if image[3] == '504':
            # 504, N
                src = np.array([[poly[1]],[poly[2]],[poly[0]],[poly[3]]])
            if image[3] == '505':
            # 505, N
                src = np.array([[poly[3]],[poly[0]],[poly[2]],[poly[1]]])
        if direction == 'S':
            if image[3] == '504':
            # 504, S
                src = np.array([[poly[1]],[poly[2]],[poly[0]],[poly[3]]])
            if image[3] == '505':
            # 505, S
                src = np.array([[poly[3]],[poly[0]],[poly[2]],[poly[1]]])
        if direction == 'E':
            # 503, E
            if image[3] == '503':
                src = np.array([[poly[2]],[poly[3]],[poly[1]],[poly[0]]])
        if direction == 'W':
            # 503, W
            if image[3] == '502':
                src = np.array([[poly[0]],[poly[1]],[poly[3]],[poly[2]]])
        if direction == 'T':
            # 501, T
            if image[3] == '501':
                src = np.array([[poly[3]],[poly[0]],[poly[2]],[poly[1]]])

        #width, height = get_image_width_height(image[2], image[3])
        dst = np.array([[0,0],[(width-1),0],[0,(height-1)],[(width-1),(height-1)]], dtype='float32')
       
        #M= cv2.getPerspectiveTransform(src, dst)
        Minv = cv2.getPerspectiveTransform(dst, src)  
        result = homo_to_eucli(Minv.dot(point))
        print(result)
        #Minv = cv2.getPerspectivetransform(dst, src)
        #result = homo_to_eucli(Minv(Minv.dot(px)
        


def check_if_point_in_polygon(location, polygon):
    point = Point(location[0][0], location[1][0])
    return polygon.contains(point)



def get_images_for_point(location, images):
    imagedata = []
    for image in images:
        temp = image
        footprintPoly = create_polygon_array(temp[1])
        is_valid = True#check_if_point_in_polygon(location, footprintPoly)
        print(is_valid)
        if is_valid == True:
            imagedata.append(temp)
    return imagedata





point= [12.3637,55.6676]
point1 = [12.3582,55.6779]
point2 = [12.3522,55.6786]
point3 = [12.3540,55.6808]
point4 = [12.3602,55.6817]
point5 = [12.3647,55.6804]
point6 = [12.3646,55.6839]
point7 = [12.3592,55.6837]
point8 = [12.3529,55.6845]

points = []
points.append(point)
points.append(point1)
points.append(point2)
points.append(point3)
points.append(point4)
points.append(point5)
points.append(point6)
points.append(point7)
points.append(point8)

pp = [1095,885]
pp2 = [1476,4996]
pp3 = [1848,8776]
pp4 = [3617,7946]
pp5 = [4499,3745]
pp6 = [3500,703]
pp7 = [6781,373]
pp8 = [6425,4457]
pp9 = [7130,9409]


for p in points:
    res = convert_lon_lat_to_grid(p)
    print(res) 

run_imagecutcontroller(pp, 'asdas@')
run_imagecutcontroller(pp2, ' ')
run_imagecutcontroller(pp3, ' ')
run_imagecutcontroller(pp4, ' ')
run_imagecutcontroller(pp5, ' ')
run_imagecutcontroller(pp6, ' ')
run_imagecutcontroller(pp7, ' ')
run_imagecutcontroller(pp8, ' ')
run_imagecutcontroller(pp9, ' ')    
