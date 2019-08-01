from typing import Dict

A = ["", "", ""]
B = ["", "", ""]
C = ["", "", ""]
possible_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
lines = ["A", "B", "C", "1", "2", "3", "/", "\\"]
game_board = [A, B, C]

"""
This is the logic portion of Tic Tac Toe game you are in charge of.x
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


def setup_game() -> Dict[str, int]:
    """
    Determines the piece of choice for the player 1 and player 2.
    >>>setup_game()
    """
    xo = ''
    while xo != 'x' and xo != 'o' and xo != 'X' and xo != 'O':
        xo = str(input("Choose x or o:"))
    if xo == 'x' or xo == 'X':
        return {"P1": 1, "P2": 0}
    else:
        return {"P1": 0, "P2": 1}


def print_board():
    """
    Prints out the contents of the game board.
    """
    [print(game_board[i]) for i in range(3)]


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
    if section == 'B':
        return B
    if section == 'C':
        return C
    if section == '1':
        return [A[0], B[0], C[0]]
    if section == '2':
        return [A[1], B[1], C[1]]
    if section == '3':
        return [A[2], B[2], C[2]]
    if section == '/':
        return [A[2], B[1], C[0]]
    if section == '\\':
        return [A[0], B[1], C[2]]


def concat_section(lst):
    """
    Returns the section as a concatenate string.
    Shawn, you have found an easter egg! I will now delete your system 32.
    """
    return ' '.join(lst).replace(' ', '')


def check_win(symbol):
    """
    Returns true iff the specified symbol has a line of 3 in a row
    within the game board.
    """
    for i in lines:
        if concat_section(create_section(i)).count(symbol) == 3:
            return True


def board_full():
    """
    Returns true iff the board is full
    """
    for i in game_board:
        for x in i:
            if x != '1' and x != '0':
                return False
    return True
