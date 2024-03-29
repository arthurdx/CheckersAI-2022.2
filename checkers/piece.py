
import pygame
from .constants import BLACK, CROWN, GREY, GREY2, WHITE, SQUARE_SIZE

#definindo a calsse peça
class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

#calculando a posição em que a peça sera desenhada a partir do centro de cada quadrado

    def calc_pos(self):

        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
#desenhando um circulo a partir do centro do quadrado
    def draw(self, window):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(window, GREY2, (self.x, self.y), radius + self.OUTLINE) #apenas um circulo para ser a borda e destacar as peças
        pygame.draw.circle(window, self.color, (self.x,self.y), radius)
        if self.king:
            window.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//1.7))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

#representação do objeto peça como uma string que contém sua cor
    def __repr__(self):
        return str(self.color)