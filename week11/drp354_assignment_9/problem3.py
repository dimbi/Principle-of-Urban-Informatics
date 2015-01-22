##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 9                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.3                                  #
##############################################

import csv
import shapefile
import sys
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers

twodim = []
center = []
xmin = -74.3 
xmax = -73.6
ymax = 40.92 
ymin = 40.46 

def initTwoDim(n):
  for i in range(n):
    twodim.append([])
    center.append([])
    for j in range(n):
      twodim[i].append(0) 
      center[i].append((0,0))
  return None
      
def mapTwoDim(p,n):
  winx = (xmax-xmin)/n
  winy = (ymax-ymin)/n
  x = (p[0]-xmin)/(xmax-xmin)
  y = (p[1]-ymin)/(ymax-ymin)
  index_x = int(x * n)
  index_y = int(y * n)
  twodim[index_x][index_y]+=1
  center[index_x][index_y]=(float(xmin+(index_x*winx)+(0.5*winx)),float(ymin+(index_y*winy)+(0.5*winy)))   
  return None



def loadComplaintsPoints(complaintsFilename,n):
  # Reads all complaints and keeps zips which have complaints.

  initTwoDim(n)

  with open(complaintsFilename) as f:
    csvReader = csv.reader(f)
    headers = csvReader.next()
    latColIndex = headers.index('Latitude')
    lngColIndex = headers.index('Longitude')
    complaintTypeIndex = headers.index('Complaint Type')
    lat = []
    lng = [] 
    num = []  
 
    for row in csvReader:
      try:
        points = ((float(row[lngColIndex]),float(row[latColIndex])))
        mapTwoDim(points,n) 
      except:
        pass
 
    for i in range(n):
      for j in range(n):
        if twodim[i][j] !=0:
          lng.append(center[i][j][0])
          lat.append(center[i][j][1])
          num.append(twodim[i][j])
        else:
          pass

    return {'lat_list': lat, 'lng_list': lng, 'num_dots': num}

def getZipBorough(zipBoroughFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(zipBoroughFilename) as f:
    csvReader = csv.reader(f)
    csvReader.next()

    return {row[0]: row[1] for row in csvReader}


def setMarkerSize(complaints):
  outputSize = []
  outputOpac = []
  minSize = 3
  maxSize = 12
  minComp= min(complaints) 
  maxComp= max(complaints) 
  for item in complaints:
    normSize = int((float(item-minComp)/(maxComp-minComp))*(maxSize-minSize))+minSize
    outputSize.append(normSize)
    #set opacity
    if normSize >=3 and normSize<6:
      outputOpac.append(0.1)
    elif normSize >=6 and normSize<9:
      outputOpac.append(0.3)
    elif normSize >=9:
      outputOpac.append(0.6)
   
  return outputSize,outputOpac
    

def drawPlot(shapeFilename, mapPoints, zipBorough):
  # Read the ShapeFile
  dat = shapefile.Reader(shapeFilename)
  
  # Creates a dictionary for zip: {lat_list: [], lng_list: []}.
  zipCodes = []
  polygons = {'lat_list': [], 'lng_list': []}

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

    record_index += 1

  #process the size
  sizes, alp = setMarkerSize(mapPoints['num_dots']) 

  # Creates the Plot
  output_file("shapeAndPoints.html", title="shape and points example")
  # hold()
  
  TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
  
  # Creates the polygons.
  patches(polygons['lng_list'], polygons['lat_list'], \
          fill_color='#C8C6C4', line_color="gray", \
          tools=TOOLS, plot_width=1100, plot_height=700, \
          title="311 complaints mapping in NY")
                  
  # # Draws mapPoints on top of map.
  hold()
  #TODO: Apply transformation to lat/lng points: all fall in the same
  #position on the map.
  scatter(mapPoints['lng_list'], mapPoints['lat_list'],
          fill_color='red',color='red', fill_alpha=alp, line_alpha=alp, size=sizes, name="mapPoints")

  show()


if __name__ == '__main__':
  if len(sys.argv) != 5:
    print 'Usage:'
    print sys.argv[0] \
    + ' <numberofwindow> <complaintsfilename> <zipboroughfilename> <shapefilename>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' data/nyshape.shp 100 data/complaints.csv zip_borough.csv'
  else:
    mapPoints = loadComplaintsPoints(sys.argv[2],int(sys.argv[1]))
    zipBorough = getZipBorough(sys.argv[3])
    drawPlot(sys.argv[4], mapPoints, zipBorough)
