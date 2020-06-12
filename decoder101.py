from length_setter import analyseHASH
from space_setter import analyseMINUS

fajl = "morse_samples_naloga2.txt"

hashes = analyseHASH(fajl)
minuses = analyseMINUS(fajl)

# print(len(hashes))
# print(len(minuses))
# print('\n')

if len(hashes) > len(minuses):
	minuses.append('space')
elif len(hashes) < len(minuses):
	minuses = minuses[:len(hashes)]

# print(len(hashes))
# print(len(minuses))
# print('\n')

morse = []
for i in range(len(hashes)):
	morse.append(hashes[i])
	morse.append(minuses[i])

# print(morse)
# print('\n')

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
	tuple([]) : ''
}

def breakWORDS(morse):
	words = []
	word = []
	for elem in morse:
		if elem != 'space':
			word.append(elem)
		elif elem == 'space':
			words.append(word)
			word = []
	return words

def condenseLETTERS(letters):
	lettersCOND = []
	for lst in letters:
		for lst2 in lst:
			lst2 = [elem for elem in lst2 if elem != 'char']
			lettersCOND.append(lst2)
	return lettersCOND


def filtrCHAR(word):
	word = [letter for letter in word if letter != 'char']
	return word


def brkLTRS(lst):
	letters = []
	word = []
	for i in range(len(lst)):
		if i == len(lst)-1:
			letters.append(lst[i])
			letters = filtrCHAR(letters)
			word.append(letters)
			letters = []
		elif lst[i] != 'letter':
			letters = filtrCHAR(letters)
			letters.append(lst[i])
		elif lst[i] == 'letter':
			word.append(letters)
			letters = []	
	return word

def breakLETTERS(words):
	lst_lst_words = []
	for lst in words:
		word = brkLTRS(lst)
		lst_lst_words.append(word)
	return lst_lst_words

def neetMorse(morse):
	words = breakWORDS(morse)
	lst_lst_words = breakLETTERS(words)
	return lst_lst_words


def toLatin(lst_lst_words):
	message = ""
	for lst_lst in lst_lst_words:
		word = ""
		for lst in lst_lst:
			word += morseDict.get(tuple(lst))
		message += word
		message += " "
	return message

def controller(morse):
	lst_lst_words = neetMorse(morse)
	message = toLatin(lst_lst_words)
	return message

print('\n')
message = controller(morse)
print(message)
print('\n')







