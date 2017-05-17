# Define an Undirected graph
import sys

def bfs(G,start):
	xp = [start]
	q = [start]
	d = {}
	d[start] = 0
	while q != []:
		u = q.pop(0)
		for i in G.getEdge(u):
			if i not in xp:
				xp.append(i)
				q.append(i)
				d[i] = d[u] + 1
	levels = []
	for i,j in d.items():
		levels.append((i,j))
	return levels	
		


def bfs1(G,start,end):
	xp = [start]
	q = [start]
	d = {}
	d[start] = 0
	t = 0
	if start == end:
		return 0
	while q != [] and (end not in xp) and (t < 5):
		u = q.pop(0)
		#print(t)
		for i in G.getEdge(u):
			if i not in xp:
				xp.append(i)
				q.append(i)
				t = d[u] + 1
				d[i] = t
				
	if end in d.keys():
		return d[i]
	else:
		return None

'''
def bfs1(G,start,end):
	xp = [start]
	q = [start]
	d = {}
	d[start] = 0
	flag = True
	if start == end:
		return 0
	while (q != []) and (end not in xp) and (not flag):
		u = q.pop(0)
		for i in G.getEdge(u):
			if i not in xp:
				t = d[u] + 1
				flag = t > 4
				xp.append(i)
				q.append(i)
				d[i] = t
				
	if end in d.keys():
		return d[i]
	else:
		return None

'''

class Graph:
	def __init__(self):
		self.item = {}
		self.level = {}
		
	def addVertex(self,u):
		self.item[u] = []
		
	def addEdge(self,u,v):
		if u not in self.item.keys():
			self.item[u] = []
		if v not in self.item.keys():
			self.item[v] = []
		self.item[u].append(v)
		self.item[v].append(u)	
		
	def getVertices(self):
		return list(self.item.keys())
	def show(self):
		for i,j in self.item.items():
			print(i,j,end = ';')
		print('')	
		
	def getEdge(self,u):
		if u in self.item.keys():
			return self.item[u]
		else:
			return ('key not present')
	def setlevel(self):
		for u in self.item.keys():
			l = bfs(self,u)
			self.level[u] = l
		pass
	def getlevel(self,u,v):
		if u in self.item.keys():
			return bfs1(self,u,v)
		else:
			return None	
	def getAlllevel(self):
		return self.level
				
	def getsize(self):
		return len(self.item.keys())
		
		
		
'''		
v = list('ABCDEF')
E = [('A','B'),('A','D'),('B','C'),('C','D'),('C','E'),('D','E')]
G = Graph()
for i in E:
	G.addEdge(i[0],i[1])
	#G.addEdge(v[i],v[i+1])


level = G.getlevel('A','D')
print(level)
#G.setlevel()
#print(G.getAlllevel())
'''








			
