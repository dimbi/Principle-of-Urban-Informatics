################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

import argparse,csv, sys, os
from datetime import date,datetime

def countTweets(filename):

  d_tweetCount = {}
  sorted_tweetCount = []

  #reading CSV
  with open(filename, 'rb') as f:
     csvReader = csv.reader(f)

     #put initial value as max value->min and the opposite
     minDate=datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
     maxDate=datetime.strptime(date.min.isoformat(),"%Y-%m-%d")
    
     for row in csvReader:
       #storing to dictionaries
       if row[0] in d_tweetCount:
         d_tweetCount[row[0]] += 1
       else:
         d_tweetCount[row[0]] = 1

       #find time range
       tweetsTime = datetime.strptime(row[1],"%a %b %d %H:%M:%S %Z %Y") 
       #compare and find min and max date
       if tweetsTime < minDate:
         minDate = tweetsTime     
       if tweetsTime > maxDate:
         maxDate = tweetsTime    
       
     #count who tweeted the most
     #userTweetMost = max(d_tweetCount.keys(), key=lambda x: d_tweetCount[x])
     sorted_tweetCount = sorted(d_tweetCount.iteritems(), key=lambda x: (-x[1],x[0]))
     #print
     print '%s tweeted the most' % (sorted_tweetCount[0][0])
     print 'Dataset range: %s and %s' % (minDate.strftime("%B %d %Y, %H:%M:%S"), 
                                         maxDate.strftime("%B %d %Y, %H:%M:%S"))

def main(csv_filename):
  countTweets(csv_filename)

      
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
