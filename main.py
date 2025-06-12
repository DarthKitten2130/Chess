import pygame as pg
from classes import *


def main():
    screen = pg.display.set_mode((1440, 1440))
    pg.display.set_caption('Chess')
    chess_grid = {i: {j: None for j in range(8)} for i in range(8)}
    board = pg.sprite.Group()
    live_pieces = pg.sprite.Group()
    dead_pieces = pg.sprite.Group()
    clicked_piece = None
    target = None
    turn = "white"
    moved = False
    checked = False

    pg.init()
    pg.font.init()
    font = pg.font.Font('Oswald-Regular.ttf', 32)
    for i in range(8):
        for j in range(8):
            board.add(Tile(i, j))

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

    def get_clicked_piece(live_pieces, mouse_pos):
        for piece in live_pieces:
            if piece.rect.collidepoint(mouse_pos):
                return piece
        return None

    def get_target(live_pieces, board, mouse_pos):
        for piece in live_pieces:
            if piece.rect.collidepoint(mouse_pos):
                return piece
        for tile in board:
            if tile.rect.collidepoint(mouse_pos):
                return tile
        return None

    def move(clicked_piece, target, turn, moved, chess_grid, screen, live_pieces, dead_pieces):
        global checked
        chess_grid[clicked_piece.x][clicked_piece.y] = None
        clicked_piece.x, clicked_piece.y = target.x, target.y
        clicked_piece.rect.topleft = (target.x * Tile.tilesize, target.y * Tile.tilesize)
        chess_grid[target.x][target.y] = clicked_piece
        if isinstance(clicked_piece, Pawn) and clicked_piece.y in (0, 7):
            promote(clicked_piece, screen, live_pieces, dead_pieces, turn)
        clicked_piece.movable_tiles.clear()
        if not clicked_piece.moved:
            clicked_piece.moved = True

        return True

    while True:
        text = font.render(turn, True, (255, 0, 0))
        trect = text.get_rect()
        t_king = next((p for p in live_pieces if isinstance(p, King) and p.color == turn), None)
        checked = t_king.check(turn, live_pieces, chess_grid)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if not clicked_piece:
                    try:
                        clicked_piece = get_clicked_piece(live_pieces, mouse_pos)
                        mt = clicked_piece.check_moves(turn, chess_grid, live_pieces)
                        x = set()
                        for piece in (piece for piece in live_pieces if piece.color == turn):
                            a = piece.check_moves(turn, chess_grid, live_pieces)
                            x = x.union(a)

                        if not x and checked:
                            Piece.checkmate(turn)
                        elif not x and not checked:
                            Piece.stalemate()

                    except AttributeError:
                        pass
                else:
                    if clicked_piece.color == turn:
                        target = get_target(live_pieces, board, mouse_pos)
                        if isinstance(target, Tile) and (target.x, target.y) and (target.x, target.y) != (
                                clicked_piece.x, clicked_piece.y) and (target.x, target.y) in mt:

                            if isinstance(clicked_piece, (King)) and clicked_piece.moved is False and (target.x,
                                                                                                       target.y) in [
                                (1, 0), (1, 7), (6, 0), (6, 7)] and (target.x, target.y) in mt:
                                if target.x == 1:
                                    rook = next((p for p in live_pieces if
                                                 isinstance(p, Rook) and p.x == 0 and p.color == turn), None)
                                    clicked_piece.castle(rook, chess_grid)
                                elif target.x == 6:
                                    rook = next((p for p in live_pieces if
                                                 isinstance(p, Rook) and p.x == 7 and p.color == turn), None)
                                    clicked_piece.castle(rook, chess_grid)

                                clicked_piece.movable_tiles.clear()
                                moved = True

                            else:
                                moved = move(clicked_piece, target, turn, moved, chess_grid, screen, live_pieces,
                                             dead_pieces)

                        elif isinstance(target, Piece) and not isinstance(target,
                                                                          King) and target.color != clicked_piece.color and (
                                target.x, target.y) and (target.x, target.y) != (clicked_piece.x, clicked_piece.y) and (
                                target.x, target.y) in mt:
                            target.kill(live_pieces, dead_pieces)
                            moved = move(clicked_piece, target, turn, moved, chess_grid, screen, live_pieces,
                                         dead_pieces)

                        mt.clear()
                        clicked_piece = None
                        target = None
                        if moved:
                            if turn == "white":
                                turn = "black"
                            else:
                                turn = "white"
                            moved = False

                    else:
                        clicked_piece = None
                        target = None
                        continue

        for piece in live_pieces:
            chess_grid[piece.x][piece.y] = piece
        board.draw(screen)
        live_pieces.draw(screen)
        if clicked_piece:
            clicked_piece.outline(screen)
        screen.blit(text, trect)

        pg.display.flip()


if __name__ == '__main__':
    main()
