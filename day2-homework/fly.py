#!/usr/bin/env python

import sys
f = open( sys.argv[1])


i = 0
for line in f:
    #if i < 100:
        if "DROME" in line:
            fields = line.split()
            if len(fields) == 4:
            print fields[2], "\t", fields[3]
            #i += 1
    
