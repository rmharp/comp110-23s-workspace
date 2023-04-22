"""Chess Game project for Hack110 2023"""

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from chessboard import *
from chess_constants import *
from chess_sprites import Pawn, King, Knight, Rook, Queen, Bishop


# Initialize game
pygame.init() 

# Set up window
screen = pygame.display.set_mode([BACKGROUND_WIDTH, BACKGROUND_HEIGHT])

# Create Sprites and background, adding sprites later
background = Background()

# Set up clock for tickrate in loop
clock = pygame.time.Clock()

from chess_pieces import *

def main():
    # Running variable
    running = True
    # Main loop
    while running:
        currently_dragged: pygame.sprite.Sprite
        #Event queue
        for event in pygame.event.get():
            #Stops loop when x button is pressed
            if event.type == QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Check for left mouse button down
                    for sprite in all_sprites:
                        if sprite.rect.collidepoint(event.pos):
                            sprite_dragging = True
                            currently_dragged = sprite
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # Check for left mouse button up
                    sprite_dragging = False

        background.update()
        background.render(screen)
        

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        #update display equivalent
        pygame.display.flip()

        # Tick at constant frame rate
        clock.tick(TICK_RATE)


if __name__ == '__main__':
    main()