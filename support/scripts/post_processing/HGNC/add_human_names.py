# Paulo Nuin July 2020

import sys
from sqlalchemy import create_engine

pg_creds = open("../pgcreds").read().strip()
db_string = f"postgresql://{pg_creds}@localhost/{sys.argv[1]}"
db = create_engine(db_string, client_encoding='utf8')
connection = db.connect()


if __name__ == '__main__':

    print('starting')
    HGNC_ids = open('HGNC.txt').read().splitlines()

    symbols = {x.split('\t')[0]: x.split('\t')[1] for x in HGNC_ids}
    try:
        human_query = connection.execute("SELECT * FROM gene WHERE primaryidentifier like '%%HGNC%%';")
        for g in human_query:
            print(g)
        for gene in human_query:
            print(gene['primaryidentifier'], symbols[gene['primaryidentifier']])
            connection.execute("UPDATE gene SET secondaryidentifier = '%s' where primaryidentifier = '%s'" % (symbols[gene['primaryidentifier']], gene['primaryidentifier']))
    except Exception as e:
        print(str(e))
