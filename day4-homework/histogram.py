#!/usr/bin/env python

"""
Create a histogram of the FPKM values for SRR072893.

filter out zero-values
log values
"""




import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table( sys.argv[1] )

df2 = df["FPKM"] > 0
new = df[(df2)]["FPKM"]
logFPKM = np.log(new)

# print logged_FPKM


plt.figure()
plt.hist (logFPKM, bins = 100, color= 'c', edgecolor = 'c')
plt.title("SRR072893 Histogram" )
plt.ylabel( "Count")
plt.xlabel( "Log(FPKM)")
# plt.show()
plt.savefig( "Question2.png")
plt.close()