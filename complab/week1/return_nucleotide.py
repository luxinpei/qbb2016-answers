#!/usr/bin/env python

import sys
import fasta
import itertools

sequence = fasta.FASTAReader(open(sys.argv[1]))
proteins = fasta.FASTAReader(open(sys.argv[2]))

l1 = []
l2 = []

for stuff in sequence:
    l1.append(stuff)
    
for stuff in proteins:
    l2.append(stuff)
    
for alignment in itertools.izip(l1,l2):
    nuc_seq = alignment[0][1]
    prot_seq = alignment[1][1]
    new_seq = []
    n = 0 
    for aa in prot_seq:
        if aa == "-":
            new_seq.append("---")
        else:
            codon = nuc_seq[n:n+3]
            n += 3
            new_seq.append(codon)
    print ">"+alignment[0][0]
    print "".join(new_seq)