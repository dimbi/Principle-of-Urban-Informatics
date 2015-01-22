##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 7                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1_2                                #
##############################################

import argparse,csv, sys, os
from datetime import date,datetime
import matplotlib.pyplot as plt
import numpy as np

#add auto label for y valu
def autolabel(rects):
  # attach some text labels
  for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
             ha='center', va='bottom')

def main(csv_filename,num):

  data = {}

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
      if agency in data:
        data[agency] += 1
      else:
        data[agency] = 1

  f.close()

  #sorting from the biggest one
  sortedData = sorted(data.iteritems(), key=lambda x: (-x[1],x[0]))  

  #set limit for number of max num
  lenData = len(data)
  if num > lenData: num = lenData
   
  #putting into lists
  agenName = []
  ind = np.arange(num)
  y = []
  for elem in sortedData[:num]:  
    agenName.append(elem[0])
    y.append(elem[1]) 

  #bar plot variable
  wid = .9
  ali = "center"
  title = "Top-%d Agency volume %s - %s" % (num,
                                            minDate.strftime("%b/%d/%Y"),
                                            maxDate.strftime("%b/%d/%Y"))
  xlim0 = -0.5 
  xlim1 = num-0.5
  alp = 0.5

  #plot
  plt.figure()
  barlist=plt.bar(ind, y, wid,alpha = alp, align=ali)
  for i in xrange(0,num):
    barlist[i].set_color(np.random.rand(50,1))
    barlist[i].set_alpha(alp)
    alp+=0.02
  plt.xlim(xlim0,xlim1)
  plt.xticks(ind,agenName)
  plt.title(title)

  #add autolabel
  autolabel(barlist)

  plt.xlabel('Agency')
  plt.ylabel('Volume')
  plt.savefig('figure_1_2.png')
  plt.show()
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  parser.add_argument("num_res",type=int, help="int number of result")
  args = parser.parse_args()
  csv_filename = args.csv_file
  num_res = args.num_res
  main(csv_filename,num_res)
