import pygame
from .piece import Piece
from .constants import BLACK, COLS, RED, ROWS, SQUARE_SIZE, WHITE, BLUE

#definindo a classe tabuleiro

class Board():
    def __init__(self):
        self.board = [[]]
        self.selected_piece = None
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.create_board()
#criando o quadriculado do tabuleiro 
    def draw_squares(self, window):
        window.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE
                , SQUARE_SIZE, SQUARE_SIZE))

#iniciando o tabuleiro, fazendo a matematica de quais colunas/linhas devem receber peças e adicionando uma peça a elas
#o quadrado que não deve receber peça recebe 0 para mantermos monitoradas quais são os quadrados vazios

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row,col, RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLUE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

#desenhando o tabuleiro inicial como um todo, inicialmente desenhando o quadriculado
#usando o metodo draw_squares e em seguida iterando sob colunas e linhas para desenhar as peças
#se o quadrado tiver uma peça (peça != 0) ela é desenhada

    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)