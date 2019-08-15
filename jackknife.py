'''
This script creates jackknifed sets from a set of orthogroups, based on a given proportion.
allfiles.txt contains the orthogroup filenames
Here we create 100 replicated with each containing a random 70% of the original orthogroups
'''

import numpy as np

f = open("allfiles.txt", "r")        # A FILE WITH ALL ORTHOGROUP FILENAMES CREATED WITH "ls OG* > allfiles.txt"
lines = f.readlines()
filenames = [x.strip() for x in lines]

jackknife_replicates = 100           # HOW MANY JACKKNIFE REPLICATES WILL BE CREATED   
percentage_included = 0.7            # WHAT PERCENTAGE OF THE TOTAL ORTHOGROUPS WILL BE IN EVERY JACKKNIFE REPLICATE  


for i in range(0,jackknife_replicates): 
    portion = np.random.choice(filenames, int(percentage_included*len(filenames)), replace = False)
    print(portion[:10]) 
    output = open("jackknife_orthofinder_" + str(i) + ".txt", "w")       # CREATES A FILE FOR EVERY ITERATION WITH ORTHOGROUP FILENAMES IN IT
    for entry in portion:
        output.write(entry + "\n")
    output.close()
