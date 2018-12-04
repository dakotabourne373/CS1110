# Dakota Bourne (db2nb) Nick Manalac (ntm4kd)
"""

"""
import math

# DO NOT MODIFY the following function; use as is
def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees
    return dist

user_lat = float(input("Enter your latitude "))
user_long = float(input("Enter your longitude "))
f = open('fiveguys.csv')
x = f.readlines()
g = 0
lst = []
for i in x:
    global y
    blue = str(x[g])
    y = blue.split(',')
    g += 1
    poi_lat = float(y[0])
    poi_long = float(y[1])
    distance = distance_between(user_lat, user_long, poi_lat, poi_long)
    lst.append(distance)
min_dist = min(lst)
g = 0
for d in lst:
    if d == min_dist:
        print(x[g])
    g += 1