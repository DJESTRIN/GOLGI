#!/bin/python
"Dependencies"
import os
import argparse 

def delete_spaces(directory):
    os.chdir(directory)
    path = os.getcwd()
    filenames = os.listdir(path)
    for filename in filenames:
        os.rename(os.path.join(path,filename),os.path.join(path,filename.replace(' ','')))
        
if __name__=="__main__":
   # Command line interface
  parser = argparse.ArgumentParser(description="Remove spaces from filenames and folders ")
  parser.add_argument("--input", type=str, help="The directory containing the input mrxs files ",required=True)
  args = parser.parse_args()
  delete_spaces(args.input)
    