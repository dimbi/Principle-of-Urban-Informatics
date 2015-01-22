################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

import argparse,csv, sys, os

def countTweets(filename1, filename2):

  d_f1 = []
  d_f2 = []
  d_tweetsUnique = []
  f1 = open(filename1)
  f2 = open(filename2)

  for line in f1:
    line = line.strip()
    for tokens in line.split(','):
      if tokens.startswith('#'):
         if tokens in d_f1:
            pass
         else:
            d_f1.append(tokens)

  for line in f2:
    line = line.strip()
    for tokens in line.split(','):
      if tokens.startswith('#'):
         if tokens in d_f2:
            pass
         else:
            d_f2.append(tokens)

  d_tweetsUnique = sorted(set(d_f1).intersection(d_f2))

  for hashtag in d_tweetsUnique:
     print hashtag


def main(csv_filename1, csv_filename2):
  countTweets(csv_filename1, csv_filename2)

      
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file1", help="enter csv file name 1/ directory")
  parser.add_argument("csv_file2", help="enter csv file name 2/ directory")
  args = parser.parse_args()
  csv_filename1 = args.csv_file1
  csv_filename2 = args.csv_file2
  main(csv_filename1, csv_filename2)
