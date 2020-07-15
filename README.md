# Utils

## EXODQM 

Files and other utilities to be used with the EXO DQM validation code.

## ROOTFiles-management

### splitAdd.py
Python script to cluster different TFiles (of the same datasets) in slices by setting the number of final ROOT files.

How to use:

```python splitAdd.py --help```

```
  Options:
  -h, --help            show this help message and exit
  -d DIR, --dir=DIR     Input directory
  -n N, --number=N      Number of chunks
  -r RUN, --run=RUN     Name of run.sh
  -s SAMPLE, --sample=SAMPLE
                        Name of sample
```

