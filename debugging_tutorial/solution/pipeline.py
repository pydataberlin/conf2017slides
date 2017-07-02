
# prediction pipeline

from parse_uniprot import parse
from summarize import get_means, calc_z
import os

IN_PATH = 'data/'
OUT_PATH = 'output/'

organisms = ['human', 'chimp', 'banana']

for org in organisms:
	in_fn = "{}/{}.fasta".format(IN_PATH, org)
	out_fn = "{}/{}_proteome.csv".format(OUT_PATH, org)
	if not os.path.exists(out_fn):
	    parse(in_fn, out_fn)


means = get_means()
print(means.sum())

z = calc_z(means)
print(z.abs().mean())


