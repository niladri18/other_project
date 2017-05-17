# Written by Niladri Gomes 

import sys

class Heap:
	def __init__(self):
		self.item = []
		self.size = 0
	
	def isEmpty(self):
		return self.item == []
	
	def getsize(self):
		return self.size	
		
	def show(self):
		print(self.item)
	def give(self):
		return self.item
		
	def handleTie(self):
		# Handles ties while removal
		root = self.item[0]
		
		# Find all nodes that have same root[1]
		i = 0
		idx = []
		buff = []
		#pdb.set_trace()
		for x in self.item:
			if x[1] == root[1]:
				idx.append(i)
				buff.append(x)
			i += 1	
		# Replace a sorted buff in the heap
		buff = sorted(buff)
		
		for i in range(len(buff)):
			self.item[idx[i]] = buff[i]				


class MinHeap(Heap):
	'''
	This MinHeap takes a tuple as input
	The tuple is defined as 
	data = ( hostname, current count of the host name(count) )
	The heap property is decided by the count
	'''

	def add(self,data):
		self.size += 1
		self.item.append(data)
		n = self.size-1
		p = (n-1)//2
		c = 0
		while p >= 0 and self.item[p][1] >= self.item[n][1]:
			tmp = self.item[p]
			self.item[p] = self.item[n]
			self.item[n] = tmp
			n = p
			p = (n-1)//2
			
		return
		
	def getmin(self):
		if self.size > 0:
			return self.item[0]
		else:
			return None 	

		
	def minchild(self,p):
		if 2*p + 2 > self.size-1:
			return 2*p + 1
		else:
			c1 = 2*p + 1
			c2 = 2*p + 2
			if self.item[c1][1] < self.item[c2][1]:
				return c1
			else:
				return c2
		
	def delmin(self):
		
		if self.size == 1:
			return self.item.pop()
			self.size -= 1
		else:
			self.handleTie()
			ans = self.item[0]
			t = self.item.pop()
			self.item[0] = t
			self.size -= 1
			p = 0
			c = self.minchild(p)
			while c < self.size and self.item[p][1] > self.item[c][1]:
				tmp = self.item[p]
				self.item[p] = self.item[c]
				self.item[c] = tmp
				p = c
				c = self.minchild(p)
			return ans	

	

class MaxHeap(Heap):
	'''
	This MaxHeap takes a tuple as input
	The tuple is defined as 
	data = ( hostname, current count of the host name(count) )
	The heap property is decided by the count
	'''


		
	def add(self,data):
	
		self.size += 1
		self.item.append(data)
		n = self.size-1
		p = (n-1)//2
		c = 0
		while p >= 0 and self.item[p][1] <= self.item[n][1]:
			tmp = self.item[p]
			self.item[p] = self.item[n]
			self.item[n] = tmp
			n = p
			p = (n-1)//2
			
		return
		

		
	def maxchild(self,p):
		if 2*p + 2 > self.size-1:
			return 2*p + 1
		else:
			c1 = 2*p + 1
			c2 = 2*p + 2
			if self.item[c1][1] > self.item[c2][1]:
				return c1
			else:
				return c2
		
	def delmax(self):
		
		if self.size == 1:
			return self.item.pop()
			self.size -= 1
		else:
			self.handleTie()
			ans = self.item[0]
			t = self.item.pop()
			self.item[0] = t
			self.size -= 1
			p = 0
			c = self.maxchild(p)
			while c < self.size and self.item[p][1] < self.item[c][1]:
				tmp = self.item[p]
				self.item[p] = self.item[c]
				self.item[c] = tmp
				p = c
				c = self.maxchild(p)
			return ans	

'''			
x = [('A',8),('B',9),('C',3),('D',5),('E',1),('F',13),('G',18),('H',22)]
h1 = MaxHeap()
h2 = MinHeap()
for i in x:
	h1.add(i)
	h2.add(i)
	
h1.show()
h2.show()
while not h2.isEmpty():
	r = h2.delmin()
	#h.show()
	print(r)
'''
