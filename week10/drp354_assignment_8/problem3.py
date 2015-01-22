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

  fig, ax = plt.subplots(1, 2,figsize=(12,6),sharey=True)
  fig.subplots_adjust(left=0.05, right=0.9, top=0.9, bottom=0.1, wspace=0.2)
  ax[0].margins(.02,.02)
  ax[0].plot(releasedYear, ind, 'ro',
             alpha=0.8)
  ax[0].yaxis.set_ticks(ind)
  ax[0].yaxis.set_ticklabels(cpuName,rotation='horizontal')
  ax[0].set_xlabel('Year Released')
  ax[0].set_ylabel('Cpu Name')
  ax[0].yaxis.grid(True)
  ax[0].margins(.07,.07)

  ax[1].semilogx(numTransistor, ind, 'bs',basex=10)
  ax[1].yaxis.set_ticks(ind)
  ax[1].yaxis.set_ticklabels(cpuName,rotation='horizontal')
  ax[1].set_xlabel('Number of transistor')
  ax[1].yaxis.grid(True)
  ax[1].margins(.07,.07,tight=False)
  
  plt.suptitle('CPU progression from time to time', linespacing = 2)
  plt.savefig('problem3.png')
  plt.show()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="enter dta file name / directory")
  args = parser.parse_args()
  filename = args.file
  main(filename)
