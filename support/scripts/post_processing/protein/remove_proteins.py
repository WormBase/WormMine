# Paulo Nuin March 2018

import sys
from sqlalchemy import create_engine

db_string = "postgres://postgres:interwormmine@localhost/" + sys.argv[1]
db = create_engine(db_string)
connection = db.connect()


if __name__ == '__main__':

    gene_ids = open('to_remove_protein.txt').read().splitlines()

    for i in gene_ids:
        print(i)
        connection.execute("DELETE from PROTEIN WHERE primaryidentifier = '%s'" % (i))
