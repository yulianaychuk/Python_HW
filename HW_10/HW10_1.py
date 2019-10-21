'''
Created on Oct 9, 2019

@author: Yuliya_Naychuk
'''

import sqlite3
import csv
import os
import argparse

DB_FILE = 'tasks_projects.db'


def create_table_from_csv(csv_file_name, cur):
#     print(csv_file_name)
    table_name = csv_file_name.split('.')[0]  # Get table name from CSV file name
#     print(table_name)
    with open(csv_file_name, 'r') as f:
        reader = csv.reader(f)
#         print(reader)
        headers = next(reader)  # first call of 'next' method reads first line containing columns names followed with data types, separated by colon (':')
#         print(headers)
        headers_with_types = ', '.join(headers).replace(':', ' ')  # make string like 'field1 varchar, field2 date' for insertion in CREATE statement
        cur.execute('CREATE TABLE IF NOT EXISTS {}({})'.format(table_name, headers_with_types))

        for row in reader:  # row is a list of values
            qry = 'INSERT INTO {} VALUES ({})'.format(table_name,
                                                      ', '.join(['"{}"'.format(val) for val in row])  # quotes are required for strings with spaces
                                                      )
#             print(qry)
            cur.execute(qry)


# Recreate DB file, if exists
if __name__ == '__main__':
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    
    create_table_from_csv('Project.csv', cur)
    create_table_from_csv('Task.csv', cur)
    
    conn.commit()  # Apply table creation statements to DB 
    
    # Get project name as user parameter
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--project", type = str, required = True, help=r'Name of the project for select query from Task table')
    args = parser.parse_args()
    project = args.project
    print('project={}'.format(project))
    
    # Get project's records
    cur.execute('select * from Task where project = ?', (project,))
    rows = cur.fetchall()
    print('RESULT:')
    for row in rows:
        print(row)
     
    
    conn.close()

# Run Configurations:
#-p Family
# or
# python hw_10_1.py --project Family from cmd
