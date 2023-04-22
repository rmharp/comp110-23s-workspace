import pygame

HEIGHT = 450
WIDTH = 800
FPS = 60

BACKGROUND_COLOR = (53, 130, 27)
PROJ_COLOR = (200, 50, 50)
LAUNCHER_COLOR = (189, 136, 66)
GOAL_COLOR = (40, 45, 45)
WALL_COLOR = (50, 65, 65)

FLOOR_FRICTION = 0.95 # this reduces balls horizontal speed when it touches the floor
RIGHT_WALL = WIDTH-10
LEFT_WALL = 12
FLOOR = HEIGHT-10
GRAVITY = 9.8
BOUNCE_COEFFECIENT = -0.7 # this flips the balls trajectory rebound off the surface, and reduces its speed to 85% of what it was

TEE: pygame.Rect = pygame.Rect(15, HEIGHT-10, 20, 20)
GOAL: pygame.Rect = pygame.Rect(WIDTH-100, HEIGHT - 25, 50, 50)
WALL: pygame.Rect = pygame.Rect(WIDTH/2, HEIGHT-90, 25, 100)
WALL_TOP: pygame.Rect = pygame.Rect(WIDTH/2, HEIGHT-100, 25, 10)
WALL_FACADE: pygame.Rect = pygame.Rect(WIDTH/2, HEIGHT-100, 25, 100)