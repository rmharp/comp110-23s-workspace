import pygame
import math
import random
import sys
#from brick_breaker.main import main

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Console")

FPS: int = 60
GAME_WIDTH: int = 150
GAME_HEIGHT: int = 100
GAP: int = 20
brick_breaker_image = pygame.image.load('hack110_r/assets/brick_breaker.png')
chess_image = pygame.image.load('hack110_r/assets/chess.png')

class Chess:
    
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x - 60
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, "white", (self.x, self.y, self.width, self.height))
        win.blit(chess_image, (self.x, self.y))
        

class Brick_Breaker:
    
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x - 60
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
            pos = pygame.mouse.get_pos()
            if pos == pygame.Rect.collidepoint():
              
              return
                

def draw(win, chess, brick_breaker):
    win.fill("black")
    chess.draw(win)
    brick_breaker.draw(win)

    pygame.display.update()
    

def main():
    clock = pygame.time.Clock()
    brick_breaker = Brick_Breaker(WIDTH/4, HEIGHT/4, GAME_WIDTH, GAME_HEIGHT)
    chess = Chess(3*WIDTH/4, HEIGHT/4, GAME_WIDTH, GAME_HEIGHT)
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
        pygame.display.update()

if __name__ == "__main__":
    main()