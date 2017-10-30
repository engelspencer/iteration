'''

First, import random

Second, make a while loop that continues infinitely as long as the user says the computer has not guessed correctly

Within the while loop have the computer generate a random integer and ask the user if it is correct, higher, or lower

If the user says higher or lower, repeat the process. If the user says correct, end the loop with a success statement.

'''

import random

correct = False
guess = 0
usercorrect = ''
cont = 'n'

while (cont != 'y'):
	cont = input('do you have a number? (y/n) ')

while (correct == False):
	print (random.randint(1,1000))
	usercorrect = input('Is this number correct, higher, or lower? (c/h/l) ')
	if (usercorrect == 'c'):
		correct = True
	elif (usercorrect == 'h' or usercorrect == 'l'):
		print ('Then I will guess again.')

print ('Yes! I win!')
