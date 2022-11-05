from copy import deepcopy
from ..checkers.board import Board, get_all_pieces
import pygame

from ..checkers.constants import RED, BLUE

def minmax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        bestMove = None
        for move in get_all_moves(position, BLUE, game):

    else:
        

def get_all_moves(color, game):
    moves = []

    for piece in get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in  valid_moves.items():
