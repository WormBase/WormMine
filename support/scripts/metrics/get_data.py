# Paulo Nuin Oct 2020

import json
import queries
import time
import urllib.parse
from intermine.webservice import Service

query_title = {
    'query_01': 'All live genes',
    'query_02': 'All pseudogenes',
    'query_03': 'All uncloned genes',
    'query_04': 'All cloned genes (minus pseudogenes)	',
    'query_05': 'All protein coding genes',
    'query_06': 'All non-coding genes',
    'query_07': 'All tRNA genes',
    'query_08': 'All rRNA genes',
    'query_09': 'All miRNA genes',
    'query_10': 'All piRNA genes',
    'query_11': 'All snRNA genes',
    'query_12': 'All snoRNA genes',
    'query_13': 'All lincRNA genes',
    'query_14': 'All asRNA genes',
    'query_15': 'All scRNA genes',
    'query_16': 'All unclassified ncRNA genes',
    'query_17': 'All genes with GO annotation',
    'query_18': 'All genes with GO experimental evidence',
    'query_19': 'All genes with phenotype',
    'query_20': 'All chromosomes (including mitochondrial)',
    'query_21': 'All distinct proteins',
    'query_22': 'All protein sequences',
    'query_23': 'All strains',
    'query_24': 'All alleles',
    'query_25': 'All SNPs',
    'query_26': 'All phenotypic alleles',
}

section = {
        'query_01': 'section_01',
        'query_02': 'section_01',
        'query_03': 'section_01',
        'query_04': 'section_01',
        'query_05': 'section_01',
        'query_06': 'section_01',
        'query_07': 'section_02',
        'query_08': 'section_02',
        'query_09': 'section_02',
        'query_10': 'section_02',
        'query_11': 'section_02',
        'query_12': 'section_02',
        'query_13': 'section_02',
        'query_14': 'section_02',
        'query_15': 'section_02',
        'query_16': 'section_02',
        'query_17': 'section_03',
        'query_18': 'section_03',
        'query_19': 'section_03',
        'query_20': 'section_04',
        'query_21': 'section_05',
        'query_22': 'section_05',
        'query_23': 'section_06',
        'query_24': 'section_07',
        'query_25': 'section_07',
        'query_26': 'section_07',

}
xml = {

'query_01': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc">   <constraint path="Gene.organism.name" op="=" value="Caenorhabditis elegans"/> </query>""",
'query_02': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0000336"/> </query>""",
'query_03': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.secondaryIdentifier" code="B" op="IS NULL"/> </query>""",
'query_04': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="!=" value="SO:0000336"/> </query>""",
'query_05': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.CDSs" code="B" op="IS NOT NULL"/> </query>""",
'query_06': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B and C">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.CDSs" code="B" op="IS NULL"/>   <constraint path="Gene.biotype" code="C" op="!=" value="SO:0000336"/> </query>""",
'query_07': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0001272"/> </query>""",
'query_08': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0001637"/> </query>""",
'query_09': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0001265"/> </query>""",
'query_10': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0001638"/> </query>	""",
'query_11': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0001268"/> </query>""",
'query_12': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0001267"/> </query>""",
'query_13': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0001641"/> </query>""",
'query_14': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0002182"/> </query>""",
'query_15': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0001266"/> </query>""",
'query_16': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.biotype" code="B" op="=" value="SO:0001263"/> </query>""",
'query_17': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B">   <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Gene.goAnnotation" code="B" op="IS NOT NULL"/> </query>""",
'query_18': """<query name="" model="genomic" view="Gene.primaryIdentifier Gene.secondaryIdentifier Gene.symbol" longDescription="" sortOrder="Gene.primaryIdentifier asc" constraintLogic="A and B and C and (D or E or F or G or H or I or J or K or L or M or N)"> <constraint path="Gene.organism.name" code="A" op="=" value="Caenorhabditis elegans"/> <constraint path="Gene.goAnnotation.qualifier" code="B" op="!=" value=" NOT|enables"/> <constraint path="Gene.goAnnotation.qualifier" code="C" op="!=" value=" NOT|enables"/> <constraint path="Gene.goAnnotation.evidence.code.name" code="D" op="=" value="Inferred from Direct Assay"/> <constraint path="Gene.goAnnotation.evidence.code.name" code="E" op="=" value="Inferred from Experiment"/> <constraint path="Gene.goAnnotation.evidence.code.name" code="F" op="=" value="Inferred from Expression Pattern "/> <constraint path="Gene.goAnnotation.evidence.code.name" code="G" op="=" value="Inferred from Genetic Interaction"/> <constraint path="Gene.goAnnotation.evidence.code.name" code="H" op="=" value="Inferred from High Throughput Direct Assay"/> <constraint path="Gene.goAnnotation.evidence.code.name" code="I" op="=" value="Inferred from High Throughput Experiment"/> <constraint path="Gene.goAnnotation.evidence.code.name" code="J" op="=" value="Inferred from High Throughput Expression Pattern"/> <constraint path="Gene.goAnnotation.evidence.code.name" code="K" op="=" value="Inferred from Hight Throughput Mutant Phenotype"/> <constraint path="Gene.goAnnotation.evidence.code.name" code="L" op="=" value="Inferred from Mutant Phenotype"/> <constraint path="Gene.goAnnotation.evidence.code.name" code="M" op="=" value="Inferred from Physical Interaction"/> <constraint path="Gene.goAnnotation.evidence.code.name" code="N" op="=" value="nferred from High Throughput Genetic Interaction"/> </query>""",
'query_19': """<query model="genomic" view="Gene.primaryIdentifier Gene.symbol Gene.secondaryIdentifier Gene.organism.name" ><constraint path="Gene" op="IN" value="metrics_list_union" code="A" /></query>""",
'query_20': """<query name="" model="genomic" view="Chromosome.primaryIdentifier" longDescription="" sortOrder="Chromosome.primaryIdentifier asc">   <constraint path="Chromosome.organism.name" op="=" value="Caenorhabditis elegans"/> </query>""",
'query_21': """<query name="" model="genomic" view="Protein.primaryIdentifier Protein.symbol" longDescription="" sortOrder="Protein.primaryIdentifier asc">   <constraint path="Protein.organism.name" op="=" value="Caenorhabditis elegans"/> </query>""",
'query_22': """<query name="" model="genomic" view="Protein.primaryIdentifier Protein.symbol Protein.sequence.residues" longDescription="" sortOrder="Protein.primaryIdentifier asc">   <constraint path="Protein.organism.name" op="=" value="Caenorhabditis elegans"/> </query>""",
'query_23': """<query name="" model="genomic" view="Strain.primaryIdentifier Strain.name" longDescription="" sortOrder="Strain.primaryIdentifier asc">   <constraint path="Strain.species" op="=" value="Caenorhabditis elegans"/> </query>""",
'query_24': """<query name="" model="genomic" view="Allele.primaryIdentifier Allele.symbol" longDescription="" sortOrder="Allele.primaryIdentifier asc"><constraint path="Allele.species" op="=" value="Caenorhabditis elegans"/></query>""",
'query_25': """<query name="" model="genomic" view="Allele.primaryIdentifier Allele.symbol" longDescription="" sortOrder="Allele.primaryIdentifier asc" constraintLogic="A and (B or C)">   <constraint path="Allele.species" code="A" op="=" value="Caenorhabditis elegans"/>   <constraint path="Allele.type" code="B" op="=" value="SNP"/>   <constraint path="Allele.type" code="C" op="=" value="Predicted_SNP"/> </query>""",
'query_26': """<query name="" model="genomic" view="Allele.primaryIdentifier Allele.symbol" longDescription="" sortOrder="Allele.primaryIdentifier asc"constraintLogic="A and B"><constraint path="Allele.species" code="A" op="=" value="Caenorhabditis elegans"/><constraint path="Allele.phenotype"code="B" op="IS NOT NULL"/> </query>""",
}

# %3Cquery%20model%3D%22genomic%22%20view%3D%22RNAi.primaryIdentifier%20RNAi.inhibitsGene.primaryIdentifier%20RNAi.inhibitsGene.secondaryIdentifier%20RNAi.inhibitsGene.symbol%20RNAi.organism.name%20RNAi.strain.primaryIdentifier%22%20sortOrder%3D%22RNAi.primaryIdentifier%20ASC%22%20name%3D%22rnai_phenotype%22%20%3E%0A%20%20%3Cjoin%20path%3D%22RNAi.organism%22%20style%3D%22OUTER%22%2F%3E%0A%20%20%3Cjoin%20path%3D%22RNAi.strain%22%20style%3D%22OUTER%22%2F%3E%0A%20%20%3Cconstraint%20path%3D%22RNAi.phenotype_not_observed.identifier%22%20op%3D%22%3D%22%20value%3D%22WBPhenotype%3A0000535%22%20code%3D%22A%22%20%2F%3E%0A%3C%2Fquery%3E%0A&trail=%7Cquery&method=xml
def run_queries():
    service = Service('http://intermine.wormbase.org/tools/wormmine/service')

    for x in dir(queries):
        item = getattr(queries, x)
        if callable(item):
            if not item.__name__ in ['assert_result', 'Service', 'assert_greater', 'save_txt_file']:
                time.sleep(1)
                yield x, item()


if __name__ == '__main__':

    prepend = 'http://intermine.wormbase.org/tools/wormmine/loadQuery.do?skipBuilder=true&query='
    append = '%0A&trail=%7Cquery&method=xml'

    output_sec1 = open('../section_01.json', 'w')
    output_sec2 = open('../section_02.json', 'w')
    output_sec3 = open('../section_03.json', 'w')
    output_sec4 = open('../section_04.json', 'w')
    output_sec5 = open('../section_05.json', 'w')
    output_sec6 = open('../section_06.json', 'w')
    output_sec7 = open('../section_07.json', 'w')

    print('Running')
    all_queries = run_queries()
    results_sec1, results_sec2, results_sec3 = {}, {}, {}
    results_sec4, results_sec5, results_sec6, results_sec7 = {}, {}, {}, {}
    for q in all_queries:
        print(q)
        qurl = urllib.parse.quote(xml[q[0]])
        if section[q[0]] == 'section_01':
            results_sec1[q[0]] = {'value': q[1], 'title': query_title[q[0]], 'url': prepend + qurl + append}
        elif section[q[0]] == 'section_02':
            results_sec2[q[0]] = {'value': q[1], 'title': query_title[q[0]], 'url': prepend + qurl + append}
        elif section[q[0]] == 'section_03':
            results_sec3[q[0]] = {'value': q[1], 'title': query_title[q[0]], 'url': prepend + qurl + append}
        elif section[q[0]] == 'section_04':
            results_sec4[q[0]] = {'value': q[1], 'title': query_title[q[0]], 'url': prepend + qurl + append}
        elif section[q[0]] == 'section_05':
            results_sec5[q[0]] = {'value': q[1], 'title': query_title[q[0]], 'url': prepend + qurl + append}
        elif section[q[0]] == 'section_06':
            results_sec6[q[0]] = {'value': q[1], 'title': query_title[q[0]], 'url': prepend + qurl + append}
        elif section[q[0]] == 'section_07':
            results_sec7[q[0]] = {'value': q[1], 'title': query_title[q[0]], 'url': prepend + qurl + append}

    json.dump(results_sec1, output_sec1)
    json.dump(results_sec2, output_sec2)
    json.dump(results_sec3, output_sec3)
    json.dump(results_sec4, output_sec4)
    json.dump(results_sec5, output_sec5)
    json.dump(results_sec6, output_sec6)
    json.dump(results_sec7, output_sec7)

#     output_json = open('../results.json', 'w')
#     json.dump(results, output_json)
#     output_json.close()

