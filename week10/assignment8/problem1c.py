##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 8                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1_c                                #
##############################################

import argparse,csv,sys,os
from datetime import date,datetime
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.tools.plotting import scatter_matrix as scatter
from pandas.io.stata import read_stata as rd_stata
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

def main(filename):

  df = pd.read_csv(filename,parse_dates=True, index_col=0)  
  fig, axes = plt.subplots(1, 2)
  df['apple'].plot(style='bo--', ax=axes[0])
  df['microsoft'].plot(style='go--', ax=axes[1])
  axes[0].axhline(y=df.ix['2006-01'].ix[0,0], 
                  linewidth=1, color='b',
                  label = 'Apple 2006/01\nbaseline')
  axes[1].axhline(y=df.ix['2006-01'].ix[0,1], 
                  linewidth=1, color='g',
                  label = 'Microsoft 2006/01\nbaseline')
  axes[0].legend(loc='upper left', shadow=True, fontsize='small')
  axes[1].legend(loc='upper left', shadow=True, fontsize='small')
  axes[0].set_ylabel('stock value')
  axes[1].set_ylabel('stock value')
  axes[0].set_xlabel('date')
  axes[1].set_xlabel('date')
  axes[0].set_ylim(0,200)
  axes[1].set_ylim(0,200)
  plt.suptitle('Stock Comparison')
  plt.savefig('problem1c.png')
  plt.show()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="enter dta file name / directory")
  args = parser.parse_args()
  filename = args.file
  main(filename)
