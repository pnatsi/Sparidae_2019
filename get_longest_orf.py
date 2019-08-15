"""                                                                                                                                                                                                                                           
This script parses the output of 'getorf', which contains predicted open reading frames (ORFs) from a set of transcripts.                                                                                                                     
The output file contains the longest predicted ORF per transcript.                                                                                                                                                                            
The script can be run as follows:                                                                                                                                                                                                             
                                                                                                                                                                                                                                              
python get_longest_orfs input_filename output_filename                                                                                                                                                                                        
                                                                                                                                                                                                                                              
The result will be in FASTA format and named 'output_filename.fa'. It will contain only the longest predicted ORF per transcript                                                                                                              
                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
For example:                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                              
python get_longest_orfs Pagrus_getorf_example.fasta Pagrus_longest_orf                                                                                                                                                                        
                                                                                                                                                                                                                                              
will output the file "Pagrus_longest_orf.fa"                                                                                                                                                                                                  
                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
"""


#!/usr/bin/python                                                                                                                                                                                                                             

import sys
import re

input_filename = sys.argv[-1]

f = open(input_filename, 'r')
lines = f.readlines()

longests = {}
pattern = 'TR\d+_c\d+_g\d+_i\d+'         #THE PATTERN IN THE FASTA HEADERS OF THE INPUT FILE.                                                                                                                                                 


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

name = sys.argv[-1]
output_filename = open(name + '.fa', 'w')

for k,v in longests.items():
    output_filename.write('>' + k + '\n')
    output_filename.write(v + '\n')
output_filename.close()
