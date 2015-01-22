import datetime
import sys
import csv

with open(sys.argv[1], 'r') as csvfile:
  reader = csv.reader(csvfile)
  tweets = 0
  mindate = datetime.datetime.strptime(datetime.date.max.isoformat(), "%Y-%m-%d")
  maxdate = datetime.datetime.strptime(datetime.date.min.isoformat(), "%Y-%m-%d")
  for row in reader:
    date = datetime.datetime.strptime(row[1], "%a %b %d %H:%M:%S %Z %Y") #Fri Sep 19 21:00:18 EDT 2014
    mindate = min(mindate, date)
    maxdate = max(maxdate, date)
    tweets+=1

  print 'There were '+str(tweets)+' tweets between '+mindate.strftime('%B %d %Y, %H:%M:%S')+' and '+maxdate.strftime('%B %d %Y, %H:%M:%S')
