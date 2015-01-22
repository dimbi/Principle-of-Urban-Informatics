##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 8                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1_a                                #
##############################################

import argparse,csv,sys,os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import date,datetime

def main(filename):

  df = pd.read_csv(filename,parse_dates=True, index_col=0)  

  plt.figure(figsize=(12,8))
  df['apple'].plot(style='o-', rot= 'horizontal')
  plt.title('Apple Stock')
  plt.xlabel('Time')
  plt.ylabel('stock value')

  #xlim and ylim
  minDate = datetime(2005,12,01,00,00).date()
  maxDate = datetime(2008,10,01,00,00).date()
  plt.xlim(minDate,maxDate)
  plt.grid(False)
  plt.ylim(30,220)

  plt.savefig('problem1a.png')
  plt.show()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="enter dta file name / directory")
  args = parser.parse_args()
  filename = args.file
  main(filename)
