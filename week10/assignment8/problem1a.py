##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 8                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1_a                                #
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
  df["apple"].plot(style='o--')
  plt.title('Apple Stock')
  plt.xlabel('date')
  plt.ylabel('stock value')
  plt.savefig('problem1a.png')
  plt.show()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="enter dta file name / directory")
  args = parser.parse_args()
  filename = args.file
  main(filename)
