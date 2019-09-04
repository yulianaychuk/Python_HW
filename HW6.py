'''
Created on Sep 4, 2019

@author: Yuliya_Naychuk
'''
# readcsv.py -path_cvs example.csv -col_name Marker_Strategy

import argparse
import csv
import sys

# parsing cmd line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-path_cvs')
parser.add_argument('-col_name')
ns = parser.parse_args(sys.argv[1:])
#print(ns.path_cvs)
#print(ns.col_name)

#------------

result = []
with open(ns.path_cvs) as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        result.append(row[ns.col_name])
        print(row[ns.col_name])
#print(result)
