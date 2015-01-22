################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

import argparse,csv, sys, os
import csv
from collections import OrderedDict,defaultdict

def countComplaint(filename):
  d = {}
  with open(filename, 'rb') as f:
     csvReader = csv.reader(f)
     headers = next(csvReader)
     for row in csvReader:
            if (row[3] not in d) or (row[7] not in d[row[3]]):
                if row[3] not in d: d[row[3]] = {}
                d[row[3]][row[7]]=1
            else:
                d[row[3]][row[7]]+=1  
 
  #sort by Agency
  d = OrderedDict(sorted(d.items(), key=lambda x: x[0]))

  for k in d:
      #sort ascending by zipcode
      d[k]= OrderedDict(sorted(d[k].items(), key=lambda x: (x[0])))

      #find max values
      m = defaultdict(list)
      ZipMax = []
      for key, val in d[k].items():
        m[val].append(key)
      ZipMax = m[max(m)]

      #printing
      print k,
      for j in ZipMax:
      	  print str(j),
      print str(max(m))

def main(csv_filename):
  countComplaint(csv_filename)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
