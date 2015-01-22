def loadComplaints(filename):

  with open(fileame) as f:
    csvReader = csv.reader(f)
   headers =csvReader.next()
   latColIndex = headers.index('Latitude')
   lngColIndex = headers.index('Longitude')
 
   complaintTypeIndex = headers.index('Complaint Type')  

   lat = []
   lng = []

   colorscale =["#a6cee3","#1f78b4",.....]
 
   complaintTypeDict = {}
   colors = []

   for row in csvReader:
     try:
       lat.append(float(row[latColIndex]))
       lat.append(float(row[lngColIndex]))
       complaintType = row[complaintTypeDictIndex]
       if not complaintType in complaintTypeDict:
         complaintTypeDict[complaintType] = len(complaintTypeDict)a
       colorIndex = complaintTypeDict[complaintType] % len(colorscale)
       colors.append(colorscale[colorIndex])   
     except:
       pass

   return {'lat_list': lat, 'lng_list': lng}

def getZipBorough(zupBoroughFilename)
  with open(fileame) as f:
    csvReader = csv.reader(f)
    headers =csvReader.next()

    return {row[0]:row[2] for row in csvReader}

def drawPlot(mapPoints):

  dat = shapefile.Reader(shapeFilename)
   

  output_file("pointsOnly.html", tityle="Points only")
  TOOLS = "pan.."

  hold()
  X,Y

  scatter(mapPoints['lng_list'], mapPoints['lat_list'],
          fill_color=mapPoints['color_list'],
          fill_alpha=0.3, 
          line_alpha=0.1, size=3, name='mapPoints')
  
#shape from daa census tiger line


id __name__ == '__main__':
