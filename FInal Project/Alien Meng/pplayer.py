import pygame
pygame.init()


class Ship:
    def __init__(self, x, y, w, h, vel, src):
        self.img = pygame.image.load(src)
        self.player_x = x
        self.player_y = y
        self.boat_width = w
        self.boat_height = h
        self.boat_vel = vel
        self.src = src
