# Sparidae_2019
Scripts used in Natsidis et al (2019)

### get_longest_orf.py


### concatenate.py


### jackknife.py

`jackknife.py` will create a number of jackknifed lists of orthogroup names given an initial list of orthogroup names and a proportion. For example:

```
python jackknife.py allfiles.txt 100 0.7
```

will create 100 replicates, each containing a random 70% of the names contained in `allfiles.txt`
