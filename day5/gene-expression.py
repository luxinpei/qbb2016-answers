#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
# import statmodels


df = pd.read_table( sys.argv[1] )

for i in df.itertuples():
    t_name = i[6]
    chr = i[2]
    
    if i[3] == "+":
        start = i[4] - 500
        end = i[4] + 500
    else:
        start = i[5] - 500
        end = i[5] + 500

        print "%s\t%d\t%d\t%s" % (chr, start, end, t_name) 
        
       
        