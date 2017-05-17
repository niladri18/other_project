import sys

def one(level):
	target = open('./paymo_output/output1.txt', 'w')
	if level == 1:
		#print('trusted')
		s = 'trusted'
	else:
		#print('unverified')
		s = 'unverified'
	target.write(s)	
	pass
	
def two(level):
	target = open('./paymo_output/output2.txt', 'w')
	if level == None:
		#print('unverified')
		s = 'unverified'
	elif level < 3:
		#print('trusted')
		s = 'trusted'
	else:
		#print('unverified')
		s = 'unverified'
	target.write(s)	
	pass

def three(level):
	target = open('./paymo_output/output3.txt', 'w')
	if level == None:
		#print('unverified')
		s = 'unverified'
	elif level < 5:
		#print('trusted')
		s = 'trusted'
	else:
		#print('unverified')
		s = 'unverified'
	target.write(s)	
	pass

	
