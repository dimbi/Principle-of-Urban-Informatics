##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 11                         #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.3                                  #
##############################################

import sys
import time
import csv
from scipy import spatial
import numpy as np

def loadTaxiTripsPickupAndDropoffs(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    lngIndex0 = header.index(' pickup_longitude')
    latIndex0 = header.index(' pickup_latitude')
    latIndex1 = header.index(' dropoff_latitude')
    lngIndex1 = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point0 = [float(l[latIndex0]),float(l[lngIndex0])]
            point1 = [float(l[latIndex1]),float(l[lngIndex1])]
            if latBounds[0] <= point0[0] <= latBounds[1] and lngBounds[0] <= point0[1] <= lngBounds[1] and latBounds[0] <= point1[0] <= latBounds[1] and lngBounds[0] <= point1[1] <= lngBounds[1]:
                result.append([point0[0],point0[1],point1[0],point1[1]])
        except:
            print l
    return result
    
def naiveApproach(tripLocations, startRectangle, endRectangle):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startRectangle region and end in the endRectangle region
    indices = []
 
    startTime = time.time()

    for idx,(y0,x0,y1,x1) in enumerate(tripLocations):
	if y0 >=startRectangle[0][0] and y0 <= startRectangle[0][1] and x0 >= startRectangle[1][0] and x0<=startRectangle[1][1]: 
	    if y1 >=endRectangle[0][0] and y1 <= endRectangle[0][1]  and x1 >= endRectangle[1][0] and x1<=endRectangle[1][1]: 
                indices.append(idx)

    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return indices

def kdtreeApproach(tripLocations, startRectangle, endRectangle):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startRectangle region and end in the endRectangle region
    indices = []
    startTime = time.time()

    spoints = []
    epoints = []
    for y0,x0,y1,x1 in tripLocations:
	spoints.append([y0,x0])
    	epoints.append([y1,x1])

    stree = spatial.KDTree(spoints)
    etree = spatial.KDTree(epoints)

    sx = ((startRectangle[1][1] - startRectangle[1][0])/2)
    sy = ((startRectangle[0][1] - startRectangle[0][0])/2)
    ex = ((endRectangle[1][1] - endRectangle[1][0])/2)
    ey = ((endRectangle[0][1] - endRectangle[0][0])/2) 
    sdistance = np.sqrt((sx**2)+(sy**2))
    edistance = np.sqrt((ex**2)+(ey**2))

    scenter = [(((startRectangle[0][1]-startRectangle[0][0])/2)+startRectangle[0][0]),(((startRectangle[1][1]-startRectangle[1][0])/2)+startRectangle[1][0])]
    ecenter = [(((endRectangle[0][1]-endRectangle[0][0])/2)+endRectangle[0][0]),(((endRectangle[1][1]-endRectangle[1][0])/2)+endRectangle[1][0])]
    scircle = stree.query_ball_point(scenter,sdistance)
    ecircle = etree.query_ball_point(ecenter,edistance)

    intersectCircle = list(set(scircle) & set(ecircle))
    for elem in intersectCircle:
        y0,x0,y1,x1  = tripLocations[elem]
        if y0 >= startRectangle[0][0] and y0 <= startRectangle[0][1] and x0 >= startRectangle[1][0] and x0 <= startRectangle[1][1]: 
            if y1 >= endRectangle[0][0] and y1 <= endRectangle[0][1]  and x1 >= endRectangle[1][0] and x1 <= endRectangle[1][1]: 
	        indices.append(elem)

    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return indices

def extraCredit(tripLocations, startPolygon, endPolygon):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startPolygon region and end in the endPolygon region
    indices = []

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip

    return indices    

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    trips             = loadTaxiTripsPickupAndDropoffs(sys.argv[1])
    #
    startRectangle    = [[40.713590,40.721319],[-74.011116,-73.994722]] #[[minLat,maxLat],[minLng,maxLng]]
    endRectangle      = [[40.744532,40.748398],[-74.003005,-73.990881]] #[[minLat,maxLat],[minLng,maxLng]]

    #You need to implement this one. You need to make sure that the counts are correct
    naiveIndices = naiveApproach(trips,startRectangle, endRectangle)

    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeIndices = kdtreeApproach(trips,startRectangle, endRectangle)
