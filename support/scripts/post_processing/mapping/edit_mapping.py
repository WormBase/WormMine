# Paulo Nuin May 2021

import sys
from sqlalchemy import create_engine

#
# db_string = "postgres://postgres:interwormmine@localhost/" + sys.argv[1] + "?client_encoding=utf8"
# db = create_engine(db_string)
# connection = db.connect()

def process_mapping(mapping):

    mapping = ['IV', ':8.51401', '±0.001138']

    position, error = mapping[1], mapping[2]

    position = position[0] + '{:0.2f}'.format(float(position[1:]))
    error = error[0] + '{:0.2f}'.format(float(error[1:]))

    print(position, error)

def get_mapping():

    mappings = {}
    all_genes = connection.execute('select * from gene where mapping is not null')
    for row in all_genes:
       temp = row['mapping'].split(' ')
       to_add = [x for x in temp if x]
       mappings[row['primaryidentifier']] = to_add

    print(mappings)

if __name__ == '__main__':

    print('Reading mapping information from genes')

    # get_mapping()
    process_mapping('')

