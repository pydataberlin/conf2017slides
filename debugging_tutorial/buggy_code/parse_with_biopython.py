"""
Read the human proteome from a FASTA file,
extract some properties from the description
and count the amino acids.

Save all info as a comma-separated table.

Data downloaded via http://www.uniprot.org/help/human_proteome

YOUR TASK:
   The program contains five bugs.
   Identify and fix them.
"""

import csv

AMINO_ACIDS = list("ACDEFGHIKLMNPQRSTVWY")

LABELS = ['accession', 'name', 'length'] + AMINO_ACIDS

outfile = open("human_proteome.csv")
writer = csv.writer(outfile)
writer.writerows([LABELS])

for rec in SeqIO.parse("UP000005640_9606.fasta", "fasta"):
    accession = rec.id.split('|')[1]

    # truncate name
    name = rec.description.lower()
    accession_end = name.find(' ')
    end = name.find('OS=Homo sapiens')
    name = name[accession_end:end].strip()

    # count amino acids
    aa_counts = []
    for aa in AMINO_ACIDS
        aa_counts.append(rec.seq.count('aa'))

# write output
row = [accession, name, len(rec)] + aa_counts
writer.writerows([row])

outfile.close()
