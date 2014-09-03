#!/usr/bin/python
#For an answer parent id corresponds to the question
import sys
import csv
from datetime import datetime
import re
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
		
		
		#if '\t' in body:
		#	print body
		body = re.sub('\s', ' ', body)
		if node_type=='question': #If type is question print uid and Q (for question) and body. [s3p7r] is a delimiter
			print '{0}[s3p7r]Q[s3p7r]{1}'.format(uid, body) 
		elif node_type=='answer' and parent_id!='': #If type is answer print parent_id and A(for answer) and body. We igorne comments
			print '{0}[s3p7r]A[s3p7r]{1}'.format(parent_id, body)



mapper()
