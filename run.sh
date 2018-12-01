#!/bin/bash

for prime in `cat prime.input`
do
    echo "Running for $prime"
    python3 certificateGraph.py $prime
done
rm sample-output/*.gv
