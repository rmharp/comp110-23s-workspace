"""Holds Sprites that act as chess pieces"""

import math
import random

import pygame
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP, RLEACCEL

from chess_constants import *


class Bishop(pygame.sprite.Sprite):
    """Generates the Bishop Piece"""

    cur_x: int 
    cur_y: int 
    color: bool 
    
    def __init__(self, color: bool, first: bool) -> None:
        # Super class initialization of the bishop sprite
        super(Bishop, self).__init__()
        self.color = color 

        #Set bishop image, convert, and set surface equal to it
        if color and first: # top left bishop (top left black)
            self.surf = pygame.image.load(B_BISHOP_IMG).convert() 
            self.rect = self.surf.get_rect(center = C8) #c8 orig
        elif color: # Top right bishop (top right black)
            self.surf = pygame.image.load(B_BISHOP_IMG).convert() 
            self.rect = self.surf.get_rect(center = F8) #f8 orig
        elif first: # bottom right white
            self.surf = pygame.image.load(W_BISHOP_IMG).convert()
            self.rect = self.surf.get_rect(center = F1) #f1 orig
        else: #Bottom left white
            self.surf = pygame.image.load(W_BISHOP_IMG).convert()
            self.rect = self.surf.get_rect(center = C1) #c1 orig
       

class King(pygame.sprite.Sprite):
    """Generates the King Piece"""

    cur_x: int
    cur_y: int
    
    def __init__(self, color: bool) -> None:
        #Super class initialization of the King Sprite
        super(King, self).__init__()

        #Set king image, convert, and set surface equal to it

        if color:
            self.surf = pygame.image.load(B_KING_IMG).convert()
            self.rect = self.surf.get_rect(center = E8)
        else:
            self.surf = pygame.image.load(W_KING_IMG).convert()
            self.rect = self.surf.get_rect(center = E1)


class Knight(pygame.sprite.Sprite):
    """Generates the Knight Piece"""

    cur_x: int 
    cur_y: int 
    
    def __init__(self, color: bool, first: bool) -> None:
        # Super class initialization of the Kight sprite
        super(Knight, self).__init__()

        #Set Knight image, convert, and set surface equal to it
        if color and first: # top left Knight (top left black)
            self.surf = pygame.image.load(B_KNIGHT_IMG).convert() 
            self.rect = self.surf.get_rect(center = B8) 
        elif color: # Top right Knight (top right black)
            self.surf = pygame.image.load(B_KNIGHT_IMG).convert() 
            self.rect = self.surf.get_rect(center = G8) 
        elif first: # bottom right white
            self.surf = pygame.image.load(W_KNIGHT_IMG).convert()
            self.rect = self.surf.get_rect(center = G1)
        else: #Bottom left white
            self.surf = pygame.image.load(W_KNIGHT_IMG).convert()
            self.rect = self.surf.get_rect(center = B1)
       


class Pawn(pygame.sprite.Sprite):
    """Generates the Pawn Piece"""

    cur_x: int
    cur_y: int

    def __init__(self, color: bool, tag: tuple) -> None:
        #Super class initialization of the Pawn Sprite
        super(Pawn, self).__init__()

        # set pawn image, convert, and set surface equal to it
        if color:
            self.surf = pygame.image.load(B_PAWN_IMG).convert()
            self.rect = self.surf.get_rect(center = tag)
        else:
            self.surf = pygame.image.load(W_PAWN_IMG).convert()
            self.rect = self.surf.get_rect(center = tag)
    


class Queen(pygame.sprite.Sprite):
    """Generates the Queen Piece"""

    cur_x: int
    cur_y: int

    def __init__(self, color: bool) -> None:
        # Super class initializing of Queen sprite
        super(Queen, self).__init__()

        #set queen image, convert, and set surface equal to it
        if color:
            self.surf = pygame.image.load(B_QUEEN_IMG).convert()
            self.rect = self.surf.get_rect(center = D8)
        else:
            self.surf = pygame.image.load(W_QUEEN_IMG).convert()
            self.rect = self.surf.get_rect(center = D1)



class Rook(pygame.sprite.Sprite):
    """Generates the Rook Piece"""

    cur_x: int
    cur_y: int

    def __init__(self, color: bool, first: bool) -> None:
        # Super class initialization of the rook sprite
        super(Rook, self).__init__()

        #Set rook image, convert, and set surface equal to it
        if color and first: # top left rook (top left black)
            self.surf = pygame.image.load(B_ROOK_IMG).convert() 
            self.rect = self.surf.get_rect(center = A8) #c8 orig
        elif color: # Top right bishop (top right black)
            self.surf = pygame.image.load(B_ROOK_IMG).convert() 
            self.rect = self.surf.get_rect(center = H8) #f8 orig
        elif first: # bottom right white
            self.surf = pygame.image.load(W_ROOK_IMG).convert()
            self.rect = self.surf.get_rect(center = H1) #f1 orig
        else: #Bottom left white
            self.surf = pygame.image.load(W_ROOK_IMG).convert()
            self.rect = self.surf.get_rect(center = A1) #c1 orig