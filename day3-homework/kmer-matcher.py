#!/usr/bin/env python

import sys
import fasta

query_fasta = open(sys.argv[1])
target_fasta = open(sys.argv[2])
k = int(sys.argv[3])
kmer_query = {}
target_gene = {}

for ident, sequence in fasta.FASTAReader( query_fasta):
    sequence = sequence.upper()
    for i in range( 0, len( sequence ) - k): 
        start = i
        end = i + k
        kmer = sequence[ i : i+k]
        if kmer not in kmer_query:
            kmer_query[ kmer ] = [start]
        else:
            kmer_query[kmer].append(start)
    # for i, kmer in enumerate(kmer_query):
    #     print kmer, kmer_query[kmer]

for ident, sequence in fasta.FASTAReader( target_fasta):
    sequence = sequence.upper()
    # target_kmer = {}
    for g, i in enumerate(range( 0, len( sequence ) - k)): 
        start = i
        end = i + k
        kmer = sequence[ i : i+k]
        if kmer in kmer_query:
            
            print ident, start, kmer_query[kmer], kmer
        if g == 1000:
            break



    
            


