import pygame as pg
from classes import Piece

def board_init(screen,grid):
    tilesize = 180
    for x in range(8):
        for y in range(8):

            rect = pg.Rect(x * tilesize, y * tilesize, tilesize, tilesize)

            if (x+y) % 2 == 0:
                pg.draw.rect(screen, (255, 255, 255),rect)
            elif (x+y) % 2 == 1:
                pg.draw.rect(screen, (51, 102, 0), rect)
            grid[x][y] = rect

def play_turn(screen,grid):
    global turn
    ltd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

    print(f"Turn: {turn}\n")
    move = input("Enter your move: ").split()

    try:
        move[0][0] = ltd[move[0][0].lower()]
        move[1][0] = ltd[move[1][0].lower()]
        start_square = move[0]
        final_square = move[1]
    except KeyError:
         print("invalidInput")
    else:
        piece = grid[int(start_square[0])][int(start_square[1])]
        piece_2 = grid[int(final_square[0])][int(final_square[1])]
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

    


def main():
    pg.init()

    screen = pg.display.set_mode((2460, 1600))
    chess_grid = [{},{},{},{},{},{},{},{}]
    board_grid = [{},{},{},{},{},{},{},{}]
    turn = 'white'
    pieceGroup = pg.sprite.Group()
    pieceGroup.add(
         Piece(7, 0, "black", "rook"),
         Piece(0, 0, "black", "rook"),
         Piece(6, 0, "black", "knight"),
         Piece(1, 0, "black", "knight"),
         Piece(2, 0, "black", "bishop"),
         Piece(5, 0, "black", "bishop"),
         Piece(3, 0, "black", "queen"),
         Piece(4, 0, "black", "king"),
         Piece(0, 1, "black", "pawn"),
         Piece(1, 1, "black", "pawn"),
         Piece(2, 1, "black", "pawn"),
         Piece(3, 1, "black", "pawn"),
         Piece(4, 1, "black", "pawn"),
         Piece(5, 1, "black", "pawn"),
         Piece(6, 1, "black", "pawn"),
         Piece(7, 1, "black", "pawn"),
         Piece(0, 7, "white", "rook"),
         Piece(7, 7, "white", "rook"),
         Piece(1, 7, "white", "knight"),
         Piece(6, 7, "white", "knight"),
         Piece(2, 7, "white", "bishop"),
         Piece(5, 7, "white", "bishop"),
         Piece(3, 7, "white", "queen"),
         Piece(4, 7, "white", "king"),
         Piece(0, 6, "white", "pawn"),
         Piece(1, 6, "white", "pawn"),
         Piece(2, 6, "white", "pawn"),
         Piece(3, 6, "white", "pawn"),
         Piece(4, 6, "white", "pawn"),
         Piece(5, 6, "white", "pawn"),
         Piece(6, 6, "white", "pawn"),
         Piece(7, 6, "white", "pawn")
    )

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.fill((153, 102, 0))
        board_init(screen,board_grid)
        for piece in pieceGroup:
            chess_grid[piece.x][piece.y] = piece
        pieceGroup.draw(screen)
        pg.display.flip()

if __name__ == '__main__':
    main()