# enumerate_lines.py
import sys

filename = sys.argv[0]
with open(filename) as file:
    for index, line in enumerate(file):
        print(f"{index+1}: {line}", end="")