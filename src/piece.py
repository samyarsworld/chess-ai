import os

class Piece:
    def __init__(self, name, color, value, shape=None, shape_pos=None):
        self.name = name
        self.color = color
        self.value = -value if color == 'black' else value
        self.shape = shape
        self.set_shape()
        self.shape_pos = shape_pos
        self.moves = []
        self.moved = False

    def set_shape(self, size=80):
        self.shape = os.path.join(f'assets/images/{size}px/{self.color}_{self.name}.png')
    
    def add_move(self, move):
        self.moves.append(move)

class Pawn(Piece):
    def __init__(self, color):
        self.dir = 1 if color == 'black' else -1
        self.en_passant = False
        super().__init__('pawn', color, 1.0)
class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)
class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)
class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.001)
class King(Piece):
    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color, 10000.0)
class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)
