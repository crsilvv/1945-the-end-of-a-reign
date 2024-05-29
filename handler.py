from sprites import *
from npc import *

# Objetos / NPC's
class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/monsters/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_posotions = {}

        #posição dos sprites no mapa
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 4.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + 'PLNTA0.png', pos=(14.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + 'PLNTA0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + 'PLNTA0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + 'PLNTA0.png', pos=(9.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + 'PLNTA0.png', pos=(14.5, 12.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + 'PLNTA0.png', pos=(9.5, 20.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + 'PLNTA0.png', pos=(10.5, 20.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + 'PLNTA0.png', pos=(3.5, 14.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + 'PLNTA0.png', pos=(3.5, 18.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 24.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 30.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 30.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 24.5)))

        #posição dos NPC's no mapa
        add_npc(DOGY(game, pos=(11.5, 4.5)))
        add_npc(DOGY(game, pos=(11.0, 19.0)))
        add_npc(DOGY(game, pos=(11.5, 6.5)))
        add_npc(DOGY(game, pos=(13.5, 6.5)))
        add_npc(DOGY(game, pos=(2.0, 20.0)))
        add_npc(SSFL(game, pos=(4.0, 29.0)))
        add_npc(SSFL(game, pos=(5.5, 14.5)))
        add_npc(HITLR(game, pos=(5.5, 16.5)))
        add_npc(HITLR(game, pos=(14.5, 25.5)))
        add_npc(DOGY(game, pos=(9.5, 4.5)))
        add_npc(DOGY(game, pos=(9.5, 19.0)))
        add_npc(DOGY(game, pos=(9.0, 6.5)))
        add_npc(DOGY(game, pos=(9.5, 6.5)))
        add_npc(DOGY(game, pos=(4.5, 20.0)))
        add_npc(SSFL(game, pos=(6.5, 29.0)))
        add_npc(SSFL(game, pos=(3.5, 10.5)))
        add_npc(HITLR(game, pos=(6.5, 16.5)))
        add_npc(HITLR(game, pos=(6.5, 25.5)))

    def update(self):
        self.npc_posotions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)
    
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)