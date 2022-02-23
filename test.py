import sys
import csv
paths = sys.argv[1].split()
rs = {"students": []}
with open(paths[0]):
    