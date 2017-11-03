'''

First, import random

Second, make a while loop that continues infinitely as long as the user says the computer has not guessed correctly

Within the while loop have the computer generate a random integer and ask the user if it is correct, higher, or lower

If the user says higher or lower, repeat the process. If the user says correct, end the loop with a success statement.

'''

import random

correct = False
rpl = 1
rph = 1000
guess = 0
usercorrect = ' '
cont = 'n'

while (cont != 'y'):
	cont = input('do you have a number? (y/n) ')

while (correct == False):
	if (usercorrect == 'h'):
		rph = guess - 1
	elif (usercorrect == 'l'):
		rpl = guess + 1
	guess = random.randint(rpl, rph)
	print (guess)
	usercorrect = input('Is this number correct, higher, or lower? (c/h/l) ')
	if (usercorrect == 'c'):
		correct = True
	else:
		print ('Then I will guess again.')
print ('Yes! I win!')
