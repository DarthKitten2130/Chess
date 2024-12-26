import pygame as pg

class Piece(pg.sprite.Sprite):
    def __init__(self, x, y, color, type):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.image = pg.image.load(f"images/{color}/{color}_{type}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * 180
        self.rect.y = y * 180

class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "king")

class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "queen")

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "bishop")

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "knight")

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "rook")

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "pawn")
