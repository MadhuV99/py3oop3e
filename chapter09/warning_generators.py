# warning_generators.py 
import sys

# inname = sys.argv[1]
# outname = sys.argv[2]

inname = 'sample_log.txt'
outname = 'no_warnings.txt'
# generator expression
# with open(inname) as infile:
#     with open(outname, "w") as outfile:
#         warnings = (
#                     l.replace("    WARNING", "") for l in infile if "WARNING" in l
#                     )
#         for l in warnings:
#             outfile.write(l)

# normal loop
with open(inname) as infile:
    with open(outname, "w") as outfile:
        for l in infile:
            if "WARNING" in l:
                outfile.write(l.replace("    WARNING", "")) 
