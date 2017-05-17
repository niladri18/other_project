import sys
from datetime import datetime,timedelta
import pdb
import heap as hp

class User:
	
	def __init__(self):
		self.item = hp.MinHeap()
		self.t1 = None

	def add(self,hostname,t):
		
		if self.t1 == None:
			self.t1 = t
			
		self.item.add((hostname,t))	
		diff = timedelta(seconds=0)
		
		t_min = self.item.getmin()[1]
		#pdb.set_trace()
		while ((t - t_min).total_seconds()) > 60:
			t_min = self.item.delmin()[1]  
		
		pass
		
	def getNumUser(self):
		return self.item.getsize()
