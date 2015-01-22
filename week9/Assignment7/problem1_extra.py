##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 7                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1_extra                            #
##############################################

import argparse,csv, sys, os
from datetime import date,datetime
import matplotlib
import matplotlib.dates as dates
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

def to_percent(y, position):
  # Ignore the passed in position. This has the effect of scaling the default
  # tick locations.
  s = str(100 * y)

  # The percent symbol needs escaping in latex
  if matplotlib.rcParams['text.usetex'] == True:
    return s + r'$\%$'
  else:
    return s + '%'

def main(csv_filename, num, sTime, eTime):

  data = {}
  sumPerAgency = {}

  #Reading the files
  with open(csv_filename, 'rb') as f:
    csvReader = csv.reader(f)
    headers = next(csvReader)

    #limit start and end time    
    startTime = datetime.strptime(sTime,"%Y/%m/%d-%H:%M:%S") 
    endTime = datetime.strptime(eTime,"%Y/%m/%d-%H:%M:%S") 

    for row in csvReader:
      agency = row[3]
      createdTime = row[1]
      
      #currenttime filed from csv file
      curTime = datetime.strptime(createdTime,"%m/%d/%Y %I:%M:%S %p") 
      #aggregate complaints per hour
      curTimeInt = int(curTime.strftime("%H"))

      #count agency volume
      if curTime>=startTime and curTime<=endTime:
        if agency in data:
          data[agency].append(curTimeInt)
          sumPerAgency[agency] += 1
        else:
          data[agency] = []
          data[agency].append(curTimeInt)
          sumPerAgency[agency] = 1
      else:
        pass
     
  f.close()

  #sorting from the top-k complaint
  sumPerAgency = sorted(sumPerAgency.iteritems(), key=lambda x: (-x[1]))  

  #sorting date and appending into lists
  agenName = []
  x=[]
  y=[]
  index = 0
  
  #iterate only for agency name that is in top-k
  for elem in sumPerAgency[:num]:
    #append agency name
    agenName.append(elem[0])
    x.append([])
    y.append([])
    
    #iterating per-day data
    for agen in data:
      if elem[0] == agen:
        #iterating into lists
        for hour in data[agen]:
          x[index].append(hour)        
          y[index].append(elem[1])
        index+=1
        #break
      else:
        pass

  #plotting histogram
  nbin = num
  colors = []
  for i in xrange(0,num):
    colors.append(np.random.rand(50,1))
  title = "24-hour histogram complaints of top %d Agency \nbetween %s - %s" % (num, sTime,eTime)
  alp = .6
  histlist=plt.hist(x, nbin, normed=1, histtype='bar', color= colors,alpha = alp, label=agenName)
  
  plt.legend(prop={'size': 10})
  plt.title(title)

  #change y-axis to percentage
  formatter = FuncFormatter(to_percent)
  plt.gca().yaxis.set_major_formatter(formatter) # Set the formatter

  plt.xlabel('Time (24 hours format)')
  plt.ylabel('Percentage of total complaints')
  plt.savefig('figure_1_extra.png')
  plt.show()
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  parser.add_argument("num_res",type=int, help="int number of result. For best view, set it at max 8")
  parser.add_argument("start_time", type=str, help="enter start time in \"06/01/2013-24:00:00\" format")
  parser.add_argument("end_time",type=str,  help="enter end time in \"06/01/2013-24:00:00\" format")
  args = parser.parse_args()
  csv_filename = args.csv_file
  num_res = args.num_res
  sTime = args.start_time
  eTime = args.end_time
  main(csv_filename,num_res,sTime,eTime)
