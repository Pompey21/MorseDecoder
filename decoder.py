file = open("sporocilo.txt", 'r')
word = []
memory = []
counter = 0

while 1:
	char = file.read(1)
	word.append(char)

	if char == '-':
		counter += 1
		if counter == 60:
			memory.append(word)
			word = []
	elif char == '#':
		counter = 0

	elif not char:
		break

# print(len(memory))


# turning lists (encoded words) to strings (still encoded words)
memoryStrs = []
for elem in memory:
	strs = ""
	for char in elem:
		strs += char
	memoryStrs.append(strs)


# *******************************************************
# *******************************************************
# -------------------------------------------------------
# 						-----------
# 						| METHODS |
#						-----------
# -------------------------------------------------------

# method 'frontCut2' cuts the '-' characters from the front to make sure
# the letter starts with either a dot or a line. method 'backCut' cuts
# the '-' characters from the back to make sure the letter ends with a 
# dot or a line. this way further encoding is much easier since the '-'
# only represents the spacing withing the same letter.
def frontCut2(memory):
	memoryCut = []
	for elem in memory:
		while True:
			if len(elem) >= 2:
				# print(elem)
				if elem[0] == '-':
					elem = elem[1:]
				else:
					memoryCut.append(elem)
					break
			else:
				break
	return memoryCut


def backCut(memory):
	memoryCut = []
	for elem in memory:
		while True:
			if len(elem) >= 2:
				#print(elem)
				if elem[-1] == '-':
					elem = elem[:-1]
				else:
					memoryCut.append(elem)
					break
			else:
				break
	return memoryCut


def spaceCut(memory):
	# cut the spaces
	frontCut = frontCut2(memory)
	allCut = backCut(frontCut)
	# form strings from lists
	final = []
	for elem in allCut:
		list2str = ""
		for char in elem:
			list2str += char
		final.append(list2str)
	return final


# final = spaceCut(memoryStrs)
# # print('\n')
# print(final)
# print('\n')


# -------------------------------------------------------
# 						-----------
# 	| RECURSIVELY CALLED ON THE WHOLE LIST OF WORDS |
#						-----------
# -------------------------------------------------------

# RECURSIVELY CALLED ON THE WHOLE LIST OF WORDS
# method 'divideWord' divides the word into separate letters
# method 'dotOrLine2' splits the letter into separate entities of dots and 
# lines defined in terms of the length os strings of '#'. method 'toMorse'
# then translates those entities into 'dot' or 'line' so that is easier
# for further decoding.

def divideWord(word):
	letters = word.split('-------------------------')
	letters = spaceCut(letters)
	return letters

# letters = divideWord(final[0])
# print(letters)

def dotOrLine2(msg):
	memory = msg.split('-')
	memory_filtered = [elem for elem in memory if elem != '']
	return memory_filtered

def toMorse(msg):
	morse = []
	for elem in msg:
		if len(elem) > 5 and len(elem) < 15:
			morse.append('dot')
		elif len(elem) > 25 and len(elem) < 35:
			morse.append('line')
	return morse

def toMorseALL(msg):
	cropped = []
	for letter in msg:
		cropped.append(toMorse(dotOrLine2(letter)))
	return cropped

# cropped = toMorseALL(letters)
# print(cropped)
# print('\n')

# method 'morseToLatin' decodes the word from the list of 'dot' and 'line'
# to latin by using the dictionary 'morseDict' defined above.
morseDict = {
	tuple(['dot', 'line']) : 'A',
	tuple(['line', 'dot', 'dot', 'dot']) : 'B',
	tuple(['line', 'dot', 'line', 'dot']) : 'C',
	tuple(['line', 'dot', 'dot']) : 'D',
	tuple(['dot']) : 'E',
	tuple(['dot', 'dot', 'line', 'dot']) : 'F',
	tuple(['line', 'line', 'dot']) : 'G',
	tuple(['dot', 'dot', 'dot', 'dot']) : 'H',
	tuple(['dot', 'dot']) : 'I',
	tuple(['dot', 'line', 'line', 'line']) : 'J',
	tuple(['line', 'dot', 'line']) : 'K',
	tuple(['dot', 'line', 'dot', 'dot']) : 'L',
	tuple(['line', 'line']) : 'M',
	tuple(['line', 'dot']) : 'N',
	tuple(['line', 'line', 'line']) : 'O',
	tuple(['dot', 'line', 'line', 'dot']) : 'P',
	tuple(['line', 'line', 'dot', 'line']) : 'Q',
	tuple(['dot', 'line', 'dot']) : 'R',
	tuple(['dot', 'dot', 'dot']) : 'S',
	tuple(['line']) : 'T',
	tuple(['dot', 'dot', 'line']) : 'V',
	tuple(['dot', 'dot', 'dot', 'line']) : 'U',
	tuple(['dot', 'line', 'line']) : 'W',
	tuple(['line', 'dot', 'dot', 'line']) : 'X',
	tuple(['line', 'dot', 'line', 'line']) : 'Y',
	tuple(['line', 'line', 'dot', 'dot']) : 'Z',
	tuple(['dot', 'line', 'line', 'line', 'line']) : '1',
	tuple(['dot', 'dot', 'line', 'line', 'line']) : '2',
	tuple(['dot', 'dot', 'dot', 'line', 'line']) : '3',
	tuple(['dot', 'dot', 'dot', 'dot', 'line']) : '4',
	tuple(['dot', 'dot', 'dot', 'dot', 'dot']) : '5',
	tuple(['line', 'dot', 'dot', 'dot', 'dot']) : '6',
	tuple(['line', 'line', 'dot', 'dot', 'dot']) : '7',
	tuple(['line', 'line', 'line', 'dot', 'dot']) : '8',
	tuple(['line', 'line', 'line', 'line', 'dot']) : '9',
	tuple(['line', 'line', 'line', 'line', 'line']) : '0',
	tuple(['dot', 'line', 'dot', 'line', 'dot', 'line']) : '.',
	tuple(['line', 'line', 'dot', 'dot', 'line', 'line']) : ',',
	tuple(['dot', 'dot', 'line', 'line', 'dot', 'dot']) : '?',
	tuple(['dot', 'dot', 'line', 'line', 'dot']) : '!',
	tuple(['line', 'line', 'line', 'dot', 'dot', 'dot']) : ':',
	tuple(['dot', 'line', 'dot', 'dot', 'line', 'dot']) : '"',
	tuple(['line', 'dot', 'dot', 'dot', 'line']) : '=',
	tuple(['line', 'dot', 'line', 'line', 'dot']) : '(',
	tuple(['line', 'dot', 'line', 'line' , 'dot', 'line']) : ')',
	tuple([]) : ''
}

def morseToLatin(morse):
	message = ""
	for char in morse:
		message += (morseDict[tuple(char)])
	return message

# message = morseToLatin(cropped)
# print(message)


def wordController(word):
	letters = divideWord(word)
	cropped = toMorseALL(letters)
	message = morseToLatin(cropped)
	return message

# message = wordController(final[0])
#print(message)

# RECURSIVE CALL ON ALL WORDS OBTAINED 
def recursiveCall(words):
	sentance = []
	for word in words:
		sentance.append(wordController(word))
	sentance = ' '.join(sentance)
	return sentance

# sentance = recursiveCall(final)
# print(sentance)


# -------------------------------------------------------
# 						-----------
# 				 	  | CONTROLLER |
#						-----------
# -------------------------------------------------------

def controller(memory):
	final = spaceCut(memoryStrs)
	sentance = recursiveCall(final)
	return sentance

sentance = controller(memory)
print(sentance)










