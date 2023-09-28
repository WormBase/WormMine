# Paulo Nuin November 2019

import sys

from sqlalchemy import create_engine, text

pg_creds = open("../pgcreds").read().strip()
db_string = f"postgresql://{pg_creds}@localhost/{sys.argv[1]}"
db = create_engine(db_string, isolation_level = 'AUTOCOMMIT')
connection = db.connect()
t = connection.begin()

if __name__ == "__main__":

    anatomy_ids = open("to_remove_anatomy_term.txt").read().splitlines()

    for i in anatomy_ids:
        result = connection.execute(text(
            "SELECT * from anatomyterm where primaryidentifier = '%s'" % (i)
        ))
        for j in result:
            print(j[0])
            definition = j[0]
            new_definition = (
                definition.replace("<![CDATA[", "").replace("]]>", "").replace("'", "`")
            )
            print(new_definition)
            try:
                connection.execute(text(
                    "UPDATE anatomyterm SET definition = '%s' where primaryidentifier = '%s'"
                    % (new_definition, i)
                ))
                result = connection.execute(text(
                    "SELECT * from anatomyterm where primaryidentifier = '%s'" % (i)
                ))
                for k in result:
                    print(k[0])
            except Exception as e:
                print("error", str(e))
    t.commit()
