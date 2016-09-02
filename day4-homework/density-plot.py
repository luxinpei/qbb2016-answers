#!/usr/bin/env python

"""
Create a density plot of the FPKM values for SRR072893
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

df = pd.read_table( sys.argv[1] )


df2 = df["FPKM"] > 0
new = df[(df2)]["FPKM"]
logFPKM = np.log(new)

density = gaussian_kde(logFPKM)

# xs = np.linspace(-50, 50, 200)
xs = np.linspace(-10, 10, 100)




plt.figure()
plt.hist (logFPKM, normed=1, color= 'c', edgecolor = 'none', alpha=.2)
plt.plot(xs, density(xs), 'r', linewidth= 2)
plt.title("Density plot" )
# plt.show()
plt.savefig( "Question4.png")
plt.close