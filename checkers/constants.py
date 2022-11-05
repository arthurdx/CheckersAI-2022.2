import pygame

#definindo constantes que serão usadas varias vezes no codigo

WIDTH, HEIGHT = 800, 800 #tamanho da tela em largura e altura de 800 pixeis
ROWS, COLS = 8,8 #8 colunas e 8 linhas, padrão de um tabuleiro de dama
SQUARE_SIZE = WIDTH//COLS # tamanho 1/1 quadrado

# cores em RGB
RED = (161,14,14)
BLUE = (4,4,161)
BLACK = (0,0,0)
GREY = (128,128,128)
GREY2 = (64,64,64)
WHITE = (202,202,202)
GREEN = (0,255,0)

CROWN = pygame.transform.scale(pygame.image.load('assets/coroa.png'), (46,46))