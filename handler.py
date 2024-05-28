from sprites import *
from npc import *

#
class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_sprite_path = 'resources/sprites/monsters'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'heads/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'heads/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'heads/0.png', pos=(9.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'heads/0.png', pos=(17.5, 8.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'heads/0.png', pos=(10.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'heads/0.png', pos=(8.5, 7.5)))

        #
        add_npc(NPC(game))

    #
    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    #
    def add_npc(self, npc):
        self.npc_list.append(npc)
    
    #
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)