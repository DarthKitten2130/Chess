import pygame as pg

class Piece(pg.sprite.Sprite):
    def __init__(self, x, y, color, type):
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
        "brook1": Piece(0, 0, "black", "rook"),
        "brook2": Piece(7, 0, "black", "rook"),
        "bknight1": Piece(1, 0, "black", "knight"),
        "bknight2": Piece(6, 0, "black", "knight"),
        "bbishop1": Piece(2, 0, "black", "bishop"),
        "bbishop2": Piece(5, 0, "black", "bishop"),
        "bqueen": Piece(3, 0, "black", "queen"),
        "bking": Piece(4, 0, "black", "king"),
        "bpawn1": Piece(0, 1, "black", "pawn"),
        "bpawn2": Piece(1, 1, "black", "pawn"),
        "bpawn3": Piece(2, 1, "black", "pawn"),
        "bpawn4": Piece(3, 1, "black", "pawn"),
        "bpawn5": Piece(4, 1, "black", "pawn"),
        "bpawn6": Piece(5, 1, "black", "pawn"),
        "bpawn7": Piece(6, 1, "black", "pawn"),
        "bpawn8": Piece(7, 1, "black", "pawn"),
        "wrook1": Piece(0, 7, "white", "rook"),
        "wrook2": Piece(7, 7, "white", "rook"),
        "wknight1": Piece(1, 7, "white", "knight"),
        "wknight2": Piece(6, 7, "white", "knight"),
        "wbishop1": Piece(2, 7, "white", "bishop"),
        "wbishop2": Piece(5, 7, "white", "bishop"),
        "wqueen": Piece(3, 7, "white", "queen"),
        "wking": Piece(4, 7, "white", "king"),
        "wpawn1": Piece(0, 6, "white", "pawn"),
        "wpawn2": Piece(1, 6, "white", "pawn"),
        "wpawn3": Piece(2, 6, "white", "pawn"),
        "wpawn4": Piece(3, 6, "white", "pawn"),
        "wpawn5": Piece(4, 6, "white", "pawn"),
        "wpawn6": Piece(5, 6, "white", "pawn"),
        "wpawn7": Piece(6, 6, "white", "pawn"),
        "wpawn8": Piece(7, 6, "white", "pawn")
    }