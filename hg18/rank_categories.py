import re
import sys
import math
import argparse

parser = argparse.ArgumentParser(description="categorize ranks")
parser.add_argument("ranks", help="file with gene ranks",type=str)
parser.add_argument("gene_names", help="file with gene names", type=str)
args = parser.parse_args()

genes = {}
f = open(args.gene_names,'r')
for line in f:
    genes[line.strip()] = 0
f.close()
print len(genes)

less_10 = 0
less_100 = 0
less_1000 = 0
more = 0
f = open(args.ranks,'r')
for line in f:
    data = re.split("\s+",line.strip())
    if data[1] not in genes:
        print data[1]
        print "not in genes"
    if genes[data[1]] == 0:
        genes[data[1]] = 1
        if int(data[0]) <= 10:
            less_10+=1
        elif int(data[0]) <= 100:
            less_100+=1
        elif int(data[0]) <= 1000:
            less_1000+=1
        else:
            more+=1
           
f.close()

for g in genes:
    if genes[g] == 0:
        more+=1
        print g

print "<= 10: " + str(less_10)
print "<= 100: " + str(less_100)
print "<= 1000: " + str(less_1000)
print "> 1000: " + str(more)

