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
t = connection.begin()

def remove_remarks():

    sql_text = """SELECT * FROM rnai"""

    res = connection.execute(text(sql_text))
    for row in res:
        print(row[7])
        if str(row[7]).find("CDATA") >= 0:
            remark = row[7]
            new_remark = (
                remark.replace("<![CDATA[", "").replace("]]>", "").replace("'", "`")
            )
            print(new_remark)
            rnai_id = row[6]
            print(rnai_id)
            connection.execute(text(
                "UPDATE rnai SET remark = '%s' where primaryidentifier = '%s'"
                % (new_remark, rnai_id)
            ))
            print("updated " + rnai_id)
            print("\n")
    t.commit()


def remove_secondaryidentifier():

    sql_text = """SELECT * FROM rnai"""

    res = connection.execute(text(sql_text))
    for row in res:
        if str(row[12]).find("CDATA") >= 0:
            print(row[12])
            secondaryidentifier = row[12]
            new_identifier = (
                secondaryidentifier.replace("<![CDATA[", "")
                .replace("]]>", "")
                .replace("'", "`")
            )
            print(new_identifier)
            rnai_id = row[6]
            print(rnai_id)
            connection.execute(text(
                "UPDATE rnai SET secondaryidentifier = '%s' where primaryidentifier = '%s'"
                % (new_identifier, rnai_id)
            ))
            print("updated " + rnai_id)
            print("\n")
    t.commit()

def remove_phenotyperemark():

    sql_text = """SELECT * FROM rnai"""

    res = connection.execute(text(sql_text))
    print(res.keys())
    for row in res:
        if str(row[11]).find("CDATA") >= 0:
            print(row[11])
            phenotyperemark = row[11]
            new_remark = (
                phenotyperemark.replace("<![CDATA[", "")
                .replace("]]>", "")
                .replace("'", "`")
            )
            print(new_remark)
            rnai_id = row[6]
            print(rnai_id)
            try:
                connection.execute(text(
                    "UPDATE rnai SET phenotyperemark = '%s' where primaryidentifier = '%s'"
                    % (new_remark, rnai_id)
                ))
                print("updated " + rnai_id)
            except Exception as e:
                print("Error updating " + rnai_id + " " + str(e))
            print("\n")


if __name__ == "__main__":

#    remove_remarks()
#    remove_secondaryidentifier()
    remove_phenotyperemark()
