##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 8                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.3                                  #
##############################################
import argparse,csv,sys,os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def main(filename):

  dataList = []
  cpuName = []
  releasedYear = []
  numTransistor = []

  #iterate each row
  with open(filename, 'rb') as f:
    Reader = csv.reader(f)
    headers = next(Reader)
    for row in Reader:
      dataList.append((row[0],row[1],row[2]))

  dataListSorted = sorted(dataList, key=lambda x: (x[1]))
  for elem in dataListSorted:
    cpuName.append(elem[0])
    releasedYear.append(elem[1])
    numTransistor.append(elem[2])

  ind = np.arange(len(cpuName))
  #colors = ["ro","go","co","yo","ko","mo",
  #          "r^","g^","c^","y^","k^","m^","rs"]

  #plt.subplots(nrows=2,ncols=1,facecolor="white",figsize=(12,8))
  fig, ax = plt.subplots(1, 2,figsize=(15,8))

#figure 1
  #for n in xrange(0,len(cpuName)):
  #  ax[0].plot(ind[n], releasedYear[n], colors[n],
  #             label=(cpuName[n]),
  #             alpha=0.8)
  ax[0].plot(ind, releasedYear, 'ro',
             alpha=0.8)
  ax[0].xaxis.set_ticks(ind)
  ax[0].xaxis.set_ticklabels(cpuName,rotation='vertical')
  ax[0].set_ylabel('Year Released')
  ax[0].set_xlabel('Cpu Name')
  ax[0].grid(True)


  #figure 2
  #for n in xrange(0,len(cpuName)):
  #  ax[1].plot(ind[n], numTransistor[n], colors[n],
  #             label=(cpuName[n]),
  #             alpha=0.8)
  #ax[1].plot(ind,numTransistor, 'bo',
  #           alpha=0.8)
  ax[1].semilogy(ind, numTransistor, 'bo',basey=10)
  ax[1].xaxis.set_ticks(ind)
  ax[1].xaxis.set_ticklabels(cpuName,rotation='vertical')
  ax[1].set_ylabel('Number of transistor')
  ax[1].set_xlabel('Cpu Name')
  ax[1].grid(True)

  plt.suptitle('CPU progression from time to time')
  plt.savefig('problem3.png')
  plt.show()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="enter dta file name / directory")
  args = parser.parse_args()
  filename = args.file
  main(filename)
