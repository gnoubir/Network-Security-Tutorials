#!/usr/bin/python
#
# computer the frequency of lowercase letters

__author__      = "Guevara Noubir"

import collections
import argparse
import string
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Analyze a file.')

# ./basic-analyze-file.py file
# program has one parameter the name of the file to analyze
#
parser.add_argument("file", type=str,
                    help="counts characters frequency file")

# parse arguments 
args = parser.parse_args()

# known statistics of alphabet letters in English text used for comparison
english_alphabet_stats = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]

letters = collections.Counter('')

# opens file and processes line by line using collections module
with open(args.file,'r') as f:
    for line in f:
        for word in line.split():
			letters.update(word.lower())
			#print letters

count = 0
stats = []

# counts the total number of lowercase letters
for l in string.ascii_lowercase:
	count += letters[l]

# computes and prints frequency/probability of each lowercase letter
for l in string.ascii_lowercase:
	stats += [float(letters[l])/count] 
	print l, ": ", float(letters[l])/count 

print "\n ----------------- \n"

#print letters.keys()
#print letters.values()


pos = np.arange(26)
width = 1.0     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos )

ax.set_xticklabels(string.ascii_lowercase)

# rects1 is 
english_bars = plt.bar(range(len(list(string.ascii_lowercase))), english_alphabet_stats, -width/3, color='r', alpha=0.5, align='edge')
this_file_bars = plt.bar(range(len(stats)), stats, width/3, color='g', alpha=0.5, align='edge')

ax.legend((english_bars[0], this_file_bars[0]), ('English Stats', args.file))

#                            
plt.show()
