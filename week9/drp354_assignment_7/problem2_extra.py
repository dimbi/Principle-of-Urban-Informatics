##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 7                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2_extra                            #
##############################################

import argparse,csv, sys, os
from datetime import date,datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
from collections import OrderedDict,defaultdict

def main(csv_filename,num,sDate,eDate):

  data = {}
  sumPerAgency = {}
  #sDate =  "10/10/2012 12:00:00 AM"
  #eDate =  "11/20/2012 11:59:00 PM"
  
  #Reading the files
  with open(csv_filename, 'rb') as f:
    csvReader = csv.reader(f)
    headers = next(csvReader)

    #limit start and end time    
    startDate = datetime.strptime(sDate,"%Y/%m/%d-%H:%M:%S") 
    endDate = datetime.strptime(eDate,"%Y/%m/%d-%H:%M:%S") 
    
    for row in csvReader:
      agency = row[3]
      createdDate = row[1]
      
      #to find min and max time in a data range
      curDate = datetime.strptime(createdDate,"%m/%d/%Y %I:%M:%S %p") 

      if curDate>=startDate and curDate<=endDate:
        #aggregate complaints per day
        curDatePerDay = curDate.strftime("%Y/%m/%d")
      
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
  title = "Top-%d Agency volume per day between %s - %s during Hurricane Sandy" % (num,sDate,eDate)

  # Create plots with pre-defined labels.
  plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
  plt.title(title)
  for n in xrange(0,num):
    #generate bold line for top-3 agency we would be interested to analyze
    if n<3:
      lineType = '-'
      lineWid=5
    else:
      lineType = ':'
      lineWid=2
    plt.plot_date(x[n], y[n], lineType, linewidth=lineWid, color=np.random.rand(50,1),label=agenName[n])
  plt.legend(loc='upper left', shadow=True, fontsize='x-large')
  plt.grid(True)
  plt.xlabel('Date')
  plt.ylabel('Number of complaints')

  #plot span to add information about a period during
  #which the Hurricane Sandy happened
  sandyStart = dates.datestr2num("2012/10/22")
  sandyEnd = dates.datestr2num("2012/11/02")
  plt.axvspan(sandyStart, sandyEnd, facecolor='r', alpha=0.2)
  plt.text(sandyStart, 4200, 'Hurricane\nperiod', horizontalalignment='left')

  plt.savefig('figure_2_extra.png')
  plt.show()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  parser.add_argument("num_res",type=int, help="int number of result")
  parser.add_argument("start_date", type=str, help="enter start time in \"2013/06/01-24:00:00\" format")
  parser.add_argument("end_date",type=str,  help="enter end time in \"2013/06/01-24:00:00\" format")
  args = parser.parse_args()
  csv_filename = args.csv_file
  num_res = args.num_res
  sDate = args.start_date
  eDate = args.end_date
  main(csv_filename,num_res,sDate,eDate)
