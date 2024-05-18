import pygame as pg
from settings import *

#
class ObjectRenderer:
    def __init__(self, game):
        self.game - game
        self.screen = game.screen

    #
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    #
    def load_wall_texture(self):
        return{
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
            1: self.get_texture('resources/textures/textures/1.png'),
    
        }