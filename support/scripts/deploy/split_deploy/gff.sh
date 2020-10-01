#!/bin/bash

# set -x
#Paulo Nuin Jan 2015, modified Feb 15 - Aug 2016, Feb 2018

# TODO: set release version as a script argument
# TODO: not process XML files already processed

#set the version to be accessed
wbrel="$1"
echo 'Release version' $wbrel


#################### Species ####################
#                                               #
#  species to be transferred                    #
#  key:value structure with species             #
#  "name" and BioProject number                 #
#  required in order to get the right           #
#  directory and file                           #
#                                               #
#################### Species ####################


declare -A species=(["c_elegans"]="PRJNA13758")
echo 'Deploying ' $species
echo
#sourcedir='/mnt/data2/acedb_dumps/WS265/WS265-test-data'
sourcedir='/mnt/data2/acedb_dumps/'$wbrel'' # <---- XML dump location
echo $sourcedir

# example test data /mnt/data2/acedb_dumps/WS261/WS261-test-data
# sourcedir='/Users/nuin/Dropbox/intermine/WS262-test-data/'

echo 'Source directory is at' $sourcedir
echo
#################### Main dirs ##################
#                                               #
#  datadir - main data directory                # 
#  acexmldir - subdir for AceDB XML files       #
#  pp - pre-processing dir with perl and bash   #
#                                               #
#################### Species ####################

intermine='/mnt/data2/4.0/WormMine'
datadir='/mnt/data2/mine_input/datadir'$wbrel''
acexmldir=$datadir'/wormbase-acedb'
testlab=$intermine'/support/scripts/'
compara=$intermine'/support/scripts/deploy/compara'


echo 'WormMine code is at ' $intermine
echo 'WormMine datadir is at ' $datadir
echo 'AceDB directory is at ' $acexmldir
echo 'Perl scripts are at ' $testlab
echo



#################### FTP ########################
#################### Species #################### 
for spe in "${!species[@]}"
do
  echo species: $spe ${species["$spe"]}


  ##################### get gff annotations ####################
  echo 'Getting gff data'
  mkdir -vp $datadir'/wormbase-gff3/raw'
  mkdir -vp $datadir'/wormbase-gff3/final'
  cd $datadir'/wormbase-gff3'
  if [ ! -f final/"$spe"."${species["$spe"]}"."$wbrel".gff ]; then
    echo 'transferring' "$spe"."${species["$spe"]}"."$wbrel".gff
    wget -q --show-progress -O raw/"$spe"."${species["$spe"]}"."$wbrel".gff.gz  "ftp://ftp.wormbase.org/pub/wormbase/releases/"$wbrel"/species/"$spe"/"${species["$spe"]}"/"$spe"."${species["$spe"]}"."$wbrel".annotations.gff3.gz"
    gunzip -v raw/"$spe"."${species["$spe"]}"."$wbrel".gff.gz
    echo 'Starting GFF3 pre-processing'


    echo "$intermine"/wormmine/support/scripts/gff3/scrape_gff3.sh $datadir/wormbase-gff3/raw/"$spe"."${species["$spe"]}"."$wbrel".gff $datadir/wormbase-gff3/final/"$spe"."${species["$spe"]}"."$wbrel".gff
    bash "$intermine"/wormmine/support/scripts/gff3/scrape_gff3.sh $datadir/wormbase-gff3/raw/"$spe"."${species["$spe"]}"."$wbrel".gff $datadir/wormbase-gff3/final/"$spe"."${species["$spe"]}"."$wbrel".gff

    cd $datadir"/wormbase-gff3/final"
    python $testlab"/gff3/exon_processing.py" "$spe"."${species["$spe"]}"."$wbrel".gff
    rm "$spe"."${species["$spe"]}"."$wbrel".gff

    echo 'Done #########################'
  else
    echo  raw/"$spe"."${species["$spe"]}"."$wbrel".gff 'found'
  fi
  echo
done
