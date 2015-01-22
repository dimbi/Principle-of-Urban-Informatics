##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 7                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1_1                                #
##############################################

import argparse,csv, sys, os
from datetime import date,datetime
import matplotlib.pyplot as plt
import numpy as np

def main(csv_filename):
  agencyName=["NYPD", 
              "DOT", 
              "DOB", 
              "TLC", 
              "DPR"]
  data = {}
  for name in agencyName:
    data[name] = 0

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
      
      #input the date filed from csv file
      curDate = datetime.strptime(createdDate,"%m/%d/%Y %I:%M:%S %p") 

      #compare and find min and max date
      minDate = min(minDate, curDate)
      maxDate = max(maxDate, curDate)

      #count agency volume
      for name in agencyName:
        if name == agency:
          if agency in data:
            data[agency] += 1
          else:
            pass
          break
  f.close()

  #sorting from the biggest one
  sortedData = sorted(data.iteritems(), key=lambda x: (-x[1],x[0]))  
   
  #putting into lists
  agenName = []
  ind = np.arange(len(data))
  
  y = []
  for elem in sortedData:
    agenName.append(elem[0])
    y.append(elem[1]) 

  #bar plot variable
  wid = .9
  alp = 0.3
  ali = "center"
  title = "Complaint volume by agency %s - %s" % (minDate.strftime("%b/%d/%Y"),
                                                  maxDate.strftime("%b/%d/%Y"))
  xlim0 = -0.5 
  xlim1 = 4.5 

  #plot
  plt.figure()
  barlist=plt.bar(ind, y, wid, alpha=alp, align=ali)
  barlist[0].set_color('b')
  barlist[1].set_color('g')
  barlist[2].set_color('r')
  barlist[3].set_color('c')
  barlist[4].set_color('m')
  plt.xlim(xlim0,xlim1)
  plt.xticks(ind,agenName)
  plt.title(title)
  plt.xlabel('Agency')
  plt.ylabel('Volume')
  plt.savefig('figure_1_1.png')
  plt.show()
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
