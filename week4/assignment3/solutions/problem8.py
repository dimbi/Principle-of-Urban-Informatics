import datetime
import sys
import csv
import operator

hashtags_ny = {}
hashtags_sf = {}
with open(sys.argv[1], 'r') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:

    lon = float(row[2])
    lat = float(row[3])

    if(lon >= -74.2557 and lon <= -73.6895 and lat >= 40.4957 and lat <= 40.9176):
      for h in row[4:]:
        if h in hashtags_ny:
          hashtags_ny[h] += 1
        else:
          hashtags_ny[h] = 1
    elif(lon >= -122.5155 and lon <= -122.3247 and lat >= 37.7038 and lat <= 37.8545):
      for h in row[4:]:
        if h in hashtags_sf:
          hashtags_sf[h] += 1
        else:
          hashtags_sf[h] = 1

#sortedcount_ny = sorted(hashtags_ny.iteritems(), key=operator.itemgetter(1), reverse=True)
#sortedcount_sf = sorted(hashtags_sf.iteritems(), key=operator.itemgetter(1), reverse=True)
sortedcount_ny = sorted(hashtags_ny.items(), key=lambda x: (-x[1],x[0]), reverse=False)
sortedcount_sf = sorted(hashtags_sf.items(), key=lambda x: (-x[1],x[0]), reverse=False)

print 'New York:'
for s in sortedcount_ny[0:5]:
  print s[0]+', '+str(s[1])

print 'San Francisco:'
for s in sortedcount_sf[0:5]:
  print s[0]+', '+str(s[1])