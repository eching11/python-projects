# Guess a number between 1 and 20

import random

print('Welcome to the Guessing Game!')
name = input('Enter player name: ')
print('Hello ' + name + ', can you guess what number I\'m thinking of between 1 and 20?')

number = random.randint(1, 20)

for guessTotal in range (1, 6):
    print('Take a guess!')
    guess = int(input())

    if guess < number:
        print('Ah, that\'s too low...')
    elif guess > number:
        print('Hmm, that\'s too high...')
    else:
        print('That\'s it! You guessed my number!')
        break

if guess != number:
    print('Oof you took too many wrong guesses.')
    print('The number I was thinking of was ' + str(number))
else:
    print('You took ' + str(guessTotal) + ' guesses.')
