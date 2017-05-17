import sys
import graph as gp
from datetime import datetime,timedelta
import pdb
import time as tm
import features as feature




start_time = tm.time()
G = gp.Graph()


#pdb.set_trace()

########################################################
'''
Read the batch file
'''
#f = open('b2.txt','r',encoding = "ISO-8859-1")
f = open('./paymo_input/batch_payment.txt','r',encoding = "ISO-8859-1")
features = f.readline().strip().split(',')
while True:
	line = f.readline().strip()
	if line == '':
		break
	#print(line)
	x = line.split(',')
	'''
	Handle corrupted lines
	'''
	if len(x) != 5:
		continue
	id1 = x[1].strip()
	id2 = x[2].strip()
	G.addEdge(id1,id2)

f.close()

########################################################
'''
Read the stream file line by line and write them to a file
'''
#f = open('s2.txt','r',encoding = "ISO-8859-1")
f = open('./paymo_input/stream_payment.txt','r',encoding = "ISO-8859-1")

'''
Open output files
'''
target1 = open('./paymo_output/output1.txt', 'w')
target2 = open('./paymo_output/output2.txt', 'w')
target3 = open('./paymo_output/output3.txt', 'w')

features = f.readline().strip().split(',')
while True:
	line = f.readline().strip()
	if line == '':
		break
	x = line.split(',')
	'''
	Handle corrupted lines
	'''
	if len(x) != 5:
		continue
	id1 = x[1].strip()
	id2 = x[2].strip()
	l = G.getlevel(id1,id2)
	
	'''
	FEATURES
	'''
	feature.one(l,target1)
	feature.two(l,target2)
	feature.three(l,target3)
		
	

f.close()
target1.close()
target2.close()
target3.close()
end_time = tm.time()		
print('')		
print('Runtime:',str(end_time - start_time)+'s')


	
