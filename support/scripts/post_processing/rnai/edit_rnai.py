# Paulo Nuin November 2019

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


if __name__ == '__main__':

#    rnai_ids = open('to_remove_rnai.txt').read().splitlines()

    remove_remarks()


#     for i in rnai_ids:
#         print(i)
#         result = connection.execute("SELECT * from rnai where primaryidentifier = '%s'" % (i))
#         for j in result:
#             remark = j['remark']
#             secondaryidentifier = j['secondaryidentifier']
#             phenotyperemark = j['phenotyperemark']
#             print(secondaryidentifier)
# #            try:
# #                new_remark = remark.replace('<![CDATA[', '').replace(']]>', '').replace('\'', '`')
# #                print(new_remark)
# #            except:
# #                print('No remark')
# #            try:
# #                new_phenotyperemark = phenotyperemark.replace('<![CDATA[', '').replace(']]>', '').replace('\'', '`')
# #                #print(new_phenotyperemark)
# #            except Exception as e:
# #                print(str(e))
# #                print('failed')
#             try:
#                 new_identifier = secondaryidentifier.replace('<![CDATA[', '').replace(']]>', '').replace('\'', '`')
#                 print(new_identifier)
#             except:
#                 print('no secondary')
# #            try:
# #            connection.execute("UPDATE rnai SET remark = '%s' where primaryidentifier = '%s'" %  (new_remark, i))
#             connection.execute("UPDATE rnai SET secondaryidentifier = '%s' where primaryidentifier = '%s'" %  (new_identifier, i))
# #            connection.execute("UPDATE rnai SET phenotyperemark = '%s' where primaryidentifier = '%s'" %  (new_phenotyperemark, i))
# #            print("UPDATE rnai SET phenotyperemark = '%s' where primaryidentifier = '%s'" %  (new_phenotyperemark, i))
# #                result = connection.execute("SELECT * from anatomyterm where primaryidentifier = '%s'" % (i))
# #                for k in result:
# #                    print(k['definition'])
# #            except Exception as e:
# #                print('error', str(e))
