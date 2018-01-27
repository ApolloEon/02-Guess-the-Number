#!/usr/bin/python3

import sys, random

assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

while True:

	#generate a random integer between 1 and 20 (inclusive) and store it in the variable [number]
	number = random.randint(1,20)
	for g in range(10):


		#ask the user for a response and store it in the variable [guess]
		guess = input("Ayyo. Let's start guessing numbers between 1-20 mate (You have {guesses} guesses left): ".format(guesses = 10 - g))


		#a try/except block is a great tool for programmers to be able to deal with errors. In this instance, it reports an error if the user enters something other than an integer
		try:
			#convert the guess to an integer
			guess = int(guess)

			#check if the guess is less than the random number
			if guess < number:
				print('Too low!')
			if guess > number:
				print('A little high pal')
			if guess == number:
				print('What? You got it!')
				break

		except ValueError:
			print('Please enter a whole number.')
	if g >= 10:
		print('So close yet so far away. Maybe next time.')
		starting_over = input('Feel like giving it another go? Yes or No?')
	else:
		print('Well done. Never doubted you for a second. You ended with {guesses} left.'.format(guesses = 10 - g))
		starting_over = input("So, feel like testing you luck again? Yes or No? ")
	if starting_over.upper() == "NO":
		break
print("Ah. That's too bad. See you next time then.")