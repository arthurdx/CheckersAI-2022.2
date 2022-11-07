from copy import deepcopy
import pygame

from checkers.constants import RED, BLUE
from minmax.algorithm import get_all_moves

def alpha_beta(position, depth, alpha, beta, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.heuristic(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            eval = alpha_beta(move, depth -1, alpha, beta, True, game)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            eval = alpha_beta(move, depth - 1, alpha, beta, False, game)
            minEval = min(minEval, eval)
            if beta <= alpha:
                break
        return minEval, best_move