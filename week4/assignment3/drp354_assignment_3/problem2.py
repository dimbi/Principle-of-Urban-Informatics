################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

import argparse,csv, sys, os
from datetime import date,datetime

uniqueTweets = []

def countTweets(filename):

  #reading CSV
  with open(filename, 'rb') as f:
     csvReader = csv.reader(f)
    
     #put initial value as max value->min and the opposite
     minDate=datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
     maxDate=datetime.strptime(date.min.isoformat(),"%Y-%m-%d")

     for row in csvReader:
         #counter for number of complaints
         if row[0] in uniqueTweets:
           pass
         else:
           uniqueTweets.append(row[0])

         #input the date filed from csv file
         creationDate = datetime.strptime(row[1],"%a %b %d %H:%M:%S %Z %Y") 

         #compare and find min and max date
         if creationDate < minDate:
           minDate = creationDate     
         if creationDate > maxDate:
           maxDate = creationDate        

     #print
     print '%d users tweeted between %s and %s' % (len(uniqueTweets), 
                                                       minDate.strftime("%B %d %Y, %H:%M:%S"), 
                                                       maxDate.strftime("%B %d %Y, %H:%M:%S"))

def main(csv_filename):
  countTweets(csv_filename)

      
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
