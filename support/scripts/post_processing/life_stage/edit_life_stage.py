# Paulo Nuin August 2019

import sys

from sqlalchemy import create_engine

pg_creds = open("../pgcreds").read().strip()
db_string = f"postgresql://{pg_creds}@localhost/{sys.argv[1]}"
db = create_engine(db_string)
connection = db.connect()


if __name__ == "__main__":

    life_stage = open(sys.argv[1]).read().splitlines()
    to_change = {}
    for i in range(0, len(life_stage)):
        if life_stage[i].startswith("Life"):
            ls = life_stage[i].split(": ")[-1].replace('"', "")
            pn = life_stage[i + 1].split("\t")[-1].replace('"', "")
        to_change[ls] = pn

    for i in to_change:
        print(i)
        print(
            "UPDATE lifestage set publicname = '%s' WHERE primaryidentifier = '%s'"
            % (to_change[i], i)
        )
        connection.execute(
            "UPDATE lifestage set publicname = '%s' WHERE primaryidentifier = '%s'"
            % (to_change[i], i)
        )
