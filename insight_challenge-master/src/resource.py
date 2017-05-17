import sys
from datetime import datetime,timedelta
import pdb
import heap as hp


class Resource:
	def __init__(self):
		self.item = {}
		self.count = {}
		
		
	def addname(self,rname,bytes):
		if rname not in self.item.keys():
			self.item[rname] = bytes
			self.count[rname] = 1
		else:
			self.item[rname] += bytes
			self.count[rname] += 1
			
	def show(self):
		print(self.item)		
