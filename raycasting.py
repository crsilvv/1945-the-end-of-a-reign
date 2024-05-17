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

            #horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            #
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            #
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            #
            for i in range(MAX_DEPTH):
                title_hor = int(x_hor), int(y_hor)
                if title_hor in self.gam.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

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
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            #depth
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            #draw for debug
            pg.draw.line(self.game.screen, 'yellow', (100 * ox, 100 * oy),
                         (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a), 2)

            #
            ray_angle += DELTA_ALGLE
    
    #
    def update(self):
        self.ray_cast()