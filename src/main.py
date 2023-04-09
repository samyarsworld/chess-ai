import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()        

    def mainloop(self):
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            # show methods 
            game.show_board(screen)
            game.show_last_move(screen)
            game.show_possible_moves(screen)
            game.show_hover(screen)
            game.show_pieces(screen)

            # Show dragging piece
            if dragger.dragging:
                dragger.update_blit(screen)

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

                        # Color if it is player turn
                        if piece.color == game.player_turn:
                            board.calc_moves(piece, clicked_row, clicked_col, is_for_check=False)
                            dragger.save_init_loc(event.pos)
                            dragger.drag(piece)


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
                        move = Move(initial, final)
                        # Apply move if move valid
                        if board.valid_move(dragger.piece, move):
                            # Check if there is a piece in the sqaure that we moved to
                            is_capture = board.squares[final_row][final_col].piece

                            # Update en passant
                            board.set_true_en_passant(dragger.piece)   

                            game.play_sound(is_capture)
                            board.move(dragger.piece, move)
                            game.change_turn()
                            
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

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                pygame.display.update()


main = Main()
main.mainloop()