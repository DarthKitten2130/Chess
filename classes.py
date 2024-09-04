import pygame as pg

class Piece(pg.sprite.Sprite):
    def __init__(self, x, y, color, type,pos):
        self.x = x
        self.y = y
        self.color = color
        self.image = pg.image.load(f"images/{color}/{color}_{type}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * 180
        self.rect.y = y * 180

    def draw(self, screen):
        screen.blit(self.image, self.rect)

pieces = {
        "brook1": Piece(0, 0, "black", "rook",'a8'),
        "brook2": Piece(7, 0, "black", "rook",'h8'),
        "bknight1": Piece(1, 0, "black", "knight",'b8'),
        "bknight2": Piece(6, 0, "black", "knight",'g8'),
        "bbishop1": Piece(2, 0, "black", "bishop",'c8'),
        "bbishop2": Piece(5, 0, "black", "bishop",'f8'),
        "bqueen": Piece(3, 0, "black", "queen",'d8'),
        "bking": Piece(4, 0, "black", "king",'e8'),
        "bpawn1": Piece(0, 1, "black", "pawn",'a7'),
        "bpawn2": Piece(1, 1, "black", "pawn",'b7'),
        "bpawn3": Piece(2, 1, "black", "pawn",'c7'),
        "bpawn4": Piece(3, 1, "black", "pawn"'d7'),
        "bpawn5": Piece(4, 1, "black", "pawn",'e7'),
        "bpawn6": Piece(5, 1, "black", "pawn",'f7'),
        "bpawn7": Piece(6, 1, "black", "pawn",'g7'),
        "bpawn8": Piece(7, 1, "black", "pawn",'h7'),
        "wrook1": Piece(0, 7, "white", "rook",'a1'),
        "wrook2": Piece(7, 7, "white", "rook",'h1'),
        "wknight1": Piece(1, 7, "white", "knight",'b1'),
        "wknight2": Piece(6, 7, "white", "knight",'g1'),
        "wbishop1": Piece(2, 7, "white", "bishop",'c1'),
        "wbishop2": Piece(5, 7, "white", "bishop",'f1'),
        "wqueen": Piece(3, 7, "white", "queen",'d1'),
        "wking": Piece(4, 7, "white", "king",'e1'),
        "wpawn1": Piece(0, 6, "white", "pawn",'a2'),
        "wpawn2": Piece(1, 6, "white", "pawn",'b2'),
        "wpawn3": Piece(2, 6, "white", "pawn",'c2'),
        "wpawn4": Piece(3, 6, "white", "pawn",'d2'),
        "wpawn5": Piece(4, 6, "white", "pawn",'e2'),
        "wpawn6": Piece(5, 6, "white", "pawn",'f2'),
        "wpawn7": Piece(6, 6, "white", "pawn",'g2'),
        "wpawn8": Piece(7, 6, "white", "pawn",'h2')
    }