import pygame


class Player:

    def __init__(self, x, y, width, height, src):
        self.img = pygame.image.load(src)
        self.img = pygame.transform.scale(self.img, (width, height))
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
