import datetime
import sys
import csv

with open(sys.argv[1], 'r') as csvfile:
  reader = csv.reader(csvfile)
  users = set()
  mindate = datetime.datetime.strptime(datetime.date.max.isoformat(), "%Y-%m-%d")
  maxdate = datetime.datetime.strptime(datetime.date.min.isoformat(), "%Y-%m-%d")
  for row in reader:
    date = datetime.datetime.strptime(row[1], "%a %b %d %H:%M:%S %Z %Y") #Fri Sep 19 21:00:18 EDT 2014
    mindate = min(mindate, date)
    maxdate = max(maxdate, date)
    users.add(row[0])

  print str(len(users))+' users tweeted between '+mindate.strftime('%B %d %Y, %H:%M:%S')+' and '+maxdate.strftime('%B %d %Y, %H:%M:%S')
