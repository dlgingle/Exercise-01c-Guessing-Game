#!/usr/bin/env python3
import sys, random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"



number = number = random.randrange(1,11)
count = 0
guess = -1
while guess is number:
    count = count + 1
    guess = input("Guess a number from 1 to 10: ")
    try:
        guess = int(guess)
        if guess != number
            print("not quite please try again")
    Except:
        print("please enter a number")
print("Great job! You got it! you were able to guess the number in " + str(count) "tries")