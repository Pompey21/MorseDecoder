	
def startMINUS(fajl):
	file = open(fajl, 'r')
	hashes = []
	counter = 0

	while 1:
		char = file.read(1)

		if char == '-':
			counter += 1
		elif char == '#':
			hashes.append(counter)
			counter = 0

		elif not char:
			break
	return hashes

	file.close()

def delet0s(hashes):
	hashesNEW = [hash for hash in hashes if hash != 0]
	return hashesNEW

def findingKs(hashes):
	maxm = max(hashes)
	minm = min(hashes)
	mid = (maxm+minm)/2
	return maxm, minm, mid

def classification(hashes):
	maxm, minm, mid = findingKs(hashes)
	legend = []
	for elem in hashes:
		options = []
		classes = {}
		classes.update(maxm=abs(elem-maxm))
		classes.update(minm=abs(elem-minm))
		classes.update(mid=abs(elem-mid))
		# print(classes)
		# print(classes.get('maxm'))

		if classes.get('maxm') <= classes.get('minm') and classes.get('maxm') <= classes.get('mid'):
			options.append('space')
		elif classes.get('minm') <= classes.get('maxm') and classes.get('minm') <= classes.get('mid'):
			options.append('char')
		else:
			options.append('letter')
		legend.append(options)

	legend = [item for sublist in legend for item in sublist]
	return legend

def controllerMINUS(hashes):
	hashesNEW = delet0s(hashes)
	legend = classification(hashesNEW)
	# print(hashesNEW)
	# print(legend)
	return legend


def analyseMINUS(fajl):
	hashes = startMINUS(fajl)
	legend = controllerMINUS(hashes)
	return legend

# legend = analyseMINUS()
#print(legend)







