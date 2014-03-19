#!/usr/bin/env python

import sys

# input comes from stdin
for line in sys.stdin:
	# remove leading and trailing white spaces
	line = line.strip()
	# split the line into words
	words = line.split()
	# increase counters
	for word in words:
		# write the results to stdout
		# this output will be the input for the reducer
		# 
		# insert a tab inbetween the word, and it's count
		print '%s\t%s' % (word, 1)
