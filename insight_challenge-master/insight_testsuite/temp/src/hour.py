import sys
from datetime import datetime,timedelta
import pdb
import heap as hp

class Hour:
	def __init__(self):
		self.item = {}
		self.t1 = None
		
		# save timestamps in an array
		#self.frame = [0 for i in range(60)]

		
			
	def show(self):
		print(self.item)
		
	
	def addtime(self,t,delta):
		# set time decrement by 1
		d = timedelta(seconds=1)
		if self.t1 == None:
			self.t1 = t
			
			
		diff = timedelta(seconds=0)
		t_curr = t 
		# populate all timestamps for which this time falls within delta
		#pdb.set_trace()
		while diff < delta:
			timestamp = t.strftime("%d/%b/%Y:%H:%M:%S -0400")
			if timestamp not in self.item.keys():
				self.item[timestamp] = 1
			else:
				self.item[timestamp] += 1
			t -= d
			if t < self.t1:
				break
			diff = t_curr - t

		
		'''
		We will evict redundant timestamps that are older than 60 secs,
		They won't contribute to the heap.
		Their contributions are saved in the heap anyway.
		
		REMEMBER: The most relevant time stamp is saved in (t) 
		
		timestamp = list(self.item.keys())
		
		for i in timestamp :
			t_i = datetime.strptime(i, "%d/%b/%Y:%H:%M:%S -0400")
			if t_i <= t:
				if i in list(self.item.keys()):
					self.item.pop(i) 
		
		'''	
		pass		
		


		
	def getHour(self):
		return self.item	
		
					 
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
				


