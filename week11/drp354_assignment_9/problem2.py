##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 9                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2                                  #
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
   
        if agency == agency1 or agency == agency2:
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
        else:
          pass      

      except:
        pass

    return {'zip_complaints': complaintsPerZip}


def getZipBorough(zipBoroughFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(zipBoroughFilename) as f:
    csvReader = csv.reader(f)
    csvReader.next()

    return {row[0]: row[1] for row in csvReader}
  

def drawPlot(shapeFilename, mapPoints, zipBorough,agency1, agency2):
  # Read the ShapeFile
  dat = shapefile.Reader(shapeFilename)
  
  # Creates a dictionary for zip: {lat_list: [], lng_list: []}.
  zipCodes = []
  polygons = {'lat_list': [], 'lng_list': [], 'color_list' : []}
  

  # Qualitative 6-class Set1
  colorDict = {}
  #colorscale = ["#0063D5","#0040FF", "#001AE1", "#0C00CA", "#5A00B4", "#8800BA", "#D500CE", "#E100C8", "#F000C3", "#FF00BF"]
  #colorscale = ["#FFBF00","#F0A400", "#E18B00", "#D57100", "#CA5900", "#C14200", "#BA2B00", "#B40000", "#730016", "#5A0000"]
  colorscale = ["#742443","#83384A", "#AF7B6D", "#C39D85", "#E3D7C8", "#B7D9D7", "#69AEB6", "#4391A6", "#1D6D90", "#03212C"]
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

        if agency1 in mapPoints['zip_complaints'][currentZip] and  agency2 in mapPoints['zip_complaints'][currentZip]:
          colorIndex = ((mapPoints['zip_complaints'][currentZip][agency1]) / float(mapPoints['zip_complaints'][currentZip][agency1]+mapPoints['zip_complaints'][currentZip][agency2])) * len(colorscale)
          color = colorscale[int(colorIndex)]
        elif agency1 in mapPoints['zip_complaints'][currentZip] and  agency2 not in mapPoints['zip_complaints'][currentZip]:
          color = colorscale[0]
        elif agency2 in mapPoints['zip_complaints'][currentZip] and  agency1 not in mapPoints['zip_complaints'][currentZip]:
          color = colorscale[9]
      else:
        color = 'white'
      polygons['color_list'].append(color)


    record_index += 1
  
  TOOLS="crosshair,pan,wheel_zoom,box_zoom,reset,previewsave"

  # Creates the Plot
  output_file("shapeAndPoints.html", title="shape and points example")
  hold()

  patches(polygons['lng_list'], polygons['lat_list'], \
          fill_color=polygons['color_list'], line_color="gray", \
          tools=TOOLS,plot_width=1100, plot_height=700, \
          title="%s VS %s number of complaints"%(agency1, agency2))

  #legend
  legendName = ["10%","20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
  x, y = -73.69, 40.58
  for idx, color in enumerate(colorscale):
    rect([x], [y], color=color, width=0.01, height=0.01)
    if idx == 0:
      text([x+.01], [y], text="100% "+agency1, angle=0, text_font_size="8pt", text_align="left", text_baseline="middle")
    elif idx == 9:
      text([x+.01], [y], text="100% "+agency2, angle=0, text_font_size="8pt", text_align="left", text_baseline="middle")
    y = y -.01

  show()
 

if __name__ == '__main__':
  if len(sys.argv) != 6:
    print 'Usage:'
    print sys.argv[0] \
    + ' <complaintsfilename> <zipboroughfilename> <shapefilename> <agency1> <agency2>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' data/nyshape.shp data/complaints.csv zip_borough.csv'
  else:
    agency1 = str(sys.argv[4])
    agency2 = str(sys.argv[5])
    mapPoints = loadComplaints(sys.argv[1])
    zipBorough = getZipBorough(sys.argv[2])
    drawPlot(sys.argv[3], mapPoints, zipBorough,agency1,agency2)
