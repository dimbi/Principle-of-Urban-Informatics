##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 7                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2_2                                #
##############################################

import argparse,csv, sys, os
from datetime import date,datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
from collections import OrderedDict,defaultdict
from itertools import cycle

def main(csv_filename,num):

  data = {}
  sumPerAgency = {}
  
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
      if agency in data:
        if curDatePerDay in data[agency]:
          data[agency][curDatePerDay] += 1
          sumPerAgency[agency] += 1
        else:
          data[agency][curDatePerDay] = 1
          sumPerAgency[agency] += 1
      else:
        data[agency] = {}
        data[agency][curDatePerDay] = 1
        sumPerAgency[agency]=1
          
  f.close()

  #sorting from the top-k complaint
  sumPerAgency = sorted(sumPerAgency.iteritems(), key=lambda x: (-x[1]))  

  #sorting date and appending into lists
  agenName = []
  x=[]
  y=[]
  index = 0
  
  #set limit for number of max num
  lenData = len(data)
  if num > lenData: num = lenData
  ind = np.arange(num)

  #iterate only for agency name that is in top-k
  for elem in sumPerAgency[:num]:
    #append agency name
    agenName.append(elem[0])
    x.append([])
    y.append([])
    
    #iterating per-day data
    for agen in data:
      if elem[0] == agen:
        #sort ascending by date
        data[agen]= OrderedDict(sorted(data[agen].items(), key=lambda x: (x[0])))
        #iterating into lists
        for iterdate, counts in data[agen].iteritems():
          iterdateNum = dates.datestr2num(iterdate)
          x[index].append(iterdateNum)        
          y[index].append(counts)
        index+=1
        #break
      else:
        pass


  #line plot variable
  title = "Top-%d Agency volume per day between %s - %s" % (num,
                                                            minDate.strftime("%b/%d/%Y"),
                                                            maxDate.strftime("%b/%d/%Y"))
  lines = ["-","--","-."]
  linecycler = cycle(lines)  

  # Create plots with pre-defined labels.
  plt.figure(num=None, linewidth=3, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
  plt.title(title)
  for n in xrange(0,num):
    plt.plot_date(x[n], y[n], next(linecycler), color=np.random.rand(50,1),label=agenName[n])
  plt.legend(loc='upper left', shadow=True, fontsize='x-large')
  plt.grid(True)
  plt.xlabel('Date')
  plt.ylabel('Number of complaints')
  plt.savefig('figure_2_2.png')
  plt.show()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  parser.add_argument("num_res",type=int, help="int number of result")
  args = parser.parse_args()
  csv_filename = args.csv_file
  num_res = args.num_res
  main(csv_filename,num_res)
