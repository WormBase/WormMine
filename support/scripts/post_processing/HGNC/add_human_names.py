# Paulo Nuin July 2020

import sys
from sqlalchemy import create_engine

db_string = "postgres://postgres:interwormmine@localhost/" + sys.argv[1]
db = create_engine(db_string)
connection = db.connect()


if __name__ == '__main__':

    HGNC_ids = open('HGNC.txt').read().splitlines()

    symbols = { x.split('\t')[0]: x.split('\t')[1] for x in  HGNC_ids}


    human_query = connection.execute("SELECT * FROM gene WHERE primaryidentifier like '%%HGNC%%';")

    for gene in human_query:
        print(gene['primaryidentifier'], symbols[gene['primaryidentifier']])
        connection.execute("UPDATE gene SET secondaryidentifier = '%s' where primaryidentifier = '%s'" % (symbols[gene['primaryidentifier']], gene['primaryidentifier']))
