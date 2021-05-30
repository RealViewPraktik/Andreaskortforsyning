import cv2
import numpy as np

# billede 2019_84_40_4_0032_00002065

# src og dst hjørner skal matche
src = np.array([[722873,6173080],[722822,6172230],[721618,6172930],[721622,6172380]], dtype='float32')

# bemærk billedet er portrait
dst = np.array([[0,0],[7699,0],[0,10299],[7699,10299]], dtype='float32')

# fra coord til px
M = cv2.getPerspectiveTransform(src,dst)

# fra px til coord
Minv = cv2.getPerspectiveTransform(dst,src)

# fra homogenous coord til euclidean coords
# de normaliseres ved at dele med 3. elemen
# hvis 3. element er 0 er det et (vanishing) punkt
#   i horizonten der ikke kan defineres i euclidean geometri
def p(x):
    if x[2] == 0: return None, None
    return x[0]/x[2], x[1]/x[2]

# fra euclidean geometri til homegenous (og i passende np format)
def mkpunkt(x,y):
    return np.array([x,y,1], dtype='float32')

sb24 = mkpunkt(722034, 6172625)
bb55 = mkpunkt(722375,6172682)
bb55px = mkpunkt(3478,2968)

print('forventet omkring 4173, 5940')
print(p(M.dot(sb24)))
print('forventet omkring 3475, 2960')
print(p(M.dot(bb55)))
print(p(Minv.dot(bb55px)))
