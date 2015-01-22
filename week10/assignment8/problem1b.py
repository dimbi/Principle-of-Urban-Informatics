##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 8                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1_b                                #
##############################################

import argparse,csv,sys,os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def main(filename):

  df = pd.read_csv(filename,parse_dates=True, index_col=0)  
  df.plot(style='o--')
  plt.axhline(y=df.ix['2006-01'].ix[0,0], 
              linewidth=1, color='b',
              label = 'Apple 2006/01\nbaseline')
  plt.axhline(y=df.ix['2006-01'].ix[0,1], 
              linewidth=1, color='g',
              label = 'Microsoft 2006/01\nbaseline')
  plt.legend(loc='upper left', shadow=True,fontsize='small')
  plt.title('Stock Comparison')
  plt.xlabel('date')
  plt.ylabel('stock value')
  plt.savefig('problem1b.png')
  plt.show()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="enter dta file name / directory")
  args = parser.parse_args()
  filename = args.file
  main(filename)
