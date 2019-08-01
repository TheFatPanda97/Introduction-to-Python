import pygame
from random import randint

pygame.init()


class Object:
    def __init__(self, game_board: pygame.display):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.color = (0, 0, 0)
        self.vel = 1
        self.game_board = game_board
        self.dodged = 0

    def rand_feat(self):
        self.x = randint(0, 800 - self.w)
        self.y = randint(-700, 0 - self.h)
        self.w = randint(50, 150)
        self.h = randint(50, 150)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 100))

    def generate_object(self):
        pygame.draw.rect(self.game_board, self.color,
                         (self.x, self.y, self.w, self.h))
