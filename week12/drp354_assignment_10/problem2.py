##############################################
##############################################
#      Principle of urban informatics        # 
#      Assignment 10                         #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2                                  #
##############################################
import csv,sys,os
from datetime import date,datetime
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
# Enable inline plotting

def main():

  # The inital set of baby names
  names = ['Bob','Jessica','Mary','John','Mel']
  np.random.seed(500)
  random_names = [names[np.random.randint(low=0,high=len(names))] for i in range(1000)]
  births = [np.random.randint(low=0,high=1000) for i in range(1000)]
  births[:10]
 
  BabyDataSet = zip(random_names,births)
  df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

  df.to_csv('births1880.txt',index=False,header=False)

  readTxt = 'births1880.txt'
  df = pd.read_csv(readTxt, header = None, names = ['Names','Births'])
  os.remove(readTxt)

  # Create a groupby object
  name = df.groupby('Names')

  # Apply the sum function to the groupby object
  df_sum = name.sum()
  Sorted = df_sum.sort(['Births'], ascending=False)
  Sorted.head(1)

  # Create graph
  plt.figure(figsize=(16,10))
  #df_sum['Births'].plot(kind='bar')
  Sorted['Births'].plot(kind='bar')

  # Print result
  print "The most popular name"
  print df_sum.sort(columns='Births', ascending=False)

  #display the plot
  plt.savefig('problem2.png')
  plt.show()

if __name__ == '__main__':
  main()
