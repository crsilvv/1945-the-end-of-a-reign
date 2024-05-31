from sprite import *
from npc import *
from random import choices, randrange

#
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
        self.npc_positions = {}
        self.enemies = 20
        self.npc_types = [SSFL, DOGY, HITLR]
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '0/0.png', pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '2/PLNTA0.png', pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '1/AMMOA0.png', pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '3/BARLA0.png', pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '4/BPNTA0.png', pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '5/CAG2A0.png', pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '7/CHANA0.png', pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '8/CRWNA0.png', pos=(14.5, 4.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '9/DRUMA0.png', pos=(14.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '10/GIBSA0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '11/HANGB0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '12/JEWLA0.png', pos=(9.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '13/MEDIA0.png', pos=(14.5, 12.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '15/P_MP40.png', pos=(9.5, 20.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '16/SPODA0.png', pos=(10.5, 20.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '6/CAG3A0.png', pos=(3.5, 14.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '17/STATA0.png', pos=(3.5, 18.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '18/STOVA0.png', pos=(14.5, 24.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '19/TCHRA0.png', pos=(14.5, 30.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '14/P_CGUN.png', pos=(1.5, 30.5)))
        add_sprite(AnimatedSprite(game, path=self.static_sprite_path + '20/WEL2A0.png', pos=(1.5, 24.5)))
        add_npc(DOGY(game, pos=(5.5, 16.5)))
        add_npc(HITLR(game, pos=(14.5, 25.5)))
    def spawn_npc(self):
        for i in range(self.enemies):
                npc = choices(self.npc_types, self.weights)[0]
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                    pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))
    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()
    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()
    def add_npc(self, npc):
        self.npc_list.append(npc)
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)