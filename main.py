import pygame as pg
from classes import pieces

def boardInit(screen):
    tileSize = 180
    for x in range(8):
        for y in range(8):

            if (x+y) % 2 == 0:
                pg.draw.rect(screen, (255, 255, 255), (x * tileSize, y * tileSize, tileSize, tileSize))
            elif (x+y) % 2 == 1:
                pg.draw.rect(screen, (51, 102, 0), (x * tileSize, y * tileSize, tileSize, tileSize))


def pieceInit(screen):
  
    for piece in pieces:
        pieces[piece].draw(screen)




def main():
    pg.init()

    screen = pg.display.set_mode((2460, 1600))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.fill((153, 102, 0))
        boardInit(screen)
        pieceInit(screen)
        pg.display.flip()

if __name__ == '__main__':
    main()