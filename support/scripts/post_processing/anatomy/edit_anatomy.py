# Paulo Nuin November 2019

from sqlalchemy import create_engine

db_string = "postgres://postgres:interwormmine@localhost/intermine_dev_4_276_2"
db = create_engine(db_string)
connection = db.connect()


if __name__ == '__main__':

    anatomy_ids = open('anatomy_ids.txt').read().splitlines()

    for i in anatomy_ids:
        result = connection.execute("SELECT * from anatomyterm where primaryidentifier = '%s'" % (i))
        for j in result:
            definition = j['definition']
            new_definition = definition.replace('<![CDATA[', '').replace(']]>', '').replace('\'', '`')
            print(new_definition)
            try:
                connection.execute("UPDATE anatomyterm SET definition = '%s' where primaryidentifier = '%s'" %  (new_definition, i))
                result = connection.execute("SELECT * from anatomyterm where primaryidentifier = '%s'" % (i))
                for k in result:
                    print(k['definition'])
            except Exception as e:
                print('error', str(e))
