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


def validate_string(str, lst) -> bool:
    """
    Returns True iff string is in lst.
    """
    for i in lst:
        if str == i:
            return true
        else:
            return false


def setup_game() -> Dict[str, int]:
    """
    Determines the piece of choice for the player 1 and player 2.
    """
    Dict = {}
    sym = input('what do you want to be x or o')
    if sym == 'o' or 'O':
        return Dict[sym: 0]
    else:
        return Dict[sym: 1]


def print_board():
    print(A)
    print(B)
    print(C)


def create_section(section: str):
    """
    Returns a sublist of the spcified section.
    Sublists should always start with an element
    in the A column and end with an element in the
    C column.
    >>> create_section("A")
    ['', '', '']
    """

    x = [A[0], B[0], C[0]]
    y = [A[1], B[1], C[1]]
    z = [A[2], B[2], C[2]]
    if x == section:
        return x
    elif y == section:
        return y
    else:
        return z


def concat_section(lst):
    """
    Returns the section as a concatenated string.
    """
    return " ".join(lst)


def check_win():
    """
    Returns true iff the specified symbol has a line of 3 in a row
    within the game board.
    """
    if A[0] and A[1] and A[2] == 1:
        return True
    elif B[0] and B[1] and B[2] == 1:
        return True
    elif C[0] and C[1] and C[2] == 1:
        return True
    elif x[0] and x[1] and x[2] == 1:
        return True
    elif y[0] and y[1] and y[2] == 1:
        return True
    elif A[0] and B[1] and C[2] == 1:
        return True
    elif C[0] and B[1] and A[2] == 1:
        return True
    if A[0] and A[1] and A[2] == 0:
        return True
    elif B[0] and B[1] and B[2] == 0:
        return True
    elif C[0] and C[1] and C[2] == 0:
        return True
    elif x[0] and x[1] and x[2] == 0:
        return True
    elif y[0] and y[1] and y[2] == 0:
        return True
    elif A[0] and B[1] and C[2] == 0:
        return True
    elif C[0] and B[1] and A[2] == 0:
        return True


def board_full():
    """
    Returns true iff the board is full
    """
    if A[0] and A[1] and A[2] and B[0] and B[1] and B[2] and C[0] and C[1] and \
            C[2] == 1 or 0:
        return True

#
# import pygame
# from A3_Solution import *
#
# """
# This is the visualizer file, once you have finished A3.py
# you can run this file to see your tic tac toe game in action!!
# DO NOT CHANGE ANYTHING IN THIS FILE, OTHERWISE THE GAME MAY NOT OPERATE PROPERLY
# """
#
# (width, height) = (300, 330)
# white = 255, 255, 255
# black = 0, 0, 0
# red = 255, 0, 0
# blue = 0, 0, 255
# click_positions = [[(0, 100), (0, 100)]]
# circle = pygame.image.load('circle.png')
# circle = pygame.transform.scale(circle, (100, 100))
# axe = pygame.image.load('axe.png')
# axe = pygame.transform.scale(axe, (100, 100))
# sprites = [circle, axe]
# made_move = False
# game_over = False
# pygame.font.init()
# myfont = pygame.font.SysFont("Times New Roman", 20)
# txt_player1 = myfont.render("Player 1", False, white)
# txt_player2 = myfont.render("Player 2", False, white)
# txt_player1_gone = myfont.render("Player 1", False, black)
# txt_player2_gone = myfont.render("Player 2", False, black)
# txt_p1_win = myfont.render("Player 1 Wins!!", False, white)
# txt_p2_win = myfont.render("Player 2 Wins!!", False, white)
# txt_draw = myfont.render("It's a draw...", False, white)
# player_option = setup_game()
# P1_sprite = player_option["P1"]
# P2_sprite = player_option["P2"]
# current_sprite = P1_sprite
# screen = pygame.display.set_mode((width, height))
# running = True
# all_clickable = []
#
# """
# Feel free to read what's written :)
# """
#
#
# def endgame(txt_condition):
#     """
#     function for displaying clearing the bottom
#     screen and displaying the endgame message
#
#     :param txt_condition:
#     :return: None
#     """
#     screen.blit(txt_player1_gone, (35, 303))
#     screen.blit(txt_player2_gone, (200, 303))
#     screen.blit(txt_condition, (100, 303))
#
#
# def zone_def():
#     """
#     function for storing which region of the game board
#     user clicked on
#     :return: None
#     """
#     A1 = [range(0, 100), range(0, 100)]
#     A2 = [range(100, 200), range(0, 100)]
#     A3 = [range(200, 300), range(0, 100)]
#     B1 = [range(0, 100), range(100, 200)]
#     B2 = [range(100, 200), range(100, 200)]
#     B3 = [range(200, 300), range(100, 200)]
#     C1 = [range(0, 100), range(200, 300)]
#     C2 = [range(100, 200), range(200, 300)]
#     C3 = [range(200, 300), range(200, 300)]
#     return [A1, A2, A3, B1, B2, B3, C1, C2, C3]
#
#
# def create_screen():
#     """
#     Function for rendering the screen
#     :return: None
#     """
#     pygame.display.set_caption("Tic Tac Toe")
#     screen.fill(black)
#     pygame.draw.circle(screen, white, (15, 315), 12, 2)
#     pygame.draw.circle(screen, red, (15, 315), 5, 5)
#     pygame.draw.circle(screen, blue, (285, 315), 5, 5)
#     pygame.draw.line(screen, white, (0, 0), (300, 0))
#     pygame.draw.line(screen, white, (0, 300), (300, 300))
#     pygame.draw.line(screen, white, (0, 100), (300, 100))
#     pygame.draw.line(screen, white, (0, 200), (300, 200))
#     pygame.draw.line(screen, white, (100, 0), (100, 300))
#     pygame.draw.line(screen, white, (200, 0), (200, 300))
#     screen.blit(txt_player1, (35, 303))
#     screen.blit(txt_player2, (200, 303))
#     all_clickable.extend(zone_def())
#
#
# create_screen()
#
# """
# while loop that runs as long as the user does click close
# """
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONUP:
#             if made_move and not game_over:
#                 made_move = False
#                 if current_sprite == P1_sprite:
#                     current_sprite = P2_sprite
#                     pygame.draw.circle(screen, black, (15, 315), 12, 2)
#                     pygame.draw.circle(screen, white, (285, 315), 12, 2)
#                 else:
#                     current_sprite = P1_sprite
#                     pygame.draw.circle(screen, white, (15, 315), 12, 2)
#                     pygame.draw.circle(screen, black, (285, 315), 12, 2)
#
#     if not game_over:
#
#         x, y = pygame.mouse.get_pos()
#         left_click, middle_click, right_click = pygame.mouse.get_pressed()
#
#         game_over = True
#         if check_win(str(P1_sprite)):
#             endgame(txt_p1_win)
#         elif check_win(str(P2_sprite)):
#             endgame(txt_p2_win)
#         elif board_full():
#             endgame(txt_draw)
#             pygame.draw.circle(screen, black, (15, 315), 12, 2)
#             pygame.draw.circle(screen, black, (285, 315), 12, 2)
#         else:
#             game_over = False
#
#         for i in range(len(all_clickable)):
#             if left_click and x in all_clickable[i][0] and y in \
#                     all_clickable[i][1] and possible_moves[
#                 i] != "" and not made_move:
#                 made_move = True
#                 possible_moves[i] = ""
#                 img_x, img_y = all_clickable[i][0][0], all_clickable[i][1][0]
#                 screen.blit(sprites[current_sprite], (img_x, img_y))
#                 if i >= 6:
#                     C[i % 3] = str(current_sprite)
#                 elif i >= 3:
#                     B[i % 3] = str(current_sprite)
#                 else:
#                     A[i % 3] = str(current_sprite)
#
#                 print_board()
#
#     pygame.display.flip()
