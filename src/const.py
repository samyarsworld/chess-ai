
# Game screen dimensions
BOARD_WIDTH = 800
BOARD_HEIGHT = 800
MOVE_LOG_WIDTH = 400
MOVE_LOG_HEIGHT = 800


# Board dimensions
COLS = 8
ROWS = 8
SQ_SIZE = BOARD_HEIGHT // ROWS

# Board pieces (80px, 128px)
PIECES = ['black_bishop', 'black_king', 'black_pawn', 'black_queen', 'black_rook', 'black_knight',
'white_bishop', 'white_king', 'white_pawn', 'white_queen', 'white_rook', 'white_knight']

# Frame per second
FPS = 60


# Piece positional values
king_positional_values = [
    # a   b   c   d   e   f   g   h
    [-30,-40,-40,-50,-50,-40,-40,-30], # 8
    [-30,-40,-40,-50,-50,-40,-40,-30], # 7
    [-30,-40,-40,-50,-50,-40,-40,-30], # 6
    [-30,-40,-40,-50,-50,-40,-40,-30], # 5
    [-20,-30,-30,-40,-40,-30,-30,-20], # 4
    [-10,-20,-20,-20,-20,-20,-20,-10], # 3
    [ 20, 20,  0,  0,  0,  0, 20, 20], # 2
    [ 20, 30, 10,  0,  0, 10, 30, 20]  # 1
]

bishop_positional_values = [
    # a   b   c   d   e   f   g   h
    [-20,-10,-10,-10,-10,-10,-10,-20], # 8
    [-10,  0,  0,  0,  0,  0,  0,-10], # 7
    [-10,  0,  5, 10, 10,  5,  0,-10], # 6
    [-10,  5,  5, 10, 10,  5,  5,-10], # 5
    [-10,  0, 10, 10, 10, 10,  0,-10], # 4
    [-10, 10, 10, 10, 10, 10, 10,-10], # 3
    [-10,  5,  0,  0,  0,  0,  5,-10], # 2
    [-20,-10,-10,-10,-10,-10,-10,-20]  # 1
]

knight_positional_values = [
    # a   b   c   d   e   f   g   h
    [-50,-40,-30,-30,-30,-30,-40,-50], # 8
    [-40,-20,  0,  0,  0,  0,-20,-40], # 7
    [-30,  0, 10, 15, 15, 10,  0,-30], # 6
    [-30,  5, 15, 20, 20, 15,  5,-30], # 5
    [-30,  0, 15, 20, 20, 15,  0,-30], # 4
    [-30,  5, 10, 15, 15, 10,  5,-30], # 3
    [-40,-20,  0,  5,  5,  0,-20,-40], # 2
    [-50,-40,-30,-30,-30,-30,-40,-50]  # 1
]

rook_positional_values = [
    # a   b   c   d   e   f   g   h
    [  0,  0,  0,  5,  5,  0,  0,  0], # 8
    [ -5,  0,  0,  0,  0,  0,  0, -5], # 7
    [ -5,  0,  0,  0,  0,  0,  0, -5], # 6
    [ -5,  0,  0,  0,  0,  0,  0, -5], # 5
    [ -5,  0,  0,  0,  0,  0,  0, -5], # 4
    [ -5,  0,  0,  0,  0,  0,  0, -5], # 3
    [  5, 10, 10, 10, 10, 10, 10,  5], # 2
    [  0,  0,  0,  0,  0,  0,  0,  0]  # 1
]

queen_positional_values = [
    # a   b   c   d   e   f   g   h
    [-20,-10,-10, -5, -5,-10,-10,-20], # 8
    [-10,  0,  0,  0,  0,  0,  0,-10], # 7
    [-10,  0,  5,  5,  5,  5,  0,-10], # 6
    [ -5,  0,  5,  5,  5,  5,  0, -5], # 5
    [  0,  0,  5,  5,  5,  5,  0, -5], # 4
    [-10,  5,  5,  5,  5,  5,  0,-10], # 3
    [-10,  0,  5,  0,  0,  0,  0,-10], # 2
    [-20,-10,-10, -5, -5,-10,-10,-20]  # 1
]


'''
Since the pawns start on the second rank in the starting position,
their position scores are higher on the third and fourth ranks where they
have more mobility and can potentially advance. The fifth rank has a slightly lower score because
the pawn cannot advance without being captured, and the sixth and seventh ranks have lower scores
still because they are closer to the opponent's pieces and can be more easily attacked.

As for the eighth rank, it is indeed an imfportant square because a pawn that reaches the eighth
rank can be promoted to a queen. However, the positional evaluation for the eighth rank is set to
0 because the pawn's mobility is limited and it is vulnerable to being captured if it cannot be promoted
immediately. Additionally, promoting a pawn to a queen is not always the best option, as sometimes promoting
to a knight or bishop can lead to a stronger position.
'''
pawn_positional_values = [
    # a   b   c   d   e   f   g   h
    [  0,  0,  0,  0,  0,  0,  0,  0], # 8
    [ 50, 50, 50, 50, 50, 50, 50, 50], # 7
    [ 10, 10, 20, 30, 30, 20, 10, 10], # 6
    [  5,  5, 10, 25, 25, 10,  5,  5], # 5
    [  0,  0,  0, 20, 20,  0,  0,  0], # 4
    [  5, -5,-10,  0,  0,-10, -5,  5], # 3
    [  5, 10, 10,-20,-20, 10, 10,  5], # 2
    [  0,  0,  0,  0,  0,  0,  0,  0]  # 1
]



PIECE_POSITIONAL_VALUES = {
    "knight_white": knight_positional_values,
    "knight_black": knight_positional_values[::-1],
    "bishop_white": bishop_positional_values,
    "bishop_black": bishop_positional_values[::-1],
    "queen_white": queen_positional_values,
    "queen_black": queen_positional_values[::-1],
    "rook_white": rook_positional_values,
    "rook_black": rook_positional_values[::-1],
    "pawn_white": pawn_positional_values,
    "pawn_black": pawn_positional_values[::-1],
    "king_white": king_positional_values,
    "king_black": king_positional_values[::-1]
}
