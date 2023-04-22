from constants import *
from math import sqrt

class Projectile:
    x: float = TEE.topleft[0]
    y: float = TEE.topleft[1]
    radius: int = 10
    vectorx: float = 0
    vectory: float = 0
    collided_last = False

    def move(self):
        self.x += self.vectorx
        if(self.y < FLOOR):
            self.vectory += (GRAVITY)/FPS
        self.y += self.vectory

    def at_rest(self):
        if((-0.2<=self.vectory<=0.2) and (-0.2<=self.vectorx<=0.2)):
            self.vectory=0
            self.vectorx=0
            return True
        return False

    def bounce(self):
        if(self.collided_last):
            self.collided_last = False # preventing multiple bounces before ball can rebound off surface
        else:
            if(self.x >= RIGHT_WALL or self.x < LEFT_WALL):
                self.vectorx = BOUNCE_COEFFECIENT * self.vectorx
                self.collided_last = True
            if(self.y >= FLOOR):
                self.collided_last = True
                self.vectory = BOUNCE_COEFFECIENT * self.vectory
                self.vectorx = self.vectorx * FLOOR_FRICTION


    def shot(self,pos: tuple[int], power_start: tuple[int]):
            if(self.y>=FLOOR-self.radius):
                c_2: float = sqrt(((pos[0] - self.x)**2)+((pos[1]-self.y)**2))
                power: float = sqrt(((power_start[0] - pos[0])**2)+((power_start[1]-pos[1])**2))

                if(power>20):
                    power = 20
                print(power)

                self.vectorx=(pos[0]-power_start[0])/c_2 *(power)
                self.vectory=(pos[1]-power_start[1])/c_2 *(power)
                self.x += self.vectorx
                self.y += self.vectory

            print(f"VECTORX: {self.vectorx}, VECTORY: {self.vectory}")

    def check_goal_hits(self) -> bool:
        if(GOAL.collidepoint(self.x, self.y)):
                print("NICE SHOT!")
                return True
        return False

    def update_ball(self, surface: pygame.Surface):
        if(not self.at_rest()):
            self.bounce()
        self.move()
        pygame.draw.circle(surface, PROJ_COLOR, (self.x, self.y), self.radius)

    def collide_with_surface(self, object: dict[str:pygame.Rect]):
        if(object["top"].colliderect(pygame.Rect(self.x-self.radius,self.y-self.radius, self.radius*2, self.radius*2))):
            if(self.vectory > 0):
                self.y -=1
            else:
                self.y +=1
            self.vectory *= -1
            
        if(object["base"].colliderect(pygame.Rect(self.x-self.radius,self.y-self.radius, self.radius*2, self.radius*2))):
            if(self.vectorx > 0):
                self.x -=1
            else:
                self.x +=1
            self.vectorx *= -1