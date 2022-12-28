# Paulo Nuin November 2019
# modified March 2021

import sys

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

pg_creds = open("../pgcreds").read().strip()
db_string = f"postgresql://{pg_creds}@localhost/{sys.argv[1]}"
db = create_engine(db_string)
connection = db.connect()
Session = sessionmaker(bind=db)
session = Session()


def remove_wormpep():

    sql_text = """SELECT * FROM protein"""

    res = db.execute(text(sql_text))
    for row in res:
        if str(row['primaryidentifier']).find('wormpep') >= 0:
            print(row['primaryidentifier'])
            pid = row['id']
            identifier = row['primaryidentifier']
            new_identifier = identifier.replace('wormpep=', '')
            print(new_identifier, pid)
            connection.execute("UPDATE protein SET primaryidentifier = '%s'  where id = '%s'" % (new_identifier, pid))
            print(f"updated {identifier}")


if __name__ == '__main__':

    remove_wormpep()
