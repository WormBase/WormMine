# Paulo Nuin November 2019
# modified March 2021

import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:interwormmine@localhost/" + sys.argv[1]
db  = create_engine(db_string)
connection = db.connect()
Session = sessionmaker(bind=db)
session = Session()


def remove_remarks():
 
    sql_text = """SELECT * FROM rnai"""

    res = db.execute(text(sql_text))
    for row in res:
        if str(row['remark']).find('CDATA') >= 0:
            print(row['remark'])
            remark = row['remark']
            new_remark = remark.replace('<![CDATA[', '').replace(']]>', '').replace('\'', '`')
            print(new_remark)
            rnai_id = row['primaryidentifier']
            print(rnai_id)
            connection.execute("UPDATE rnai SET remark = '%s' where primaryidentifier = '%s'" %  (new_remark, rnai_id))
            print('updated ' + rnai_id)
            print('\n')


def remove_secondaryidentifier():

    sql_text = """SELECT * FROM rnai"""

    res = db.execute(text(sql_text))
    for row in res:
        if str(row['secondaryidentifier']).find('CDATA') >= 0:
            print(row['secondaryidentifier'])
            secondaryidentifier = row['secondaryidentifier']
            new_identifier = secondaryidentifier.replace('<![CDATA[', '').replace(']]>', '').replace('\'', '`')
            print(new_identifier)
            rnai_id = row['primaryidentifier']
            print(rnai_id)
            connection.execute("UPDATE rnai SET secondaryidentifier = '%s' where primaryidentifier = '%s'" %  (new_identifier, rnai_id))
            print('updated ' + rnai_id)
            print('\n')


def remove_phenotyperemark():

    sql_text = """SELECT * FROM rnai"""

    res = db.execute(text(sql_text))
    for row in res:
        if str(row['phenotyperemark']).find('CDATA') >= 0:
            print(row['phenotyperemark'])
            phenotyperemark = row['phenotyperemark']
            new_remark = phenotyperemark.replace('<![CDATA[', '').replace(']]>', '').replace('\'', '`')
            print(new_remark)
            rnai_id = row['primaryidentifier']
            print(rnai_id)
            try:
                connection.execute("UPDATE rnai SET phenotyperemark = '%s' where primaryidentifier = '%s'" %  (new_remark, rnai_id))
                print('updated ' + rnai_id)
            except:
                print('Error updating ' +  rnai_id)
            print('\n')


if __name__ == '__main__':

    remove_remarks()
    remove_secondaryidentifier()
    remove_phenotyperemark()

