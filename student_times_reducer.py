#!/usr/bin/python
# format is author_id \t hour
import sys
from datetime import datetime

def reducer():
	oldKey = None
	mydic ={}
	maxkey=None
	maxval=0
	maxflag=0
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 2:
			continue
		
		thisKey, thisHour = data

		if oldKey and oldKey!= thisKey:
			#print '********************************* AUTHOR ID = {0} **********************************'.format(oldKey)
			for k, v in mydic.items(): #Check if there a tie in the maximum activity at an hour. If there is a tie print all authors
				if v > maxval:
					maxval = v
					maxkey = k
				elif v==maxval:
					maxflag=1
					break
				
			if maxflag == 0: #No tie since maxflag was zero
				print "AUTHOR {0} MAXIMUM HOUR IS {1}, THE NUMBER OF RESPONSES IS {2} ".format(oldKey, maxkey, maxval)

			else: # two or more hours had maximum activity so print all the hours and their maximums
				print "AUTHOR {0} HAD MORE THAN 1 HOUR OF MAXIMUM ACTIVITY ".format(oldKey)
				for k,v in mydic.items():
					if v==maxval: #CODE CHANGE-print only the maximum hours
						print "\tIN HOUR {0} THE AUTHOR RESPONDED {1} TIME ".format(k, v)
			#print '#########################################################################################'
			oldKey= thisKey
			mydic={}
			maxflag=0
			maxkey=None
			maxval=0
		oldKey=thisKey
		if thisHour in mydic.keys(): #Each hour becomes a key in the dictionary with the count of occurences in that hour as the value
			mydic[thisHour] += 1
		else:
			mydic[thisHour] = 1
	if oldKey!=None:
		#print '********************************* AUTHOR ID = {0} **********************************'.format(oldKey)
		for k, v in mydic.items(): #Check if there a tie in the maximum activity at an hour. If there is a tie print all authors
			if v > maxval:
				maxval = v
				maxkey = k
			elif v==maxval:
				maxflag=1
				break
				
		if maxflag == 0: #No tie since maxflag was zero
			print "AUTHOR {0} MAXIMUM HOUR IS {1}, THE NUMBER OF RESPONSES IS {2} ".format(oldKey, maxkey, maxval)
		else: # two or more hours had maximum activity so print all the hours and their maximums
			print "AUTHOR {0} HAD MORE THAN 1 HOUR OF MAXIMUM ACTIVITY ".format(oldKey)
			for k,v in mydic.items():
				print "\tIN HOUR {0} THE AUTHOR RESPONDED {1} TIME ".format(k, v)
		#print '#########################################################################################'

reducer()


	


	
	

