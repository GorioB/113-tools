from random import randint,sample

def randomHex(hexSize):
	retVal=''
	for i in range(0,hexSize):
		retVal=retVal+sample(['1','2','3','4',
			'5','6','7','8',
			'9','0','a','b',
			'c','d','e','f'],1)[0]
	return retVal

def randomize(filename,n):
	f = open(filename,'w')
	d=[]
	pool=[]
	for i in range(0,8):
		pool.append(randomHex(5))

	for i in range(0,n):
		d.append(sample(pool,1)[0]+randomHex(3))

	d = '\n'.join(d)
	f.write(d)
	f.close()

if __name__=='__main__':
	randomize("testaddresses.txt",1024)
	e = raw_input("OK!")