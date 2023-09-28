# Paulo Nuin March 2018

import sys

from sqlalchemy import create_engine, text

pg_creds = open("../pgcreds").read().strip()
db_string = f"postgresql://{pg_creds}@localhost/{sys.argv[1]}"
db = create_engine(db_string, isolation_level = 'AUTOCOMMIT')
connection = db.connect()


if __name__ == "__main__":

    gene_ids = open("to_remove_gene.txt").read().splitlines()
    print(gene_ids)

    for i in gene_ids:
        print(i)
        connection.execute(text("DELETE from GENE WHERE primaryidentifier = '%s'" % (i)))
