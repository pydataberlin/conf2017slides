"""
Reads protein sequences from a FASTA sequence file,
extract some properties from the description
and count the amino acids.

Save all info as a comma-separated table.

Data downloaded via http://www.uniprot.org/help/human_proteome
"""

import csv
import re
import sys

# characters representing amino acids, the building blocks of proteins
AMINO_ACIDS = list("ACDEFGHIKLMNPQRSTVWY")

# column labels for the output file
LABELS = ['accession', 'name', 'length'] + AMINO_ACIDS

def read_fasta(filename):
    """Generates (header,sequence) pairs from a FASTA file"""
    with open(filename) as uniprot_file:
        header = ''
        seq = ''
        for line in uniprot_file:
            if line.startswith('>'):
                if seq:
                    yield header, seq
                    seq = ''
                header = line.strip()
            else:
                seq += line.strip()
    yield header, seq


def parse_header(header):
    """Extracts the ID and protein name from a one-line header"""
    accession = header.split('|')[1]
    name = header.split('|')[2]
    name = name.lower()
    name = name[:]  # cut off accession number
    fragment = int(bool(re.search('\(fragment\)', name)))
    name = name.replace('(fragment)', '')

    # simplify name
    accession_end = name.find(' ') + 1
    end = name.find('OS=Homo sapiens')
    name = name[accession_end:end].strip()
    return accession, name


def parse(input_fn, output_fn):
    # prepare output file
    with open(output_fn, "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerows([LABELS])

        # process protein entries
        for header, seq in read_fasta(input_fn):
            accession, name = parse_header(header)

            length = len(seq)
            aa_counts = []
            for aa in AMINO_ACIDS:
                aa_counts.append(seq.count(aa) / length)

            row = [accession, name, length] + aa_counts
            writer.writerows([row])



if __name__ == '__main__':
    parse(sys.argv[1], sys.argv[2])
