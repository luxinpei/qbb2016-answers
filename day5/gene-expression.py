#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
# import statmodels


df = pd.read_table( sys.argv[1] )


for i in df.itertuples():
    t_name = i[6]
    chr = i[2]
    chrom_list = ["2L", "2R", "3L", "3R", "4", "X"]
    fpkm = i[12]
    
    if i[3] == "+":
        start = i[4] - 500
        end = i[4] + 500
    else:
        start = i[5] - 500
        end = i[5] + 500
    if chr not in chrom_list:
        continue 

    print "%s\t%d\t%d\t%s\t%d" % (chr, start, end, t_name, fpkm) 
        
       
        