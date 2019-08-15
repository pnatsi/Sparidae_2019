'''
This script concatenates several fasta files into a superalignment, suitable for use in phylogenetics analysis.
In all files, sequences from the same species must have identical headers. The headers are provided in "headers.txt"

allfiles.txt contains the titles of the files to be concatenated
headers.txt contains the FASTA headers for each of the species in the separate alignment files. This will also be the header in the final output

The output superalignment "concatenated.aln" will be in FASTA format
'''


from Bio import SeqIO

f = open("allfiles.txt", 'r')
lines = f.readlines()
filenames = []
for line in lines:
    filenames.append(line.strip())

f = open("headers.txt", 'r')
lines = f.readlines()
species = []
for line in lines:
    species.append(line.strip()[1:])
final = {}

for fish in species:
    final[fish] = ''

for filename in filenames:
    fasta_sequences = SeqIO.parse(open(filename),'fasta')
    localspecies = list(species)
    for seq in fasta_sequences:
        final[seq.id] += str(seq.seq)
        localspecies.remove(seq.id)    
    length = len(str(seq.seq))
    for fish in localspecies:
        final[fish] += '-'*length
    print(filename, length)

for fish in species:
    print(fish, len(final[fish]))

output = 'concatenated.aln'
h = open(output, 'w')
for fish in species:
    h.write(">" + fish + "\n" + final[fish] + "\n")

h.close
