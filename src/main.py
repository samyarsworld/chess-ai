import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move


class Main:
    def __init__(self):
        pygame.init()
        # Set display screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Set window name
        pygame.display.set_caption('Chess')
        # Initilize the game with all the pieces at initial location
        self.game = Game()     
        # Clock and FPS
        self.clock = pygame.time.Clock()

    def mainloop(self):
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        flag = True
        ai_move_calc = True
        
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
            
            ################
            if game.player_turn == board.opponent_color and ai_move_calc:
                ai_move_calc = False
                board.calc_AI_moves()
               
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
                            ################## Calculate possible moves for the clicked piece
                            if game.player_turn == board.player_color:
                                board.calc_player_moves(piece, clicked_row, clicked_col, is_for_check=False)
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
                            # Check if there is a piece in the square that we moved to
                            

                            # Update en passant
                            board.set_true_en_passant(dragger.piece)   

                            board.move(dragger.piece, move)
                            is_capture = move.captured_piece
                            game.play_sound(is_capture)

                            if is_capture:
                                print('x ', end='')
                            print(move)
                            
                            game.change_turn()

                           
                    ################# if you play only player, clear valid move can be one statemnet and outside of the above if statement for board.valid
                            ai_move_calc = True
                            # Clear valid moves
                            dragger.piece.moves = []
                            # It means it was blacks turn and now changed to white
                            if game.player_turn == board.player_color:
                                board.AI_possible_moves = []

                        else:
                            if game.player_turn == board.player_color:
                                # Clear valid moves
                                dragger.piece.moves = []

                    dragger.undrag() 
                

                # Key press
                elif event.type == pygame.KEYDOWN:
                    # Restart game
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                    # Undo move
                    if event.key == pygame.K_u:
                        if board.undo_move():
                            game.change_turn()
                            board.AI_possible_moves = []
                            ai_move_calc = True
                    
                    # # Restart and change color move
                    # if event.key == pygame.K_c:
                    #     pass

                        
                        
                elif event.type == pygame.QUIT:
                    flag = False
                    pygame.quit()
                    sys.exit()
                
                # self.clock.tick(FPS)
                pygame.display.update()


main = Main()
main.mainloop()