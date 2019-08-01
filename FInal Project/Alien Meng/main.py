# Adventures of Shawn
# By: Ailen

import pygame
import time
from pplayer import Ship
from object import Object
from buttons import Button

speed_inc = {1: 1.5, 2: 1.75, 5: 2.5, 7: 3, 8: 3.25, 9: 3.5, 10: 3.75, 12: 5}

pygame.init()
board_width = 800
board_height = 650

GRAY = (69, 69, 69)
RED = (200, 0, 0)
LIGHT_RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (77, 192, 227)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREEN = (52, 168, 10)

game_board = pygame.display.set_mode((board_width, board_height))
o1 = Object(game_board)
o2 = Object(game_board)
o3 = Object(game_board)
o4 = Object(game_board)
o5 = Object(game_board)
o6 = Object(game_board)
o7 = Object(game_board)
o8 = Object(game_board)
o9 = Object(game_board)
o10 = Object(game_board)

ob = (o1, o2, o3, o4, o5, o6, o7, o8, o9, o10)

pygame.display.set_caption('Adventures of Shawn')

timer = pygame.time.Clock()

p1 = Ship(800 / 2 - board_height / 2, board_height * 0.83, 45, 80, 5,
          'player.png')


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 75)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((board_width / 2), (board_height / 2))
    game_board.blit(text_surf, text_rect)

    pygame.display.update()


def crash():
    game_board.fill(WHITE)
    message_display('You Crashed')
    for o in ob:
        o.rand_feat()
        o.vel = 1
        o.dodged = 0

    time.sleep(2)
    start_menu()


b1 = Button(20, 'freesansbold.ttf', BLACK, board_width / 2, 475, 100, 50, GREEN,
            LIGHT_GREEN,
            game_board)


def main_loop():
    p1.player_x = board_width / 2 - p1.boat_width / 2
    p1.player_y = board_height * 0.84
    x_change = 0

    crashed = False

    while not crashed:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -p1.boat_vel
                elif event.key == pygame.K_RIGHT:
                    x_change = p1.boat_vel

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        p1.player_x += x_change
        game_board.fill(LIGHT_BLUE)
        game_board.blit(p1.img, (p1.player_x, p1.player_y))

        for o in ob:
            o.y += o.vel
            o.generate_object()

            if o.y > board_height + o.h:
                o.dodged += 1
                o.rand_feat()
                o.vel = speed_inc.get(o.dodged, o.vel)

            if o.y < board_height:
                if p1.player_y < o.y + o.h:
                    if o.x < p1.player_x < o.x + o.w or o.x < p1.player_x + p1.boat_width < o.x + o.w:
                        crash()

        if p1.player_x > board_width - p1.boat_width:
            p1.player_x = board_width - p1.boat_width
        if p1.player_x < 0:
            p1.player_x = 0

        pygame.display.flip()

        timer.tick(120)


def start_menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_board.fill(LIGHT_BLUE)
        large_text = pygame.font.Font('freesansbold.ttf', 70)
        text_surf, text_rect = text_objects("Adventures of Shawn", large_text)
        text_rect.center = ((board_width / 2), (board_height / 2))
        game_board.blit(text_surf, text_rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if board_width / 2 - b1.w / 2 + b1.w > mouse[
            0] > board_width / 2 - b1.h and 450 + b1.h > mouse[1] > 450:
            b1.draw_ac()
            if click[0] == 1:
                main_loop()
        else:
            b1.draw_ic()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surf, text_rect = text_objects('start', small_text)
        text_rect.center = b1.center_x, b1.center_y
        game_board.blit(text_surf, text_rect)

        pygame.display.update()
        pygame.display.flip()
        timer.tick(15)


start_menu()
pygame.quit()
quit()
