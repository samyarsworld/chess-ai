import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move
from piece import King, Pawn


pygame.init()

FONT = pygame.font.SysFont('comicsans', 60)
checkmate_text = FONT.render("CHECKMATE! Press R to restart.", True, (0, 0, 0))
checkmate_text_rect = checkmate_text.get_rect()
stalemate_text = FONT.render("STALEMATE! Press R to restart.", True, (0, 0, 0))
stalemate_text_rect = stalemate_text.get_rect()
    
class Main:
    def __init__(self):
        # Set display screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Set window name
        pygame.display.set_caption('Chess')
        # Initilize the game with all the pieces at initial location
        self.game = Game()     
        # Clock and FPS
        self.clock = pygame.time.Clock()

        # End game alerts
        checkmate_text_rect.center = self.screen.get_rect().center
        stalemate_text_rect.center = self.screen.get_rect().center

    def mainloop(self):
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        flag = True
        get_valid_moves = True

        while flag:
            # Show methods in proper order
            game.show_board(screen)
            game.show_last_move(screen)
            game.show_possible_moves(screen)
            game.show_hover(screen)
            game.show_pieces(screen)

            # Show dragging piece
            if dragger.dragging:
                dragger.update_blit(screen)
            
            # At the beggining of each turn, calculate all the valid moves
            if get_valid_moves:
                board.calc_all_valid_moves(game.player_turn)
                
                # Call checkmate or stalemate if no valid moves
                if not board.all_possible_moves:
                    if board.is_king_in_check(game.player_turn):
                        self.screen.blit(checkmate_text, checkmate_text_rect)
                    else:
                        self.screen.blit(stalemate_text, stalemate_text_rect)
                    pygame.display.flip()
                    flag = False
                # Don't repeat the calculation on every frame (only once per turn)
                get_valid_moves = False
                
               
            # Listen for events
            for event in pygame.event.get():
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
                            
                            game.change_turn()

                            # Clear all valid moves
                            board.all_possible_moves = []
                            # Set calculating valid moves true for the next turn
                            get_valid_moves = True

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
                            get_valid_moves = True
                    
                    # # Restart and change color move
                    # if event.key == pygame.K_c:
                    #     pass

                        
                elif event.type == pygame.QUIT:
                    flag = False
                    pygame.quit()
                    sys.exit()
                
                # self.clock.tick(FPS)
                pygame.display.update()


        # Game ended
        while True:
            self.clock.tick(10)
            # Listen for events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # Restart game
                    if event.key == pygame.K_r:
                        print('hey3')
                        main = Main()
                        main.mainloop()



main = Main()
main.mainloop()