################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

naive = []
def buildNaive(points,n):
  global naive
  del naive[:] #erasing previous data
  naive = points
  return None


onedim = []
def buildOneDim(points,n):
  global onedim
  del onedim[:] #erasing previous data
  xWin = 1/float(n)
  onedim = [[] for win in xrange(0,n)]
  for data_x,data_y in points:
    xWinId = int(data_x/xWin)  
    onedim[xWinId].append((data_x,data_y)) 
  return None


twodim = []
def buildTwoDim(points,n):
  global twodim
  del twodim[:] #erasing previous data  
  xWin = 1/float(n)
  yWin = xWin
  twodim = [[[] for xWin in xrange(0,n)] for yWin in xrange(0,n)]
  for data_x,data_y in points:
    xWinId = int(data_x/xWin)  
    yWinId = int(data_y/yWin)  
    twodim[xWinId][yWinId].append((data_x,data_y)) 
  return None


def queryNaive(x0, y0, x1, y1):
  count = 0 
  insideBox = []
  #see if it's within the box
  for data_x, data_y in naive:
    if (data_x>=x0) and (data_x<=x1): 
      if (data_y>=y0) and (data_y<=y1): 
        insideBox.append((data_x,data_y))
      else:pass
    else:pass
  #Count  
  count = len(insideBox)
  return count


def queryOneDim(x0, y0, x1, y1):
  count = 0
  insideBox = []
  numWindow = len(onedim)
  xWin = 1/float(numWindow)

  #see if it's within the box
  for window in xrange(0,numWindow):
    x0Win = int(x0/xWin)
    x1Win = int(x1/xWin)
  #Now count everything only in respective window
  #see if it's within the partial window(s)
  for xWinId in xrange(x0Win, x1Win):
    for data_x, data_y in onedim[xWinId]: 
      if (data_x>=x0) and (data_x<=x1): 
        if (data_y>=y0) and (data_y<=y1): 
          insideBox.append((data_x,data_y))
        else:pass
      else:pass
  #Count  
  count = len(insideBox)   
  return count
  

def queryTwoDim(x0, y0, x1, y1):
  count = 0
  insideBox = []
  numWindow = len(twodim)
  xWin = 1/float(numWindow)
  yWin = xWin
  #see if it's within the box
  for window in xrange(0,numWindow):
    x0Win = int(x0/xWin)
    x1Win = int(x1/xWin)
    y0Win = int(y0/yWin)
    y1Win = int(y1/yWin)
  #Now count everything only in respective window
  #see if it's within the partial window(s)
  for xWinId in xrange(x0Win, x1Win):
    for yWinId in xrange(y0Win, y1Win):
      for data_x, data_y in twodim[xWinId][yWinId]: 
        if (data_x>=x0) and (data_x<=x1): 
          if (data_y>=y0) and (data_y<=y1): 
            insideBox.append((data_x,data_y))
          else:pass
        else:pass
  #Count  
  count = len(insideBox)   
  return count

