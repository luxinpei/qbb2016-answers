#!/usr/bin/env python

import sys
import fasta
from itertools import cycle
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt



nucleotide = fasta.FASTAReader(open(sys.argv[1])) 
queryfile = fasta.FASTAReader(open(sys.argv[2]))

codontable = { 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

synonomous = {}
nonsynonomous = {}
final_codons = []

for identifier, sequence in nucleotide:
    final_codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]


query_codons = []
for identifier2, sequence2 in queryfile:
    query_codons = [sequence2[i:i+3] for i in range(0, len(sequence2),3)]

for index, i in enumerate(query_codons):
    synonomous[index] = 0
    nonsynonomous[index] = 0
index = 0

 
for (a,b) in zip(final_codons, cycle(query_codons)):
    if a not in codontable:
        continue
    elif b not in codontable:
        continue
    elif a == b:
        continue
    elif codontable[a] == codontable[b]:
        synonomous[index] += 1
    else:
        nonsynonomous[index] += 1
    if index <= 3427:
        index += 3
    else:
        index = 0    

dS = []
dN = []
positions = []

for i in synonomous:
    dS.append(synonomous[i])
    
for i in nonsynonomous:
    dN.append(nonsynonomous[i])
for i in synonomous:
    positions.append(i)


dS_dN = []
for i in synonomous and nonsynonomous:
    dS_dN.append((synonomous[i], nonsynonomous[i]))
    
d = []
for value in dS_dN:
    d.append(value[1]-value[0])
    
array_of_d = np.array(d)
z_score = stats.zscore(array_of_d)
    
    
    
plt.figure()
plt.style.use('ggplot')
plt.title("Synonomous vs Nonsynonomous")
plt.scatter(positions, z_score, c='g', edgecolors='none', s=20, alpha=0.1)
plt.xlabel("position")
plt.ylabel("z-score")
plt.savefig("plot.png")