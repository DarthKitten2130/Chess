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
    def __init__(self, x, y, color, type):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.image = pg.image.load(f"images/{color}/{color}_{type}.png")
        self.rect = pg.Rect(x * Tile.tilesize, y * Tile.tilesize, Tile.tilesize, Tile.tilesize)
        self.movable_tiles = []
        self.moved = False

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
        lst = []
        for i in range(self.x-1,self.x+2):
            for j in range(self.y-1,self.y+2):
                if 0 <= i <= 7 and 0 <= j <= 7 and i != self.x and j != self.y:
                    if chess_grid[i][j] and chess_grid[i][j].color != self.color:
                            lst.append([i,j])
                    else:
                        lst.append([i,j])
        self.movable_tiles = lst

    def castle(self,target,chess_grid):
        pass

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "rook")

    def castle(self,target,chess_grid):
        pass

    def legal_move(self,chess_grid):
        lst = []
        for i in range(self.y,8):
            if chess_grid[i][self.y]:
                if chess_grid[i][self.y].color != self.color:
                    lst.append([i,self.y])
                break
            else:
                lst.append([i,self.y])

        for i in range(self.y,0,-1):
            if chess_grid[i][self.y]:
                if chess_grid[i][self.y].color != self.color:
                    lst.append([i, self.y])
                break
            else:
                lst.append([i,self.y])

        for j in range(self.x,8):
            if chess_grid[self.x][j]:
                if chess_grid[self.x][j].color != self.color:
                    lst.append([self.x,j])
                break
            else:
                lst.append([self.x,j])

        for j in range(self.x,0,-1):
            if chess_grid[self.x][j]:
                if chess_grid[self.x][j].color != self.color:
                    lst.append([self.x,j])
                break
            else:
                lst.append([self.x,j])

        self.movable_tiles = lst

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "bishop")

    def legal_move(self,chess_grid):
        lst = []
        for i in range(8):
            if 0 <= self.x+i <= 7 and 0 <= self.y+i <= 7 and i != self.x and i != self.y:
                if chess_grid[self.x+i][self.y+i]:
                    if chess_grid[self.x+i][self.y+i].color != self.color:
                        lst.append([self.x+i,self.y+i])
                    break
                else:
                    lst.append([self.x+i,self.y+i])

        for i in range(8):
            if 0 <= self.x-i <= 7 and 0 <= self.y-i <= 7 and i != self.x and i != self.y:
                if chess_grid[self.x-i][self.y-i]:
                    if chess_grid[self.x-i][self.y-i].color != self.color:
                        lst.append([self.x-i,self.y-i])
                    break
                else:
                    lst.append([self.x-i,self.y-i])

        for i in range(8):
            if 0 <= self.x+i <= 7 and 0 <= self.y-i <= 7 and i != self.x and i != self.y:
                if chess_grid[self.x+i][self.y-i]:
                    if chess_grid[self.x+i][self.y-i].color != self.color:
                        lst.append([self.x+i,self.y-i])
                    break
                else:
                    lst.append([self.x+i,self.y-i])

        for i in range(8):
            if 0 <= self.x-i <= 7 and 0 <= self.y+i <= 7 and i != self.x and i != self.y:
                if chess_grid[self.x-i][self.y+i]:
                    if chess_grid[self.x-i][self.y+i].color != self.color:
                        lst.append([self.x-i,self.y+i])
                    break
                else:
                    lst.append([self.x-i,self.y+i])

        self.movable_tiles = lst

class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "queen")

    def legal_move(self,chess_grid):
        lst = []
        b = Bishop(self.x,self.y,self.color)
        r = Rook(self.x,self.y,self.color)
        b.legal_move(chess_grid)
        r.legal_move(chess_grid)
        self.movable_tiles = b.movable_tiles + r.movable_tiles

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "knight")

    def legal_move(self,chess_grid):
        lst = []
        for i in range(-2,3):
            for j in range(-2,3):
                if abs(i) + abs(j) == 3:
                    if 0 <= self.x+i <= 7 and 0 <= self.y+j <= 7 and self.x != i and self.y != j:
                        if chess_grid[self.x+i][self.y+j]:
                            if chess_grid[self.x+i][self.y+j].color != self.color:
                                lst.append([self.x+i,self.y+j])
                        else:
                            lst.append([self.x+i,self.y+j])
        self.movable_tiles = lst

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "pawn")

    def legal_move(self,chess_grid):
        lst = []
        if not self.moved:
            if self.color == 'white':
                if not chess_grid[self.x][self.y-1]:
                    lst.append([self.x,self.y-1])
                if not chess_grid[self.x][self.y-2]:
                    lst.append([self.x,self.y-2])
            else:
                if not chess_grid[self.x][self.y+1]:
                    lst.append([self.x,self.y+1])
                if not chess_grid[self.x][self.y+2]:
                    lst.append([self.x,self.y+2])
        else:
            if self.color == 'white':
                if not chess_grid[self.x][self.y+1]:
                    lst.append([self.x,self.y+1])
            else:
                if not chess_grid[self.x][self.y-1]:
                    lst.append([self.x,self.y-1])

        if self.color == 'white':
            if chess_grid[self.x+1][self.y+1] and chess_grid[self.x+1][self.y+1].color != self.color:
                lst.append([self.x+1,self.y+1])
            if chess_grid[self.x-1][self.y+1] and chess_grid[self.x-1][self.y+1].color != self.color:
                lst.append([self.x-1,self.y+1])
        else:
            if chess_grid[self.x+1][self.y-1] and chess_grid[self.x+1][self.y-1].color != self.color:
                lst.append([self.x+1,self.y-1])
            if chess_grid[self.x-1][self.y-1] and chess_grid[self.x-1][self.y-1].color != self.color:
                lst.append([self.x-1,self.y-1])

        self.movable_tiles = lst

    def promote(self,live_pieces,piece):
        live_pieces.remove(self)
        live_pieces.add(piece.capitalize()(self,self.x,self.y,self.color))