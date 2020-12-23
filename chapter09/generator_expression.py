# generator_expression.py
import sys

# inname = sys.argv[1]
# outname = sys.argv[2]
inname = 'sample_log.txt'
outname = 'sample_warnings.txt'
with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (l for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)
