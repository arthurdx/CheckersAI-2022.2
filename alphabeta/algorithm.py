from copy import deepcopy
import pygame

from checkers.constants import RED, BLUE
from minmax.algorithm import get_all_moves

def alpha_beta(position, depth, alpha, beta, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.heuristic(), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            eval = alpha_beta(move, depth - 1, alpha, beta, True, game)[0]
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            eval = alpha_beta(move, depth - 1, alpha, beta, False, game)[0]
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        best_move = move
        return min_eval, best_move