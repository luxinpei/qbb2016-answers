#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_893 = pd.read_table( sys.argv[1])
df_915 = pd.read_table( sys.argv[2])

chrom=["2L", "2R", "3L", "3R", "4", "X"]
for ch in chrom:
    df_893roi = df_893[ "chr" ] == ch
    df_chrom = df_893[ df_893roi ]
    rollingmean893 = df_chrom[ "FPKM" ].rolling( 200 ).mean()

    df_915roi = df_915[ "chr" ] == ch
    df_chrom = df_915[ df_915roi ]
    rollingmean915 = df_chrom[ "FPKM" ].rolling( 200 ).mean()

    plt.figure()
    plt.plot( rollingmean893)
    plt.plot( rollingmean915)
    plt.title( "Rolling mean (size=200) for "+ ch+ " chromosome" )
    plt.savefig( ch+ ".png" )
    plt.close()
    
