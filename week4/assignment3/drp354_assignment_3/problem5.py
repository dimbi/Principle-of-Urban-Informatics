################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

import argparse,csv, sys, os
from datetime import date,datetime

def countTweets(filename):

  d_tweetCount = {}

  #reading CSV
  with open(filename, 'rb') as f:
     csvReader = csv.reader(f)
    
     for row in csvReader:
       #input the date filed from csv file
       tweetsTime = datetime.strptime(row[1],"%a %b %d %H:%M:%S %Z %Y") 
       tweetsTime_str = tweetsTime.strftime("%B %d %Y, %H:%M:%S")
       if tweetsTime_str in d_tweetCount:
         d_tweetCount[tweetsTime_str]+= 1
       else:
         d_tweetCount[tweetsTime_str] = 1
 
  maxTweetTime = max(d_tweetCount.keys(), key=lambda x: d_tweetCount[x])
  
  print '%s with %d tweets' % (maxTweetTime, d_tweetCount[maxTweetTime])

def main(csv_filename):
  countTweets(csv_filename)

      
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
