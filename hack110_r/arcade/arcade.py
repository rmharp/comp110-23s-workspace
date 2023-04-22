import pygame
import math
import random
import sys
sys.path.append('hack110_r')
from brick_breaker.BB import *

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Console")

FPS: int = 1000
GAME_WIDTH: int = 150
GAME_HEIGHT: int = 100
GAP: int = 20
brick_breaker_image = pygame.image.load('hack110_r/assets/brick_breaker.png')
chess_image = pygame.image.load('hack110_r/assets/chess.png')
GAME_ONE_x, GAME_ONE_y = WIDTH/4, HEIGHT/4
GAME_TWO_x, GAME_TWO_y = 3*WIDTH/4, HEIGHT/4

class Chess:
    
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x - GAME_WIDTH / 2
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, "white", (self.x, self.y, self.width, self.height))
        win.blit(chess_image, (self.x, self.y))
        

class Brick_Breaker:
    
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x - GAME_WIDTH / 2
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, "white", (self.x, self.y, self.width, self.height))
        win.blit(brick_breaker_image, (self.x, self.y))

def select():
    pos = None  # Initialize pos to None
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.display.update()
            pos = pygame.mouse.get_pos()
            # Check if the mouse position is within the bounds of the Chess button
            if (GAME_TWO_x <= pos[0] <= GAME_TWO_x + GAME_WIDTH and
                GAME_TWO_y <= pos[1] <= GAME_TWO_y + GAME_HEIGHT):
                # Start Chess game
                #mainChess()
                pass
            # Check if the mouse position is within the bounds of the Brick Breaker button
            elif (GAME_ONE_x <= pos[0] <= GAME_ONE_x + GAME_WIDTH and
                GAME_ONE_y <= pos[1] <= GAME_ONE_y + GAME_HEIGHT):
                # Start Brick Breaker game
                mainBB()

def draw(win, chess, brick_breaker):
    win.fill("black")
    chess.draw(win)
    brick_breaker.draw(win)
    pygame.display.update()
    

def main():
    clock = pygame.time.Clock()
    brick_breaker = Brick_Breaker(GAME_ONE_x, GAME_ONE_y, GAME_WIDTH, GAME_HEIGHT)
    chess = Chess(GAME_TWO_x, GAME_TWO_y, GAME_WIDTH, GAME_HEIGHT)
    # Set a running bool variable to True, can be set to False at any time to end the game loop
    run = True
    # Main loop
    while run:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()

        # Event queue
        for event in pygame.event.get():
        # Stop loop when X button is hit
            if event.type == pygame.QUIT:
                run = False
                break
        if keys[pygame.K_ESCAPE]: 
            run = False 
            break
        draw(win, brick_breaker, chess)
        select()
        pygame.display.update()

if __name__ == "__main__":
    main()