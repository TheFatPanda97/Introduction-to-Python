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


def validate_string() -> bool:
    """
    Returns True iff string is in lst.
    """


def setup_game() -> Dict[str, int]:
    """
    Determines the piece of choice for the player 1 and player 2.
    """


def print_board():
    """
    Prints out the contents of the game board.
    """


def create_section(section: str):
    """
    Returns a sublist of the specified section.
    Sublists should always start with an element
    in the A column and end with an element in the
    C column.
    >>> create_section("A")
    ['', '', '']
    """


def concat_section(lst):
    """
    Returns the section as a concatenated string.
    """


def check_win():
    """
    Returns true iff the specified symbol has a line of 3 in a row
    within the game board.
    """


def board_full():
    """
    Returns true iff the board is full
    """
