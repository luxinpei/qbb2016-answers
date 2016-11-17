#!/usr/bin/env python
import sys
import h5py

file = h5py.File("enrichment.heat")

ctcf = open(sys.argv[1])

ctcf_positions = []
for i, line in enumerate(ctcf):
    fields = line.rstrip("\n\r").split("\t")
    if fields[0] == "chrX":
        ctcf_positions.append(fields[1])
    else:
        continue

# print ctcf_position

positions = file['0.positions'][...]

print positions