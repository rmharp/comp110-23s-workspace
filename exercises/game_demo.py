import pygame
import sys
from random import randint

#
pygame.init()
#Constant to define window size and set FPS
HEIGHT = 450
WIDTH = 800
FPS = 60
BACKGROUND_COLOR = [53,130,27]
BASKET_COLOR = [189,136,66]
APPLE_COLOR = [27,130,50]

apples: list[pygame.Rect] = []

# apples with randomized locations to list
for i in range(1,10):
    random_x: int = randint(0,WIDTH - 100)
    random_y: int = randint()

basket: pygame.Rect() = pygame.Rect(WIDTH-110, HEIGHT - 60, 100, 50)
#Creates clock object to limit FPS
FramePerSec = pygame.time.Clock()

#Create surface to throw objects on
displaysurface = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Game")

holding_apples: bool = False

while True:

    for event in pygame.event,get():
        #This allows you to close the window
        if event.type == pygame.QUIT():
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos  = pygame.mouse.get_pos()
            if(apple.collidepoint(pos)): # this method checks whether a point is inside the rectangle
                holding_apple = not holding_apple
                current_apple = apple
        
    if holding_apple:
        pos = pygame.mouse.get_pos()
        if(pos.y(1) <= HEIGHT-50):
            apple.center = pygame.mouse.get_pos()
        if(current_apple.colliderect[basket]): #this checks whether the two rectangles are overlapping
            holding_apple = False
            apples_in_basket += 1
            current_apples,centery = current_apples. 



    pygame.draw.circle(displaysurface,(displaysurface,APPLE_COLOR,apple.center,apple.width/2))
    pygane.draw.rect(displaysurface,)
    displaysurface.fill(BACKGROUND_COLOR)
    pygame.display.update()
    FramePerSec.tick(FPS)