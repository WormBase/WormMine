#!/bin/bash

# FASTA-only deployment script for WormMine
# Processes protein and genomic FASTA files from FTP or local sources

wbrel="$1"
echo 'Release version' "$wbrel"

#################### Species ####################
declare -A species=(["c_elegans"]="PRJNA13758"
                    ["b_malayi"]="PRJNA10729"
                    ["c_angaria"]="PRJNA51225"
                    ["c_brenneri"]="PRJNA20035"
                    ["c_briggsae"]="PRJNA10731"
                    ["c_japonica"]="PRJNA12591"
                    ["c_remanei"]="PRJNA53967"
                    ["c_tropicalis"]="PRJNA53597"
                    ["o_volvulus"]="PRJEB513"
                    ["s_ratti"]="PRJEB125"
                    ["p_pacificus"]="PRJNA12644")

#################### Directories ####################
sourcedir='/root/data/ftp_files'
intermine='/opt/intermine/wormmine'
datadir='/root/data/mine_input/datadir'$wbrel''

echo 'Source directory is at' "$sourcedir"
echo 'WormMine code is at ' "$intermine"
echo 'WormMine datadir is at ' "$datadir"
echo

#################### Process Protein FASTA ####################
for spe in "${!species[@]}"
do
  echo "Processing species: $spe ${species["$spe"]}"

  # Create directories
  mkdir -vp "$datadir/fasta/$spe/proteins/raw"
  mkdir -vp "$datadir/fasta/$spe/proteins/prepped"

  # Check if we have the file locally first
  # Try different possible locations - both compressed and uncompressed
  local_file_ftp_gz="$sourcedir/ftp/$spe.${species["$spe"]}.$wbrel.protein.fa.gz"
  local_file_ftp="$sourcedir/ftp/$spe.${species["$spe"]}.$wbrel.protein.fa"
  local_file_gz="$sourcedir/species/$spe/${species["$spe"]}/$spe.${species["$spe"]}.$wbrel.protein.fa.gz"
  target_raw="$datadir/fasta/$spe/proteins/raw/$spe.${species["$spe"]}.$wbrel.protein.fa"

  echo "  Looking for: $local_file_ftp"

  if [ -f "$local_file_ftp_gz" ]; then
    echo "  Found local compressed file: $local_file_ftp_gz"
    if [ ! -f "$target_raw" ]; then
      echo "  Extracting to $target_raw"
      gunzip -c "$local_file_ftp_gz" > "$target_raw"
    else
      echo "  Raw file already exists: $target_raw"
    fi
  elif [ -f "$local_file_ftp" ]; then
    echo "  Found local uncompressed file: $local_file_ftp"
    if [ ! -f "$target_raw" ]; then
      echo "  Copying to $target_raw"
      cp "$local_file_ftp" "$target_raw"
    else
      echo "  Raw file already exists: $target_raw"
    fi
  elif [ -f "$local_file_gz" ]; then
    echo "  Found local compressed file: $local_file_gz"
    if [ ! -f "$target_raw" ]; then
      echo "  Extracting to $target_raw"
      gunzip -c "$local_file_gz" > "$target_raw"
    else
      echo "  Raw file already exists: $target_raw"
    fi
  else
    echo "  ERROR: No local file found, cannot download (Cloudflare blocks FTP)"
    echo "  Tried:"
    echo "    - $local_file_ftp_gz"
    echo "    - $local_file_ftp"
    echo "    - $local_file_gz"
    continue
  fi

  # Prep the FASTA file
  if [ -f "$target_raw" ]; then
    echo "  Pre-processing protein FASTA file"
    awk '{ if (NF > 1) {split($2,res,"="); print ">"res[2]} else {print}}' \
      < "$target_raw" \
      > "$datadir/fasta/$spe/proteins/prepped/$spe.${species["$spe"]}.$wbrel.protein.final.fa"
    echo "  ✓ Prepped: $datadir/fasta/$spe/proteins/prepped/$spe.${species["$spe"]}.$wbrel.protein.final.fa"
  else
    echo "  ✗ ERROR: Raw protein file not found for $spe"
  fi
  echo
done

#################### Process Genomic FASTA (C. elegans only) ####################
declare -A species2=(["c_elegans"]="PRJNA13758")

for spe in "${!species2[@]}"
do
  echo "Processing genomic data for: $spe ${species2["$spe"]}"

  mkdir -vp "$datadir/fasta/$spe/genomic"
  mkdir -vp "$datadir/fasta/$spe/cds/raw"
  mkdir -vp "$datadir/fasta/$spe/cds/prepped"

  # Genomic FASTA
  local_genomic_ftp_gz="$sourcedir/ftp/$spe.${species2["$spe"]}.$wbrel.genomic.fa.gz"
  local_genomic_ftp="$sourcedir/ftp/$spe.${species2["$spe"]}.$wbrel.genomic.fa"
  local_genomic_gz="$sourcedir/species/$spe/${species2["$spe"]}/$spe.${species2["$spe"]}.$wbrel.genomic.fa.gz"
  target_genomic="$datadir/fasta/$spe/genomic/$spe.${species2["$spe"]}.$wbrel.genomic.fa"

  if [ -f "$local_genomic_ftp_gz" ]; then
    echo "  Found local compressed genomic file"
    gunzip -c "$local_genomic_ftp_gz" > "$target_genomic"
  elif [ -f "$local_genomic_ftp" ]; then
    echo "  Found local uncompressed genomic file"
    cp "$local_genomic_ftp" "$target_genomic"
  elif [ -f "$local_genomic_gz" ]; then
    echo "  Found local compressed genomic file (alt location)"
    gunzip -c "$local_genomic_gz" > "$target_genomic"
  else
    echo "  ERROR: No local genomic file found"
  fi

  # CDS FASTA
  local_cds_ftp_gz="$sourcedir/ftp/$spe.${species2["$spe"]}.$wbrel.CDS_transcripts.fa.gz"
  local_cds_ftp="$sourcedir/ftp/$spe.${species2["$spe"]}.$wbrel.CDS_transcripts.fa"
  local_cds_gz="$sourcedir/species/$spe/${species2["$spe"]}/$spe.${species2["$spe"]}.$wbrel.CDS_transcripts.fa.gz"
  target_cds_raw="$datadir/fasta/$spe/cds/raw/$spe.${species2["$spe"]}.$wbrel.CDS_transcripts.fa"

  if [ -f "$local_cds_ftp_gz" ]; then
    echo "  Found local compressed CDS file"
    gunzip -c "$local_cds_ftp_gz" > "$target_cds_raw"
  elif [ -f "$local_cds_ftp" ]; then
    echo "  Found local uncompressed CDS file"
    cp "$local_cds_ftp" "$target_cds_raw"
  elif [ -f "$local_cds_gz" ]; then
    echo "  Found local compressed CDS file (alt location)"
    gunzip -c "$local_cds_gz" > "$target_cds_raw"
  else
    echo "  ERROR: No local CDS file found"
  fi

  # Prep CDS FASTA
  if [ -f "$target_cds_raw" ]; then
    echo "  Pre-processing CDS FASTA file"
    awk '{ if (NF > 1) {split($2,res,"="); print ">"res[2]} else {print}}' \
      < "$target_cds_raw" \
      > "$datadir/fasta/$spe/cds/prepped/$spe.${species2["$spe"]}.$wbrel.CDS_transcripts.final.fa"
    echo "  ✓ Prepped CDS"
  else
    echo "  ✗ ERROR: Raw CDS file not found"
  fi
  echo
done

echo "================================"
echo "FASTA deployment complete!"
echo "================================"
