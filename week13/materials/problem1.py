##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 11                         #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1                                  #
##############################################

import sys
import time
import csv
from scipy import spatial
import numpy as np

def loadRoadNetworkIntersections(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    listWithIntersectionCoordinates = []
    f = open(filename)
    reader = csv.reader(f, delimiter=' ')
    for l in reader:
        try:
            point = [float(l[0]),float(l[1])]
            if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
                listWithIntersectionCoordinates.append(point)
        except:
            print l

    return listWithIntersectionCoordinates

def loadTaxiTrips(filename):
    #load pickup positions
    loadPickup = True
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    if loadPickup:        
        lngIndex = header.index(' pickup_longitude')
        latIndex = header.index(' pickup_latitude')
    else:
        latIndex = header.index(' dropoff_latitude')
        lngIndex = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point = [float(l[latIndex]),float(l[lngIndex])]
            if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
                result.append(point)

        except:
            print l
    return result
    
def naiveApproach(intersections, tripLocations):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which has the key as the closest
    #intersection.
    counts = {}
    startTime = time.time()

    for y1,x1 in tripLocations:
        minRange = 10**10
	idx = 0 
	for index,(y0,x0) in enumerate(intersections):
	    r = ((y1-y0)**2)+((x1-x0)**2)

	    if r<minRange:
                minRange = r 
		idx = index

        if idx not in counts:
            counts[idx] = 1
        else:
            counts[idx] += 1
    
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return counts

def kdtreeApproach(intersections, tripLocations):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which has the key as the closest
    #intersection.
    counts = {}
    startTime = time.time()
    idx = 0

    tree = spatial.KDTree(intersections)
    for tripCoord in tripLocations:
        minRange = tree.query(tripCoord)
        idx = minRange[1]
        if idx not in counts:
            counts[idx] =1
        else:
            counts[idx] +=1

    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return counts

def plotResults(intersections, counts):
    #TODO: intersect the code to plot here
    print 'TODO'

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    roadIntersections = loadRoadNetworkIntersections(sys.argv[1])
    tripPickups       = loadTaxiTrips(sys.argv[2])

    #You need to implement this one. You need to make sure that the counts are correct
    naiveCounts = naiveApproach(roadIntersections,tripPickups)

    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeCounts = kdtreeApproach(roadIntersections,tripPickups)

    #
    plotResults(roadIntersections,kdtreeCounts)
