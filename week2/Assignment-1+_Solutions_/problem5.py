import sys
import csv
import time

if len(sys.argv) != 2:
    print "Usage: python problem5.py filename"
    sys.exit()

datafilename = sys.argv[1]

#open file
countComplaintsPerWeekDay = {}
with open(datafilename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader,None)
    format_string = "%m/%d/%Y %H:%M:%S %p"
    for row in reader:
        strCreatedDate = row[1]
        stTime = time.strptime(strCreatedDate,format_string)
        dayOfWeek = stTime.tm_wday
        if dayOfWeek in countComplaintsPerWeekDay:
            countComplaintsPerWeekDay[dayOfWeek] += 1
        else:
            countComplaintsPerWeekDay[dayOfWeek] = 1


#print output 
dayToString = {}
dayToString[0] = 'Monday'
dayToString[1] = 'Tuesday'
dayToString[2] = 'Wednesday'
dayToString[3] = 'Thursday'
dayToString[4] = 'Friday'
dayToString[5] = 'Saturday'
dayToString[6] = 'Sunday'

for i in xrange(0,7):
    count = 0
    if i in countComplaintsPerWeekDay:
        count = countComplaintsPerWeekDay[i]
    print '%s == %d'%(dayToString[i],count)
