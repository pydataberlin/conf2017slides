
# Bugs introduced in the exercise

## parse_uniprot.py

* missing colon at end of line 65
* missing "w" while opening file in line 55
* paragraph for writing to file dedented, line 68+69
* misquoted 'aa' in line 66
* 'OS=Homo sapiens' must be lowercase
* name and accession swapped in line  50
* extra yield missing in line 34
* line 62 is a relic, it does nothing
* strip() missing in line 33
* amino acid X not accounted for


## summarize.py

* line 18 missing return
* line 13-15, all indices should be 2
* line 24-25, panda and banana swapped

## pipeline.py

* line 16 potentially dangerous, logging is better
* accidental comparison operator

