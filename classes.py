import pygame as pg

class Tile(pg.sprite.Sprite):
    tilesize = 180
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color = (255, 255, 255) if (x + y) % 2 == 0 else (51, 102, 0)
        self.rect = pg.Rect(x * self.tilesize, y * self.tilesize, self.tilesize, self.tilesize)
        self.image = pg.Surface((self.tilesize, self.tilesize))
        self.image.fill(self.color)

    def outline(self,screen):
        pg.draw.rect(screen, (0,0,255), self.rect, 5)


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

    def outline(self,screen):
        pg.draw.rect(screen, (255, 0, 0), self.rect, 5)


class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "king")

    def kill(self):
        raise AttributeError("Kings cannot be killed")

    def legal_move(self,chess_grid):
        lst = super().__getattribute__("movable_tiles")
        for i in range(self.x-1,self.x+2):
            for j in range(self.y-1,self.y+2):
                if 0 <= i <= 7 and 0 <= j <= 7 and i != self.x and j != self.y:
                    if chess_grid[i][j] and chess_grid[i][j].color != self.color:
                            lst.append([i,j])
                    else:
                        lst.append([i,j])
        return lst

    def castle(self,target,chess_grid):
        pass

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

    def castle(self,target,chess_grid):
        pass


class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "pawn")

    def promote(self,live_pieces,piece):
        live_pieces.remove(self)
        live_pieces.add(piece.capitalize()(self,self.x,self.y,self.color))