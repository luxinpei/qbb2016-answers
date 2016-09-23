#!/usr/bin/env python

import sys
# import fasta

file = open(sys.argv[1], 'r')
string_list = file.read().split(">")
length = []

for i in range(1, len(string_list)):
    length.append(float(string_list[i].split("_")[3]))

a = str(sum(length) / float(2))
half = float(a)

for item in length:
    item = int(item)

sortedlist = sorted(length)

counter = 0
for item in sortedlist:
    if counter < half:
        counter += item
    else:
        print ("N50 " + str(item))
        break
