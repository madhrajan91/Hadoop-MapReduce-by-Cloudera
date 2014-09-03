#!/usr/bin/python
import sys
import csv

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	firstline = 0
	for line in reader: #Parse the file
		if firstline==0:
			firstline = 1
			continue
		uid = line[0]
		title = line[1]
		tagnames = line[2]
		author_id = line[3]
		body = line[4]
		node_type = line[5]
		parent_id = line[6]
		abs_parent_id = line[7]
		added_at = line[8]
		score = line[9]
		if node_type == 'question': #If the node_type is a 'question' split the tags by space and print the tag and a value 1
			tags = tagnames.split()
			for tag in tags:
				print '{0}\t1'.format(tag)

mapper()

		

		
