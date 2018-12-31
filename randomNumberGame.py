#this is a guess the numer game

import random

print('Hello, what is your name?')
name = input()

print('Well ' + name + ', I am thinking of a number between 1 and 20. Can you guess what it is?')
secretNumber = random.randint(1, 20)

print('DEBUG: Secret number is ' + str(secretNumber))  ##Use to check that the random number generated is being used (can be removed).

for guessesTaken in range(1, 7):
    print('Take a guess..')
    guess= int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print ('Your guess is too high.')
    else:
        break  #This condition is for the correct guess.

if guess == secretNumber:
    print('Good job!! You got my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope the number I was thinking of was ' + str(secretNumber) +'.')

