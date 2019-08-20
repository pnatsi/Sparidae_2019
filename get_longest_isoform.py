import sys
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
