from const import *
import pygame
from board import Board
from dragger import Dragger
import os


class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.player_turn = 'white'
        self.hover = None
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.alphacols = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        
    # Render methods
    def show_board(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                color = (229, 230, 252) if (row + col) % 2 == 0 else (104, 106, 192)
                rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(screen, color, rect)

                # row coordinates
                if col == 0:
                    color = '#C86464' if row % 2 == 0 else '#C84646'
                    label = self.font.render(str(ROWS - row), 1, color)
                    label_pos = (5, 5 + row * SQ_SIZE)
                    screen.blit(label, label_pos)

                # col coordinates
                if row == 7:
                    color = '#C86464' if (row + col) % 2 == 0 else '#C84646'
                    label = self.font.render(self.alphacols[col], 1, color)
                    label_pos = (col * SQ_SIZE + SQ_SIZE - 20, HEIGHT - 20)
                    screen.blit(label, label_pos)
    
    def show_pieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                # Show if there is a piece
                if self.board.squares[row][col].piece:
                    piece = self.board.squares[row][col].piece
                    # All pieces except dragging piece
                    if piece is not self.dragger.piece:
                        img = piece.shape
                        img_loc = (col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2)
                        piece.shape_pos = img.get_rect(center=img_loc)
                        screen.blit(img, piece.shape_pos)
                    
    def show_possible_moves(self, screen):
        if self.dragger.dragging:
            piece = self.dragger.piece

            ###################
            if piece.color == 'black':
                for move in self.board.all_possible_moves:
                    color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                    rect = (move.final.col * SQ_SIZE, move.final.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                    pygame.draw.rect(screen, color, rect)
                return

            # Show all valid moves
            for move in piece.moves:
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                rect = (move.final.col * SQ_SIZE, move.final.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(screen, color, rect)

    def show_last_move(self, surface):
        if self.board.move_log:
            initial = self.board.move_log[-1].initial
            final = self.board.move_log[-1].final

            for pos in [initial, final]:
                color = (244, 247, 116) if (pos.row + pos.col) % 2 == 0 else (172, 195, 51)
                rect = (pos.col * SQ_SIZE, pos.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(surface, color, rect)

    def show_hover(self, surface):
        if self.hover:
            color = (180, 180, 180)
            rect = (self.hover.col * SQ_SIZE, self.hover.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            pygame.draw.rect(surface, color, rect, width=3)


    def change_turn(self):
        self.player_turn = 'white' if self.player_turn == 'black' else 'black'


    def set_hover(self, row, col):
        if 0 <= row < ROWS and 0 <= col < COLS:
            self.hover = self.board.squares[row][col]

    def play_sound(self, capture=False):
        if capture:
            pygame.mixer.Sound(os.path.join('assets/sounds/capture.wav')).play()
        else:
            pygame.mixer.Sound(os.path.join('assets/sounds/move.wav')).play()
