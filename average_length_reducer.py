#!/usr/bin/python
#'[s3p7r]
import sys
import csv

def reducer():
	oldKey = None
	anslist = []
	qbody= None
	for line in sys.stdin:
		data = line.strip().split('[s3p7r]')
		if len(data) != 3:
			print 'some thing is wrong with the length'
			continue		
		thisID, thisType, thisBody = data
		if oldKey and oldKey!=thisID:
			if anslist!=None and len(anslist)>0:
				anssum=0
				for ans in anslist: #iterate through the answers for a question
					anssum+=len(ans) #sum up the lengths
					#if oldKey=='44246':
					#	print ans
				anslen=anssum/len(anslist) #Average length
			else:
				anslen=0
			if qbody!=None:
				qlen=len(qbody) #find the length of question
			else:
				qlen=0
			#if oldKey=='44246':
			#	print len(anslist)
			print '{0}\t{1}\t{2}'.format(oldKey, qlen, anslen)  #key question-length answer-length
			qbody=None
			anslist=[]
			

		oldKey=thisID
		if thisType == 'A': #If answer and add answer to the answer list
			anslist.append(thisBody)
		elif thisType == 'Q':#If question assign question to a variable called qbody
			qbody=thisBody

			
	if oldKey!=None:
		anssum=0
		for ans in anslist:
			anssum+=len(ans)
		anslen=anssum/len(anslist)
		print '{0}\t{1}\t{2}'.format(oldKey, len(qbody), anslen) #key question-length answer-length		
		
	

		
reducer()


	


	
	

