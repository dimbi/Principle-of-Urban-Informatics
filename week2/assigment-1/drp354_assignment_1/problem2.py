################################################
#***CUSP Principle of urban informatic class***#
#-------Dimas R.Putro / drp354@nyu.edu---------#
################################################

import argparse,csv, sys, os

def countComplaint(filename):
  d=dict()

  #reading CSV
  with open(filename, 'rb') as f:
     csvReader = csv.reader(f)
     headers = next(csvReader)

     for row in csvReader:
       #checking if the complaints is already stored
       #then add the counter (value) 
       if row[5] in d:
          d[row[5]] += 1
       else:
          d[row[5]] = 1
  
  for key, value in d.iteritems() :
     print key+' with '+str(value)+' complaints'

def main(csv_filename):
  countComplaint(csv_filename)

      
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
