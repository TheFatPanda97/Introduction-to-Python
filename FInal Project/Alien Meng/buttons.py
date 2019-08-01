import pygame

pygame.init()


class Button:
    def __init__(self, font_size, font, color, center_x, center_y, w, h, ic, ac, game_board: pygame.display):
        self.font_size = font_size
        self.font = font
        self.color = color
        self.center_x = center_x
        self.center_y = center_y
        self.x = center_x - w / 2
        self.y = center_y - h / 2
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.game_board = game_board

    def draw_ic(self):
        pygame.draw.rect(self.game_board, self.ic, (self.x, self.y, 100, 50))

    def draw_ac(self):
        pygame.draw.rect(self.game_board, self.ac, (self.x, self.y, 100, 50))
