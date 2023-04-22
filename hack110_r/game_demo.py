import pygame
import sys
from random import randint

# starts window
pygame.init()

# constants to define window size and set FPS
HEIGHT = 450
WIDTH = 800
FPS = 60
BACKGROUND_COLOR = [53, 130, 27]
BASKET_COLOR = [189,136,66]
APPLE_COLOR = [27,130,50]


# creates clock object to limit FPS
FramePerSec = pygame.time.Clock()

# Create surface to draw objects on
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

apples = []

# adds apples with randomized locations to list
for i in range(1, 10):
    random_x = randint(0, WIDTH - 100)
    random_y = randint(0, HEIGHT - 100)
    apples.append(pygame.Rect(random_x, random_y, 20, 20))

# basket to hold the apples
basket = pygame.Rect(WIDTH - 110, HEIGHT - 60, 100, 50)

# These track if/which apple we've got in hand
holding_apple = False
current_apple = None

while True:
    pos = None  # Initialize pos to None
    for event in pygame.event.get():
        # this allows you to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            for apple in apples:
                if apple.collidepoint(pos):  # This method checks whether two rectangles are overlapping
                    if not holding_apple:
                        holding_apple = True
                        current_apple = apple

    displaysurface.fill(BACKGROUND_COLOR)
    # These draw our surface on screen


    for apple in apples:
        pygame.draw.circle(displaysurface, APPLE_COLOR, apple.center, apple.width)

    pygame.draw.rect(displaysurface, BASKET_COLOR, basket)

    if holding_apple and current_apple is not None:
        current_apple.center = pygame.mouse.get_pos()

    # update surface and move forward clock
    pygame.display.update()
    FramePerSec.tick(FPS)