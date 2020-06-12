def startHASH(fajl):
	file = open(fajl, 'r')
	hashes = []
	counter = 0

	while 1:
		char = file.read(1)

		if char == '#':
			counter += 1
		elif char == '-':
			hashes.append(counter)
			counter = 0

		elif not char:
			break
	return hashes

	file.close()

def delet0s(hashes):
	hashesNEW = [hash for hash in hashes if hash != 0]
	return hashesNEW

def getMid(hashes):
	maxm = max(hashes)
	minm = min(hashes)
	mid = (maxm + minm) / 2
	return maxm, minm, mid

def classification(hashes):
	maxm, minm, mid = getMid(hashes)
	legend = []
	for elem in hashes:
		options = []
		classes = {}
		classes.update(maxm=abs(elem-maxm))
		classes.update(minm=abs(elem-minm))
		# print(classes)

		if classes.get('maxm') <= classes.get('minm'):
			options.append('line')
		else:
			options.append('dot')
		legend.append(options)

	legend = [item for sublist in legend for item in sublist]
	return legend

def controllerHASH(hashes):
	hashesNEW = delet0s(hashes)
	legend = classification(hashesNEW)
	# print(hashesNEW)
	# print(legend)
	return legend

def analyseHASH(fajl):
	hashes = startHASH(fajl)
	legend = controllerHASH(hashes)
	return legend


# legend = analyseHASH("morse_samples_naloga3.txt")
#print(legend)
