#!/usr/bin/env python

"""
create a boxplot for all the Sxl transcripts that have an FPKM >0 in SRR072893 and SRR072915. 
log() the values, add a title, label the y-axis, and label each sample on the x-axis.
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

df_893ctab = pd.read_table( sys.argv[1])
df_915ctab = pd.read_table( sys.argv[2])

df_roi = df_893ctab[ "gene_name"] == "Sxl"
df_output =df_893ctab[ df_roi ]
df_roi2 = df_output[ "FPKM"] > 0 
df_output2 = df_output[df_roi2]


df_915roi = df_915ctab[ "gene_name"] == "Sxl"
df_915output = df_915ctab[ df_915roi ]
df_915roi2 = df_915output[ "FPKM"] > 0 
df_915output2 = df_915output[df_915roi2]

# print df_output2, df_915output2
fpkm893 = df_output2 [ "FPKM"]
fpkm915 = df_915output2[ "FPKM"]

# print fpkm893, fpkm915

plt.figure()
plt.boxplot( [fpkm893 , fpkm915], labels =["fpkm893", "fpkm915"] )
plt.title( "Question1" )
plt.ylabel( "log(FPKM)")
plt.savefig( "Question1" )
plt.yscale('log')
#plt.show()