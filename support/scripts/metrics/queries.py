# Paulo Nuin Oct 2020

from intermine.webservice import Service
service = Service("http://intermine.wormbase.org/tools/wormmine/service")

def query_01():
    """
    All live genes
    """

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")


    return len(query.rows())

def query_02():
    """
    All pseudogenes
    """

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0000336", code="B")

    return len(query.rows())

def query_03():
    """
    All uncloned genes
    """

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("secondaryIdentifier", "IS NULL", code="B")

    return len(query.rows())

def query_04():
    """
    All cloned genes (minus pseudogenes)
    """

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "!=", "SO:0000336", code="B")

    return len(query.rows())


def query_05():
    """
    All protein coding genes
    """

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("CDSs", "IS NOT NULL", code="B")

    return len(query.rows())

def query_06():
    """
    All non-coding genes
    """

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("CDSs", "IS NULL", code="B")
    query.add_constraint("biotype", "!=", "SO:0000336", code="C")

    return len(query.rows())


def query_07():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0001272", code="B")

    return len(query.rows())


def query_08():


    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0001637", code="B")

    return len(query.rows())


def query_09():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0001265", code="B")

    return len(query.rows())

def query_10():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0001638", code="B")

    return len(query.rows())

def query_11():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0001268", code="B")

    return len(query.rows())

def query_12():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0001267", code="B")

    return len(query.rows())

def query_13():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0001641", code="B")

    return len(query.rows())

def query_14():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0002182", code="B")

    return len(query.rows())

def query_15():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0001266", code="B")

    return len(query.rows())

def query_16():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("biotype", "=", "SO:0001263", code="B")

    return len(query.rows())

def query_17():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("goAnnotation", "IS NOT NULL", code="B")

    return len(query.rows())

def query_18():

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("goAnnotation.qualifier", "!=", " NOT|enables", code="B")
    query.add_constraint("goAnnotation.qualifier", "!=", " NOT|enables", code="C")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "Inferred from Direct Assay", code="D")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "Inferred from Experiment", code="E")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "Inferred from Expression Pattern ", code="F")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "Inferred from Genetic Interaction", code="G")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "Inferred from High Throughput Direct Assay", code="H")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "Inferred from High Throughput Experiment", code="I")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "Inferred from High Throughput Expression Pattern", code="J")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "Inferred from Hight Throughput Mutant Phenotype", code="K")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "Inferred from Mutant Phenotype", code="L")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "Inferred from Physical Interaction", code="M")
    query.add_constraint("goAnnotation.evidence.code.name", "=", "nferred from High Throughput Genetic Interaction", code="N")
    query.set_logic("A and B and C and (D or E or F or G or H or I or J or K or L or M or N)")

    return len(query.rows())

def query_19():

    iden_list = []
    iden_list2 = []

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("allele.phenotype", "IS NOT NULL", code="B")

    for row in query.rows():
        iden_list.append(row['primaryIdentifier'])

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "secondaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("RNAiResult.phenotype", "IS NOT NULL", code="B")

    for row in query.rows():
        iden_list2.append(row['primaryIdentifier'])

    return len(set(iden_list).union(iden_list2))


def query_20():

    query = service.new_query("Chromosome")
    query.add_view("primaryIdentifier")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")

    return len(query.rows())


def query_21():

    query = service.new_query("Protein")
    query.add_view("primaryIdentifier", "symbol")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")

    return len(query.rows())


def query_22():

    query = service.new_query("Protein")
    query.add_view("primaryIdentifier", "symbol", "sequence.residues")
    query.add_constraint("organism.name", "=", "Caenorhabditis elegans", code="A")

    return len(query.rows())

def query_23():

    query = service.new_query("Strain")
    query.add_view("primaryIdentifier", "name")
    query.add_constraint("species", "=", "Caenorhabditis elegans", code="A")

    return len(query.rows())

def query_24():

#     query = service.new_query("Allele")
#     query.add_view("primaryIdentifier", "symbol")
#     query.add_constraint("species", "=", "Caenorhabditis elegans", code="A")
#
#     return len(query.rows())

    return 1858087

def query_25():

#     query = service.new_query("Allele")
#     query.add_view("primaryIdentifier", "symbol")
#     query.add_constraint("species", "=", "Caenorhabditis elegans", code="A")
#     query.add_constraint("type", "=", "SNP", code="B")
#     query.add_constraint("type", "=", "Predicted_SNP", code="C")
#     query.set_logic("A and (B or C)")
#
#     return len(query.rows())

    return 290017

def query_26():

    query = service.new_query("Allele")
    query.add_view("primaryIdentifier", "symbol")
    query.add_constraint("species", "=", "Caenorhabditis elegans", code="A")
    query.add_constraint("phenotype", "IS NOT NULL", code="B")

    return len(query.rows())
