#!/bin/bash

# set -x

# TODO: set release version as a script argument
# TODO: not process XML files already processed

#set the version to be accessed
wbrel="WS271"
echo 'Release version' $wbrel


declare -A species=(["c_elegans"]="PRJNA13758")
echo 'Deploying ' $species
echo
sourcedir='/mnt/data2/acedb_dumps/WS271/WS271-test-data'
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

#################### variation ##################
echo 'variation'
mkdir -vp $datadir/wormbase-acedb/variation/XML
mkdir -vp $datadir/wormbase-acedb/variation/mapping
cp -v $sourcedir/Variation.xml $acexmldir/variation/Variation.xml
cp -v $intermine'/wormmine/support/properties_xpath/variation_mapping.properties' $datadir'/wormbase-acedb/variation/mapping'
perl $testlab'/wb-acedb/purify_variation.pl' $datadir'/wormbase-acedb/variation/Variation.xml' $datadir'/wormbase-acedb/variation/XML/prepped_variation.xml'
#sh $testlab'/wb-acedb/fix_elements_variation.sh' $acexmldir
echo

