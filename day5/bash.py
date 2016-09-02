#!/bin/bash

for i in *.bw
do
    bigWigAverageOverBed -bedOut=${i%bw}bed $i promoter.bed ${i%bw}tab
done