##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 7                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.3_1                                #
##############################################

import argparse,csv, sys, os
from datetime import date,datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
import statsmodels.api as sm

def main(csv_filename,zip_filename):
  
  zipComplaint = {}

  #Reading the files
  with open(csv_filename, 'rb') as f:
    csvReader = csv.reader(f)
    headers = next(csvReader)
 
   #put initial value as max value->min and the opposite
    minDate=datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
    maxDate=datetime.strptime(date.min.isoformat(),"%Y-%m-%d")

    for row in csvReader:
      zipCode = row[8]
      createdDate = row[1]
      
      #to find min and max time in a data range
      curDate = datetime.strptime(createdDate,"%m/%d/%Y %I:%M:%S %p") 
      minDate = min(minDate, curDate)
      maxDate = max(maxDate, curDate)

      #count agency volume
      if zipCode == "":
        continue
      if zipCode in zipComplaint:
        zipComplaint[zipCode] += 1
      else:
        zipComplaint[zipCode] = 1

  with open(zip_filename, 'r') as f2:
    csvReader2 = csv.reader(f2)
    headers = next(csvReader2) 
  
    #create lists of x and y for plotting
    x=[]
    y=[]

    for row in csvReader2:
      zipCode2 = row[0]
      population = int(row[1])
      if zipCode2 in zipComplaint:
        x.append(population) #adding population
        y.append(zipComplaint[zipCode2]) #appending number of complaint
      else:
        pass

  #closing file after iteration process
  f.close()
  f2.close()
  
  #Fit regression model
  X = sm.add_constant(x)
  model = sm.OLS(y, X)
  result = model.fit()
  #print result.summary()

  # Create plots with pre-defined labels.
  title = "Population VS Number of complaints by zip code\n  %s - %s" % (minDate.strftime("%b/%d/%Y"),
                                                                         maxDate.strftime("%b/%d/%Y"))
  plt.figure()
  plt.title(title)
  plt.scatter(x, y, c='g', 
              label='population vs complaints\nper zip code',
              alpha=0.3, 
              edgecolors='none')
  plt.plot(x, result.fittedvalues, 'r', alpha=0.7, 
           linewidth=1.5,label=('fitted model'))
  plt.text(90000, 4500, 'Beta=%s\nConst=%s'%(result.params[1],result.params[0]), style='italic', fontsize=9)

  plt.legend(loc='upper left', shadow=True)
  plt.grid(True)
  plt.xlim(left=0)
  plt.ylim(bottom=0)
  plt.xlabel('Population by zip code')
  plt.ylabel('Number of complaints by zipcode')
  plt.savefig('figure_3_1-fitted_model.png')
  plt.show()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  parser.add_argument("zip_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  zip_filename = args.zip_file
  main(csv_filename, zip_filename)
