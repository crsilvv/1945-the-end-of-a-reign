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
        self.IAMGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()

    #
    def get_sprite_projection(self):
        proj = SCREE_DIST / self.norm_dist
        proj_wi

    #
    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        #
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy <0):
            delta += math.tau

        #
        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        #
        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()


    #
    def update(self):
        self.get_sprite()