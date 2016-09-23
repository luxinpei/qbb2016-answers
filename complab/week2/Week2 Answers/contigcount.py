#!/usr/bin/env python

import sys

file = open(sys.argv[1], 'r')
string_list = file.read().split(">")
length = []

for i in range(1, len(string_list)):
    length.append(float(string_list[i].split("_")[3]))

print ("Min " + str(min(length)))
print ("Max " + str(max(length)))
a= str(sum(length) / (len(length)))
print ("average " + a) 
half = str(sum(length) / float(2))
print("halfway " + half)




