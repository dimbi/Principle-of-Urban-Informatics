##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 9                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1                                  #
##############################################

import csv
import shapefile
import sys
import math
import operator
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers
from bokeh.objects import HoverTool
from collections import OrderedDict,defaultdict

def loadComplaints(complaintsFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(complaintsFilename) as f:
    csvReader = csv.reader(f)
    headers = csvReader.next()
    zipIndex = headers.index('Incident Zip')
    latColIndex = headers.index('Latitude')
    lngColIndex = headers.index('Longitude')
    agencyIndex = headers.index('Agency')

    lat = []
    lng = []  
    
    agencyDict = {}
    colors = []
    complaintsPerZip = {}

    for row in csvReader:
      try:
        lat.append(float(row[latColIndex]))
        lng.append(float(row[lngColIndex]))
        agency = row[agencyIndex]
        zipCode = row[zipIndex]
        if not agency in agencyDict:          
          agencyDict[agency] = len(agencyDict)

        if zipCode in complaintsPerZip:
          if agency in complaintsPerZip[zipCode]:
            complaintsPerZip[zipCode][agency]+=1
          else:
            complaintsPerZip[zipCode][agency]=1
        else:
          complaintsPerZip[zipCode]={}
          complaintsPerZip[zipCode][agency]=1

      except:
        pass

    return {'zip_complaints': complaintsPerZip}


def getZipBorough(zipBoroughFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(zipBoroughFilename) as f:
    csvReader = csv.reader(f)
    csvReader.next()

    return {row[0]: row[1] for row in csvReader}
  

def drawPlot(shapeFilename, mapPoints, zipBorough):
  # Read the ShapeFile
  dat = shapefile.Reader(shapeFilename)
  
  # Creates a dictionary for zip: {lat_list: [], lng_list: []}.
  zipCodes = []
  polygons = {'lat_list': [], 'lng_list': [], 'color_list' : []}
  

  # Qualitative 6-class Set1
  colorDict = {}
  colorscale = ['#EA5455','#8743D4', '#66A7E1', '#45C966','#F4DF46','#E97F31','#7D7F72','#AE8E3B']

  record_index = 0
  colorIdx = 0
  zid=[]
  aid=[]
  cid=[]
  agencyList = []

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


      # Calculate color, according to number of complaints
      if currentZip in mapPoints['zip_complaints']:

        # Top complaint type
        sortedlist = sorted(mapPoints['zip_complaints'][currentZip].items(), key=operator.itemgetter(1), reverse=True)
        agency = sortedlist[0][0]

        #for hover
        zid.append(str(currentZip))
        cid.append(str(mapPoints['zip_complaints'][currentZip][agency]))
        aid.append(str(agency))

        #print currentZip, agency
        if agency in colorDict:
          color = colorDict[agency]
        else:
          #for hovering
          colorDict[agency] = colorscale[colorIdx]
          color = colorDict[agency]
          agencyList.append(agency)
          colorIdx+=1
      else:
        color = 'white'
        aid.append("not available")
        cid.append("not available")
        zid.append("not available")

      polygons['color_list'].append(color)

    record_index += 1
  
  TOOLS="crosshair,pan,wheel_zoom,box_zoom,reset,hover,previewsave"

  source = ColumnDataSource(
    data=dict(zid=zid,
              aid=aid,
              cid=cid,)
  )

  # Creates the Plot
  output_file("shapeAndPoints.html", title="shape and points example")

  hold()

  patches(polygons['lng_list'], polygons['lat_list'], \
          fill_color=polygons['color_list'], line_color="gray", \
          tools=TOOLS, source=source,plot_width=1100, plot_height=700, \
          title="Top complaints by Agency for each Zip codes in NY")

  #legend
  x, y = -73.69, 40.58
  for agenIter,colorIter in colorDict.iteritems():
    rect([x], [y], color=colorIter, width=0.01, height=0.01)
    text([x+.01], [y], text=agenIter, angle=0, text_font_size="8pt", text_align="left", text_baseline="middle")
    y = y -.01

  #hover parameter
  hover = curplot().select(dict(type=HoverTool))
  hover.tooltips = OrderedDict([
      ("zip code", "@zid"),
      ("agency", "@aid"),
      ("complaints number", "@cid"),
  ])

  show()
 

if __name__ == '__main__':
  if len(sys.argv) != 4:
    print 'Usage:'
    print sys.argv[0] \
    + '<complaintsfilename> <zipboroughfilename> <shapefilename>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' data/nyshape.shp data/complaints.csv zip_borough.csv'
  else:
    mapPoints = loadComplaints(sys.argv[1])
    zipBorough = getZipBorough(sys.argv[2])
    drawPlot(sys.argv[3], mapPoints, zipBorough)
