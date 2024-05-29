import pygame as pg

#
class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.monster_pain = pg.mixer.Sound(self.path + 'mosnter_pain.wav')
        self.monster_death = pg.mixer.Sound(self.path + 'monster_death.wav')
        self.monster_attack = pg.mixer.Sound(self.path + 'monster_attack.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.music.load(self.path + 'doom_music.mp3')
