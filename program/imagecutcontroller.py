from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import psycopg2
from psycopg2 import Error
import cv2
import numpy as np
import kafkamailproducer as kmp

import os

from request import order 
import DBfacade as DBF

def get_image_list(location):
    images = ['2019_84_40_5_0001_00005767', '2019_84_40_5_0001_00005768','2019_84_40_5_0001_00005769', '2019_84_41_1_0021_00007492', '2019_84_41_1_0021_00007493', '2019_84_41_1_0021_00007494', '2019_84_41_1_0022_00007195', '2019_84_41_1_0022_00007196', '2019_84_41_1_0022_00007197', '2019_84_41_2_0021_00007497', '2019_84_41_2_0021_00007498','2019_84_41_2_0021_00007499', '2019_84_41_2_0022_00007190', '2019_84_41_2_0022_00007191', '2019_84_41_2_0022_00007192', '2019_84_41_3_0021_00007487', '2019_84_41_3_0021_00007488', '2019_84_41_3_0021_00007489', '2019_84_41_3_0022_00007200', '2019_84_41_3_0022_00007201', '2019_84_41_3_0022_00007202', '2019_84_41_4_0020_00007559', '2019_84_41_4_0020_00007560', '2019_84_41_4_0020_00007561']

    return images

def check_if_point_in_polygon(location, polygon):
    point = Point(location[0][0], location[1][0])
    return polygon.contains(point)

def get_footprint_from_DB(imageid):
    result = DBF.get_footprint_from_db(imageid)
    return result

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


def get_images_for_point(location, images):
    imagedata = []
    for image in images:
        temp = image
        footprintPoly = create_polygon_array(temp[1])
        is_valid = check_if_point_in_polygon(location, footprintPoly)
        if is_valid == True:
            imagedata.append(temp)  
    return imagedata     

def get_image_width_height(cameraid, coneid):
    
    width, height = DBF.get_camera_width_height(cameraid, coneid)
    return width, height

def homo_to_eucli(coords):
    if coords[2] == 0: return none, none
    return coords[0]/coords[2], coords[1]/coords[2]

def mk_point(x,y):
    return np.array([x, y, 1], dtype='float32')

def find_point_on_image(images,location, order):
    point = mk_point(location[0][0], location[1][0])
    orderid = order.orderID
    parent_dir = 'data/cutimage/'
    directory = f'{orderid}'
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print(path)
    for image in images:
        print(image[4])
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
          
        width, height = get_image_width_height(image[2], image[3])
        dst = np.array([[0,0],[(width-1),0],[0,(height-1)],[(width-1),(height-1)]], dtype='float32')
        M = cv2.getPerspectiveTransform(src, dst)
        print(M)
        result = homo_to_eucli(M.dot(point))
        
        cut_and_save_location(image, result, order, path)
        order.image_directory = path
 
def cut_and_save_location(image, pointPx, order, path):
    x =round(pointPx[0])
    y =round(pointPx[1])
    centroid_t = image[5]
    imageid = image[0]
    direction = image[4]
    orderid = order.orderID

    try:
        my_image=cv2.imread(f"/home/plandata/Andreas/program/data/temp/tempdisc/{centroid_t}/{imageid}.jpg", 1)
        #print(type(my_image))
        #my_image = cv2.circle(my_image,(x ,y), 25, (255,0,0), -1)
        my_image = my_image[y-350:y+350, x-350:x+350]
        cv2.imwrite(f'{path}/{orderid}_{imageid}_{direction}.jpg', my_image) 
    except:
        print('location to close to edge; did not cut')

def run_imagecutcontroller(location, email):
    try:
        new_order = order(None, None, email, location)
        location = np.array([[location[0]], [location[1]]])
        print(location)
        DBF.create_order(new_order)
    
        footprints = [];    
        images = get_image_list(location)
        print(len(images))
        for imageid in images:      
            footprint = DBF.get_footprint_from_db(imageid)
            footprints.append(footprint)     
        valid_images = get_images_for_point(location, footprints)
        print(len(valid_images))    
        find_point_on_image(valid_images,location, new_order)        

        DBF.update_order(new_order)
        kmp.send_order(new_order.orderID, new_order.email)
        return id    
    except:
        print('something bad happend')

#location = [711222, 6175207]
#location = [711947, 6175284]
#location = [710874,6175679]
#location = [711544, 6175343]
#run_imagecutcontroller(location, 'jaja@jaja.co')






