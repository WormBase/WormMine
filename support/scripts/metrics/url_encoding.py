# Paulo Nuin Feb 2021

import urllib.parse

queries = [

"""<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc">   <constraint path="Gene.organism.name" op="=" value="Caenorhabditis elegans"/> </query>""",
"""<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0000336"/> </query>""",
"""<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.secondaryIdentifier" code="B" op="IS NULL"/> </query>""",
"""<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="!=" value="SO:0000336"/> </query>""",
"""<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.CDSs" code="B" op="IS NOT NULL"/> </query>""",
"""<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B and C">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.CDSs" code="B" op="IS NULL"/>   <constraint path="Gene.biotype" code="C" op="!=" value="SO:0000336"/> </query>""",
]



if __name__ == '__main__':

    for i in queries:
        print(urllib.parse.quote(i))

