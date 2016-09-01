#!/usr/bin/env python

"""
add timecourse of male Sxl abundance to the same plot
style it similarly to Lott et al., 2011 PLoS Biology (i.e. x-axis tick labels, color, legend, etc.)
add stage 14 replicates to the same plot (~/data/fastq/replicates.csv)

HINT: since there are only replicates for 14A/B/C/D, you will need to "skip" plotting 10/11/12/13
HINT: plt.plot( x, y, 'o' )
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_meta = pd.read_csv( sys.argv[1] )
ctab_dir = sys.argv[2]
df_dots = pd.read_csv( sys.argv[3])

fem_Sxl =[]

df_roi = df_meta["sex"] == "female" 
for sample in df_meta[ df_roi ][ "sample" ]:
    filename = ctab_dir + sample + "/t_data.ctab"
    df = pd.read_table( filename ) 
    df_roi2 = df["t_name"] == "FBtr0331261"
    fem_Sxl.append( df[ df_roi2 ]["FPKM"].values )




male_Sxl =[]

df_roi3 = df_meta["sex"] == "male"
for sample in df_meta[ df_roi3 ][ "sample" ]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table ( filename )

    df_roi4 = df["t_name"] == "FBtr0331261"
    male_Sxl.append( df[ df_roi4 ] ["FPKM"].values)
#
#
# #adding replicates dots
#
fem_replicates =[]

df_roi = df_dots["sex"] == "female"
for sample in df_dots[ df_roi ][ "sample" ]:
    filename = ctab_dir + sample + "/t_data.ctab"
    df = pd.read_table ( filename )
    df_roi2 = df["t_name"] == "FBtr0331261"
    fem_replicates.append( df[ df_roi2 ] ["FPKM"].values)
#
male_replicates =[]

df_roi = df_dots["sex"] == "male"
for sample in df_dots[ df_roi ][ "sample" ]:
    filename = ctab_dir + sample + "/t_data.ctab"
    df = pd.read_table ( filename )
    df_roi2 = df["t_name"] == "FBtr0331261"
    male_replicates.append( df[ df_roi2 ] ["FPKM"].values)

    
#making the plot pretty
x = [0,1,2,3,4,5,6,7]
xaxis = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]

plt.figure()
plt.plot( fem_Sxl, label = "Female", color = "r", linewidth = 3 )
plt.plot( male_Sxl,label = "Male", color = "b", linewidth = 3 )
plt.plot([4,5,6,7], fem_replicates, 'ro')
plt.plot([4,5,6,7], male_replicates, 'bo')
plt.title( "Sxl Timecourse")
plt.legend( loc="upper left")
plt.xlabel( "Developmental Stages")
plt.ylabel( "mRNA Abundance (FPKM)")
plt.xticks(x, xaxis)
plt.savefig( "timecourse.png")
plt.close()