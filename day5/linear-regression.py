#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import statsmodels.api as sm

files = sys.argv[1:]

for i in files: 
    df = pd.read_table(i, header=None)
    fpkm = df[4]
    mean = df[5]
    results = sm.OLS(fpkm, mean).fit()
    print "################     %s      ################\n" % i.replace(".bed", " ")
    print results.summary()
    print "\n\n\n\n\n"