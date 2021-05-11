# Paulo Nuin May 2021

import sys
from sqlalchemy import create_engine


db_string = "postgres://postgres:interwormmine@localhost/" + sys.argv[1] + "?client_encoding=utf8"
db = create_engine(db_string)
connection = db.connect()


if __name__ == '__main__':

    print('Reading mapping information from genes')

    mappings = {}
    all_genes = connection.execute('select * from gene where mapping is not null')
    for row in all_genes:
        temp = row['mapping'].split(' ')
        to_add = [x for x in temp if x]
        mappings[row['primaryidentifier']] = to_add
 
    print(mappings)
