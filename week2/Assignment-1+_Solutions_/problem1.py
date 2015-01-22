# Solution for problem:
#
# Read csv file and output range of complaints creation date, in the format
#   "month/day/year hour:minutes:seconds".
#
# e.g. output:
# 350567 complaints between 02/24/2003 09:20:06 and 08/23/2014 19:20:06
#
# @author Cesar Palomo <cesarpalomo@gmail.com>

from datetime import date, datetime
import csv
import os
import sys



# e.g. dateStr: 01/31/2014 12:00:00 AM
def dateFromInputDateStr(dateStr):
  return datetime.strptime(dateStr, "%m/%d/%Y %I:%M:%S %p")



# e.g. return: 01/31/2014 12:00:00 AM
def dateToOutputStr(d):
  return d.strftime("%m/%d/%Y %H:%M:%S")



# Problem 1 solution.
def solution(filename):
  minDate = datetime.strptime(date.max.isoformat(), "%Y-%m-%d")
  maxDate = datetime.strptime(date.min.isoformat(), "%Y-%m-%d")

  # Columns:
  # Unique Key,Created Date,...
  with open(filename) as f:
    csvReader = csv.reader(f)
    headers = next(csvReader)

    numRows = 0
    for row in csvReader:
      numRows += 1
      createDate = dateFromInputDateStr(row[1])
      if createDate < minDate:
        minDate = createDate
      if createDate > maxDate:
        maxDate = createDate

  print '%d complaints between %s and %s' % (numRows, \
  dateToOutputStr(minDate), dateToOutputStr(maxDate))



# Executes solution to problem 1 with provided input filename.
if __name__ == '__main__':
  # Runs with provided filename.
  solution(sys.argv[1])
