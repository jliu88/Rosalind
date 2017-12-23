#!/usr/bin/env python

from math import ceil

import pandas as pd


dirt = r'filepath'
foo = open(dirt, 'r')

bar = foo.readlines()
listo = []

for i in bar:
    num = i.split()
    listo.append(num)
    
listo.pop(0)

halve = ceil(len(listo[0])/2)
rslt = []

for arrays in listo:
    s = pd.Series(arrays)
    county = s.value_counts()

    if county[0] >= halve:
        maj = county.index[0]   
    else:
        maj = -1
        
    rslt.append(maj)
    
print(*rslt)
