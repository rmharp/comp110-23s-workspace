import pygame
import sys
from math import sqrt
from constants import * 
from projectile import Projectile
# starts window
pygame.init()
# creates clock object to limit FPS 
FramePerSec = pygame.time.Clock()

# create surface to draw objects on
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

proj: Projectile = Projectile()
power_start: tuple[int] = None

def draw_power_line():
    global power_start
    if(power_start):
        pos = pygame.mouse.get_pos()
        pygame.draw.line(displaysurface, (255, 0, 0), (proj.x,proj.y), 
                         (proj.x+(pos[0]-power_start[0]),proj.y+(pos[1]-power_start[1])), 2)

def draw_setting(): 
    displaysurface.fill((150,150,230))
    pygame.draw.rect(displaysurface, LAUNCHER_COLOR, TEE)
    pygame.draw.rect(displaysurface, GOAL_COLOR, GOAL)
    pygame.draw.rect(displaysurface, WALL_COLOR, WALL_FACADE)

while True:
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        # this allows you to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            power_start = pos
        elif event.type == pygame.MOUSEBUTTONUP:
            proj.shot(pos, power_start)
            power_start = None

    draw_setting()
    draw_power_line()

    proj.update_ball(displaysurface)
    proj.collide_with_surface({"top": WALL_TOP, "base":WALL})
    if(proj.check_goal_hits()):
        proj = Projectile()

    pygame.display.update()
    FramePerSec.tick(FPS)