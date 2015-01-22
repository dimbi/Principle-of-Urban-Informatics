import sys
import csv
import time

if len(sys.argv) != 2:
    print "Usage: python problem6.py filename"
    sys.exit()

datafilename = sys.argv[1]

#open file
agencyComplaintsByZip = {}
with open(datafilename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader,None)
    for row in reader:
        agency  = row[3]
        zipCode = row[7]
        #in case to test if either the zipcode or agency was blank
        # if zipCode == "" or agency == "":
        #     continue
        if agency in agencyComplaintsByZip:
            if zipCode in agencyComplaintsByZip[agency]:
                agencyComplaintsByZip[agency][zipCode] += 1
            else:
                agencyComplaintsByZip[agency][zipCode] = 1
        else:
            myDict = {}
            myDict[zipCode] = 1
            agencyComplaintsByZip[agency] = myDict

sortedAgencies = sorted(agencyComplaintsByZip.keys())

#print result
for agency in sortedAgencies:     
    counts = agencyComplaintsByZip[agency]
    maxCount = -1
    maxKey = ""
    for zip in counts:
        count = counts[zip]
        if count > maxCount:
            maxCount = count
            maxKey   = zip
    if maxCount == 0:
        assert(False)
        
    allMax = [z for z,t in counts.iteritems() if t == maxCount]
    strAllMax = " ".join(sorted(allMax))

    print "%s %s %d" % (agency,strAllMax,maxCount)
    
