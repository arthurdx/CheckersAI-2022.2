import sys
import pygame
from checkers.constants import BLUE, RED, SQUARE_SIZE, WHITE, WIDTH, HEIGHT 
from checkers.board import Board
from checkers.game import Game
from minmax.algorithm import minmax
from alphabeta.algorithm import alpha_beta
from button.button import Button


pygame.init()
FPS = 60
#desenhando a janela onde o jogo ira rodar
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_position_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def menu():
    run = True

    while run:
        game = Game(WINDOW)
        pygame.init()

        
        mx, my = pygame.mouse.get_pos()

        font = pygame.font.SysFont('arial', 50)
        menu_text = font.render('Selecione Dificuldade', True, "white")
        menu_rect = menu_text.get_rect(center=(20,20))


        easy_button = Button(None, 200, 100, 'Facil', font)
        medium_button = Button(None,  200, 200, 'Médio', font)
        hard_button = Button(None, 200, 300, 'Difícil', font)

        game.window.blit(menu_text, menu_rect)

        for button in [easy_button, medium_button, hard_button]:
            button.changeColor((mx,my))
            button.update(game.window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.checkForInput((mx,my)):
                    main(1)
                if medium_button.checkForInput((mx,my)):
                    main(3)
                if hard_button.checkForInput((mx,my)): 
                    main(5)
        

    pygame.quit()


def main(dificulty, IA=True):
    #loop que mantem a janela do jogo aberta
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)

        game.window.fill((0,0,0))

        if IA:
            if game.turn == BLUE:
                value, new_board = minmax(game.get_board(), dificulty, BLUE, game)
                game.ai_move(new_board)

        #IA jogando com poda alpha beta prevendo 3 jogadas
        # if game.turn == BLUE:
        #     value, new_board = alpha_beta(game.get_board(), 3, '-inf', 'inf', BLUE, game)
        #     game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        #evento que fecha o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            # eventos de click de mouse para selecionar peça
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position_from_mouse(pos)
                game.select(row, col)
           
            #desenhando o tabuleiro usando os metodos da classe board
        game.update()

         
    pygame.quit()

main(1)
