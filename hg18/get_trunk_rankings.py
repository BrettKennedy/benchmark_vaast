#!/usr/bin/python

import re
import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Get ranks of doped genes")
parser.add_argument("nodope", help="vaast ouput of undoped file",type=str)
parser.add_argument("doped", help="vaast output of doped file",type=str)
parser.add_argument("gene_names", help="file of gene names that were doped",type=str)
args = parser.parse_args()

gene_names = {}
f = open(args.gene_names,'r')
for line in f:
    name = line.strip()
    gene_names[name] = 0
f.close()

gene_scores = {}
index = 0
f = open(args.nodope,'r')
for line in f:
    if index > 0:
        data = re.split("\s+",line.strip())
        gene = data[1]
        gene_scores[gene] = [gene,float(data[4]),float(data[2])]
    index+=1
f.close()

index = 0
f = open(args.doped,'r')
for line in f:
    if index > 0:
        data = re.split("\s+",line.strip())
        gene = data[1]
        if gene in gene_names:
            rank = 1
            genes_info = gene_scores.values() 
            genes_info.append([gene,float(data[4]),float(data[2])])
            for g in sorted(genes_info,key=lambda x: (x[2],-x[1])):
                if g[0] == gene:
                    print rank,g[0]
                    break
                rank+=1
    index+=1
f.close()

