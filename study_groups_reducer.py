#!/usr/bin/python
import sys



def reducer():
	oldKey=None
	count=0
	authorlist={}
	for line in sys.stdin:
		data = line.strip().split('\t')
		if len(data)!=2:
			print 'something is wrong with the length'
			continue
		
		thisTag, thisAuthor = data
		
		if oldKey and oldKey!=thisTag:
			#print '{0}\t{1}'.format(oldKey, count)
			print '######################' #print the discussion thread and the number of posts
			print 'The thread with id: {0} there were {1} posts'.format(oldKey, count)
			for k,v in authorlist.items(): #print the authors participating in that thread and their intensity
				print '\t The author {0} had an intensity of {1}'.format(k, v)
			authorlist={}
			count=0

		oldKey=thisTag
		if thisAuthor in authorlist.keys(): #add author to the key for each discussion thread and the value being the intensity-which is count of the number of times they have participated in the same discussion	
			authorlist[thisAuthor]+=1
		else:
			authorlist[thisAuthor]=1
		count+=1
		
	if oldKey!=None:
		print '######################'
		print 'The thread with id: {0} there were {1} posts'.format(oldKey, count)
		for k,v in authorlist.items():
			print '\t The author {0} had an intensity of {1}'.format(k, v)
		
		

	
reducer()
