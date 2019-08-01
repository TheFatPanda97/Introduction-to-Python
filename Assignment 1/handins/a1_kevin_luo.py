import random, time
from typing import List


def random_num(a: int, b: int) -> int:

    return random.randint(a, b)
numofguesses = 0

print("hello and welcome to the guessing game you will choose a range and i will choose a number in the range")

a, b = str(input("Give me a range of the random number I should choose (a,b): ")).split(",")
number = random_num(int(a), int(b))

guess = ""
while numofguesses > -1:
    print("take a guess")
    guess = input()
    guess = int(guess)
    numofguesses = numofguesses + 1
    if guess < number:
       print("too small try again")
    if guess > number:
       print("too big try again")
    print("number of guesses is")
    print(numofguesses)
    if guess == number:

        break
if guess == number:
    print("you win")