import pygame as pg
from settings import *

#
class ObjectRenderer:
    def __init__(self, game):
        self.game - game
        self.screen = game.screen
        self.wall_texture = self.load_wall_texture()

    #
    def draw(self):
        self.render_game_objects()

    #
    def render_game_objects(self):
        list_objects = self.game.raycasting.objectst_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    #
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    #
    def load_wall_texture(self):
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
            14: self.get_texture('resources/textures/textures/14.png'),
            15: self.get_texture('resources/textures/textures/15.png'),
            16: self.get_texture('resources/textures/textures/16.png'),
        }