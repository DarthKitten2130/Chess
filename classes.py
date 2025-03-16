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

    def copy(self):
        new_piece = self.__class__(self.x, self.y, self.color)
        new_piece.moved = self.moved
        return new_piece

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

    def legal_move(self, chess_grid):
        lst = set()
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if 0 <= i <= 7 and 0 <= j <= 7 and (i, j) != (self.x, self.y):
                    if chess_grid[i][j] and chess_grid[i][j].color != self.color:
                        lst.add((i, j))
                    elif not chess_grid[i][j]:
                        lst.add((i, j))
        self.movable_tiles = lst

    def castle(self, target, chess_grid):
        if self.moved or target.moved:
            return

        if self.color == "white":
            row = 7
        else:
            row = 0

        if target.x == 7:
            path = [5, 6]
            king_new_pos, rook_new_pos = (6, row), (5, row)
        elif target.x == 0:
            path = [1, 2, 3]
            king_new_pos, rook_new_pos = (2, row), (3, row)
        else:
            return

        for x in path:
            if chess_grid[x][row]:
                return

        chess_grid[self.x][self.y] = None
        chess_grid[target.x][target.y] = None
        self.x, self.y = king_new_pos
        target.x, target.y = rook_new_pos
        self.rect.topleft = (king_new_pos[0] * Tile.tilesize, king_new_pos[1] * Tile.tilesize)
        target.rect.topleft = (target.x * Tile.tilesize, target.y * Tile.tilesize)
        chess_grid[self.x][self.y] = self
        chess_grid[target.x][target.y] = target


class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "rook")

    def castle(self, target, chess_grid):
        if self.moved or target.moved:
            return

        if self.color == "white":
            row = 7
        else:
            row = 0

        if self.x == 7:
            path = [5, 6]
            king_new_pos, rook_new_pos = (6, row), (5, row)
        elif self.x == 0:
            path = [1, 2, 3]
            king_new_pos, rook_new_pos = (2, row), (3, row)
        else:
            return

        for x in path:
            if chess_grid[x][row]:
                return

        chess_grid[self.x][self.y] = None
        chess_grid[target.x][target.y] = None
        self.x, self.y = rook_new_pos
        target.x, target.y = king_new_pos
        self.rect.topleft = (rook_new_pos[0] * Tile.tilesize, rook_new_pos[1] * Tile.tilesize)
        target.rect.topleft =  (target.x * Tile.tilesize, target.y * Tile.tilesize)
        chess_grid[self.x][self.y] = self
        chess_grid[target.x][target.y] = target

    def legal_move(self,chess_grid):
        lst = set()
        for i in range(self.x+1,8):
            if chess_grid[i][self.y]:
                if chess_grid[i][self.y].color != self.color:
                    lst.add((i,self.y))
                break
            else:
                lst.add((i,self.y))

        for i in range(self.x-1,-1,-1):
            if chess_grid[i][self.y]:
                if chess_grid[i][self.y].color != self.color:
                    lst.add((i, self.y))
                break
            else:
                lst.add((i,self.y))

        for j in range(self.y+1,8):
            if chess_grid[self.x][j]:
                if chess_grid[self.x][j].color != self.color:
                    lst.add((self.x,j))
                break
            else:
                lst.add((self.x,j))

        for j in range(self.y-1,-1,-1):
            if chess_grid[self.x][j]:
                if chess_grid[self.x][j].color != self.color:
                    lst.add((self.x,j))
                break
            else:
                lst.add((self.x,j))

        self.movable_tiles = lst

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "bishop")

    def legal_move(self, chess_grid):
        lst = set()
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in directions:
            i, j = self.x + dx, self.y + dy
            while 0 <= i <= 7 and 0 <= j <= 7:
                if chess_grid[i][j]:
                    if chess_grid[i][j].color != self.color:
                        lst.add((i, j))
                    break
                else:
                    lst.add((i, j))
                i += dx
                j += dy
        self.movable_tiles = lst

class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "queen")

    def legal_move(self,chess_grid):
        lst = set()
        b = Bishop(self.x,self.y,self.color)
        r = Rook(self.x,self.y,self.color)
        b.legal_move(chess_grid)
        r.legal_move(chess_grid)
        self.movable_tiles = b.movable_tiles | r.movable_tiles

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "knight")

    def legal_move(self,chess_grid):
        lst = set()
        for i in range(-2,3):
            for j in range(-2,3):
                if abs(i) + abs(j) == 3:
                    if 0 <= self.x+i <= 7 and 0 <= self.y+j <= 7:
                        if chess_grid[self.x+i][self.y+j] and chess_grid[self.x+i][self.y+j].color != self.color:
                            lst.add((self.x+i,self.y+j))

                        lst.add((self.x+i,self.y+j))
        self.movable_tiles = lst

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, "pawn")

    def legal_move(self,chess_grid):
        lst = set()
        try:
            if not self.moved:
                if self.color == 'white':
                    if not chess_grid[self.x][self.y-1]:
                        lst.add((self.x,self.y-1))
                    if not chess_grid[self.x][self.y-2]:
                        lst.add((self.x,self.y-2))
                else:
                    if not chess_grid[self.x][self.y+1]:
                        lst.add((self.x,self.y+1))
                    if not chess_grid[self.x][self.y+2]:
                        lst.add((self.x,self.y+2))
            else:
                if self.color == 'white':
                    if not chess_grid[self.x][self.y-1]:
                        lst.add((self.x,self.y-1))
                else:
                    if not chess_grid[self.x][self.y+1]:
                        lst.add((self.x,self.y+1))

            if self.color == 'white':
                if chess_grid[self.x+1][self.y-1] and chess_grid[self.x+1][self.y-1].color != self.color:
                    lst.add((self.x+1,self.y-1))
                if chess_grid[self.x-1][self.y-1] and chess_grid[self.x-1][self.y-1].color != self.color:
                    lst.add((self.x-1,self.y-1))
            else:
                if chess_grid[self.x+1][self.y+1] and chess_grid[self.x+1][self.y+1].color != self.color:
                    lst.add((self.x+1,self.y+1))
                if chess_grid[self.x-1][self.y+1] and chess_grid[self.x-1][self.y+1].color != self.color:
                    lst.add((self.x-1,self.y+1))
        except KeyError:
            pass
        self.movable_tiles = lst



def promote(self,board,screen,live_pieces,dead_pieces,turn):

    popup = True
    selected = None

    pieces = []
    while popup:
        promos = pg.sprite.Group()
        promos.add(
            Queen(2,3,turn),
            Bishop(3,3,turn),
            Knight(4,3,turn),
            Rook(5,3,turn))


        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                for piece in promos:
                    if piece.rect.collidepoint(mouse_pos):
                        selected = type(piece).__name__
                        popup = False
                        promos.empty()
                        break
        pieces = {"Queen":Queen,"Bishop":Bishop,"Knight":Knight,"Rook":Rook}
        screen.fill((255, 87, 51))
        promos.draw(screen)
        pg.display.flip()

    self.kill(live_pieces,dead_pieces)
    self = pieces[selected](self.x,self.y,turn)
    live_pieces.add(self)
