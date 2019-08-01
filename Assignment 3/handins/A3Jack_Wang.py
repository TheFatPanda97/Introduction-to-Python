from typing import List, Dict

A = ["", "", ""]
B = ["", "", ""]
C: List[str] = ["", "", ""]
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


def setup_game() -> Dict[str, int]:
    """
    Determines the piece of choice for the player 1 and player 2.
    """
    message = input('do you want to be x or o: ')
    dict = {}
    if message == 'x' or message == 'X':
        return {'P1': 1, 'P2': 0}
    elif message == 'o' or message == 'O':
        return {'P1'}
    else:
        return setup_game()


def print_board():
    """
    Prints out the contents of the game board.
    """
    return print('', A, '\n', B, '\n', C)


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
    elif section == '/':
        return [A[2], B[1], C[0]]


def concat_section(lst):
    """
    Returns the section as a concatenated string.
    """
    y = ''
    for i in lst:
        y += i
    return y


def check_win(sprite):
    """
    Returns true iff the specified symbol has a line of 3 in a row
    within the game board.
    >>> A = ["0", "1", "0"]
        B = ["1", "1", "1"]
        C = ["0", "1", '1']
        check_win('1')
        True

    """
    check_list = ['', '', '', '', '', '', '', '']
    check_list[0] = concat_section(A)
    check_list[1] = concat_section(B)
    check_list[2] = concat_section(C)
    check_list[3] = concat_section([A[0], B[0], C[0]])
    check_list[4] = concat_section([A[1], B[1], C[1]])
    check_list[5] = concat_section([A[2], B[2], C[2]])
    check_list[6] = concat_section([A[0], B[1], C[2]])
    check_list[7] = concat_section([A[2], B[1], C[0]])
    check_result = False
    for i in check_list:
        if sprite * 3 == i:
            check_result = True
    return check_result


def board_full():
    """
    Returns true iff the board is full
    >>> A = ["0", "1", "0"]
        B = ["1", "1", "1"]
        C = ["0", "1", '1']
        board_full()
        True
    """
    h = 0
    for i in game_board:
        for t in i:
            if t == '1' or t == '0':
                h += 1
    return h == 9
