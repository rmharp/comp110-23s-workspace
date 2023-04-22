"""Generates Chessboard, Chess Piece Sprites, and piece positions (x,y coords)"""

import pygame
from chess_constants import CHESS_BACKGROUND
from chess_constants import BACKGROUND_HEIGHT
from chess_constants import BACKGROUND_WIDTH


class Background():
    """Generates background chessboard surface"""

    def __init__(self):
        # Initialize super class
        super(Background, self).__init__()

        # Creates surface chessboard using laod method of iamge, and converting it
        surface = pygame.image.load(CHESS_BACKGROUND).convert()

        # Scale to size of screen window
        self.surf = pygame.transform.scale(surface, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))

        self.x = 0
        self.y = 0

    def update(self):
        # Update screen
        self.x = self.x

    def render(self, screen):
        # Render method because not in sprite group
        screen.blit(self.surf, (self.x, self.y))