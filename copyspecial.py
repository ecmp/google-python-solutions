#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


"""
##################################
Code written by (Jason) Rui Jia Ma
###################################
"""


import sys
import re
import os
import shutil
import commands
import zipfile

"""Copy Special exercise
"""

def get_special_paths(path, dirs):
    if os.path.isfile(path): dirs.append(path)
    elif os.path.exists(path):
        filenames = os.listdir(path)		
        for filename in filenames:
            newpath = os.path.join(path,filename)                  
            dirs.append(newpath)
            if os.path.isdir(newpath): get_special_paths(newpath,dirs)
    else: print "Directory <"+path+"> does not exist."
    return dirs

def copy_to(paths, todir):
    
    existing_files = []
    todir_len = len(todir)
    root = os.path.commonprefix(paths)
    root_len = len(root)
    dirname = os.path.dirname(todir)
    dir_len = len(dirname)
    
    if not os.path.exists(todir): os.mkdir(todir)        
    else:        
        existing_files = get_special_paths(todir, existing_files)
        for i in range(len(existing_files)):
            existing_files[i] = existing_files[i][todir_len:]
    
    for path in paths:
        if path[root_len-1:] not in existing_files and path != todir \
           and path[:todir_len+1] != todir+"\\":
            try:
                if os.path.isfile(path):
                    shutil.copy(path,todir)                
                elif os.path.isdir(path):
                    newdir = os.path.join(todir,path[root_len:])
                    shutil.copytree(path,newdir)
            except OSError: sys.stderr.write('***Problem copying: '+path+'\n')

		
def zip_to(paths, zippath):

    existing_files = []
    zippath_len = len(zippath)
    root = os.path.commonprefix(paths)
    root_len = len(root)
    
    if os.path.exists(zippath): 
	zf = zipfile.ZipFile(zippath, "a")
	existing_files = zf.namelist()
	print existing_files
    else: zf = zipfile.ZipFile(zippath, "w")
    for path in paths:
        print path[root_len:].replace("\\","/")
        if path[root_len:].replace("\\","/") not in existing_files and path[:zippath_len] != zippath:
            try: zf.write(path[root_len:])               
            except OSError: sys.stderr.write('***Problem zipping: '+path+'\n') 
    zf.close()


def main():
  args = sys.argv[1:7]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  todir = ''
  if len(args) > 0 and args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if len(args) > 0 and args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  path = os.path.abspath(args[0])
  paths = []
  paths = get_special_paths(path, paths)
  #for path in paths: print path
  if todir != '': copy_to(paths, os.path.abspath(todir))
  if tozip != '': zip_to(paths, os.path.abspath(tozip))
  	

  
if __name__ == "__main__":
  main()
