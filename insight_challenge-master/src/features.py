import sys
from datetime import datetime,timedelta
import time
import pdb
import heap as hp
import host
import resource as rsc
import hour 
import blocked as blk
import time as tm


def one(host):
	'''
	FEATURE ONE
	'''

	target = open('./log_output/hosts.txt', 'w')
	
	h = hp.MaxHeap()
	
	for i,j in host.item.items():
		#pdb.set_trace()
		h.add((i,j))
	
	#pdb.set_trace()
	i = 0
	while i < 10:
		if h.isEmpty():
			break
		curr = h.delmax()
		print(curr[0],curr[1])
		s = str(curr[0]) + ','+ str(curr[1]) + '\n'
		target.write(s)
		i += 1
		
	pass
			
def two(resource):
	'''
	FEATURE TWO
	'''
	target = open('./log_output/resources.txt', 'w')	
	h = hp.MaxHeap()
		
	for i,j in resource.item.items():
		#pdb.set_trace()
		h.add((i,j))
		
	i = 0
	prev = -1
	while i < 10 and not h.isEmpty():
		curr = h.delmax()
		print(curr[0])
		s = str(curr[0]) + '\n'
		target.write(s)
		i += 1
		
	pass		
					
def three(hours):
	'''
	FEATURE THREE
	'''
	target = open('./log_output/hours.txt', 'w')
	h = hp.MaxHeap()
	for i,j in hours.items():
		#pdb.set_trace()
		h.add((i,j))
	
	i = 0
	while not h.isEmpty() and i < 10:
		curr = h.delmax()
		print(curr)
		s = str(curr[0]) + ','+ str(curr[1]) + '\n'
		target.write(s)
		i += 1
	pass	


		
def four(blockedlist):
	'''
	FEATURE FOUR
	'''
	target = open('./log_output/blocked.txt', 'w')
	for i in blockedlist:
		target.write(i+'\n')
		print(i)
	pass				

def five(connectedIP):
	'''
	FEATURE FIVE (ADDITIONAL)
	'''
	target = open('./log_output/connectIP.txt', 'w')	
	h = hp.MaxHeap()
		
	for i,j in connectedIP.item.items():
		#pdb.set_trace()
		tmp = (i,j)
		h.add((tmp,len(j)))
		
	i = 0
	prev = -1
	while i < 10 and not h.isEmpty():
		curr = h.delmax()
		print(curr[0][0],curr[1])
		s = str(curr[0][0]) +','+str(curr[1])+ '\n'
		target.write(s)
		i += 1
		
	pass						


