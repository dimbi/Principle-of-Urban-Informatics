import datetime
import sys
import csv
import operator

with open(sys.argv[1], 'r') as csvfile:
  reader = csv.reader(csvfile)
  datecount = {}
  for row in reader:
    date = datetime.datetime.strptime(row[1], "%a %b %d %H:%M:%S %Z %Y") #Fri Sep 19 21:00:18 EDT 2014

    if date in datecount:
      datecount[date] += 1
    else:
      datecount[date] = 1

sortedcount = sorted(datecount.iteritems(), key=operator.itemgetter(1), reverse=True)

print sortedcount[0][0].strftime('%B %d %Y, %H:%M:%S')+' with '+str(sortedcount[0][1])+' tweets'