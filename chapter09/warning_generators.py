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
# with open(inname) as infile:
#     with open(outname, "w") as outfile:
#         for l in infile:
#             if "WARNING" in l:
#                 outfile.write(l.replace("    WARNING", "")) 

# object-oriented
# class WarningFilter:
#     def __init__(self, insequence):
#         self.insequence = insequence

#     def __iter__(self):
#         return self

#     def __next__(self):
#         l = self.insequence.readline()
#         while l and "WARNING" not in l:
#             l = self.insequence.readline()
#         if not l:
#             raise StopIteration
#         return l.replace("    WARNING", "")

# with open(inname) as infile:
#     with open(outname, "w") as outfile:
#         filter = WarningFilter(infile)
#         for l in filter:
#             outfile.write(l)

# # Generator with yield
def warnings_filter(insequence):
    # for l in insequence:
    #     if "WARNING" in l:
    #         yield l.replace("    WARNING", "")
    yield from (
                l.replace("    WARNING", "") for l in insequence if "WARNING" in l
                )


with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)

# print(dir(warnings_filter([])))