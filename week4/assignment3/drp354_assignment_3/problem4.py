################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

import argparse,csv, sys, os

def countTweets(filename):

  d_hashCount = {}

  f = open(filename)

  for line in f:
    line = line.strip()
    for tokens in line.split(','):
      if tokens.startswith('#'):
         if tokens in d_hashCount:
           d_hashCount[tokens] += 1
         else:
           d_hashCount[tokens] = 1

  sorted_hash = sorted(d_hashCount.iteritems(), key=lambda x: (-x[1],x[0]))  

  for k,v in sorted_hash[:10]:
    print '%s, %s' % (k,v)

def main(csv_filename):
  countTweets(csv_filename)

      
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
