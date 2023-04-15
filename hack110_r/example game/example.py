import pygame
from projectiles import Bullet, Asteroid, blt, ast, bltList, astList

from random import randint
import time
from typing import Union
from typing import Optional
bullet_obj: Optional[Bullet] = None


pygame.init()


screen = pygame.display.set_mode([800, 600])
background = pygame.image.load('HACK110/Assets/background1.png')

clock = pygame.time.Clock()
running = True

ship : pygame.Rect = pygame.Rect(600, 20, 50, 50)

# blt: list[Bullet] = list()  # Bullet(randint(0, 600), randint(0, 600), 10, 10)
# ast: list[Asteroid] = list()



start = time.time()



ship : pygame.Rect = pygame.Rect(600, 20, 50, 50)

###Riley: change file image location
shipimg = pygame.image.load('HACK110/Assets/spaceship.png')
playerx = ship.x
playery = ship.y

def player():
    screen.blit(shipimg, (playerx, playery))

# hearts and their locations
h1 = pygame.image.load('HACK110/Assets/heart.png')
h2 = h1
h3 = h1
lives: int = 3
bullet: list[pygame.Rect] = list()
hearts: list = [1, 1, 1]

# blt: list[Bullet] = list()  # Bullet(randint(0, 600), randint(0, 600), 10, 10)
# ast: list[Asteroid] = list()
# rect: pygame.Rect = blt.getRect()
while running:
    clock.tick(60)

    screen.fill((120, 200, 255))

    screen.blit(background, (0, 0))

    if len(hearts) >= 1:
        screen.blit(h1, (50, 550))
    if len(hearts) >= 2:
        screen.blit(h2, (100, 550))
    if len(hearts) >= 3:
        screen.blit(h3, (150, 550))

    player()
   
    ship.x = pygame.mouse.get_pos()[0] - 25
    ship.y = pygame.mouse.get_pos()[1] - 25
    playerx = ship.x
    playery = ship.y
    
    

    for item in ast:
        # rect = item.getAst()
        rect2 = item.getAst()
        astList.append(rect2)
        rect_goodbad: bool = False
        rect2_goodbad: bool = False
        if item.vector[1] == -1:
            pygame.draw.rect(screen, (0, 0, 0), rect)
            rect_goodbad = False
        else:
            pygame.draw.rect(screen, (255, 255, 255), rect2)
            rect2_goodbad = True
        item.move()

        



    for item in blt:
        rect = item.getBul()
        bltList.append(rect)
        # rect2: pygame.Rect = item.getBul()
        rect_goodbad: bool = False
        rect2_goodbad: bool = False
        if item.vector[1] == -1:
            pygame.draw.rect(screen, (0, 0, 0), rect)
            rect_goodbad = False
        else:
            pygame.draw.rect(screen, (255, 255, 255), rect2)
            rect2_goodbad = True

        # item.astLoop()



        # fire_hit: bool = (rect2.colliderect(rect)) and (not (rect2_goodbad == rect_goodbad))
        ship_hit: bool = (rect.colliderect(ship)) and (not (rect2_goodbad == rect_goodbad))

        
        if item.fire_hit(rect, rect2):
            blt.remove(item)
        if ship_hit:
            ast.remove(item)
            lives -= 1
            hearts.pop()
            # if lives == 2:
            #     h3 = ""
            # elif lives == 1: 
            #     h2 = ""
            # elif lives == 0:
            #     h1 = ""
            
        if lives == 0: 
            running = False


        item.move()




    ticks: list[int] = list()
    ticks.append(pygame.time.get_ticks())
    for event in pygame.event.get():
        fired: bool = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # bullet_obj = Bullet(ship.x, ship.y - 25, 10, 10, 1, [0, -1])
                blt.append(Bullet(ship.x, ship.y - 25, 10, 10, 1, [0, -1]))
                # for i in range(0, len(blt)):
                #     bullet.append(pygame.Rect(blt[i].x, blt[i].y, 50, 50))
                
                fired = True
        

        if event.type == pygame.QUIT:
            running = False
    for tick in ticks:
            if tick % 11 == 0:
                ast.append(Asteroid(randint(0, 800), 1, 5, 7, 0, [0, 1]))

    pygame.display.flip()
        

end = time.time()
print(f"score: {end - start}")

pygame.quit()