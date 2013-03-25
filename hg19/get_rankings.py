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
f = open(args.nodope,'r')
for line in f:
    m = re.search("Parent=([0-9A-Za-z_-]+)",line.strip())
    if m:
        gene = m.group(1)
        #if gene not in gene_names:
        data = re.split("\s+",line.strip())
        gene_scores[gene] = [gene,float(data[1]),float(data[2])]
    else:
        print "problem, gene name not found"
        print line.strip()
        sys.exit(0) 
f.close()

f = open(args.doped,'r')
for line in f:
    m =re.search("Parent=([0-9A-Za-z_-]+)",line.strip())
    if m:
        gene = m.group(1)
        if gene in gene_names:
            data = re.split("\s+",line.strip())
            #gene_scores[gene] = [gene,float(data[1]),float(data[2])]
            rank = 1
            genes_info = gene_scores.values() 
            genes_info.append([gene,float(data[1]),float(data[2])])
            for g in sorted(genes_info,key=lambda x: (x[2],-x[1])):
                if g[0] in gene_names:
                    print rank,g[0]
                    break
                rank+=1
    else:
        print "problem, gene name not found"
        print line.strip()
        sys.exit(0)
f.close()

