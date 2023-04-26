
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
knight_positional_values = [[0, 1, 2, 2, 2, 2, 1, 0],
                 [1, 3, 5, 5, 5, 5, 3, 1],
                 [2, 5, 6, 6.5, 6.5, 6, 5, 2],
                 [2, 5.5, 6.5, 7, 7, 6.5, 5.5, 2],
                 [2, 5, 6.5, 7, 7, 6.5, 5, 2],
                 [2, 5.5, 6, 6.5, 6.5, 6, 5.5, 2],
                 [1, 3, 5, 5.5, 5.5, 5, 3, 1],
                 [0, 1, 2, 2, 2, 2, 1, 0]]

bishop_positional_values = [[0, 2, 2, 2, 2, 2, 2, 0],
                 [2, 4, 4, 4, 4, 4, 4, 2],
                 [2, 4, 5, 6, 6, 5, 4, 2],
                 [2, 5, 5, 6, 6, 5, 5, 2],
                 [2, 4, 6, 6, 6, 6, 4, 2],
                 [2, 6, 6, 6, 6, 6, 6, 2],
                 [2, 5, 4, 4, 4, 4, 5, 2],
                 [0, 2, 2, 2, 2, 2, 2, 0]]

rook_positional_values = [[2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5],
               [5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 5],
               [0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0],
               [0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0],
               [0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0],
               [0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0],
               [0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0],
               [2.5, 2.5, 2.5, 5, 5, 2.5, 2.5, 2.5]]

queen_positional_values = [[0, 2, 2, 3, 3, 2, 2, 0],
                [2, 4, 4, 4, 4, 4, 4, 2],
                [2, 4, 5, 5, 5, 5, 4, 2],
                [3, 4, 5, 5, 5, 5, 4, 3],
                [4, 4, 5, 5, 5, 5, 4, 3],
                [2, 5, 5, 5, 5, 5, 4, 2],
                [2, 4, 5, 4, 4, 4, 4, 2],
                [0, 2, 2, 3, 3, 2, 2, 0]]

pawn_positional_values = [[8, 8, 8, 8, 8, 8, 8, 8],
               [7, 7, 7, 7, 7, 7, 7, 7],
               [3, 3, 4, 5, 5, 4, 3, 3],
               [2.5, 2.5, 3, 4.5, 4.5, 3, 2.5, 2.5],
               [2, 2, 2, 4, 4, 2, 2, 2],
               [2.5, 1.5, 1, 2, 2, 1, 1.5, 2.5],
               [2.5, 3, 3, 0, 0, 3, 3, 2.5],
               [2, 2, 2, 2, 2, 2, 2, 2]]

piece_positional_values = {"knight_white": knight_positional_values,
                         "knight_black": knight_positional_values[::-1],
                         "bishop_white": bishop_positional_values,
                         "bishop_black": bishop_positional_values[::-1],
                         "queen_white": queen_positional_values,
                         "queen_black": queen_positional_values[::-1],
                         "rook_white": rook_positional_values,
                         "rook_black": rook_positional_values[::-1],
                         "pawn_white": pawn_positional_values,
                         "pawn_black": pawn_positional_values[::-1]}
