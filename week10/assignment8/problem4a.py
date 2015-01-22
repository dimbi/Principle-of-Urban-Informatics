##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 8                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.4a                                 #
##############################################
import argparse,csv,sys,os
from datetime import date,datetime
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from pandas.tools.plotting import scatter_matrix as scatter
from pandas.io.stata import read_stata as rd_stata
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

def main(filename):

  df = pd.read_csv(filename)  
  correlationTable = df.corr(method='pearson', min_periods=1)
  print correlationTable
  correlationTable = correlationTable.sort(['A'], ascending=[0])
  geneName=correlationTable.ix[:,0].index.tolist()
  print "Correlation in descending: %s, %s, %s, %s" % (geneName[0],
                                                       geneName[1],
                                                       geneName[2],
                                                       geneName[3])
  df = df.reindex(columns=geneName)
  pd.scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
  plt.suptitle('Correlation Scattermatrix\nA,B,C,D')
  plt.savefig('problem4a.png')


  plt.show()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="enter dta file name / directory")
  args = parser.parse_args()
  filename = args.file
  main(filename)
