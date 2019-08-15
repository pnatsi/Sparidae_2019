# Sparidae_2019
Scripts used in Natsidis et al (2019)

### get_longest_orf.py

```
python get_longest_orf.py Pagrus_getorf_example.fasta Pagrus_longest_orf PAGR
```

### get_longest_isoform.py

```
python get_longest_isoform


### concatenate.py

`concatenate.py` will take a set of alignments in FASTA format and will concatenated into one superalignment, suitable for phylogenetic analysis. For example:

```
python concatenate.py allfiles.txt headers.txt
```

will take all alignments contained in `allfiles.txt` and concatenate them into a single output file called `concatenated.aln`
The headers in the output file will be the same for each species as in the initial, separate alignment files.
When a species is missing from an alignment, its sequence will be filled with '-' characters in the final superalignment.

### jackknife.py

`jackknife.py` will create a number of jackknifed lists of orthogroup names given an initial list of orthogroup names and a proportion. For example:

```
python jackknife.py allfiles.txt 100 0.7
```

will take the orthogroup names contained in `allfiles.txt` and create 100 replicates, each containing a random 70% of the initial orthogroup names These files can then be used to retrieve the corresponding orthogroups and perform jackknifed phylogenetic trees.
