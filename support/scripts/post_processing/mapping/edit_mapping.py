# Paulo Nuin May 2021

import sys
from sqlalchemy import create_engine, null


db_string = "postgresql://postgres:interwormmine@localhost/" + sys.argv[1] + "?client_encoding=utf8"
db = create_engine(db_string)
connection = db.connect()

def process_mapping(mapping):

    position, error = mapping[1], mapping[2]

    position = position[0] + str('{:0.2f}'.format(float(position[1:])))
    error = error[0] + str('{:0.2f}'.format(float(error[1:])))

    final_mapping = mapping[0] + position + ' '  + error[0] + ' ' + error[1:] + ' cM'
#    print(final_mapping)

    return final_mapping

def get_mapping():

    all_genes = connection.execute('select * from gene where mapping is not null')
    mappings = {}

    for row in all_genes:
        try:
           temp = row['mapping'].split(' ')
           to_add = [x for x in temp if x]
           mappings[row['primaryidentifier']] = process_mapping(to_add)
           # print(row['primaryidentifier'] + ' added')
        except Exception as e:
           if row['mapping'].startswith(':') or len(row['mapping']) < 5:
               mappings[row['primaryidentifier']] = None
#            print(str(e))

    # for i in mappings:
    #     print(i, mappings[i])

    return mappings

def update_mappings(mappings):

    for i in mappings:
        print(i, mappings[i])
        if mappings[i] == None:
            connection.execute("UPDATE gene SET mapping = '%s' where primaryidentifier = '%s'" % ('data unavailable', i))
        else:
            connection.execute("UPDATE gene SET mapping = '%s' where primaryidentifier = '%s'" % (mappings[i], i))

if __name__ == '__main__':

    print('Reading mapping information from genes')

    mappings = get_mapping()
    update_mappings(mappings)
#    process_mapping('')

