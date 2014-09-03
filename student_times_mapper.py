#!/usr/bin/python
import sys
import csv
from datetime import datetime
def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	firstline = 0
	for line in reader: # Parse the file
		if firstline==0:
			firstline = 1
			continue
		uid = line[0]
		title = line[1]
		tagnames = line[2]
		author_id = line[3]
		node_type = line[5]
		parent_id = line[6]
		abs_parent_id = line[7]
		added_at = line[8]
		score = line[9]
	
		added_at = added_at.split('.')[0] # Ignore micro-second value
		dateobj =datetime.strptime(added_at, '%Y-%m-%d %H:%M:%S') # Create the date object
		print '{0}\t{2}'.format(author_id, added_at, dateobj.hour) #Print author and hour




mapper()
