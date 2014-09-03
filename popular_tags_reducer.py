#!/usr/bin/python
#incoming format is tag \t 1
import sys



def reducer():
	oldKey=None
	count=0
	toptenlist = [0]*10 #Stores the top ten tags' value.
	toptennames= [None]*10 #Stores the top ten tagnames. A more efficient way would have been to have an array of classes whose members were count and name
	for line in sys.stdin:
		data = line.strip().split('\t')
		if len(data)!=2:
			print 'something is wrong with the length'
			continue
		
		thisTag, thisCount = data
		
		if oldKey and oldKey!=thisTag:
			#print '{0}\t{1}'.format(oldKey, count)
			for i in range(10):
				if count > toptenlist[i]: #add the value and the name to their respective lists if the count is > than the value at that position
					toptenlist.insert(i, count)
					toptennames.insert(i, oldKey)
					break
			count=0

		oldKey=thisTag
		count+=int(thisCount)
		
	if oldKey!=None:
		for i in range(10):
			if count > toptenlist[i]:
				toptenlist.insert(i, count)
				toptennames.insert(i, oldKey)
				break
		
		

	for i in range(10):
		print toptennames[i], "\t", toptenlist[i]
reducer()
