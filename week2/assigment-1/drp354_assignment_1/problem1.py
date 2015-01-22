################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

import argparse,csv, sys, os
from datetime import date,datetime

def countComplaint(filename):
  numberOfComplaints = 0

  #reading CSV
  with open(filename, 'rb') as f:
     csvReader = csv.reader(f)
     headers = next(csvReader)
    
     #put initial value as max value->min and the opposite
     minDate=datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
     maxDate=datetime.strptime(date.min.isoformat(),"%Y-%m-%d")

     for row in csvReader:
         #counter for number of complaints
         numberOfComplaints += 1

         #input the date filed from csv file
         creationDate = datetime.strptime(row[1],"%m/%d/%Y %I:%M:%S %p") 

         #compare and find min and max date
         if creationDate < minDate:
           minDate = creationDate     
         if creationDate > maxDate:
           maxDate = creationDate        

     #print
     print str(numberOfComplaints)+' complaints between '+minDate.strftime("%m/%d/%Y %H:%M:%S")+' and '+maxDate.strftime("%m/%d/%Y %H:%M:%S")

def main(csv_filename):
  countComplaint(csv_filename)

      
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
