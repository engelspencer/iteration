'''

First, generate the random integer and import random

Develop a while loop to iterate as long as they have not guessed the correct answer, in which you have them guess the number each time

Use if statements within the loop to determine if the guess was:

-equal to, break out of the loop, tell them good job
-less than, tell them they guessed low
-greater than, tell them they guessed high

'''

import random

num = random.randint(1,1000)

userinput = 0
guess = False

while (guess == False):
	userinput = int(input('Guess my number. '))
	if (userinput == num):
		guess = True
		print ('You guessed right!')
	elif (userinput < num):
		print ('Your guess was too low.')
	elif (userinput > num):
		print ('Your guess was too high.')
