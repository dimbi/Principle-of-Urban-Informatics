##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 8                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.4b                                 #
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
import statsmodels.formula.api as smf
from statsmodels.sandbox.regression.predstd import wls_prediction_std

def main(filename):

  df = pd.read_csv(filename)  
  fig, ax = plt.subplots(3, 1)
  correlationTable = df.corr(method='pearson', min_periods=1)
  correlationTable = correlationTable.sort(['A'], ascending=[0])
  geneName=correlationTable.ix[1:,0].index.tolist()

  for idx,gene in enumerate(geneName):
    ax[idx].set_title('A vs '+gene)
    ax[idx].scatter(df['A'], df[gene], c='b',marker='o',alpha=0.8)
    ax[idx].set_ylabel(gene)
    ax[idx].set_xlabel('A')
    ax[idx].set_xlim(0,1)
    ax[idx].set_ylim(0,1)
    ax[idx].grid(True)

    #Fit regression model
    #linear
    if idx == 0:
      X = sm.add_constant(df['A'])
      model = sm.OLS(df[gene], X)
      result = model.fit()
      ax[idx].plot(df['A'], result.fittedvalues, 'gs', alpha=1, 
                   linewidth=1.5,label=("linear fitted \nBeta = %.2f\nConts = %.2f"%(result.params[1],result.params[0])))
      ax[idx].legend(loc='lower right', shadow=True, fontsize="small")
    # cubic
    if idx == 1:
      model_cubic = smf.ols(formula='%s~ 1 + A+ I(A ** 2.0)'%(gene), data=df)
      result = model_cubic.fit()
      ax[idx].plot(df['A'], result.fittedvalues, 'gs', alpha=1, 
                   linewidth=1.5,label=("cubic fitted \nBeta = %.2f\nConts = %.2f"%(result.params[1],result.params[0])))
      ax[idx].legend(loc='lower right', shadow=True, fontsize="small")
    # 5 polynomial
    if idx == 2:
      model_poly = smf.ols(formula='%s~ 1 + A+ I(A ** 2.0)+ I(A ** 3.0)+ I(A ** 4.0)+ I(A ** 5.0)'%(gene), data=df)
      result = model_poly.fit()
      ax[idx].plot(df['A'], result.fittedvalues, 'gs', alpha=1, 
                   linewidth=1.5,label=("5 polynomial \nBeta = %.2f\nConts = %.2f"%(result.params[1],result.params[0])))
      ax[idx].legend(loc='lower right', shadow=True, fontsize="small")

  plt.suptitle('Correlation plot')
  plt.savefig('problem4b.png')
  plt.show()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="enter dta file name / directory")
  args = parser.parse_args()
  filename = args.file
  main(filename)
