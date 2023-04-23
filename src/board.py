from square import Square
from move import Move
from piece import *
from const import *


class Board:
    def __init__(self):
        self.squares = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.move_log = []
        self.all_possible_moves = []
        self.player_color = 'white'
        self.opponent_color = 'black'
        self.checkmate = False
        self.stalemate = False
        self.black_king_loc = [0, 4]
        self.white_king_loc = [7, 4]

        self._create()
        

    def _create(self):
        # Set pawns and empty sqaures
        for row in range(ROWS):
            for col in range(COLS):
                if row == 1:
                    color = 'black'
                    self.squares[row][col] = Square(row, col, Pawn(color))
                elif row == 6:
                    color = 'white'
                    self.squares[row][col] = Square(row, col, Pawn(color))
                else:
                    self.squares[row][col] = Square(row, col)

        # Set major pieces
        # White pieces
        c = self.player_color
        row = 7
        self.squares[row][0] = Square(row, 0, Rook(c))
        self.squares[row][1] = Square(row, 1, Knight(c))
        self.squares[row][2] = Square(row, 2, Bishop(c))
        self.squares[row][3] = Square(row, 3, Queen(c))
        self.squares[row][4] = Square(row, 4, King(c))
        self.squares[row][5] = Square(row, 5, Bishop(c))
        self.squares[row][6] = Square(row, 6, Knight(c))
        self.squares[row][7] = Square(row, 7, Rook(c))
        # Black pieces
        c = self.opponent_color
        row = 0
        self.squares[row][0] = Square(row, 0, Rook(c))
        self.squares[row][1] = Square(row, 1, Knight(c))
        self.squares[row][2] = Square(row, 2, Bishop(c))
        self.squares[row][3] = Square(row, 3, Queen(c))
        self.squares[row][4] = Square(row, 4, King(c))
        self.squares[row][5] = Square(row, 5, Bishop(c))
        self.squares[row][6] = Square(row, 6, Knight(c))
        self.squares[row][7] = Square(row, 7, Rook(c))

    def calc_player_moves(self, piece, row, col, is_for_check):
        '''
            Calculate all possbile moves of a piece
        '''
        def is_range(r, c):
            return 0 <= r <= 7 and 0 <= c <= 7
        
        def straight_line_moves(dirs):
            '''
                Creates and adds moves for pieces that move more than one move diagonally, vertically, or horizontally
            '''
            for dir in dirs:
                r_increment, c_increment = dir
                move_row, move_col = row + r_increment, col + c_increment

                # Increment move until move is not valid
                while True:
                    # Check for valid moves
                    if is_range(move_row, move_col):
                        # Can be None or a piece
                        final_piece = self.squares[move_row][move_col].piece
                        initial, final = Square(row, col), Square(move_row, move_col, final_piece)
                        move = Move(initial, final, self)

                        # Add if square is empty
                        if self.squares[move_row][move_col].is_empty():
                            # Check if does not cause self check
                            # If we are not validating for checks then validate for checks first
                            if not is_for_check:
                                if not self.will_be_check(piece, move):
                                    piece.add_move(move)
                                else:
                                    break
                            else:
                                piece.add_move(move)
                        # Break if aquare has my piece
                        elif self.squares[move_row][move_col].has_my_piece(piece.color):
                            break
                        # Add then break if aquare has opponent piece
                        elif self.squares[move_row][move_col].has_opponent_piece(piece.color):
                            # Check if does not cause self check
                            # If we are not validating for checks then validate for checks first
                            if not is_for_check:
                                if not self.will_be_check(piece, move):
                                    piece.add_move(move)
                                else:
                                    break
                            else:
                                piece.add_move(move)
                            break
                        move_row, move_col = move_row + r_increment , move_col + c_increment 
                    else:
                        break

        def pawn_moves():
            # Vertical moves
            moves = [row + piece.dir]
            # Check if the pawn has ever moved or the first square is blocked (checking to validate possibility of doduble jump)
            if not piece.times_moved and self.squares[row + piece.dir][col].is_empty():
                moves.append(row + piece.dir * 2)

            for move_row in moves:
                # Check for valid moves
                if is_range(move_row, col) and self.squares[move_row][col].is_empty():
                    # Create and add the valid move to piece possbile moves
                    initial, final = Square(row, col), Square(move_row, col)
                    move = Move(initial, final, self)

                    # Check if does not cause self check
                    # If we are not validating for checks then validate for checks first
                    if not is_for_check:
                        if not self.will_be_check(piece, move):
                            piece.add_move(move)
                    else:
                        piece.add_move(move)

            # Diagonal moves
            first, second = col + 1, col - 1
            move_row = row + piece.dir

            for move_col in [first, second]:
                # Check for valid moves
                if is_range(move_row, move_col) and self.squares[move_row][move_col].has_opponent_piece(piece.color):
                    # Create and add the valid move to piece possbile moves
                    final_piece = self.squares[move_row][move_col].piece
                    initial, final = Square(row, col), Square(move_row, move_col, final_piece)
                    move = Move(initial, final, self)

                    # Check if does not cause self check
                    if not is_for_check:
                        if not self.will_be_check(piece, move):
                            piece.add_move(move)
                    else:
                        piece.add_move(move)

            # En passant move
            r = 3 if piece.color == self.player_color else 4
            final_r = 2 if piece.color == self.player_color else 5
            # Left en passant
            if 0 <= col - 1 <= 7 and row == r:
                if self.squares[row][col - 1].has_opponent_piece(piece.color):
                    p = self.squares[row][col - 1].piece
                    if isinstance(p, Pawn) and p.en_passant:
                        # Create move
                        move = Move(Square(row, col), Square(final_r, col - 1, p), self)
                        # Check if does not cause self check
                        if not is_for_check:
                            if not self.will_be_check(piece, move):
                                piece.add_move(move)
                        else:
                            piece.add_move(move)
            
            # Right en passant
            if 0 <= col + 1 <= 7 and row == r:
                if self.squares[row][col + 1].has_opponent_piece(piece.color):
                    p = self.squares[row][col + 1].piece
                    if isinstance(p, Pawn) and p.en_passant:
                        # Create a new move
                        move = Move(Square(row, col), Square(final_r, col + 1, p), self)
                        # Check if does not cause self check
                        if not is_for_check:
                            if not self.will_be_check(piece, move):
                                piece.add_move(move)
                        else:
                            piece.add_move(move)

        def rook_moves():
            # Valid moving directions
            dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            straight_line_moves(dirs)

        def knight_moves():
            moves = [
               (row - 2, col - 1), (row - 2, col + 1),  (row - 1, col - 2), (row - 1, col + 2), 
               (row + 1, col - 2), (row + 1, col + 2), (row + 2, col + 1), (row + 2, col + -1)
            ] 
            for move in moves:
                move_row, move_col = move

                # Check for valid moves
                if is_range(move_row, move_col) and not self.squares[move_row][move_col].has_my_piece(piece.color):
                    # Create and add the valid move to piece possbile moves
                    final_piece = self.squares[move_row][move_col].piece
                    initial, final = Square(row, col), Square(move_row, move_col, final_piece)
                    move = Move(initial, final, self)
                    
                    # Check if does not cause self check
                    if not is_for_check:
                        if not self.will_be_check(piece, move):
                            piece.add_move(move)
                        else:
                            # Moving the knight is not possible at all so break
                            break
                    else:
                        piece.add_move(move)

        def bishop_moves():
            # Valid moving directions
            dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            straight_line_moves(dirs)
            
        def queen_moves():
            # Valid moving directions
            dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (0, -1), (-1, 0), (0, -1)]
            straight_line_moves(dirs)

        def king_moves():
            # Valid moving directions
            for move in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (0, -1), (-1, 0), (0, -1)]:
                move_row, move_col = row + move[0], col + move[1]
                # Check for valid moves
                if is_range(move_row, move_col) and not self.squares[move_row][move_col].has_my_piece(piece.color):
                    # Create and add the valid move to piece possbile moves
                    initial, final = Square(row, col), Square(move_row, move_col)
                    move = Move(initial, final, self)
                    
                    # Check if does not cause self check
                    # If we are not validating for checks then validate for checks first
                    if not is_for_check:
                        if not self.will_be_check(piece, move):
                            piece.add_move(move)
                    else:
                        piece.add_move(move)

            # Castling moves
            if not piece.times_moved:
                # Queen castling
                left_rook = self.squares[row][0].piece

                if left_rook and left_rook.name == 'rook' and not left_rook.times_moved:
                    # Check if no piece are between king and rook
                    for c in range(1, 4):
                        if self.squares[row][c].piece: break
                        if c == 3:
                            # Add king move
                            move_king = Move(Square(row, col), Square(row, 2), self)
                            # Check if does not cause self check
                            if not is_for_check:
                                # Check if king is not cut off by opponent piece when castling
                                if Move(Square(row, col), Square(row, 3), self) in piece.moves:
                                    if not self.will_be_check(piece, move_king):
                                        piece.add_move(move_king)
                            else:
                                piece.add_move(move_king)

                # King castling
                right_rook = self.squares[row][7].piece

                if right_rook and right_rook.name == 'rook' and not right_rook.times_moved:
                    for c in range(5, 7):
                        # Check if no piece are between king and rook
                        if self.squares[row][c].piece: break
                        if c == 6:
                            # Add king move
                            move_king = Move(Square(row, col), Square(row, 6), self)
                            # Check if does not cause self check
                            if not is_for_check:
                                # Check if king is not cut off by opponent piece when castling
                                if Move(Square(row, col), Square(row, 5), self) in piece.moves:
                                    if not self.will_be_check(piece, move_king):
                                        piece.add_move(move_king)
                            else:
                                piece.add_move(move_king)


        if piece.name == 'pawn': pawn_moves()
        elif piece.name == 'rook': rook_moves()
        elif piece.name == 'knight': knight_moves()
        elif piece.name == 'bishop': bishop_moves()
        elif piece.name == 'queen': queen_moves()
        elif piece.name == 'king': king_moves()


    def valid_move(self, piece, move):
        # If we are playing vs AI this code should be here
        if piece.color == self.opponent_color:
            return move in self.all_possible_moves
        return move in piece.moves
    
    def move(self, piece, move):
        initial, final = move.initial, move.final
        # Check if en passant final location is empty
        en_passant_check = self.squares[final.row][final.col].is_empty()
        # Update move
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        # Pawn
        if piece.name == 'pawn':
            diff = final.col - initial.col
            
            # Pawn promotion
            if final.row in [0, 7]:
                self.squares[final.row][final.col].piece = Queen(piece.color)

            # En passant capture, check if pawn column changed, hence en passant
            elif diff != 0 and en_passant_check:
                # Save the captured piece
                move.captured_piece = self.squares[initial.row][initial.col + diff].piece
                # Save that the move is en passant
                move.is_enpassant = True
                self.squares[initial.row][initial.col + diff].piece = None
                self.squares[final.row][final.col].piece = piece

        # Castle
        if isinstance(piece, King) and abs(initial.col - final.col) == 2:
            if final.col - initial.col < 0:
                # Queen side castle
                rook = self.squares[initial.row][0].piece
                self.squares[initial.row][0].piece = None
                self.squares[initial.row][3].piece = rook
            else:
                # King side castle
                rook = self.squares[initial.row][7].piece
                self.squares[initial.row][7].piece = None
                self.squares[initial.row][5].piece = rook
            
            self.squares[final.row][final.col].piece = piece
            self.squares[initial.row][initial.col].piece = None
            rook.times_moved += 1

        # Moved piece, useful for pawns first move and castle related moves
        piece.times_moved += 1


        # Append last move
        self.move_log.append(move)

        # Update king location
        if isinstance(piece, King):
            if piece.color == 'black':
                self.black_king_loc = [final.row, final.col]
            else:
                self.white_king_loc = [final.row, final.col]


    def undo_move(self):
        if self.move_log:
            move = self.move_log.pop()
            piece = move.moved_piece
            final, initial = move.final, move.initial

            # Pawn En P
            if move.is_enpassant:
                self.squares[final.row][final.col].piece = None
                self.squares[initial.row][initial.col].piece = piece
                self.squares[initial.row][final.col].piece = move.captured_piece

            # Castle
            elif isinstance(piece, King) and abs(initial.col - final.col) == 2:
                if final.col - initial.col < 0:
                    # Queen side castle
                    rook = self.squares[final.row][3].piece
                    # Set previous rook position
                    self.squares[final.row][0].piece = rook
                    # Remove rook 
                    self.squares[final.row][3].piece = None
                    # Set previous king position
                    self.squares[final.row][4].piece = piece
                    # Remove king 
                    self.squares[final.row][2].piece = None
                else:
                    # King side castle
                    rook = self.squares[final.row][5].piece
                    # Set previous rook position
                    self.squares[final.row][7].piece = rook
                    # Remove rook 
                    self.squares[final.row][5].piece = None
                    # Set previous king position
                    self.squares[final.row][4].piece = piece
                    # Remove king 
                    self.squares[final.row][6].piece = None
                # Decrement rook moves
                rook.times_moved -= 1
                
            # All other
            else:
                self.squares[final.row][final.col].piece = move.captured_piece
                self.squares[initial.row][initial.col].piece = piece

            # Decrement piece moves
            piece.times_moved -= 1
            return True
        # Return false if there is no undo to make so we don't change player's turn
        return False


    def will_be_check(self, piece, move):
        # Move the piece and check if the new position opens the king to the opponent
        self.move(piece, move)
        
        is_check = self.is_king_in_check(piece.color)
        
        self.undo_move()
        return is_check


    def set_true_en_passant(self, piece):
        if not isinstance(piece, Pawn):
            return

        for row in range(ROWS):
            for col in range(COLS):
                if isinstance(self.squares[row][col].piece, Pawn):
                    self.squares[row][col].piece.en_passant = False
        
        piece.en_passant = True

    
    def is_king_in_check(self, color):
        for row in range(ROWS):
            for col in range(COLS):
                # Check each opponents piece valid moves
                if self.squares[row][col].has_opponent_piece(color):
                    p = self.squares[row][col].piece
                    self.calc_player_moves(p, row, col, is_for_check=True)
                    for m in p.moves:
                        if isinstance(m.final.piece, King):
                            # Reset the opponet saved moves
                            p.moves = []
                            return True
                    # Reset the opponet saved moves
                    p.moves = []


    # AI
    def calc_all_valid_moves(self, color):
        for row in range(ROWS):
            for col in range(COLS):
                if self.squares[row][col].has_my_piece(color):
                    piece = self.squares[row][col].piece
                    self.calc_player_moves(piece, row, col, False)
                    for move in piece.moves:
                        self.all_possible_moves.append(move)
                    piece.moves = []
                    


                
