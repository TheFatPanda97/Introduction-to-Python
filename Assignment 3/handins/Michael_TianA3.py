from typing import List, Dict

A = ["", "", ""]
B = ["", "", ""]
C = ["", "", ""]
possible_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
lines = ["A", "B", "C", "1", "2", "3", "/", "\\"]
game_board = [A, B, C]

"""
This is the logic portion of Tic Tac Toe game you are in charge of.
Note: store this and the visualizer.py in the same folder, otherwise
the game may not display

Words Definition:
iff: if and only if
meaning both direction of a logic statement has to be true
Eg:
you will pass iff you get 50    
Direction 1: you will pass if you get a 50 (True)
Direction 2: if you get a 50, you will pass(True)
"""


def validate_string(x, lst) -> bool:
    """
    Returns True iff string is in lst.
    """
    for i in lst:
        if x == i:
            return True
        else:
            return False


def setup_game() -> Dict[str, int]:
    """
    Determines the piece of choice for the player 1 and player 2.
    """
    x = input('would you like to be x or o')
    dict = {"P1": 'player 1', 'P2': 'player 2'}
    if dict == 'x' or 'X':
        return True
    elif dict == 'o' or 'O':
        return True
    else:
        return False


def print_board():
    """
    Prints out the contents of the game board.
    """
    x = [A[1] + B[1] + C[1]]
    y = [A[2] + B[2] + C[2]]
    v = [A[3] + B[3] + C[3]]
    print(print_board())


def create_section(section: str):
    """
    Returns a sublist of the specified section.
    Sublists should always start with an element
    in the A column and end with an element in the
    C column.
    #>>> create_section("A")
    ['', '', '']
    """


print(A)
print(B)
print(C)


def concat_section(lst):
    """
    Returns the section as a concatenated string.
    """
    a = 1
    b = 0
    if a in lst:
        return (a)
    if b in lst:
        return (b)


def check_win(z):
    """
    Returns true iff the specified symbol has a line of 3 in a row
    within the game board.
    """

    if 1 == A == B == C:
        return True
    elif 2 == A == B == C:
        return True
    elif 3 == A == B == C:
        return True
    elif A == 1 == 2 == 3:
        return True
    elif B == 1 == 2 == 3:
        return True
    elif C == 1 == 2 == 3:
        return True
    elif A[1] == B[2] == C[3]:
        return True
    elif A[3] == B[2] == C[1]:
        return True
    else:
        return False


def board_full():
    """
    Returns true iff the board is full
    """
    if board_full() == 9:
        return True
    elif 'X' or 'x' == 3:
        return True
    elif 'O' or 'o' == 3:
        return True
    else:
        return False
