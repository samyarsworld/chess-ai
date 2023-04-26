class Move:
    rank_to_row = {i: 8 - i for i in range(8)}
    row_to_rank = {8 - i: i for i in range(8)}
    file_to_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    col_to_file = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def __init__(self, initial, final, board):
        self.initial = initial
        self.final = final
        self.moved_piece = board.squares[self.initial.row][self.initial.col].piece
        self.captured_piece = board.squares[self.final.row][self.final.col].piece
        self.is_enpassant = False
        self.is_queen_castle = False
        self.is_king_castle = False
        self.is_check = False


    def __str__(self):
        # Castle move
        if self.is_king_castle:
            return "O-O"
        elif self.is_queen_castle:
            return "O-O-O"
        # Create chess notation
        abv = self.moved_piece.name[0].upper()
        if self.moved_piece.name == 'knight':
            abv = 'N'
        elif self.moved_piece.name == 'pawn':
            abv = ''
        # Moving piece name
        s = f'{abv}'

        # Add x if it is a capture
        if self.captured_piece:
            s += 'x'

        # Final location of the moving piece
        s += f'{self.col_to_file[self.final.col]}{self.rank_to_row[self.final.row]}'
        
        # Add + if the position causes check
        if self.is_check:
            s += '+'
            
        return s

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final