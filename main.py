import pygame as pg
from classes import *

def get_clicked_piece(live_pieces, mouse_pos):
    for piece in live_pieces:
        if piece.rect.collidepoint(mouse_pos):
            return piece
    return None

def get_target(live_pieces,board,mouse_pos):
    for piece in live_pieces:
        if piece.rect.collidepoint(mouse_pos):
            return piece
    for tile in board:
        if tile.rect.collidepoint(mouse_pos):
            return tile
    return None

def main():
    pg.init()
    screen = pg.display.set_mode((1440, 1440))
    chess_grid = {i: {j: None for j in range(8)} for i in range(8)}
    board = pg.sprite.Group()
    live_pieces = pg.sprite.Group()
    dead_pieces = pg.sprite.Group()
    clicked_piece = None
    target = None
    turn = "white"

    for i in range(8):
        for j in range(8):
            board.add(Tile(i,j))

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
            elif event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if not clicked_piece:
                    try:
                        clicked_piece = get_clicked_piece(live_pieces, mouse_pos)
                        clicked_piece.legal_move(chess_grid)
                    except AttributeError:
                        pass
                else:
                    target = get_target(live_pieces, board, mouse_pos)
                    if isinstance(target, Tile) and [target.x, target.y] in clicked_piece.movable_tiles:
                        chess_grid[clicked_piece.x][clicked_piece.y] = None
                        clicked_piece.x, clicked_piece.y = target.x, target.y
                        clicked_piece.rect.topleft = (target.x * Tile.tilesize, target.y * Tile.tilesize)
                        chess_grid[target.x][target.y] = clicked_piece
                        clicked_piece.movable_tiles.clear()

                    elif isinstance(clicked_piece,(King,Rook)) and isinstance(target,(King,Rook)) and clicked_piece.color == target.color:
                        clicked_piece.castle(target, chess_grid)
                        clicked_piece.movable_tiles.clear()

                    elif isinstance(target,Piece) and not isinstance(target,King) and target.color != clicked_piece.color and [target.x, target.y] in clicked_piece.movable_tiles:
                        target.kill(live_pieces, dead_pieces)
                        chess_grid[clicked_piece.x][clicked_piece.y] = None
                        clicked_piece.x, clicked_piece.y = target.x, target.y
                        clicked_piece.rect.topleft = (target.x * Tile.tilesize, target.y * Tile.tilesize)
                        chess_grid[target.x][target.y] = clicked_piece
                        clicked_piece.movable_tiles.clear()

                    elif isinstance(clicked_piece,Pawn) and clicked_piece.y in [0,7]:
                        promote(clicked_piece,chess_grid,screen,live_pieces,dead_pieces,turn)
                    clicked_piece = None
                    target = None

        for piece in live_pieces:
            chess_grid[piece.x][piece.y] = piece
        board.draw(screen)
        live_pieces.draw(screen)
        if clicked_piece:
            clicked_piece.outline(screen)
        pg.display.flip()

if __name__ == '__main__':
    main()