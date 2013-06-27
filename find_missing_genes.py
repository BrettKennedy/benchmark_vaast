#!/usr/bin/python                                                                                                                                                                                              

import re
import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Get names of missing genes")
parser.add_argument("vaast_output", help="vaast output of doped file",type=str)
parser.add_argument("gene_names", help="file of gene names that were doped",type=str)
args = parser.parse_args()

gene_names = {}
f = open(args.gene_names,'r')
for line in f:
    name = line.strip()
    gene_names[name] = 0
f.close()

f = open(args.vaast_output,'r')
for line in f:
    m = re.search("Parent=([a-zA-Z0-9-_]+)",line.strip())
    if not m:
        print "problem, could not find gene name"
        print line.strip()
        sys.exit(0)
    name = m.group(1)
    if name in gene_names:
        gene_names[name] = 1
f.close()

for gn in gene_names:
    if gene_names[gn] == 0:
        print gn
