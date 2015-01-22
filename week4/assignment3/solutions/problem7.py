import datetime
import sys
import csv
import operator

with open(sys.argv[1], 'r') as csvfile:
  reader = csv.reader(csvfile)
  users = {}
  mindate = datetime.datetime.strptime(datetime.date.max.isoformat(), "%Y-%m-%d")
  maxdate = datetime.datetime.strptime(datetime.date.min.isoformat(), "%Y-%m-%d")
  for row in reader:
    date = datetime.datetime.strptime(row[1], "%a %b %d %H:%M:%S %Z %Y") #Fri Sep 19 21:00:18 EDT 2014
    mindate = min(mindate, date)
    maxdate = max(maxdate, date)

    if row[0] in users:
      users[row[0]] += 1
    else:
      users[row[0]] = 1

#sortedcount = sorted(users.iteritems(), key=operator.itemgetter(1), reverse=True)
sortedcount = sorted(users.items(), key=lambda x: (-x[1],x[0]), reverse=False)

print sortedcount[0][0]+' tweeted the most'
print 'Dataset range: '+mindate.strftime('%B %d %Y, %H:%M:%S')+' and '+maxdate.strftime('%B %d %Y, %H:%M:%S')
