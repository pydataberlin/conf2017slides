"""
Read the human proteome from a FASTA file,
extract some properties from the description
and count the amino acids.

Save all info as a comma-separated table.

Data downloaded via http://www.uniprot.org/help/human_proteome
"""

from Bio import SeqIO
import csv
import re

AMINO_ACIDS = list("ACDEFGHIKLMNPQRSTVWY")

LABELS = ['accession', 'name', 'length', 'fragment'] + AMINO_ACIDS

outfile = open("human_proteome.csv", "w")
writer = csv.writer(outfile)
writer.writerows([LABELS])

for rec in SeqIO.parse("UP000005640_9606.fasta", "fasta"):
    accession = rec.id.split('|')[1]
    name = rec.description
    name = name.lower()
    name = name[:]  # cut off accession
    fragment = int(bool(re.search('\(fragment\)', name)))
    name = name.replace('(fragment)', '')

    accession_end = name.find(' ') + 1
    end = name.find('OS=Homo sapiens')
    name = name[accession_end:end].strip()

    aa_counts = []
    for aa in AMINO_ACIDS:
        aa_counts.append(rec.seq.count(aa))

    row = [accession, name, len(rec), fragment] + aa_counts
    writer.writerows([row])
