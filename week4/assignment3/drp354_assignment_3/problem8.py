################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

import argparse,csv, sys, os
import re

def countTweets(filename):

  d_newyork = {}
  d_sanfran = {}
  sorted_newyork = []
  sorted_sanfran = []

  #reading CSV
  with open(filename, 'rb') as f:
    csvReader = csv.reader(f)
    for tokens in csvReader:
      #New York
      if (float(tokens[2]) > (-74.2557)) and (float(tokens[2])<(-73.6895)):
        if (float(tokens[3]) > (40.4957)) and (float(tokens[3])<(40.9176)):
          for hashtags in tokens[4:]:
            match = re.findall(r"#(\w+)", hashtags)
            if match:
              if hashtags in d_newyork:
                d_newyork[hashtags] += 1
              else:
                d_newyork[hashtags] = 1

      #San Fransisco
      elif (float(tokens[2]) > (-122.5155)) and (float(tokens[2])<(-122.3247)):
        if (float(tokens[3]) > (37.7038)) and (float(tokens[3])<(37.8545)):
          for hashtags in tokens[4:]:
            match = re.findall(r"#(\w+)", hashtags)
            if match:
              if hashtags in d_sanfran:
                d_sanfran[hashtags] += 1
              else:
                d_sanfran[hashtags] = 1

  #sorting
  sorted_newyork = sorted(d_newyork.iteritems(), key=lambda x: (-x[1],x[0]))
  sorted_sanfran = sorted(d_sanfran.iteritems(), key=lambda x: (-x[1],x[0]))
 
  #print
  print 'New York:'
  for k,v in sorted_newyork[:5]:
    print '%s, %s' % (k,v)
  print 'San Francisco:'
  for k,v in sorted_sanfran[:5]:
    print '%s, %s' % (k,v)

def main(csv_filename):
  countTweets(csv_filename)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="enter csv file name / directory")
  args = parser.parse_args()
  csv_filename = args.csv_file
  main(csv_filename)
