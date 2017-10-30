'''

First, create a for loop that will iterate a number of times equal to the length of the user's phrase

Next, create an if structure to determine if userphrase[x] is a space or not

Concatenate the next character of userphrase to tempword if the character is not a space

Append tempword to wordsInPhrase and set tempword equal to an empty string if the character is a space

when finished, print wordsInPhrase

'''

userphrase = input('Please enter a sentence or phrase: ') + ' '
uplen = len(userphrase)
wordsInPhrase = []
tempword = ''

for x in range (uplen):
	if (userphrase[x] != ' '):
		tempword = tempword + userphrase[x]
	elif (userphrase[x] == ' ' and userphrase[x-1] == ' '):
		continue
	else:
		wordsInPhrase.append(tempword)
		tempword = ''

print (wordsInPhrase)
