#// your Python code to implement the features could be placed here
#// note that you may use any language, there is no preference towards Python

import sys
from datetime import datetime,timedelta
import time
import pdb
import heap as hp
import host
import resource as rsc
import hour 
import blocked as blk
import time as tm
import features
import graph as gp
import user



#########################################################
'''
MAIN PROGRAM
'''
#########################################################



start_time = tm.time()

	
f = open('./log_input/log.txt','r',encoding = "ISO-8859-1")

#########################################################
'''
Initialize classes for HOST, RESOURCES, HOURS & BLOCKED
'''
host = host.Host()
resource = rsc.Resource()
ds_hours = hour.Hour()
blockedlist = []
fail = blk.Fail()

#Define the timeframe by delta
delta = timedelta(seconds=60)


#########################################################
'''
Turn the 'feature_five_flag' True if feature SIX is wanted
''' 
feature_five_flag = False
if feature_five_flag:
	connectedIP = gp.Graph()

#########################################################
'''
Turn the 'feature_six_flag' True if feature SIX is wanted
''' 
feature_six_flag = False
if feature_six_flag:
	num_user = user.User()
	target = open('./log_output/user.txt', 'w')
#########################################################


#Define the timeframe by delta
delta = timedelta(seconds=60)



print('Reading files..')

while True:
	line = f.readline().strip()
	#print(line)
	#########################################################
	'''
	STEP 1:
	Read each line and first split them into two parts:
		PART 1: left = x[0]
			This part will contain the HOSTNAME and
			TIMESTAMP
		PART 2: middle = x[1]
			This part will contain the RESOURCE and
			REPLY and BYTE
	'''
	x = line.split('] \"')
	n = len(x)
	if n < 2:
		break

	left = x[0].strip().split('[')
	hostname = left[0].split()[0].strip()

	
	# Save Host
	host.addname(hostname)
	#########################################################
	'''
	Save hours
	'''
	#pdb.set_trace()
	time = left[1].strip()
	t = datetime.strptime(time.split()[0].strip(), "%d/%b/%Y:%H:%M:%S")
	#pdb.set_trace()
	ds_hours.addtime(t, delta)
	
	#########################################################
	'''
	FEATURE 6:
	# Add hostname and user to get number of users for the last 60 secs.
	'''
	if feature_six_flag:
		num_user.add(hostname,t)
		print(time, num_user.getNumUser())
		s = time + ' : '+ str(num_user.getNumUser())+'\n'
		target.write(s)
	
	

	#########################################################
	'''
	STEP 2:
	Split (middle) into several parts to get the values for 
	RESOURCE, REPLY and BYTE
	Use the first THREE elements of the splitted (middle = x[1].split())
		to find the RESOURCE
	Use the last TWO elements of the splitted (middle) to find
		REPLY and BYTE 
	'''
	middle = x[1].strip().split('\"')
	rsrc = middle[0].strip().split()
	
	#########################################################
	'''
	SKIP corrupted lines
	'''
	if len(rsrc) < 2:
		continue
	resourcename = rsrc[1]

	right = middle[-1].strip().split()
	#print(right)
	reply = int(right[0])
	#########################################################
	'''
	blocked IP address
	'''
	if reply == 401:
		#pdb.set_trace()
		data = (hostname, t)
		fail.add(data)
	#else:
	#Check if hostname is in blocked list
	blist = fail.getBkeys()
	if hostname in blist:
		t0 = fail.getBtime(hostname)
		#pdb.set_trace()
		tmp = (t-t0).total_seconds()
		# search if falls within 5 mins time
		if tmp < 301 and tmp > 0:
			blockedlist.append(line)
				
	#########################################################	 
	'''
	Save resources
	'''
	
	if right[1] == '-':
		bytes = 0
		
	else:
		bytes = int(right[1])
	
	
	# Save resources with band width
	resource.addname(resourcename, bytes)	
	#########################################################
	'''
	FEATURE FIVE: Set feature_five_flag to True
	'''
	if feature_five_flag:
		connectedIP.addEdge(resourcename, hostname)
	
	#########################################################




print('File read!')
print('')	
f.close()

'''
FILE HAS BEEN READ. WE SHALL NOW COMPUTE THE FEATURES
'''

print('Printing FEATURE 1')
features.one(host)
print('')


print('Printing FEATURE 2')
features.two(resource)
print('')	


print('Printing FEATURE 3')
hours = ds_hours.getHour()
features.three(hours)	
print('')


print('Printing FEATURE  4')
features.four(blockedlist)


if feature_five_flag:
	print('')
	print('Feature 5')
	features.five(connectedIP)


end_time = tm.time()		
print('')		
print('Runtime:',str(end_time - start_time)+'s')

