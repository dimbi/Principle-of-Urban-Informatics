import datetime
import sys
import csv
import operator

hashtags = {}
with open(sys.argv[1], 'r') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    for h in row[4:]:
      if h in hashtags:
        hashtags[h] += 1
      else:
        hashtags[h] = 1

#sortedcount = sorted(hashtags.iteritems(), key=operator.itemgetter(1), reverse=True)
sortedcount = sorted(hashtags.items(), key=lambda x: (-x[1],x[0]), reverse=False)

for s in sortedcount[0:10]:
  print s[0]+', '+str(s[1])