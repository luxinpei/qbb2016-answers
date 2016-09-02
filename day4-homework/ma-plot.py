#!/usr/bin/env python

"""
Instead of plotting FPKM values for SRR072893 and SRR072915 directly, 
transform the data to make an MA-plot. 
This time do not drop rows with 0 FPKM. plt.scale( 'log' ) 
is not enough so you will have to log etc your values first.
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table( sys.argv[1] )
df2 = pd.read_table( sys.argv[2] )

values_R = df["FPKM"]
values_G = df2["FPKM"]

logR = np.log2(values_R)
logG = np.log2(values_G)

the_M = logR - logG
the_A = 0.5 * (logR + logG)

colors = np.random.rand(len(values_R))
area = np.pi*(4* np.random.rand(len(values_R)))**2
# area = np.random.rand(200, 800)

plt.figure()
plt.scatter(the_M + 1, the_A + 1, c=colors, edgecolors='none', s=area, alpha=0.5)
plt.title("MA plot" )
plt.ylabel( "M")
plt.xlabel( "A")
plt.show()
# plt.savefig( "Question3.png")
# plt.close()

