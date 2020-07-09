# Paulo Nuin July 2020

import sys
from sqlalchemy import create_engine

db_string = "postgres://postgres:interwormmine@localhost/" + sys.argv[1]
db = create_engine(db_string)
connection = db.connect()


if __name__ == '__main__':

    HGNC_ids = open('HGNC.txt').read().splitlines()

    symbols = { x.split('\t')[0]: x.split('\t')[1] for x in  HGNC_ids}

    for i in symbols:
        print(i, symbols[i])

#    for i in gene_ids:
#        print(i)
#        connection.execute("DELETE from GENE WHERE primaryidentifier = '%s'" % (i))
