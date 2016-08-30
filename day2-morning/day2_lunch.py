#!/usr/bin/env python

import sys
f = open( sys.argv[1] )

counter = 0
for line in f:
    if line.startswith( "SRR"):
        counter +=1

print counter

# f = open( 'SRR072893.sam' )
#
# counter = 0
# for line in f:
#     if line.startswith( "SRR"):
#         fields = line.rstrip( "\r\n").split( "\t") #= equals
#         if fields[5] == "40M": #== checking
#             counter +=1
#
# print counter

# import sys
#
# f = open( sys.argv[1] )
#
# counter = 0
# for line in f:
#     if "NH:i:1" in line:
#             counter +=1
#
# print counter

# import sys
# f = open( sys.argv[1] )
#
# counter = 0
#
# for line in f:
#     if line.startswith( "SRR"):
#         print(lines.split("\t")[2])
#         counter +=1
#     if counter == 10:
#         break
#
# import sys
# f = open( sys.argv[1] )
# total_value = 0
# entry = 0.0
#
# for line in f:
#     if line.startswith( "SRR"):
#         if line.split("\t")[4] != "255":
#            total_value += int(line.split("\t")[4])
#            entry += 1
#
# print (total_value / entry )
















        