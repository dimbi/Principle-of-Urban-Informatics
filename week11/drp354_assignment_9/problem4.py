##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 9                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.4                                  #
##############################################

import csv
import shapefile
import sys
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers

def loadComplaintsPoints(complaintsFilename):
  # Reads all complaints and keeps zips which have complaints.
  complaintsByZip = {}

  with open(complaintsFilename) as f:
    csvReader = csv.reader(f)
    headers = csvReader.next()
    zipIndex = headers.index('Incident Zip')
    latColIndex = headers.index('Latitude')
    lngColIndex = headers.index('Longitude')
    complaintTypeIndex = headers.index('Complaint Type')
    lat = []
    lng = [] 
    num = []  
 
    for row in csvReader:
      zipCode = row[zipIndex]
      try:
        if zipCode in complaintsByZip:
          complaintsByZip[zipCode] += 1
        else:
          complaintsByZip[zipCode] = 1
      except:
        pass
 
    return {'zip_complaints': complaintsByZip}


def getZipBorough(zipBoroughFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(zipBoroughFilename) as f:
    csvReader = csv.reader(f)
    csvReader.next()

    return {row[0]: row[1] for row in csvReader}


def findCenter(lons,lats):

  numLon=len(lons)
  numLat=len(lats)
  centerLon = float(sum(lons)/len(lons))
  centerLat = float(sum(lats)/len(lats))

  return (centerLon,centerLat)


def setMarkerSize(complaints,zipCodes):
  outputSize = []
  outputOpac = []
  minSize = 5
  maxSize = 12
  maxComp = -1
  minComp = 10000000
  for zipCode in zipCodes:
    if zipCode in complaints:
      minComp= min(complaints[zipCode],minComp) 
      maxComp= max(complaints[zipCode],maxComp) 

  for zipCode in zipCodes:
    if zipCode in complaints:
      numComplaints = complaints[zipCode]
      normSize = int((float(numComplaints-minComp)/(maxComp-minComp))*(maxSize-minSize))+minSize
      outputSize.append(normSize)
      if normSize >=5 and normSize<7:
        outputOpac.append(0.1)
      elif normSize >=7 and normSize<9:
        outputOpac.append(0.3)
      elif normSize >=9:
        outputOpac.append(0.5)
  return outputSize,outputOpac
    

def drawPlot(shapeFilename, mapPoints, zipBorough):
  # Read the ShapeFile
  dat = shapefile.Reader(shapeFilename)
  
  zipCodes = []
  sizes = []
  alp = []
  center = []
  polygons = {'lat_list': [], 'lng_list': [], 'centerLon': [],'centerLat': []}

  record_index = 0
  for r in dat.iterRecords():
    currentZip = r[0]

    # Keeps only zip codes in NY area.
    if currentZip in zipBorough:

      zipCodes.append(currentZip)

      # Gets shape for this zip.
      shape = dat.shapeRecord(record_index).shape
      points = shape.points

      # Breaks into lists for lat/lng.
      lngs = [p[0] for p in points]
      lats = [p[1] for p in points]

      # Stores lat/lng for current zip shape.
      polygons['lng_list'].append(lngs)
      polygons['lat_list'].append(lats)

      # needs find center
      centerLon, centerLat = findCenter(lngs,lats)
      polygons['centerLon'].append(centerLon)
      polygons['centerLat'].append(centerLat)


    record_index += 1

  #process the size and alpha
  sizes, alp = setMarkerSize(mapPoints['zip_complaints'], zipCodes) 

  # Creates the Plot
  output_file("shapeAndPoints.html", title="shape and points example")
  # hold()
  
  TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
  
  # Creates the polygons.
  patches(polygons['lng_list'], polygons['lat_list'], \
          fill_color='#C8C6C4', line_color="gray", \
          tools=TOOLS, plot_width=1100, plot_height=700, \
          title="Complaints by zip codes in NY")
                  
  # # Draws mapPoints on top of map.
  hold()
  #TODO: Apply transformation to lat/lng points: all fall in the same
  #position on the map.
  scatter(polygons['centerLon'], polygons['centerLat'],
          fill_color='#00A368',color='#00A368', fill_alpha=alp, line_alpha=alp, size=sizes, name="mapPoints")

  show()


if __name__ == '__main__':
  if len(sys.argv) != 4:
    print 'Usage:'
    print sys.argv[0] \
    + ' <complaintsfilename> <zipboroughfilename> <shapefilename>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' data/nyshape.shp 100 data/complaints.csv zip_borough.csv'
  else:
    mapPoints = loadComplaintsPoints(sys.argv[1])
    zipBorough = getZipBorough(sys.argv[2])
    drawPlot(sys.argv[3], mapPoints, zipBorough)
