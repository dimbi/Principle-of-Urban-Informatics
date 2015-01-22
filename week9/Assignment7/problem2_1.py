##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 7                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2_1                                #
##############################################

import argparse,csv, sys, os
from datetime import date,datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
from collections import OrderedDict,defaultdict

def main(csv_filename):
  agencyName=["NYPD", 
              "TLC", 
              "DPR"]
  data = {}
  for name in agencyName:
    data[name] = {}

  #Reading the files
  with open(csv_filename, 'rb') as f:
    csvReader = csv.reader(f)
    headers = next(csvReader)
    
    #put initial value as max value->min and the opposite
    minDate=datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
    maxDate=datetime.strptime(date.min.isoformat(),"%Y-%m-%d")

    for row in csvReader:
      agency = row[3]
      createdDate = row[1]
      
      #to find min and max time in a data range
      curDate = datetime.strptime(createdDate,"%m/%d/%Y %I:%M:%S %p") 

      #aggregate complaints per day
      curDatePerDay = curDate.strftime("%m/%d/%Y")
      
      #compare and find min and max date
      minDate = min(minDate, curDate)
      maxDate = max(maxDate, curDate)

      #count agency volume
      for name in agencyName:
        if name == agency:
          if curDatePerDay in data[name]:
            data[name][curDatePerDay] += 1
          else:
            data[name][curDatePerDay] = 1
          break

  f.close()

  #sorting and appending into lists
  agenName = []
  x=[]
  y=[]
  index = 0
  for agen in data:
    #append agency name
    agenName.append(agen)
    x.append([])
    y.append([])

    #sort ascending by data
    data[agen]= OrderedDict(sorted(data[agen].items(), key=lambda x: (x[0])))
    #iterating into lists
    for iterdate, counts in data[agen].iteritems():
      iterdateNum = dates.datestr2num(iterdate)
      x[index].append(iterdateNum)        
      y[index].append(counts) 
    index+=1
  ind = np.arange(len(agenName))

  #line plot variable
  alp = 0.3
  title = "Agency volume per day between %s - %s" % (minDate.strftime("%b/%d/%Y"),
                                                     maxDate.strftime("%b/%d/%Y"))
  # Create plots with pre-defined labels.
  plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
  plt.title(title)
  plt.plot_date(x[0], y[0], 'g-',label=agenName[0])
  plt.plot_date(x[1], y[1], 'b-',label=agenName[1])
  plt.plot_date(x[2], y[2], 'r-',label=agenName[2])
  plt.legend(loc='upper left', shadow=True, fontsize='x-large')
  plt.xlabel('Date')
  plt.ylabel('Number of complaints')
  #plt.savefig('figure_2_1.png')
  plt.show()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
