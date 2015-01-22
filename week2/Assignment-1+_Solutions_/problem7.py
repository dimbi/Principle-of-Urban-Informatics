import sys
import csv
import time

if len(sys.argv) != 3:
    print "Usage: python problem7.py [filename] [zip_borought]"
    sys.exit()

datafilename = sys.argv[1]
zipfilename = sys.argv[2]

#open complaints file
complaintsByZip = {}
with open(datafilename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader,None)
    for row in reader:
        zipCode = row[7]
        if zipCode in complaintsByZip:
            complaintsByZip[zipCode] += 1
        else:
            complaintsByZip[zipCode] = 1

#open zip-borough.csv
zipBorought = {}
with open(zipfilename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader,None)
    for row in reader:
        zipCode = row[0]
        borought = row[1]
        zipBorought[zipCode] = borought

#sum all complaints by borought
result = {}
for zipCode in complaintsByZip:
    borought = zipBorought[zipCode]
    complaints = complaintsByZip[zipCode]
    if borought in result:
        result[borought] += complaints
    else:
        result[borought] = complaints

#sort
for k in sorted(result, key=result.get, reverse=True):
    print k.title()+' with '+str(result[k])+' complaints'
