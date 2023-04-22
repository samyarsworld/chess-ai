from const import *

class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def is_empty(self):
        return self.piece == None
    
    def has_opponent_piece(self, color):
        return self.piece != None and self.piece.color != color
        
    def has_my_piece(self, color):
        return self.piece != None and self.piece.color == color
