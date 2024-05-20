import pygame as pg
from settings import *

#
class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/sky.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0

    #
    def draw(self):
        self.draw_background()
        self.render_game_objects()

    #
    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        #floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    #
    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    #
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    #
    def load_wall_textures(self):
        return{
            1: self.get_texture('resources/textures/textures/1.png'),
            2: self.get_texture('resources/textures/textures/2.png'),
            3: self.get_texture('resources/textures/textures/3.png'),
            4: self.get_texture('resources/textures/textures/4.png'),
            5: self.get_texture('resources/textures/textures/5.png'),
            6: self.get_texture('resources/textures/textures/6.png'),
            7: self.get_texture('resources/textures/textures/7.png'),
            8: self.get_texture('resources/textures/textures/8.png'),
            9: self.get_texture('resources/textures/textures/9.png'),
            10: self.get_texture('resources/textures/textures/10.png'),
            11: self.get_texture('resources/textures/textures/11.png'),
            12: self.get_texture('resources/textures/textures/12.png'),
            13: self.get_texture('resources/textures/textures/13.png'),
        }