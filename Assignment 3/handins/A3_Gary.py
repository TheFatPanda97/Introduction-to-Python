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
    return x in lst


def setup_game():
    """
    Determines the piece of choice for the player 1 and player 2.
    """
    ask = input("Do you want to be X or O?")
    if ask == 'x' or ask == 'X':
        return {'P1': 1, 'P2': 0}
    elif ask == 'o' or ask == 'O':
        return {'P1': 0, 'P2': 1}
    else:
        return setup_game()


def print_board():
    """
    Prints out the contents of the game board.
    """
    [print(i) for i in game_board]


def create_section(section: str):
    """
    Returns a sublist of the specified section.
    Sublists should always start with an element
    in the A column and end with an element in the
    C column.
    >>> create_section("A")
    ['', '', '']
    """
    if section == 'A':
        return A
    elif section == 'B':
        return B
    elif section == 'C':
        return C
    elif section == '1' or section == '2' or section == '3':
        return [A[int(section) - 1], B[int(section) - 1], C[int(section) - 1]]
    elif section == '\\':
        return [A[0], B[1], C[2]]
    elif section == "/":
        return [A[2], B[1], C[0]]


def concat_section(lst):
    """
    Returns the section as a concatenated string.
    """
    return (lst.join(" ").replace(" ", ""))


def check_win(symbol):
    """
    Returns true iff the specified symbol has a line of 3 in a row
    within the game board.
    >>> check_win()
    """
    for i in lines:
        if create_section(i).count(symbol) == 3:
            return True


def board_full():
    """
    Returns true iff the board is full
    """
    a = 0
    for i in game_board:
        for j in i:
            if j == '1' or j == '0':
                a += 1
    return a == 9
