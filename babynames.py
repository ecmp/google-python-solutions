#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


"""
##################################
Code written by (J)RJM
###################################
"""


import sys
import re

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename,'rU')
  namelist = []
  for line in f:
  	  year = re.search(r'Popularity in (\d\d\d\d)',line)
  	  if year: namelist.append(year.group(1))
  	  rank_name = re.search(r'<tr align="right"><td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>',line)
  	  if rank_name: 
  	  	  namelist.extend([rank_name.group(3)+' '+rank_name.group(1), 
  	  	  	  			  rank_name.group(2)+' '+rank_name.group(1)])
  f.close()
  alist = sorted(namelist[1:len(namelist)],key=lambda a:int(re.search('[\d]+',a).group()),reverse=True)
  return namelist[0:1]+alist


def main():
  args = sys.argv[1:4]
  print args

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  infile = args[0]
  output = extract_names(infile)
  if summary:
  	  outfile = args[1]
  	  f = open(outfile,'w')
  	  for i in [2*i for i in range(len(output)/2+1)]:
  	  	  if i == 0: f.write('POPULAR BABY NAMES IN YEAR '+ output[i]+'\n\n')
  	  	  else: f.write(output[i-1]+'\t\t'+output[i]+'\n')
  	  f.close()
  else: print output
  
if __name__ == '__main__':
  main()
