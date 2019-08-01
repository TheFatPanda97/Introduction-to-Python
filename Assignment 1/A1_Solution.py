import random, time
from typing import List


# TODO HELPER 1
def random_num(a: int, b: int) -> int:
    """
    given a range a and b, returns a random number between (and including)
    those 2 numbers

    >>> x = random_num(1,10)
    >>> 1 <= x <= 10
    True
    >>> x > 10
    False
    >>> x < 1
    False
    """
    # COMPLETE BODY FUNCTION
    return random.randint(a, b)


# TODO HELPER 2
def verify(guess: int, actual: int, num_guess: int) -> List:
    """
    given the number <guess>, output:
    "Too small try again!" if guess < actual
    "Too large try again!" if guess > actual
    "Good job you got it!" if guess == actual
    In addition, increase <num_guess> by 1

    >>> verify(3,5,0)
    ["Too small try again!",1]
    >>> verify(6,5,1)
    ["Too large try again!",2]
    >>> verify(5,5,10)
    ["Good job you got it!",11]
    """
    # COMPLETE BODY FUNCTION
    if guess < actual:
        return ["Too small try again!", num_guess + 1]
    elif guess > actual:
        return ["Too big try again!", num_guess + 1]
    else:
        return ["Good job you got it!", num_guess + 1]


# =========================================================================================================
# DO NOT MODIFY!!! But feel free to look at what's happening


l1 = "hello and welcome to the guessing game!\n"
l2 = "The rules are: I will pick a random number and you try to guess it\n"
l3 = "AND if you guess incorrectly I will also tell if your guess is too big or too small\n"
l4 = "NOW LET THE GUESSING BEGIN!!\n"
introduction = [l1, l2, l3, l4]

for line in introduction:
    for letter in line:
        print(letter, flush=True, end=""), time.sleep(.05)
    time.sleep(.8)

a, b = str(input(
    "Give me a range of the random number I should choose (a,b): ")).split(
    ",")

num = random_num(int(a), int(b))
num_guess = 0
guess = int(input(
    "Guess what the number is (number of guesses right now, {}): ".format(
        num_guess)))

while guess != num:
    message, num_guess = verify(guess, num, num_guess)
    guess = int(input(
        "{} (number of guess right now, {}): ".format(message, num_guess)))

message, num_guess = verify(guess, num, num_guess)
print(message, "It took you {} guesses".format(num_guess))
