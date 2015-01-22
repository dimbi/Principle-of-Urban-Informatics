##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 8                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2                                  #
##############################################

import argparse,csv,sys,os
from datetime import date,datetime,timedelta
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.dates import date2num
#import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

def main(filename):
  mainTime = ["2007-09-18 12:00:00",
              "2007-09-18 12:00:00",
              "2007-10-04 12:00:00",
              "2007-10-25 12:00:00",
              "2007-11-27 12:00:00",
              "2007-12-15 12:00:00",
              "2007-12-11 12:00:00"]

  timeStamp = []
  day_index = set()

  with open(filename, 'rb') as f:
    Reader = csv.reader(f)
    headers = next(Reader)

    #put initial value as max value->min and the opposite
    minDate=datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
    maxDate=datetime.strptime(date.min.isoformat(),"%Y-%m-%d")

    for row in Reader:
      createdDate = row[0]
      #to find min and max time in a data range
      curDate = datetime.strptime(createdDate,"%Y-%m-%d %H:%M:%S")

      #aggregate complaints per day
      day_index.add(curDate.strftime("%Y-%m-%d"))

      #compare and find min and max date
      minDate = min(minDate, curDate)
      maxDate = max(maxDate, curDate)

      timeStamp.append(curDate)

  deltaDate = maxDate - minDate
  nbin = int(deltaDate.days)
  ind = [date2num(minDate + timedelta(days=x)) for x in range(0, 99,2)]
  dateList = [(minDate + timedelta(days=x)).strftime("%Y-%m-%d") for x in range(0, 99,2)]


  #plotting histogram
  plt.figure(figsize=(24,12))
  title = "Submission date \nbetween %s - %s" % (minDate,maxDate)
  alp = .6
  plt.hist(date2num(timeStamp), nbin, histtype='bar', alpha = alp)
  plt.xticks(ind,dateList, rotation=45)
  plt.xlim(date2num(minDate),date2num(maxDate))

  #Assignment deadlines
  for dates in mainTime:
    tempDate = datetime.strptime(dates,"%Y-%m-%d %H:%M:%S")  
    plt.axvline(x=date2num(tempDate), linewidth=2, color='r')
    plt.text(date2num(tempDate), 8000, 'Deadlines', 
             color = 'r',horizontalalignment='left',
             rotation='vertical')

  plt.xlabel('Date')
  plt.ylabel('Number of submissions')
  plt.legend(prop={'size': 10})
  plt.title(title)
  plt.savefig('problem2.png')
  plt.show()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="enter dta file name / directory")
  args = parser.parse_args()
  filename = args.file
  main(filename)
