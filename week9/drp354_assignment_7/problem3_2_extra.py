##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 7                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.3_2_extra                          #
##############################################

import argparse,csv, sys, os
from datetime import date,datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
from collections import OrderedDict,defaultdict
import statsmodels.api as sm

def main(csv_filename,zip_filename):

  #variable init
  agencyName=["NYPD",
              "DOT",
              "DOB",
              "TLC",
              "DPR"]
  zipComplaint = {}
  sumPerZip = {}

  #Reading the files
  with open(csv_filename, 'rb') as f:
    csvReader = csv.reader(f)
    headers = next(csvReader)
 
   #put initial value as max value->min and the opposite
    minDate=datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
    maxDate=datetime.strptime(date.min.isoformat(),"%Y-%m-%d")

    for row in csvReader:
      createdDate = row[1]
      agency = row[3]
      zipCode = row[8]
      
      #to find min and max time in a data range
      curDate = datetime.strptime(createdDate,"%m/%d/%Y %I:%M:%S %p") 
      minDate = min(minDate, curDate)
      maxDate = max(maxDate, curDate)

      #count agency volume
      if zipCode == "":
        continue
      if zipCode in zipComplaint:
        if agency in zipComplaint[zipCode]:
          zipComplaint[zipCode][agency] += 1
          sumPerZip[zipCode]['complaints'] += 1
        else:
          zipComplaint[zipCode][agency] = 1
          sumPerZip[zipCode]['complaints'] += 1
      else:
        zipComplaint[zipCode] = {}
        zipComplaint[zipCode][agency] = 1
        sumPerZip[zipCode] = {}
        sumPerZip[zipCode]['complaints'] = 1
      
 
  #sorting zip complaint to find out top 
  #complaint by agency for each zip code
  for zipIter in  zipComplaint:
    zipComplaint[zipIter]= OrderedDict(sorted(zipComplaint[zipIter].items(), key=lambda x: (-x[1])))
    for k,v in zipComplaint[zipIter].iteritems():
      sumPerZip[zipIter]['top']= k
      break
 
  #create lists of x and y for plotting
  x={}
  y={}
  x['all'] = []
  y['all'] = []
  for agenName in agencyName:
    x[agenName] = []
    y[agenName] = []
  

  #iterate second file (zip code - population)
  with open(zip_filename, 'r') as f2:
    csvReader2 = csv.reader(f2)
    headers = next(csvReader2) 
    for row in csvReader2:
      zipCode2 = row[0]
      population = int(row[1])

      if zipCode2 in zipComplaint:
        #appending total complaints
        #x['all'].append(population) #appending population
        #y['all'].append(sumPerZip[zipCode2]['complaints']) #appending number of complaint
        #appending complaints by agencies we are interested to observe
        for agenName in agencyName:
          if agenName in zipComplaint[zipCode2]:
            x[agenName].append(population) #appending population
            y[agenName].append(zipComplaint[zipCode2][agenName]) #appending number of complaint each top Agency
        else:
          pass
      else:
        pass


  #closing file after iteration process
  f.close()
  f2.close()

  #plot variable init
  title = "Population VS Number of complaints by zip code\n  %s - %s" % (minDate.strftime("%b/%d/%Y"),
                                                                         maxDate.strftime("%b/%d/%Y"))
  color = ['r','b','g','y','c']
  markr = ['o','^','8','s','h']

  # Create plots with pre-defined labels.
  plt.figure(figsize=(13, 13), dpi=80, facecolor='w', edgecolor='k')
  plt.title(title)
  
  #for agencies we are interested to estimate
  for n in xrange(0,len(agencyName)):
    #Fit regression model
    Xlist = sm.add_constant(x[agencyName[n]])
    Ylist = y[agencyName[n]]
    model = sm.OLS(Ylist, Xlist)
    result = model.fit()
    plt.plot(x[agencyName[n]], result.fittedvalues, c=color[n], alpha=0.5, linewidth=1.5)
    plt.scatter(x[agencyName[n]], y[agencyName[n]], c=color[n],marker=markr[n],s=45,
                label=(agencyName[n]+'\nBeta='+str(result.params[1])+'\nConst= '+str(result.params[0])),
                alpha=0.5, 
                edgecolors='none')
   
  # for other agencies
  #X = sm.add_constant(x['all'])
  #model = sm.OLS(y['all'], X)
  #result = model.fit()
  #plt.plot(x['all'], result.fittedvalues, 'k--', alpha=0.3, 
  #         linewidth=1)
  #plt.scatter(x['all'], y['all'], c='k',s=15,
  #            label=('All complaints\nBeta='+str(result.params[1])+'\nConst= '+str(result.params[0])),
  #            alpha=0.3, edgecolors='none')


  plt.legend(loc='upper left', shadow=True)
  plt.grid(True)
  plt.xlim(left=0)
  plt.ylim(bottom=0)
  plt.xlabel('Population by zip code')
  plt.ylabel('Number of complaints by zipcode')
  plt.savefig('figure_3_2_extra.png')
  plt.show()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  parser.add_argument("zip_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  zip_filename = args.zip_file
  main(csv_filename, zip_filename)
