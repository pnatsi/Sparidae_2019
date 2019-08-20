"""                                                                                                                                                                                                                                           
This script parses the output of 'get_longest_orf.py', which contains the longest predicted open reading frames (ORFs) per transcript.
These ORFs may be different isoforms of the same gene, so we are interested in keeping the longest isoform per gene.
The script can be run as follows:                                                                                                                                                                                                             
                                                                                                                                                                                                                                              
python get_longest_isoform.py input_filename output_filename header_prefix                                                                                                                                                                                     
                                                                                                                                                                                                                                              
The result will be in FASTA format and named 'output_filename'. It will contain only the longest predicted isoform per gene                                                                                                              
                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
For example:                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                              
python get_longest_isoform.py Pagrus_longest_orfs.fasta Pagrus_longest_isoforms.fasta PAGR                                                                                                                                                                  
                                                                                                                                                                                                                                              
will output the file "Pagrus_longest_isoforms.fasta" with sequence headers:

>PAGR_...
...
>PAGR_...
...

"""


#!/usr/bin/pythonimport sys
import re

infilename = sys.argv[-3]
outfilename = sys.argv[-2]
headername = sys.argv[-1]

f = open(infilename, 'r')
lines = f.readlines()

longests = {}

for line in lines:
    if line[0] == '>':
        m = re.search('TR\d+_c\d+_g\d+', line)
        current = m.group()
        protein = ''
        if current not in longests:
            longests[current] = ''
    else:
        protein += line.strip()
        if len(protein) > len(longests[current]):
            longests[current] = protein
            
output = open(outfilename, "w")

for k,v in longests.items():
    output.write('>' + headername + '_' + k + '\n')
    output.write(v + '\n')
output.close()
