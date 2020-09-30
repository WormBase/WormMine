echo "Scraping GFF3"

egrep "^\S*\s(WormBase)\S*\s(gene|mRNA|CDS|exon|miRNA|mRNA|ncRNA|scRNA|snoRNA|snRNA|piRNA|pseudogenic_transcript|nc_primary_transcript|pseudogenic_tRNA|tRNA|antisense_RNA|lincRNA|rRNA|pseudogenic_rRNA|pre_miRNA|circular_RNA)" $1 > $2
