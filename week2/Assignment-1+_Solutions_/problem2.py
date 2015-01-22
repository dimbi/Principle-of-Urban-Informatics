# Solution for problem:
#
# Use dictionary/list to break complaints into different complaint types, and
# output one complaint type per line, followed by the number of complaints of
# that type.
#
# e.g. output:
# Street Condition with 350 complaints
# Street Sign - Damaged with 121 complaints
# street condition with 54 complaints
#
# Notes: lines 1 and 3 are considered different, i.e., break into case-sensitive
# complaint types.
#
# @author Cesar Palomo <cesarpalomo@gmail.com>

import csv
import os
import sys

# Problem solution.
def solution(filename):
  complaintTypeCount = {}
  # Columns:
  # Unique Key,Created Date,Closed Date,Agency,Agency Name,Complaint Type,...
  with open(filename) as f:
    csvReader = csv.reader(f)
    headers = next(csvReader)

    for row in csvReader:
      complaintType = row[5]
      count = complaintTypeCount.setdefault(complaintType, 0)
      complaintTypeCount[complaintType] = count + 1

  for complaintType,count in complaintTypeCount.iteritems():
    print '%s with %d complaints' % (complaintType, count)



# Executes solution to problem with provided input filename.
if __name__ == '__main__':
  # Runs with provided filename.
  solution(sys.argv[1])
