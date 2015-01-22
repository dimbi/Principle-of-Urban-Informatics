################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

import argparse,csv, sys, os
from datetime import date,datetime

#reading CSV
def countComplaintPerDay(filename):
  list_d = []
  d={'Monday':0, 
     'Tuesday':0, 
     'Wednesday':0, 
     'Thursday':0, 
     'Friday':0,
     'Saturday':0,
     'Sunday':0}
  day_sort = ['Monday', 
              'Tuesday', 
              'Wednesday', 
              'Thursday', 
              'Friday',
              'Saturday',
              'Sunday']

  with open(filename, 'rb') as f:
     csvReader = csv.reader(f)
     headers = next(csvReader)
    
     for row in csvReader:
         day_of_date=datetime.strptime(row[1], "%m/%d/%Y %I:%M:%S %p").strftime('%A')
         if day_of_date in d:
            d[day_of_date] += 1

     list_d = d.items() 
     list_d.sort(key=lambda x: day_sort.index(x[0]))
     for x in list_d :
         print x[0]+' == '+str(x[1])

def main(csv_filename):
  countComplaintPerDay(csv_filename)

      
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
