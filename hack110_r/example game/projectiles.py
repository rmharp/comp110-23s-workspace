from __future__ import annotations
import pygame
from typing import Optional

# ship : pygame.Rect = pygame.Rect(600, 20, 50, 50)
# ship.x = pygame.mouse.get_pos()[0] - 25
# ship.y = pygame.mouse.get_pos()[1] - 25


class Bullet:
        x: int
        y: int
        radius: int
        speed: float
        vector: list[float]
        goodbad: int
   

        def __init__(self, x_pos: int, y_pos: int, radius: int, speed: float, goodbad: int, vector: list[float] = [0,1]):
                self.x = x_pos
                self.y = y_pos
                self.radius = radius
                self.speed = speed
                self.vector = vector
                self.goodbad = goodbad
                


        def move(self):
                self.x += (self.vector[0] * self.speed)
                self.y += (self.vector[1] * self.speed)

        
        def getBul(self) -> pygame.Rect:
                return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 3, self.radius * 3)

        # def getRect(self, obj = None):
        #         rect: pygame.Rect = self.getRect()

        def fire_hit(self, rect: Bullet, rect2: pygame.Rect):
                if astList.__contains__(rect2) and rect2.colliderect(rect):
                        return True

        def astLoop(self):
                for stroid in ast:
                        rect2: pygame.Rect = stroid.getRect()
                        for ject in blt:
                                rect: pygame.Rect = ject.getRect()
                                if ject.fire_hit(ject, stroid):
                                        return ast.remove(stroid)


        


               

class Asteroid:
        x: int
        y: int
        radius: int
        speed: float
        vector: list[float]

        def __init__(self, x_pos: int, y_pos: int, radius: int, speed: float, goodbad: int, vector: list[float] = [0,1]):
                self.x = x_pos
                self.y = y_pos
                self.radius = radius
                self.speed = speed
                self.vector = vector
                


        def move(self):
                self.x += (self.vector[0] * self.speed)
                self.y += (self.vector[1] * self.speed)


        def getAst(self) -> pygame.Rect:
                return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 3, self.radius * 3)

        
        


        
blt: list[Bullet] = list()  # Bullet(randint(0, 600), randint(0, 600), 10, 10)
ast: list[Asteroid] = list()
astList: list[pygame.Rect] = list()
bltList: list[pygame.Rect] = list()