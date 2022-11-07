import pygame
from checkers.constants import BLUE, RED, SQUARE_SIZE, WIDTH, HEIGHT 
from checkers.board import Board
from checkers.game import Game
from minmax.algorithm import minmax
from alphabeta.algorithm import alpha_beta

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
    pygame.init()
    #loop que mantem a janela do jogo aberta
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)

        #IA jogando com o minmax prevendo 3 jogadas
        if game.turn == BLUE:
            value, new_board = minmax(game.get_board(), 3, BLUE, game)
            game.ai_move(new_board)

        #IA jogando com poda alpha beta prevendo 3 jogadas
        # if game.turn == BLUE:
        #     value, new_board = alpha_beta(game.get_board(), 3, float('-inf'), float('inf'), BLUE, game)
        #     game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        #evento que fecha o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # eventos de click de mouse para selecionar peça
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position_from_mouse(pos)
                game.select(row, col)
           
            #desenhando o tabuleiro usando os metodos da classe board
        game.update()

         
    pygame.quit()

main()
