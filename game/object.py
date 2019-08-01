from random import randint
import pygame


class Object:
    def __init__(self, screen: pygame.display):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.pos_x = 0
        self.pos_y = 0
        self.width = 0
        self.height = 0
        self.screen = screen
        self.color = (r, g, b)

    def generate_loc(self):
        self.width = randint(50, 200)
        self.height = randint(50, 200)
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.pos_x = randint(0, screen_width - self.width)
        self.pos_y = -self.height

    def generate_object(self):
        pygame.draw.rect(self.screen, self.color,
                         (self.pos_x, self.pos_y, self.width, self.height))
