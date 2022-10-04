import pygame
from checkers.constants import RED, SQUARE_SIZE, WIDTH, HEIGHT 
from checkers.board import Board
from checkers.game import Game

FPS = 60
#desenhando a janela onde o jogo ira rodar
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_position_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    #loop que mantem a janela do jogo aberta
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)
        #evento que fecha o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # eventos de click de mouse ainda a ser definidos
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position_from_mouse(pos)
                if game.turn == RED:
                    game.select(row, col)
           
            #desenhando o tabuleiro usando os metodos da classe board
        game.update()

         

    pygame.quit()

main()
