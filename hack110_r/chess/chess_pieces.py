""" Generates Piece Sprite Groups"""

from chess_sprites import *

from chess_constants import *


w_pawns: list[tuple] = [A2, B2, C2, D2, E2, F2, G2, H2]
new_w_pawns: list[Pawn] = []
for pawn in w_pawns:
    new_w_pawns.append(Pawn(False, pawn))

b_pawns: list[tuple] = [A7, B7, C7, D7, E7, F7, G7, H7]
new_b_pawns: list[Pawn] = []
for pawn in b_pawns:
    new_b_pawns.append(Pawn(True, pawn))


# Individual chess pieces
b_bishop1 = Bishop(True, True)
b_bishop2 = Bishop(True, False)
w_bishop1 = Bishop(False, True)
w_bishop2 = Bishop(False, False)

b_king = King(True)
w_king = King(False)

b_queen = Queen(True)
w_queen = Queen(False)

b_knight1 = Knight(True, True)
b_knight2 = Knight(True, False)
w_knight1 = Knight (False, True)
w_knight2 = Knight(False, False)

b_rook1 = Rook (True, True)
b_rook2 = Rook (True, False)
w_rook1 = Rook (False, True)
w_rook2 = Rook (False, False)

b_pawn1 = Pawn(True, A7)
b_pawn2 = Pawn(True, B7)
b_pawn3 = Pawn(True, C7)
b_pawn4 = Pawn(True, D7)
b_pawn5 = Pawn(True, E7)
b_pawn7 = Pawn(True, F7)
b_pawn8 = Pawn(True, G7)

w_pawn1 = Pawn(False, A2)
w_pawn2 = Pawn(False, B2)
w_pawn3 = Pawn(False, C2)
w_pawn4 = Pawn(False, D2)
w_pawn5 = Pawn(False, E2)
w_pawn6 = Pawn(False, F2)
w_pawn7 = Pawn(False, G2)
w_pawn8 = Pawn(False, H2)



# Group Holding all sprites
all_sprites = pygame.sprite.Group()

all_sprites.add(b_bishop1)
all_sprites.add(b_bishop2)
all_sprites.add(w_bishop1)
all_sprites.add(w_bishop2)

all_sprites.add(b_king)
all_sprites.add(w_king)

all_sprites.add(b_queen)
all_sprites.add(w_queen)

all_sprites.add(b_knight1)
all_sprites.add(b_knight2)
all_sprites.add(w_knight1)
all_sprites.add(w_knight2)

for pawn in new_b_pawns:
    all_sprites.add(pawn)

for pawn in new_w_pawns:
    all_sprites.add(pawn)


all_sprites.add(b_rook1)
all_sprites.add(b_rook2)
all_sprites.add(w_rook1)
all_sprites.add(w_rook2)