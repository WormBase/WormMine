# Paulo Nuin November 2019

import sys
from sqlalchemy import create_engine

db_string = "postgres://postgres:interwormmine@localhost/" + sys.argv[1]
db = create_engine(db_string)
connection = db.connect()


if __name__ == '__main__':

    rnai_ids = open('to_remove_rnai.txt').read().splitlines()

    for i in rnai_ids:
        print(i)
        result = connection.execute("SELECT * from rnai where primaryidentifier = '%s'" % (i))
        for j in result:
            remark = j['remark']
            secondaryidentifier = j['secondaryidentifier']
            phenotyperemark = j['phenotyperemark']
            print(secondaryidentifier)
#            try:
#                new_remark = remark.replace('<![CDATA[', '').replace(']]>', '').replace('\'', '`')
#                print(new_remark)
#            except:
#                print('No remark')
#            try:
#                new_phenotyperemark = phenotyperemark.replace('<![CDATA[', '').replace(']]>', '').replace('\'', '`')
#                #print(new_phenotyperemark)
#            except Exception as e:
#                print(str(e))
#                print('failed')
            try:
                new_identifier = secondaryidentifier.replace('<![CDATA[', '').replace(']]>', '').replace('\'', '`')
                print(new_identifier)
            except:
                print('no secondary')
#            try:
#            connection.execute("UPDATE rnai SET remark = '%s' where primaryidentifier = '%s'" %  (new_remark, i))
            connection.execute("UPDATE rnai SET secondaryidentifier = '%s' where primaryidentifier = '%s'" %  (new_identifier, i))
#            connection.execute("UPDATE rnai SET phenotyperemark = '%s' where primaryidentifier = '%s'" %  (new_phenotyperemark, i))
#            print("UPDATE rnai SET phenotyperemark = '%s' where primaryidentifier = '%s'" %  (new_phenotyperemark, i))
#                result = connection.execute("SELECT * from anatomyterm where primaryidentifier = '%s'" % (i))
#                for k in result:
#                    print(k['definition'])
#            except Exception as e:
#                print('error', str(e))
