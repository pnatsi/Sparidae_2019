'''
This script creates jackknifed sets from a set of orthogroups, based on a given proportion.

python jackknife.py input_filename 100 0.7

input_filename will contain the orthogroup filenames
Here 100 jackknife replicates are created with each containing a random 70% of the original orthogroups
These 100 files can then used to retrieve the sequences from the corresponding orthogroups
'''

import numpy as np

input_filename = sys.argv[-3]
jackknife_replicates = sys.argv[-2]           # HOW MANY JACKKNIFE REPLICATES WILL BE CREATED   
percentage_included = sys.argv[-1]            # WHAT PERCENTAGE OF THE TOTAL ORTHOGROUPS WILL BE IN EVERY JACKKNIFE REPLICATE 

f = open(input_filename, "r")                 # A FILE WITH ALL ORTHOGROUP FILENAMES CREATED WITH "ls OG* > allfiles.txt"
lines = f.readlines()
filenames = [x.strip() for x in lines]

for i in range(0, jackknife_replicates): 
    random_subset = np.random.choice(filenames, int(percentage_included * len(filenames)), replace = False)
    output = open("jackknife_orthofinder_" + str(i) + ".txt", "w")       # CREATES A FILE FOR EVERY ITERATION WITH ORTHOGROUP FILENAMES IN IT
    for entry in random_subset:
        output.write(entry + "\n")
    output.close()
