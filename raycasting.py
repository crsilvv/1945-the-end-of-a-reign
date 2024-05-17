import pygame as pg
import math
from settings import *

#
class RayCasting:
    def __init__(self, game):
        self.game = game

    #
    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        #
        ray_angle = self.game.player.angle
        for ray in range (NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            #verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            #
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            #
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            #
            for i in range(MAX_DEPTH):
                title_vert = int(x_vert), int(y_vert)
                if title_vert in self.game.map.world_map:
                    break

            #
            ray_angle += DELTA_ALGLE
    
    #
    def update(self):
        self.ray_cast()