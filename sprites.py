import pygame as pg
from settings import *

#
class SpriteObject:
    def __init__(self, game, path='resources/sprites/static_sprites/ARMRA0.png', pos=(10.5, 3.5)):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2

    #
    def get_sprite(self):