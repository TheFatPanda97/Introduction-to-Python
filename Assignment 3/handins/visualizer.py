import pygame
from Michael_TianA3 import *
"""
This is the visualizer file, once you have finished A3.py
you can run this file to see your tic tac toe game in action!!
DO NOT CHANGE ANYTHING IN THIS FILE, OTHERWISE THE GAME MAY NOT OPERATE PROPERLY
"""

(width, height) = (300, 330)
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
blue = 0, 0, 255
click_positions = [[(0, 100), (0, 100)]]
circle = pygame.image.load('circle.png')
circle = pygame.transform.scale(circle, (100, 100))
axe = pygame.image.load('axe.png')
axe = pygame.transform.scale(axe, (100, 100))
sprites = [circle, axe]
made_move = False
game_over = False
pygame.font.init()
myfont = pygame.font.SysFont("Times New Roman", 20)
txt_player1 = myfont.render("Player 1", False, white)
txt_player2 = myfont.render("Player 2", False, white)
txt_player1_gone = myfont.render("Player 1", False, black)
txt_player2_gone = myfont.render("Player 2", False, black)
txt_p1_win = myfont.render("Player 1 Wins!!", False, white)
txt_p2_win = myfont.render("Player 2 Wins!!", False, white)
txt_draw = myfont.render("It's a draw...", False, white)
player_option = setup_game()
P1_sprite = player_option["P1"]
P2_sprite = player_option["P2"]
current_sprite = P1_sprite
screen = pygame.display.set_mode((width, height))
running = True
all_clickable = []

"""
Feel free to read what's written :)
"""


def endgame(txt_condition):
    """
    function for displaying clearing the bottom
    screen and displaying the endgame message

    :param txt_condition:
    :return: None
    """
    screen.blit(txt_player1_gone, (35, 303))
    screen.blit(txt_player2_gone, (200, 303))
    screen.blit(txt_condition, (100, 303))


def zone_def():
    """
    function for storing which region of the game board
    user clicked on
    :return: None
    """
    A1 = [range(0, 100), range(0, 100)]
    A2 = [range(100, 200), range(0, 100)]
    A3 = [range(200, 300), range(0, 100)]
    B1 = [range(0, 100), range(100, 200)]
    B2 = [range(100, 200), range(100, 200)]
    B3 = [range(200, 300), range(100, 200)]
    C1 = [range(0, 100), range(200, 300)]
    C2 = [range(100, 200), range(200, 300)]
    C3 = [range(200, 300), range(200, 300)]
    return [A1, A2, A3, B1, B2, B3, C1, C2, C3]


def create_screen():
    """
    Function for rendering the screen
    :return: None
    """
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(black)
    pygame.draw.circle(screen, white, (15, 315), 12, 2)
    pygame.draw.circle(screen, red, (15, 315), 5, 5)
    pygame.draw.circle(screen, blue, (285, 315), 5, 5)
    pygame.draw.line(screen, white, (0, 0), (300, 0))
    pygame.draw.line(screen, white, (0, 300), (300, 300))
    pygame.draw.line(screen, white, (0, 100), (300, 100))
    pygame.draw.line(screen, white, (0, 200), (300, 200))
    pygame.draw.line(screen, white, (100, 0), (100, 300))
    pygame.draw.line(screen, white, (200, 0), (200, 300))
    screen.blit(txt_player1, (35, 303))
    screen.blit(txt_player2, (200, 303))
    all_clickable.extend(zone_def())


create_screen()


"""
while loop that runs as long as the user does click close 
"""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if made_move and not game_over:
                made_move = False
                if current_sprite == P1_sprite:
                    current_sprite = P2_sprite
                    pygame.draw.circle(screen, black, (15, 315), 12, 2)
                    pygame.draw.circle(screen, white, (285, 315), 12, 2)
                else:
                    current_sprite = P1_sprite
                    pygame.draw.circle(screen, white, (15, 315), 12, 2)
                    pygame.draw.circle(screen, black, (285, 315), 12, 2)

    if not game_over:

        x, y = pygame.mouse.get_pos()
        left_click, middle_click, right_click = pygame.mouse.get_pressed()

        game_over = True
        if check_win(str(P1_sprite)):
            endgame(txt_p1_win)
        elif check_win(str(P2_sprite)):
            endgame(txt_p2_win)
        elif board_full():
            endgame(txt_draw)
            pygame.draw.circle(screen, black, (15, 315), 12, 2)
            pygame.draw.circle(screen, black, (285, 315), 12, 2)
        else:
            game_over = False

        for i in range(len(all_clickable)):
            if left_click and x in all_clickable[i][0] and y in all_clickable[i][1] and possible_moves[i] != "" and not made_move:
                made_move = True
                possible_moves[i] = ""
                img_x, img_y = all_clickable[i][0][0], all_clickable[i][1][0]
                screen.blit(sprites[current_sprite], (img_x, img_y))
                if i >= 6:
                    C[i % 3] = str(current_sprite)
                elif i >= 3:
                    B[i % 3] = str(current_sprite)
                else:
                    A[i % 3] = str(current_sprite)

                print_board()

    pygame.display.flip()
