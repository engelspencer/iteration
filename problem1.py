'''
First, I want to make a loop that iterates 100 times, in which I print out each iteration

Second, I want to replace all iterations of multiples of 3 with 'Burrito'

After, I want to do the same with the following values and print statements:

- 5, 'Cheeto'
- 7, 'Veto'
- 3 & 7, 'BurritoVeto'
- 5 & 7, 'CheetoVeto'
- 3 & 5 & 7, 'BurritoCheetoVeto'
'''

for x in range(1,1001):
	if (x % 3 == 0 and x % 5 == 0 and x % 7 == 0):
		print ('BurritoCheetoVeto')
	elif (x % 5 == 0 and x % 7 == 0):
		print ('CheetoVeto')
	elif (x % 3 == 0 and x % 7 == 0):
		print ('BurritoVeto')
	elif (x % 7 == 0):
		print ('Veto')
	elif (x % 5 == 0):
		print ('Cheeto')
	elif (x % 3 == 0):
		print ('Burrito')
	else:
		print (x)
