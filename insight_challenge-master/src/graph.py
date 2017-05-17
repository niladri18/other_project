import sys
from datetime import datetime,timedelta
import pdb
import heap as hp


class Graph:
	def __init__(self):
		self.item = {}
		
		
	def addEdge(self,rname,hostname):
		if rname not in self.item.keys():
			self.item[rname] = [hostname]
		else:
			if hostname not in self.item[rname]:
				self.item[rname].append(hostname)
			
	def show(self):
		print(self.item)		
