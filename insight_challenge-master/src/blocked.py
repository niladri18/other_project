import sys
from datetime import datetime,timedelta
import pdb
import heap as hp

class Fail:
	def __init__(self):
		self.item = {}
		self.blocked = {}
		self.t0 = None
		
	def add(self,data):
		'''
		# We start a MinHeap in the name of every new
		# failed hostname(= data[0] ),
		# with the time (data[1]) as the key
		'''
		#pdb.set_trace()
		
		t = data[1]
		if data[0] not in list(self.item.keys()):
			self.item[data[0]] = hp.MinHeap()
		
		self.item[data[0]].add(data)
		
		# Get the minimum time in the heap
		t0 = self.item[data[0]].getmin()
		
		#pdb.set_trace()
		
		# Update self.item[hostname] based on the 20 sec rule
		while (t-t0[1]).total_seconds() > 20:
			t0 = self.item[data[0]].delmin()
			
		# if the number of failed attempt is 3, add
		# the IP address and the time stamp to the blocked list
		if self.item[data[0]].getsize()	== 3:
			self.blocked[data[0]] = t
			
	def show(self):
		print(self.item)	

	def getBlist(self):
		return self.blocked
		
	def getBkeys(self):
		return list(self.blocked.keys())
	def getBtime(self,u):
		return self.blocked[u]
		
		
