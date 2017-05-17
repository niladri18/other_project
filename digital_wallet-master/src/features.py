import sys
'''
CALCULATES THE FEATURES 
'''


def one(level,target):
	if level == 1:
		#print('trusted')
		s = 'trusted'
	else:
		#print('unverified')
		s = 'unverified'
	target.write(s+'\n')	
	pass
	
def two(level,target):
	
	if level == None:
		#print('unverified')
		s = 'unverified'
	elif level < 3:
		#print('trusted')
		s = 'trusted'
	else:
		#print('unverified')
		s = 'unverified'
	target.write(s+'\n')	
	pass

def three(level,target):
	
	if level == None:
		#print('unverified')
		s = 'unverified'
	elif level < 5:
		#print('trusted')
		s = 'trusted'
	else:
		#print('unverified')
		s = 'unverified'
	target.write(s+'\n')	
	pass

	
