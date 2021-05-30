import numpy as np
import math
import cv2
import psycopg2
import psycopg2.extras
from sympy import symbols, solve
from psycopg2 import Error

 
A = np.array([[711526],[6176140],[0], [1]])
B = np.array([[711691],[6175090],[0], [1]])
C = np.array([[710553],[6175090],[0], [1]])
D = np.array([[710712],[6176130],[0], [1]])
P = np.array([[711543],[6175441],[0], [1]])
P1 = np.array([[711237],[6175752],[0], [1]])
P2 = np.array([[711133],[6175167],[0], [1]])
P3 = np.array([[711289],[6175890],[0], [1]])
P4 = np.array([[711543],[6175341],[0], [1]])
P5 = np.array([[711432],[6177247],[0], [1]])

#dic = get_image_data('2019_84_41_3_0021_00007488')


#X,Y,Z = 710734, 6175827, 0 


def perspective_correction(point):
    # 3d World Coordinates (in world units)
    X,Y,Z = point[0][0], point[1][0], point[2][0]
    #camera translation (in world units)
    locX, locY, locZ = 711118, 6177247, 1557

# camera rotaitons (in radian)
    rotX, rotY, rotZ = -45.319*(math.pi/180), -0.0646*(math.pi/180), -179.860*(math.pi/180)

#image resolutions in pixels
    pX, pY = 10300, 7700  #7700,10300

#sensor size in mm (in world units) sX and sY; pixelSize*imageWidth, pixelSize*imageHeight.
    sX, sY = 53.56, 40.04

#focal length in mm
    f = 123.000

#Skew?
    s = 0

#2d image Coordinates, orthographic coordinates
    x, y, z = 0,0,0
    Gx, Gz, Gy = 0,0,0
    offsetX, offsetY = pX/2, pY/2
 
    matrix1 = np.array([[ ((f*pX)/(2*sX)), s, 0, 0],[0 , ((f*pY)/(2*sY)) , 0 , 0 ],[0,-1,1,0],[0,0,0,1]])
    matrix2 = np.array([[1,0,0,0],[0, math.cos(rotX), -math.sin(rotX), 0],[0,math.sin(rotX), math.cos(rotX), 0],[0,0,0,1]])
    matrix3 = np.array([[math.cos(rotY), math.sin(rotY), 0,0],[0,1,0,0], [-math.sin(rotY), math.cos(rotY), 1, 0], [0,0,0,1]])
    matrix4 = np.array([[math.cos(rotZ), -math.sin(rotZ), 0, 0], [math.sin(rotZ), math.cos(rotZ), 0,0], [0,0,1,0], [0,0,0,1]])
    matrix5 = np.array([[1,0,0,-locX], [0,1,0,-locY], [0,0,1, -locZ], [0,0,0,1]])
    G = np.array([[ 1, 0, 0, -Gx ],[ 0, 1, 0, -Gy ],[ 0, 0, 1, -Gz ],[ 0, 0, 0, 1 ]])  

    pointMatrix = np.array([[X], [Y], [Z], [1]])
    #print('------Matrix 1---------')
    #print(matrix1)
    #print('------Matrix 2---------')
    #print(matrix2)
    #print('------Matrix 3---------')
    #print(matrix3)
    #print('------Matrix 4---------')
    #print(matrix4)
    #print('------Matrix 5---------')
    #print(matrix5)
    #print('------pointMatrix------')
    #print(pointMatrix)
    #print('------resultMatrix-----')
    #res = matrix1.dot(matrix2).dot(matrix3).dot(matrix4).dot(matrix5).dot(pointMatrix)
    res = matrix5.dot(pointMatrix)
    res = matrix4.dot(res)
    res = matrix3.dot(res)
    res = matrix2.dot(res)
    res = matrix1.dot(res)
    #print(res)
    print('---PerspectiveMatrix---')
    x, y, z = res[0][0], res[1][0], res[2][0]
    M = np.array([[1/z,0,0,0],[0,1/z,0,0],[0,0,1,0],[0,0,0,1]])
    Plocal = np.array([[x],[y], [z], [1]])   
    persCoords = M.dot(res)
    #print(persCoords)
    # Perspective Coordinates
    print('Perspective Coordinates: x\'',persCoords[0][0],', y\'', persCoords[1][0],', z', persCoords[2][0])
    return persCoords
   
  


Points = [A, B, C, D, P4]
TransPoints = []
for p in Points:
    #print(p[1])    
    temp = perspective_correction(p)
    TransPoints.append(temp)


def calculate_plane(TransPoints):   
    #A
    p1 = np.array([TransPoints[0][0][0], TransPoints[0][1][0],TransPoints[0][2][0]])
    p2 = np.array([TransPoints[1][0][0], TransPoints[1][1][0],TransPoints[1][2][0]])
    p3 = np.array([TransPoints[2][0][0], TransPoints[2][1][0],TransPoints[2][2][0]])
    p4 = np.array([TransPoints[3][0][0], TransPoints[3][1][0],TransPoints[3][2][0]])

    B = np.array([TransPoints[4][0][0], TransPoints[4][1][0],TransPoints[4][2][0]])
    #print(p1,p2,p3, p4)
    
    v1 = p3-p1
    v2 = p2-p1
    #print(v1, v2)
    cp = np.cross(v1, v2)
    a,b,c = cp
    d = np.dot(cp, p3)

    VK = B-p1
    VN = a,b, c
    print(VN)
    print('The equation is {0}x + {1}y + {2}z = {3}'.format(a, b, c, d))

calculate_plane(TransPoints)

image = '2019_84_41_3_0021_00007488'
image_path =f'../temp/tempdisc/1km_6175_711/{image}.jpg'
image_path='new_img2.jpg'
def colour_spot():
    x = 7700-6958# math.trunc((imageHeight*AP_AB)/100)
    y = 1893# math.trunc((imageWidth*CP_CB)/100)
    z = -2696
    #d = ( z / 2)
    #print(d)
    x1 = x
    y1 = y
    print(x,y)
    print(x1, y1)
    image=cv2.imread(f"{image_path}", 1)
    image[y1:y1+100, x1:x1+100] = (0,255,0)
    cv2.imwrite('new_img2.jpg', image)
    return y,x

print(colour_spot())
#colour_spot()
