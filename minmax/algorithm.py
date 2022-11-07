from copy import deepcopy
import pygame

from checkers.constants import RED, BLUE

def minmax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.heuristic(), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            eval = minmax(move, depth - 1, True, game)[0]
            max_eval = max(max_eval, eval)
            if max_eval == eval:
                best_move = move

        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            eval = minmax(move, depth - 1, False, game)[0]
            min_eval = min(max_eval, eval)
            if min_eval == eval:
                best_move = move

        return min_eval, best_move
        
        

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in  valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

def draw_moves(game, board, piece):
    board.get_corner_piece(RED)
    board.get_corner_piece(BLUE)
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.window)
    pygame.draw.circle(game.window, (0,255,255), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    font = pygame.font.SysFont('arial', 50)
    text = font.render(str(board.blue_left - board.red_left + (board.blue_kings * 0.5 - board.red_kings * 0.5) + (
        board.blue_corner * 0.3 - board.red_corner * 0.3)), True, (180, 60, 0))
    game.window.blit(text, (piece.x, piece.y))
    pygame.display.update()
    pygame.time.delay(400)
