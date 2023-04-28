import random
from const import *

CHECKMATE = 10000
STALEMATE = 0


def find_ai_move(board, algorithm, depth=2):
    '''
    Find ai moves associated with the chosen engine
    '''
    if algorithm == 'minimax':
        print(depth)
        _, move = minimax(board, depth, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=False)

    elif algorithm == 'greedy':
        move = greedy_2step(board, 'black', board.all_possible_moves)
    
    elif algorithm == 'random':
        move = find_random_move(board.all_possible_moves)

    return move

def find_random_move(moves):
    '''
    Random move finder algorithm
    '''
    return moves[random.randint(0, len(moves) - 1)]

def minimax(board, depth, alpha, beta, maximizingPlayer):
    '''
    Minimax with n depths with alpha beta pruning algorithm
    '''
    # Check if we reached our depth or the game has ended
    if depth == 0 or board.checkmate or board.stalemate:
        return evaluate_board_on_material_and_position(board), None

    # Checking for the player who wants to get a higher score (white)
    if maximizingPlayer:
        # Set the worst case to a very small number
        max_score = float("-inf")
        best_move = None

        # Calculate maximizing player's (white) valid moves
        white_moves = board.calc_all_valid_moves('white')
        random.shuffle(white_moves)

        for move in white_moves:
            # Make the possible best move
            board.move(move.moved_piece, move)
            score = minimax(board, depth - 1, alpha, beta, False)[0]
            board.undo_move()

            if score > max_score:
                max_score = score
                best_move = move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score, best_move

    # Checking for the player who wants to get a lower score (black)
    else:
        min_score = float("inf")
        best_move = None

        # Calculate maximizing player's (white) valid moves
        black_moves = board.calc_all_valid_moves('black')
        random.shuffle(black_moves)

        for move in black_moves:
            # Make the possible best move
            board.move(move.moved_piece, move)
            score = minimax(board, depth - 1, alpha, beta, True)[0]
            board.undo_move()

            if score < min_score:
                min_score = score
                best_move = move
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score, best_move

def greedy_2step(board, ai_player, moves):
    '''
    Greedy algorithm based on based on material count with two depth
    '''
    # Negative for black turn and positive for white turn
    turn = 1 if ai_player == 'white' else -1
    human_color = 'white' if ai_player =='black' else 'white'

    ai_best_score = -CHECKMATE * turn
    ai_best_move = None

    for ai_move in moves:
        # Make the possible best ai move
        board.move(ai_move.moved_piece, ai_move)

        # Calculate all the human player moves in the new board
        board.calc_all_valid_moves(human_color)
        human_moves = board.all_possible_moves

        # Set the human player worst score
        human_best_score = CHECKMATE * turn
        
        # Calculate human player best possible score after making a move
        for human_move in human_moves:
            # Make the human player possible best move
            board.move(human_move.moved_piece, human_move)

            # Check the new state of the board after human played a move
            if board.checkmate:
                # Human gets the highest score if after the move we have a checkmate
                score = -CHECKMATE * turn
            elif board.stalemate:
                score = STALEMATE
            else:
                # Calculate score only based on board material count
                score = evaluate_board_on_material(board)

            # If human is white, best move is the most positive, else, it is the most negative
            if human_color == 'white':
                # If the new score is higher than the previous high, replace it
                if score > human_best_score:
                    human_best_score = score
            else:
                if score < human_best_score:
                    human_best_score = score

            # Turn back the move and head back to try other human moves
            board.undo_move()
        
        # Check if the max score of human moves is lower for this ai move than the previous ai moves
        if human_best_score < ai_best_score:
            ai_best_score = human_best_score
            ai_best_move = ai_move

        # Turn back the move and head back to try other ai moves
        board.undo_move()
       
    return ai_best_move

def greedy_1step(board, ai_player, moves):
    '''
    Greedy algorithm based on based on material count with two depth
    '''
    # Negative for black turn and positive for white turn
    turn = 1 if ai_player == 'white' else -1
    human_color = 'white' if ai_player =='black' else 'white'

    ai_best_score = -CHECKMATE * turn
    ai_best_move = None

    for ai_move in moves:
        # Make the possible best ai move
        board.move(ai_move.moved_piece, ai_move)
        
        # Check the new state of the board after human played a move
        if board.checkmate:
            score = CHECKMATE * turn
        elif board.stalemate:
            score = STALEMATE
        else:
            # Calculate score only based on board material count
            score = evaluate_board_on_material(board)

        # If human is white, best move is the most positive, else, it is the most negative
        if human_color == 'white':
            # If the new score is higher than the previous high, replace it
            if score < ai_best_score:
                ai_best_score = score
                ai_best_move = ai_move
        else:
            if score > ai_best_score:
                ai_best_score = score
                ai_best_move = ai_move
        # Turn back the move and head back to try other ai moves
        board.undo_move()
       
    return ai_best_move

def evaluate_board_on_material(board):
    '''
    Sum total score at the current board state
    '''
    score = 0
    for row in range(ROWS):
        for col in range(COLS):
            piece =  board.squares[row][col].piece
            if piece:
                score += piece.value

    return score


def evaluate_board_on_material_and_position(board):
    '''
    Sum the total score at the current board state including positional advantage
    '''
    score = 0
    for row in range(ROWS):
        for col in range(COLS):
            piece =  board.squares[row][col].piece
            if piece:
                key = f"{piece.name}_{piece.color}"
                additional_value = PIECE_POSITIONAL_VALUES[key][row][col] * 0.02
                score += (piece.value + additional_value)

    return score