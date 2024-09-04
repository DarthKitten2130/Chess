import pygame as pg
from classes import pieces

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

            grid[letter[x]].append([rect])


def pieceInit(screen,grid):
  
    for piece in pieces:
        pieces[piece].draw(screen)
        grid[piece.pos[0]]





def main():
    pg.init()

    screen = pg.display.set_mode((2460, 1600))
    grid = {'h':[],'g':[],'f':[],'e':[],'d':[],'c':[],'b':[],'a':[]}

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.fill((153, 102, 0))
        boardInit(screen,grid)
        pieceInit(screen)
        pg.display.flip()

if __name__ == '__main__':
    main()