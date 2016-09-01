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


#part2
answer_dic = {}
for query_ident, query_sequence in fasta.FASTAReader(query_fasta_2): 
    for gene in target_gene: 
        for kmer in target_gene[gene]: 
            if kmer in kmer_query: 
                for target_start in target_gene[gene][kmer]: 
                    for query_start in kmer_query[kmer]: 
                        target_start = int(target_start)
                        query_start = int(query_start)
                        query_end = int(query_start) + k 
                        target_end = int(target_start) + k
                        match = True

                        while match == True:
                            query_end += 1
                            target_end += 1
                            query_match = query_sequence[query_start:query_end]
                            target_match = target_dict[gene][target_start:target_end]
                            if query_match == target_match:
                                element = [query_start, target_start]
                                if target_match not in answer_dic:
                                    answer_dic[target_match] = [element]
                                answer_dic[target_match].append(element)
                            else:
                                match = False

                         
for i in sorted(answer_dic, key=lambda i: len(i), reverse = True):
    print i
    
            


