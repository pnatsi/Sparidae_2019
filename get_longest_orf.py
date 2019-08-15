"""
This script parses a fasta file and returns the longest isoform per gene, based on a given regular expression pattern
The pattern in this script is specifically for the file Pagellus_unprocessed.fa

The script can be run as follows:

python get_longest_orfs input_filename output_filename species_initials

The result will be in FASTA format and named 'output_filename.fa'
Each header in the output file will contain as prefix the user-specified species initials

For example:


python get_longest_orfs Pagellus_unprocessed PAGEL_longest PAGEL

will output the file "PAGEL_longest.fa" with headers:

>PAGEL_TR_cx_gx_....


"""


#!/usr/bin/python

import sys
import re

input_filename = sys.argv[-3]

f = open(input_filename, 'r')
lines = f.readlines()

longests = {}
pattern = 'TR\d+_c\d+_g\d+_i\d+'         #THE PATTERN OF THE FASTA HEADERS IN THE INPUT FILE.


for line in lines:
    if line[0] == '>':
        m = re.search(pattern, line)
        current = m.group()
        protein = ''
        if current not in longests:
            longests[current] = ''
    else:
        protein += line.strip()
        if len(protein) > len(longests[current]):
            longests[current] = protein

name = sys.argv[-2]
species = sys.argv[-1]
output_filename = open(name + '.fa', 'w')

for k,v in longests.items():
    output_filename.write('>' + species + '_' + k + '\n')
    output_filename.write(v + '\n')
output_filename.close()
