##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 11                         #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2                                  #
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
    
def naiveApproach(intersections, tripLocations, distanceThreshold):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which are within a distance of
    #distanceThreshold from the intersection
    counts = {}
    startTime = time.time()

    distanceSquared = distanceThreshold**2

    for idx,(y0,x0) in enumerate(intersections):
        minRange = 10**10

	counter = 0
        for y1,x1 in tripLocations:
	    r = ((y1-y0)**2)+((x1-x0**2)
	    if r<distanceSquared:
                counter += 1
		    
        counts[idx] = counter
   

    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return counts

def kdtreeApproach(intersections, tripLocations, distanceThreshold):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which are within a distance of
    #distanceThreshold from the intersection
    counts = {}
    startTime = time.time()

    tree = spatial.KDTree(tripLocations)
    for idx,intersect in enumerate(intersections):
        minRangeList = tree.query_ball_point(intersect,distanceThreshold)
        counts[idx] = len(minRangeList)

    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return counts

def plotResults(intersections, counts):
    #TODO: intersect the code to plot here
    print 'TODO'

def extraCredit(intersections, counts):
    #TODO: intersect the code to plot here
    print 'TODO'

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    roadIntersections = loadRoadNetworkIntersections(sys.argv[1])
    tripPickups       = loadTaxiTrips(sys.argv[2])
    distanceThreshold = float(sys.argv[3])

    #You need to implement this one. You need to make sure that the counts are correct
    naiveCounts = naiveApproach(roadIntersections,tripPickups, distanceThreshold)

    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeCounts = kdtreeApproach(roadIntersections,tripPickups, distanceThreshold)

    #
    plotResults(roadIntersections,kdtreeCounts)
