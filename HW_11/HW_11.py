import argparse
import csv
from pymongo import MongoClient


def connect_mongo_db(db_name, host='localhost', port=27017, username=None, password=None):
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    # Remove DB if exists
    if db_name in conn.list_database_names():
        conn.drop_database(db_name)

    return conn[db_name]  # Create empty database, return its pointer (object)


def create_table_from_csv(csv_file_name, db):
    table_name = csv_file_name.split('.')[0]  # Get table name from CSV file name
    with open(csv_file_name, 'r') as f:
        reader = csv.DictReader(f)
#         print (reader.fieldnames)
        mycol = db[table_name]
        for row in reader:  # insert rows one by one to avoid maximum memory usage (in case of huge CSV file)
            mycol.insert_one(row)


if __name__ == '__main__':

    # Get project name as user parameter
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--status", type = str, required = True, help=r'Enter task status') #Run configurations: -s ongoing
    args = parser.parse_args()
    print('status={}'.format(args.status))

    # Connect to mongo db (recreate if exists)
    db = connect_mongo_db('tasks_projects')

    # Fill collections (tables) from CSV files
    create_table_from_csv('Task.csv', db)
    create_table_from_csv('Project.csv', db)

    # Fetch documents (records) by provided status
    for row in db.Task.find({'status': args.status}):
        print(row)

#Run Configurations: -s ongoing