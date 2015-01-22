##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 10                         #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1                                  #
##############################################
import csv,sys,os
from datetime import date,datetime
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

def main(filename):

  df = pd.read_csv(filename, parse_dates=True, index_col = 1)
  complaints = df[['Borough']]
  del df
  complaints = complaints[complaints.index!=pd.NaT]
  complaints['counter']=1

  plt.figure(figsize=(16,10))
  idx=0
  for key, group in complaints.groupby('Borough'):
    if key != 'Unspecified':
      temp_df = group.counter.resample('D', how="sum")
      temp_df.plot(label = key, x_compat=True)
      idx += 1
 
  plt.legend(loc='upper right', shadow=True)
  plt.grid(False)
  plt.ylim(0,2500)
  plt.xlabel('Time')
  plt.ylabel('Number of complaints')
  plt.title('Complaints per borough per day')
  plt.margins(.07,.07)
  plt.savefig('problem1.png')
  plt.show()

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print 'Usage:'
    print sys.argv[0] \
    + '< complaintsfilename>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' data/complaints.csv'
  else:
    main(sys.argv[1])
