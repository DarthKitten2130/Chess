import pygame as pg

class Tile(pg.sprite.Sprite):
    tilesize = 180
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color = lambda x, y: (255, 255, 255) if (x + y) % 2 == 0 else (51, 102, 0)
        self.rect = pg.Rect(x * self.tilesize, y * self.tilesize, self.tilesize, self.tilesize)



class Piece(pg.sprite.Sprite):
    movable_tiles = []
    def __init__(self, x, y, color, type):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.image = pg.image.load(f"images/{color}/{color}_{type}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * 180
        self.rect.y = y * 180

    def kill(self,live_pieces,dead_pieces):
        dead_pieces.add(self)
        live_pieces.remove(self)

    def promote(self,live_pieces,piece):
        live_pieces.remove(self)
        live_pieces.add(piece.capitalize()(self,self.x,self.y,self.color))



class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "king")

    def kill(self):
        raise AttributeError("Kings cannot be killed")

    def promote(self):
        raise AttributeError("Cannot promote to a King")

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
