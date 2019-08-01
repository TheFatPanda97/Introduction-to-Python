import pygame


class Bullet:

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 20
        self.height = 35
        self.img = pygame.image.load("bullet.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
