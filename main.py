import pygame as pg
from classes import *

turn = 'white'
def board_init(screen,grid):
    tilesize = Tile.tilesize
    for x in range(8):
        for y in range(8):
            rect = Tile(x,y)

            if (x+y) % 2 == 0:
                pg.draw.rect(screen, (255, 255, 255),rect)
            elif (x+y) % 2 == 1:
                pg.draw.rect(screen, (51, 102, 0), rect)
            grid[x][y] = rect

def play_turn(screen,grid):
    global turn
    ltd = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7'}

    print(f"Turn: {turn}\n")
    move = input("Enter your move: ").split()

    try:
        start_square = ltd[move[0][0].lower()] + move[0][1]
        final_square = ltd[move[1][0].lower()] + move[1][1]
    except KeyError:
         print("invalidInput")
    else:
        try:
            piece = grid[int(start_square[0])][int(start_square[1])]
        except KeyError:
            piece = None
        try:
            piece_2 = grid[int(final_square[0])][int(final_square[1])]
        except KeyError:
            piece_2 = None
        if len(move) != 2 or int(start_square) > 77 or int(final_square) > 77:
           print("You have to enter two valid coordinates")

        elif piece is None:
            print("No piece on that square")
        elif piece_2 is not None:
            if piece_2.color == turn:
                print("You can't take your own piece!")
            elif piece_2.type == "king":
                print("You can't take the king!")

        elif piece.color != turn:
            print("That is not your piece!")

        else:
            if piece_2 is not None and piece_2.type != "king":
                piece_2.kill()
            piece.x = int(final_square[0])
            piece.y = int(final_square[1])
            turn = "white" if turn == "black" else "black"

    


def main():
    pg.init()
    global turn
    screen = pg.display.set_mode((2460, 1600))
    chess_grid = [{},{},{},{},{},{},{},{}]
    board_grid = [{},{},{},{},{},{},{},{}]
    board = pg.sprite.Group()
    live_pieces = pg.sprite.Group()
    dead_pieces = pg.sprite.Group()
    live_pieces.add(
         Rook(7, 0, "black"),
         Rook(0, 0, "black"),
         Knight(6, 0, "black"),
         Knight(1, 0, "black"),
         Bishop(2, 0, "black"),
         Bishop(5, 0, "black"),
         Queen(3, 0, "black"),
         King(4, 0, "black"),
         Pawn(0, 1, "black"),
         Pawn(1, 1, "black"),
         Pawn(2, 1, "black"),
         Pawn(3, 1, "black"),
         Pawn(4, 1, "black"),
         Pawn(5, 1, "black"),
         Pawn(6, 1, "black"),
         Pawn(7, 1, "black"),
         Rook(0, 7, "white"),
         Rook(7, 7, "white"),
         Knight(1, 7, "white"),
         Knight(6, 7, "white"),
         Bishop(2, 7, "white"),
         Bishop(5, 7, "white"),
         Queen(3, 7, "white"),
         King(4, 7, "white"),
         Pawn(0, 6, "white"),
         Pawn(1, 6, "white"),
         Pawn(2, 6, "white"),
         Pawn(3, 6, "white"),
         Pawn(4, 6, "white"),
         Pawn(5, 6, "white"),
         Pawn(6, 6, "white"),
         Pawn(7, 6, "white")
    )

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.fill((153, 102, 0))
        board_init(screen,board_grid)
        for piece in live_pieces:
            chess_grid[piece.x][piece.y] = piece
        live_pieces.draw(screen)
        play_turn(screen,chess_grid)
        pg.display.flip()

if __name__ == '__main__':
    main()