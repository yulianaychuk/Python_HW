# readcsv.py -path_csv example.csv -col_name Marker_Strategy

import argparse
import csv
import sys

# parsing cmd line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-path_csv')
parser.add_argument('-col_name')
ns = parser.parse_args(sys.argv[1:])
# print(ns.path_cvs)
# print(ns.col_name)

# reading column
result = []
with open(ns.path_csv) as f:
    reader = csv.DictReader(f)  # read rows into a dictionary format
#     for row in reader:  # read a row as {column1: value1, column2: value2,...}
#         result.append(row[ns.col_name])
    result = [row[ns.col_name] for row in reader]
#         print('appended ' + row[ns.col_name])
print('\n'.join(result))
