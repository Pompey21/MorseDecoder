print("What would you like to encode today? (type bellow)")

# This is where your input is read and stored -> text
text = input("")

# Parsing the inputed text into separate words
text = text.split()
#print(text)

morseCode = {
	'A' : ['dot', 'line'],
	'a' : ['dot', 'line'],
	'B' : ['line', 'dot', 'dot', 'dot'],
	'b' : ['line', 'dot', 'dot', 'dot'],
	'C' : ['line', 'dot', 'line', 'dot'],
	'c' : ['line', 'dot', 'line', 'dot'],
	'D' : ['line', 'dot', 'dot'],
	'd' : ['line', 'dot', 'dot'],
	'E' : ['dot'],
	'e' : ['dot'],
	'F' : ['dot', 'dot', 'line', 'dot'],
	'f' : ['dot', 'dot', 'line', 'dot'],
	'G' : ['line', 'line', 'dot'],
	'g' : ['line', 'line', 'dot'],
	'H' : ['dot', 'dot', 'dot', 'dot'],
	'h' : ['dot', 'dot', 'dot', 'dot'],
	'I' : ['dot', 'dot'],
	'i' : ['dot', 'dot'],
	'J' : ['dot', 'line', 'line', 'line'],
	'j' : ['dot', 'line', 'line', 'line'],
	'K' : ['line', 'dot', 'line'],
	'k' : ['line', 'dot', 'line'],
	'L' : ['dot', 'line', 'dot', 'dot'],
	'l' : ['dot', 'line', 'dot', 'dot'],
	'M' : ['line', 'line'],
	'm' : ['line', 'line'],
	'N' : ['line', 'dot'],
	'n' : ['line', 'dot'],
	'O' : ['line', 'line', 'line'],
	'o' : ['line', 'line', 'line'],
	'P' : ['dot', 'line', 'line', 'dot'],
	'p' : ['dot', 'line', 'line', 'dot'],
	'Q' : ['line', 'line', 'dot', 'line'],
	'q' : ['line', 'line', 'dot', 'line'],
	'R' : ['dot', 'line', 'dot'],
	'r' : ['dot', 'line', 'dot'],
	'S' : ['dot', 'dot', 'dot'],
	's' : ['dot', 'dot', 'dot'],
	'T' : ['line'],
	't' : ['line'],
	'V' : ['dot', 'dot', 'line'],
	'v' : ['dot', 'dot', 'line'],
	'U' : ['dot', 'dot', 'dot', 'line'],
	'u' : ['dot', 'dot', 'dot', 'line'],
	'W' : ['dot', 'line', 'line'],
	'w' : ['dot', 'line', 'line'],
	'X' : ['line', 'dot', 'dot', 'line'],
	'x' : ['line', 'dot', 'dot', 'line'],
	'Y' : ['line', 'dot', 'line', 'line'],
	'y' : ['line', 'dot', 'line', 'line'],
	'Z' : ['line', 'line', 'dot', 'dot'],
	'z' : ['line', 'line', 'dot', 'dot'],
	'1' : ['dot', 'line', 'line', 'line', 'line'],
	'2' : ['dot', 'dot', 'line', 'line', 'line'],
	'3' : ['dot', 'dot', 'dot', 'line', 'line'],
	'4' : ['dot', 'dot', 'dot', 'dot', 'line'],
	'5' : ['dot', 'dot', 'dot', 'dot', 'dot'],
	'6' : ['line', 'dot', 'dot', 'dot', 'dot'],
	'7' : ['line', 'line', 'dot', 'dot', 'dot'],
	'8' : ['line', 'line', 'line', 'dot', 'dot'],
	'9' : ['line', 'line', 'line', 'line', 'dot'],
	'0' : ['line', 'line', 'line', 'line', 'line'],
	'.' : ['dot', 'line', 'dot', 'line', 'dot', 'line'],
	',' : ['line', 'line', 'dot', 'dot', 'line', 'line'],
	'?' : ['dot', 'dot', 'line', 'line', 'dot', 'dot'],
	'!' : ['dot', 'dot', 'line', 'line', 'dot'],
	':' : ['line', 'line', 'line', 'dot', 'dot', 'dot'],
	'"' : ['dot', 'line', 'dot', 'dot', 'line', 'dot'],
	'=' : ['line', 'dot', 'dot', 'dot', 'line'],
	'(' : ['line', 'dot', 'line', 'line', 'dot'],
	')' : ['line', 'dot', 'line', 'line' , 'dot', 'line'],
	'' : []
}

# Translate a word
def translateWord(word):
	translatedWord = []
	for letter in word:
		translatedWord.append(morseCode.get(letter))
	return translatedWord

# Translating all given words
def translateWordByWord(text):
	sentance = []
	for word in text:
		translatedWord = translateWord(word)
		sentance.append(translatedWord)
	#print(sentance)
	return sentance

message = translateWordByWord(text)

morseSigns = {
	'dot' : '##########',
	'line' : '##############################',
	'insideCharSpace' : '----------',
	'insideWordSpace' : '------------------------------',
	'betweenWordsSpace' : '----------------------------------------------------------------------'
}

# print(message)

# setting spaces between words
firstFix = []
for elem in message:
	for elem2 in elem:
		firstFix.append(elem2)
	firstFix.append(morseSigns.get('betweenWordsSpace'))
#print(firstFix)

# setting spaces inside words - between characters
secondFix = []
for elem in firstFix:
	for elem2 in elem:
		if elem2[0] != '-':
			secondFix.append(elem2)
	secondFix.append(morseSigns.get('insideWordSpace'))
#print(secondFix)

# setting spaces between chars
thirdFix = []
for elem in secondFix:
	if elem[0] != '-':
		thirdFix.append(morseSigns.get(elem))
	else:
		thirdFix.append(elem)
#print(thirdFix)

thirdFix = morseSigns.get('insideCharSpace').join(thirdFix)
#print(thirdFix)


# opening a text file and writing encoded message into it
fileOpen = open("sporocilo.txt", 'w')
fileOpen.write(thirdFix)
fileOpen.close()






