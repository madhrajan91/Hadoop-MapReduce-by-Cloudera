#!/usr/bin/python
import sys
import csv

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	firstline = 0
	for line in reader: #parse the file
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
		if node_type == 'question': #print uid, author_id for a question
			print '{0}\t{1}'.format(uid, author_id)
		elif node_type =='comment' or node_type=='answer': #Since comments might be present for both question and answers, abs_parent_id holds the question uid where as parent_id might be an answer's uid if the comment was for a question. So we print the abs_parent_id and author_id
			print '{0}\t{1}'.format(abs_parent_id, author_id)

mapper()

		

		
