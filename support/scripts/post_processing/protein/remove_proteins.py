# Paulo Nuin March 2018

from sqlalchemy import create_engine

db_string = "postgres://postgres:interwormmine@localhost/intermine_dev_4_276_2"
db = create_engine(db_string)
connection = db.connect()


if __name__ == '__main__':

    gene_ids = open('to_remove.txt').read().splitlines()

    for i in gene_ids:
        print(i)
        connection.execute("DELETE from PROTEIN WHERE primaryidentifier = '%s'" % (i))
