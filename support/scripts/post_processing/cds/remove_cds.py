# Paulo Nuin March 2018

import sys
from sqlalchemy import create_engine

db_string = "postgres://postgres:interwormmine@localhost/" + sys.argv[1]
db = create_engine(db_string)
connection = db.connect()


if __name__ == '__main__':

    transcript_ids = open('to_remove_cds.txt').read().splitlines()

    for i in transcript_ids:
        print(i)
        connection.execute("DELETE from cds WHERE primaryidentifier = '%s'" % (i))
