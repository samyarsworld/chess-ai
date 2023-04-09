import pygame
from const import *

class Dragger:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.pointer_x = 0
        self.pointer_y = 0
        self.init_row = 0
        self.init_col = 0
    
    # Update clicked position
    def update_pointer(self, pos):
        self.pointer_x, self.pointer_y = pos
    
    # Save initial position of dragging piece
    def save_init_loc(self, pos):
        self.init_row = pos[1] // SQ_SIZE
        self.init_col = pos[0] // SQ_SIZE
    
    # Show dragging piece
    def update_blit(self, screen):
        self.piece.set_shape(128)
        img = pygame.image.load(self.piece.shape)
        img_loc = (self.pointer_x, self.pointer_y)
        self.piece.shape_pos = img.get_rect(center=img_loc)
        screen.blit(img, self.piece.shape_pos)

    # Set dragging piece
    def drag(self, piece):
        self.piece = piece
        self.dragging = True

    # Set undragging piece
    def undrag(self):
        self.piece = None
        self.dragging = False

