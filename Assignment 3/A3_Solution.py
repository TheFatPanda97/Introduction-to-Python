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


def validate_string(string, lst) -> bool:
    """
    Returns True iff string is in lst.
    >>> validate_string("Hello", ["Hello", "There"])
    True
    >>> validate_string("A1", ["B1", "C3"])
    False
    """
    return string in lst


def setup_game() -> Dict[str, int]:
    """
    Determines the piece of choice for the player 1 and player 2.
    If the player enters something other than x or o, then ask the user
    again to enter the correct value
    Note: the key of the dictionary HAS TO BE "P1" and "P2"
    if P1 choose 'X', the value for P1 in the dictionary would be 1
    and the value for P2 would be 0. Vice-versa.
    """
    while True:
        print("Enter whether you would like to be X or O")
        player_input = input().upper()
        if validate_string(player_input.upper(), ["X", "O"]):
            break
    if player_input == "X":
        P1 = 1
        P2 = 0
    else:
        P1 = 0
        P2 = 1
    return {"P1": P1, "P2": P2}


def print_board():
    """
    Prints out the contents of the game board.
    """
    print(A)
    print(B)
    print(C)


def create_section(section: str):
    """
    Returns a sublist of the specified section.
    Sublists should always start with an element
    in the A column and end with an element in the
    C column.
    >>> create_section("A")
    ['', '', '']
    """
    if section == "A":
        return A
    elif section == "B":
        return B
    elif section == "C":
        return C
    elif section == "1":
        return [A[0], B[0], C[0]]
    elif section == "2":
        return [A[1], B[1], C[1]]
    elif section == "3":
        return [A[2], B[2], C[2]]
    elif section == '/':
        return [A[2], B[1], C[0]]
    elif section == "\\":
        return [A[0], B[1], C[2]]
    return None


def concat_section(lst):
    """
    Returns the section as a concatenated string.
    """
    return "".join(lst)


def check_win(symbol):
    """
    Returns true iff the specified symbol has a line of 3 in a row
    within the game board.

    >>>A = ["X", "X", "X"]
    >>>B = ["", "", ""]
    >>>C = ["", "", ""]
    >>>check_win("X")
    True
    >>>check_win("O")
    False

    """
    for line in lines:
        if concat_section(create_section(line)) == (symbol * 3):
            return True
    return False


def board_full():
    """
    Returns true iff the board is full
    """
    for col in game_board:
        for item in col:
            if item == "":
                return False
    return True
