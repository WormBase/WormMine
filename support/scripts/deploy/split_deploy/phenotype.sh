#!/bin/bash

# set -x

# TODO: set release version as a script argument
# TODO: not process XML files already processed

#set the version to be accessed
wbrel="WS265"
echo 'Release version' $wbrel


declare -A species=(["c_elegans"]="PRJNA13758")
echo 'Deploying ' $species
echo
sourcedir='/mnt/data2/acedb_dumps/WS265/WS265-test-data'
#sourcedir='/mnt/data2/acedb_dumps/'$wbrel'' # <---- XML dump location


echo 'Source directory is at' $sourcedir
echo
intermine='/mnt/data2/wormmine'

datadir=$intermine'/datadir_small'   # for now the datadir is inside the intermine directory
#datadir=$intermine'/datadir'$wbrel''   # for now the datadir is inside the intermine directory
acexmldir=$datadir'/wormbase-acedb'
testlab=$intermine'/wormmine/support/scripts/'
compara=$intermine'/wormmine/support/compara'

echo 'WormMine datadir is at ' $intermine
echo 'AceDB directory is at ' $acexmldir
echo 'Perl scripts are at ' $testlab
echo


#################### phenotype #####################
echo 'phenotype'
mkdir -vp $datadir/wormbase-acedb/phenotype/XML
mkdir -vp $datadir/wormbase-acedb/phenotype/mapping
cp -v $sourcedir/Phenotype.xml $acexmldir/phenotype/Phenotype.xml
cp -v $intermine'/wormmine/support/properties/phenotype_mapping.properties' $datadir'/wormbase-acedb/phenotype/mapping'
perl $testlab'/wb-acedb/purify_xace.pl' $datadir'/wormbase-acedb/phenotype/Phenotype.xml' $datadir'/wormbase-acedb/phenotype/XML/purified_phenotype.xml'
echo

