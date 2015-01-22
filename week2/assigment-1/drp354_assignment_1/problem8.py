################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################


import argparse,csv, sys, os
from datetime import date,datetime
import csv
from collections import OrderedDict
import collections

def countComplaint(filename,zipname):
  zipcode_d = {}
  filename_d = {}

  with open(zipname, 'rb') as f:
     zipReader = csv.reader(f)
     headers = next(zipReader)
     for row in zipReader:
          zipcode_d[row[0]] = row[1]
     #print zipcode_d

  with open(filename, 'rb') as g:
     csvReader = csv.reader(g)
     headers = next(csvReader)
     for row in csvReader:
          if row[7]:
            if row[7] in zipcode_d:
               if zipcode_d[row[7]] in filename_d:
                  filename_d[zipcode_d[row[7]]] += 1 
               else:
                  filename_d[zipcode_d[row[7]]] = {} 
                  filename_d[zipcode_d[row[7]]] = 1 

  filename_d = OrderedDict(sorted(filename_d.items(), key=lambda x: -x[1]))
  
  for k in filename_d:
      print str.title(k)+' with '+str(filename_d[k])+' complaints  '
               
#  with open(filename, 'rb') as f:
#     csvReader = csv.reader(f)
#     headers = next(csvReader)
#     for row in csvReader:
#        row[3]
  


def main(csv_filename,zip_filename):
  countComplaint(csv_filename,zip_filename)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  parser.add_argument("zip_file", help="enter zipcode per borough csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  zip_filename = args.zip_file
  main(csv_filename,zip_filename)
