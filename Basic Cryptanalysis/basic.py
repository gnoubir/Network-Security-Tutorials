#!/usr/bin/python
#
#
__author__      = "Guevara Noubir"

import collections
import argparse
import string
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Process a file.')

parser.add_argument("file1", type=str,
                    help="counts characters frequency in a file")

parser.add_argument("file2", type=str,
                    help="counts characters frequency in a file")

args = parser.parse_args()

english_alphabet_stats = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]

letters1 = collections.Counter('')
letters2 = collections.Counter('')

#print letters

with open(args.file1,'r') as f:
    for line in f:
        for word in line.split():
			letters1.update(word.lower())
			#print letters

count1 = 0
stats1 = []

for l in string.ascii_lowercase:
	count1 += letters1[l]

for l in string.ascii_lowercase:
	stats1 += [float(letters1[l])/count1] 
	print l, ": ", float(letters1[l])/count1 

print "\n ----------------- \n"

with open(args.file2,'r') as f:
    for line in f:
        for word in line.split():
			letters2.update(word.lower())
			#print letters

count2 = 0
stats2 = []

for l in string.ascii_lowercase:
	count2 += letters2[l]

for l in string.ascii_lowercase:
	stats2 += [float(letters2[l])/count2] 
	print l, ": ", float(letters2[l])/count2 

print "\n ----------------- \n"

for l in string.ascii_lowercase:
	print l, ": ", float(letters1[l])/count1 - float(letters2[l])/count2 

print "\n ----------------- \n"

print letters1.keys()
print letters1.values()

pos = np.arange(26)
width = 1.0     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos + (width / 2))

ax.set_xticklabels(string.ascii_lowercase)

print "*****"
print stats1

plt.bar(range(len(stats1)), stats1, width/2, color='g', alpha=0.5, align='edge')
plt.bar(range(len(list(string.ascii_lowercase))), english_alphabet_stats, -width/2, color='r', alpha=0.5, align='edge')
#                            
plt.show()
