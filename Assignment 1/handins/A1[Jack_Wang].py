import random, time
from typing import List

# TODO HELPER 1
def random_num(a: int, b: int) -> int:
    """
    given a range a and b, returns a random number between (and including)
    those 2 numbers

    >>> x = random_num(1, 10)
    >>> 1 <= x <= 10
    True
    >>> x > 10
    False
    >>> x < 1
    False
    """
    # COMPLETE BODY FUNCTION
    random_num = random.randint(lowerlim, upperlim)
    guess = int(input('guess: '))
#TODO HELPER 2
def varify(guess: int, actual: int, num_guess:int) -> List:
    """
    given the number <guess>, output:
    "Too small try again!" if guess < actual
    "Too large try again!" if guess > actual
    "Good job you got it!" if guess == actual
    In addition, increase <num_guess> by 1

    >>> varify(3,5,0)
    ["Too small try again!",1]
    >>> varify(6,5,1)
    ["Too large try again!",2]
    >>> varify(5,5,10)
    ["Good job you got it!",11]
    """
    # COMPLETE BODY FUNCTION
    num_guess += 1
    if guess > actual:
        return['too large try again.', num_guess]
    elif guess < actual:
        return['Too small try again.', num_guess]
    else:
        return['good job you got it', num_guess]


