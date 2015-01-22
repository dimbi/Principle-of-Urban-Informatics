################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

import argparse,csv, sys, os
from datetime import date,datetime

def countComplaintTop(filename,num_result):
  d=dict()
  with open(filename, 'rb') as f:
     csvReader = csv.reader(f)
     headers = next(csvReader)

     for row in csvReader:
       if row[5] in d:
          d[row[5]] += 1
       else:
          d[row[5]] = 1
  sorted_d = sorted(d.iteritems(), key=lambda x: (-x[1],x[0]))  

  for x in sorted_d[:num_result]:  
   print x[0]+' with '+str(x[1])+' complaints'
 

def main(csv_filename,num_result):
  countComplaintTop(csv_filename,num_result)

      
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  parser.add_argument("num_res",type=int, help="int number of result")
  args = parser.parse_args()
  csv_filename = args.csv_file
  num_res = args.num_res
  main(csv_filename,num_res)
