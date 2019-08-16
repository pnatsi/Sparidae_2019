# Sparidae_2019
Scripts used in Natsidis et al (2019)

### get_longest_orf.py

`get_longest_orf.py` will parse the output of 'getorf', which contains predicted open reading frames (ORFs) for given transcripts. It will then return the longest ORF per transcript. Output will be written in FASTA format. For example:


```
python get_longest_orf.py Pagrus_getorf_example.fasta Pagrus_longest_orf.fasta
```

will parse all sequences from `Pagrus_getorf_example.fasta` and return the longest among the sequences that have the same transcript ID. The longest ORFs will be written in `Pagrus_longest_orf.fasta`


### get_longest_isoform.py

`get_longest_isoform.py` will parse the output of `get_longest_orf` and it will return the longest isoform per gene. Multiple transcripts can represent different fragments or versions (allelles) of the same gene, however we are more interested in the longest isoform within the context of phylogenetic analysis. The different isoforms of the same gene can be distinguished by the 'i1', 'i2', 'i3', ..., notation in their FASTA headers. Output will be written in FASTA format. For example:

```
python get_longest_isoform.py 
```

will parse all sequences from `Pagrus_longest_orf.fasta` and will keep only the longest of the isoforms based on their FASTA headers. The result will be written in `Pagrus_longest_isoforms.fasta` and each sequence header will have the format:

```
>PAGR_transcript_id1
>PAGR_transcript_id2
...
```

This file is ready to use in orthology inference analysis, together with other proteomes.


### concatenate.py

`concatenate.py` will take a set of alignments in FASTA format and will concatenated into one superalignment, suitable for phylogenetic analysis. For example:

```
python concatenate.py allfiles.txt headers.txt
```

will take all alignments contained in `allfiles.txt` and concatenate them into a single output file called `concatenated.aln`
The headers in the output file will be the same for each species as in the initial, separate alignment files.
When a species is missing from an alignment, its sequence will be filled with '-' characters in the final superalignment.

### jackknife.py

`jackknife.py` will create a number of jackknifed lists of orthogroup names from a given list of names and a proportion. For example:

```
python jackknife.py allfiles.txt 100 0.7
```

will take the orthogroup names contained in `allfiles.txt` and create 100 replicates, each containing a random 70% of the initial orthogroup names These files can then be used to retrieve the corresponding orthogroups and perform jackknifed phylogenetic trees.
