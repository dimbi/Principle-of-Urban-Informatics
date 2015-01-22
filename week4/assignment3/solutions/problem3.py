import datetime
import sys
import csv

hashtags1 = set()
with open(sys.argv[1], 'r') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    for h in row[4:]:
      hashtags1.add(h)


hashtags2 = set()
with open(sys.argv[2], 'r') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    for h in row[4:]:
      hashtags2.add(h)

inter = hashtags1.intersection(hashtags2)
sortable = []
for h in inter:
  sortable.append(h)

sortable.sort()

for s in sortable:
  print s