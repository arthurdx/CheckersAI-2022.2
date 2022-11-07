import pygame
from checkers.piece import Piece
from checkers.constants import BLACK, COLS, RED, ROWS, SQUARE_SIZE, WHITE, BLUE

#definindo a classe tabuleiro

class Board():
    def __init__(self):
        self.board = [[]]
        self.red_left = self.blue_left = 12
        self.red_kings = self.blue_kings = 0
        self.get_corner_piece(BLUE)
        self.get_corner_piece(RED)
        self.create_board()
        self.winner()
#criando o quadriculado do tabuleiro 
    def draw_squares(self, window):
        window.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE
                , SQUARE_SIZE, SQUARE_SIZE))

    def heuristic(self):
         self.get_corner_piece(RED)
         self.get_corner_piece(BLUE)
         return (self.blue_left - self.red_left) + (self.blue_kings * 0.5 - self.red_kings * 0.5) + (
            self.blue_corner * 0.3 - self.red_corner * 0.3)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def get_corner_piece(self, color):
        cornered = 0
        for piece in self.get_all_pieces(color):
            if piece.col == 0 or piece.col == COLS -1:
                cornered += 1
        if color == RED:
            self.red_corner = cornered
        else:
            self.blue_corner = cornered



    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == BLUE:
                self.blue_kings += 1
            else:
                self.red_kings += 1
    
    def get_piece(self, row, col):
        return self.board[row][col]

#iniciando o tabuleiro, fazendo a matematica de quais colunas/linhas devem receber peças e adicionando uma peça a elas
#o quadrado que não deve receber peça recebe 0 para mantermos monitoradas quais são os quadrados vazios

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row,col, BLUE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
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

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.blue_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return "Azul venceu"
        elif self.blue_left <= 0:
            return "Vermelho venceu"
        else:
            return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == BLUE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, -1)
                    else:
                        row = min(r+3, ROWS)
                    if skipped:
                        moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last+skipped))
                        moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last+skipped))
                    else:
                        moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                        moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, -1)
                    else:
                        row = min(r+3, ROWS)
                    if skipped:
                        moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last+skipped))
                        moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last+skipped))
                    else:
                        moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                        moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves