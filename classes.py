import pygame as pg

class Piece(pg.sprite.Sprite):
    def __init__(self, x, y, color, type,pos):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.image = pg.image.load(f"images/{color}/{color}_{type}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * 180
        self.rect.y = y * 180
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def Update(self,events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    print("wow")