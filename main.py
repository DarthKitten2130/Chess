import pygame as pg
from classes import Piece

def boardInit(screen,grid):
    tileSize = 180
    letter = ['h','g','f','e','d','c','b','a']
    for x in range(8):
        for y in range(8):

            rect = pg.Rect(x * tileSize, y * tileSize, tileSize, tileSize)

            if (x+y) % 2 == 0:
                pg.draw.rect(screen, (255, 255, 255),rect)
            elif (x+y) % 2 == 1:
                pg.draw.rect(screen, (51, 102, 0), rect)
            grid[x][y] = rect


def pieceInit(screen,grid):
  
    for piece in pieces.values():
        piece.draw(screen)
        piece.Update(pg.event.get())

        grid[piece.x][piece.y] = piece





def main():
    pg.init()

    screen = pg.display.set_mode((2460, 1600))
    chessGrid = [{},{},{},{},{},{},{},{}]
    boardGrid = [{},{},{},{},{},{},{},{}]
    pieceGroup = pg.sprite.Group()
    pieceGroup.add(
         Piece(7, 0, "black", "rook",'h8'),
         Piece(0, 0, "black", "rook",'a8'),
         Piece(1, 0, "black", "knight",'b8'),
         Piece(6, 0, "black", "knight",'g8'),
         Piece(2, 0, "black", "bishop",'c8'),
         Piece(5, 0, "black", "bishop",'f8'),
         Piece(3, 0, "black", "queen",'d8'),
         Piece(4, 0, "black", "king",'e8'),
         Piece(0, 1, "black", "pawn",'a7'),
         Piece(1, 1, "black", "pawn",'b7'),
         Piece(2, 1, "black", "pawn",'c7'),
         Piece(3, 1, "black", "pawn",'d7'),
         Piece(4, 1, "black", "pawn",'e7'),
         Piece(5, 1, "black", "pawn",'f7'),
         Piece(6, 1, "black", "pawn",'g7'),
         Piece(7, 1, "black", "pawn",'h7'),
         Piece(0, 7, "white", "rook",'a1'),
         Piece(7, 7, "white", "rook",'h1'),
         Piece(1, 7, "white", "knight",'b1'),
         Piece(6, 7, "white", "knight",'g1'),
         Piece(2, 7, "white", "bishop",'c1'),
         Piece(5, 7, "white", "bishop",'f1'),
         Piece(3, 7, "white", "queen",'d1'),
         Piece(4, 7, "white", "king",'e1'),
         Piece(0, 6, "white", "pawn",'a2'),
         Piece(1, 6, "white", "pawn",'b2'),
         Piece(2, 6, "white", "pawn",'c2'),
         Piece(3, 6, "white", "pawn",'d2'),
         Piece(4, 6, "white", "pawn",'e2'),
         Piece(5, 6, "white", "pawn",'f2'),
         Piece(6, 6, "white", "pawn",'g2'),
         Piece(7, 6, "white", "pawn",'h2'))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.fill((153, 102, 0))
        boardInit(screen,boardGrid)
        pieceGroup.draw(screen)
        pg.display.flip()

if __name__ == '__main__':
    main()