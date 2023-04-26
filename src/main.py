import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move
from chessAi import find_ai_move
pygame.init()


FONT = pygame.font.SysFont('comicsans', 60)
LOG_FONT = pygame.font.SysFont('aerial', 20)
checkmate_text = FONT.render("CHECKMATE! Press R to restart.", True, (0, 0, 0))
checkmate_text_rect = checkmate_text.get_rect()
stalemate_text = FONT.render("STALEMATE! Press R to restart.", True, (0, 0, 0))
stalemate_text_rect = stalemate_text.get_rect()
    
class Main:
    def __init__(self):
        # Set display screen
        self.screen = pygame.display.set_mode((BOARD_WIDTH + MOVE_LOG_WIDTH, BOARD_HEIGHT))
        # Set window name
        pygame.display.set_caption('Chess')
        # Initilize the game with all the pieces at initial location
        self.game = Game()     
        # Clock and FPS
        self.clock = pygame.time.Clock()
        # End game alerts
        checkmate_text_rect.center = self.screen.get_rect().center
        stalemate_text_rect.center = self.screen.get_rect().center

    def mainloop(self, player='AI', difficulty=1):
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        flag = True
        begin_turn = True
        # Player 1 represents player with white pieces
        player1 = 'human'
        # Player 2 represents player with black pieces
        player2 = player
        
        while flag:
            # Show methods in proper order
            game.show_board(screen)
            game.show_last_move(screen)
            game.show_possible_moves(screen)
            game.show_hover(screen)
            game.show_pieces(screen)
            
            # Show dragging piece
            if dragger.dragging: dragger.update_blit(screen)
            
            # Only at the begining of each turn
            if begin_turn:
                game.show_movelog(screen)
                
                # It is human's turn if the human is player1 and it's whites turn or human is player 2 and it's black to move
                human_turn = (player1 == 'human' and game.player_turn == 'white') or (player2 == 'human' and game.player_turn == 'black')  
                # Calculate all the valid moves
                board.calc_all_valid_moves(game.player_turn)
                
                # Call checkmate or stalemate if no valid moves
                if not board.all_possible_moves:
                    if board.is_king_in_check(game.player_turn):
                        board.checkmate = True
                        self.screen.blit(checkmate_text, checkmate_text_rect)
                    else:
                        board.stalemate = True
                        self.screen.blit(stalemate_text, stalemate_text_rect)
                    pygame.display.flip()
                    flag = False
                    break
                # Don't repeat the calculation on every frame (only once per turn)
                begin_turn = False
            
            # If AI turn to move
            if not human_turn:
                # Find best ai move
                move = find_ai_move(board, 'minimax', difficulty)

                if not move:
                    # Find a random move
                    move = find_ai_move(board, 'random')
                # Update en passant
                board.set_true_en_passant(move.moved_piece)
                board.move(move.moved_piece, move)
                is_capture = move.captured_piece
                game.play_sound(is_capture)

                if is_capture:
                    print('x ', end='')
                print(move)

                # Clear all valid moves
                board.all_possible_moves = []
                # Set calculating valid moves true for the next turn
                begin_turn = True
                game.change_turn()
                # Update the screen
                pygame.display.update()
                continue

            
            # Listen for events
            for event in pygame.event.get():
                # If human is to move, enable manual activated events
                if human_turn:
                    # Mouse click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        dragger.update_pointer(event.pos)
                        clicked_row = dragger.pointer_y // SQ_SIZE
                        clicked_col = dragger.pointer_x // SQ_SIZE

                        # If there is a piece in the clicked sqaure
                        if game.board.squares[clicked_row][clicked_col].piece :
                            piece = game.board.squares[clicked_row][clicked_col].piece

                            # Check color to see if it is the player's turn
                            if piece.color == game.player_turn:
                                # Get the possible moves for the clicked piece
                                for move in board.all_possible_moves:
                                    if move.initial.col == clicked_col and move.initial.row == clicked_row:
                                        piece.moves.append(move)
                                    
                                # Save initial location of the clicked piece
                                dragger.save_init_loc(event.pos)
                                # Set dragging is true and the dragging piece
                                dragger.drag(piece)
                                

                    # Mouse moving while clicked
                    elif event.type == pygame.MOUSEMOTION:
                        # Apply hover visuals as mouse moves on screen
                        game.set_hover(event.pos[1] // SQ_SIZE, event.pos[0] // SQ_SIZE)

                        if dragger.dragging:
                            dragger.update_pointer(event.pos)

                            
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if dragger.dragging:
                            dragger.update_pointer(event.pos)
                            final_row, final_col = dragger.pointer_y // SQ_SIZE, dragger.pointer_x // SQ_SIZE
                            initial, final = Square(dragger.init_row, dragger.init_col), Square(final_row, final_col)
                            move = Move(initial, final, board)
                            # Apply move if move valid
                            if board.valid_move(dragger.piece, move):
                                # Update en passant
                                board.set_true_en_passant(dragger.piece)

                                board.move(dragger.piece, move)
                                is_capture = move.captured_piece
                                game.play_sound(is_capture)

                                if is_capture:
                                    print('x ', end='')
                                print(move)
                        
                                # Clear all valid moves
                                board.all_possible_moves = []
                                # Set calculating valid moves true for the next turn
                                begin_turn = True
                                game.change_turn()
                            # Clear piece valid moves
                            dragger.piece.moves = []
                        dragger.undrag() 


                    # Key press
                    elif event.type == pygame.KEYDOWN:
                        # Restart game
                        if event.key == pygame.K_r:
                            main = Main()
                            main.mainloop()

                        # Undo move
                        if event.key == pygame.K_u:
                            if board.undo_move():
                                game.change_turn()
                                board.all_possible_moves = []
                                begin_turn = True
                            # We need double undo to skip the ai turn as well
                            if (player1 == 'AI' or player2 == 'AI') and board.undo_move():
                                game.change_turn()

                            
                    elif event.type == pygame.QUIT:
                        flag = False
                        pygame.quit()
                        sys.exit()
            
                # Update the screen
                pygame.display.update()


        # Game ended
        while True:
            self.clock.tick(10)
            # Listen for events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # Restart game
                    if event.key == pygame.K_r:
                        main = Main()
                        main.mainloop()


if __name__ == '__main__':
    main = Main()
    main.mainloop()