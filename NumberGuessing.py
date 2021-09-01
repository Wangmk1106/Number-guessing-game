import math
import random

print('Number Guessing Game')

number = random.randint(1,9)
chances = 0

print('Guess a number between 1-9 ')

while chances<5:
    guess = int(input('Enter your guess '))
    if guess == number: 
        print('Congratulations you won')
        break
    elif guess<number:
        print('Guess higher than', guess)
    else:
        print('Guess lower than', guess)
    chances = chances+1

if not chances<5:
    print('You lose. The number is', number)
