import sys
from datetime import datetime,timedelta
import pdb
import heap as hp

class Host:
	def __init__(self):
		self.item = {}
		
		
	def addname(self,hostname):
		if hostname not in self.item.keys():
			self.item[hostname] = 1
		else:
			self.item[hostname] += 1
			
	def show(self):
		print(self.item)
		
		

