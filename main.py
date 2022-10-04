import pygame
from checkers.constants import WIDTH, HEIGHT 
from checkers.board import Board
FPS = 60
#desenhando a janela onde o jogo ira rodar
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def main():
    #loop que mantem a janela do jogo aberta
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        #evento que fecha o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # eventos de click de mouse ainda a ser definidos
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            #desenhando o tabuleiro usando os metodos da classe board
            board.draw(WINDOW)
            pygame.display.update()

         

    pygame.quit()

main()
