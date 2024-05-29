import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/SKY2.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.blod_screen = self.get_texture('resources/textures/blood.png' ,RES)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'resources/textures/digits/{i}.png', [self.digit_size] * 2)
                             for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_image = self.get_texture('resources/textures/screens/game_over.png', RES)

    # loop
    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()

    # tela de game over
    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    # exibir vida do jogador na tela
    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, 0))

    # tela de dano
    def player_damage(self):
        self.screen.blit(self.blod_screen, (0, 0))

    # fundo/sky
    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        # chão
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    # renderização
    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    # metodo get
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    # local das texturas
    def load_wall_textures(self):
        return{
            1: self.get_texture('resources/textures/textures/blue (1).png'),
            2: self.get_texture('resources/textures/textures/blue (2).png'),
            3: self.get_texture('resources/textures/textures/blue (3).png'),
            4: self.get_texture('resources/textures/textures/blue (4).png'),
            5: self.get_texture('resources/textures/textures/blue (5).png'),
            6: self.get_texture('resources/textures/textures/brik (1).png'),
            7: self.get_texture('resources/textures/textures/brik (3).png'),
            8: self.get_texture('resources/textures/textures/brik (4).png'),
            9: self.get_texture('resources/textures/textures/brik (5).png'),
            10: self.get_texture('resources/textures/textures/brik (6).png'),
            11: self.get_texture('resources/textures/textures/cyan (1).png'),
            12: self.get_texture('resources/textures/textures/cyan (2).png'),
            13: self.get_texture('resources/textures/textures/cyan (3).png'),
            14: self.get_texture('resources/textures/textures/cyan (4).png'),
        }