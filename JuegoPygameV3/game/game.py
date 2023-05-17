import pygame as pg
import sys
import random
from .world import World
from .player import Player
from .enemy import Enemy

class Game:

    def __init__(self, screen, clock):
        self.start_time = 0
        self.time = 0
        self.screen = screen
        self.clock = clock
        self.font = pg.font.Font(None, 50)
        self.contador_volumen = 0.5

        self.inven_surf = self.font.render('Invencibility ON', False, 'Yellow')
        self.inven_rect = self.inven_surf.get_rect(topright = (600,0))


    def run(self,total_time, pause_time, flag, music_flag, tries):
        self.playing = True
        if flag == False:
            self.set_start(music_flag)
        if music_flag == False:
            self.background_music.play(-1)
            music_flag = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            win_dead = self.update(total_time, pause_time, flag, tries)
            self.draw()

        return win_dead, self.time, music_flag


    def events(self):
        #hacemos una lista de eventos, ya que solo podemos instanciar pg.event.get() una vez y tenemos muchos eventos que manejar
        event_list = pg.event.get()
        for event in event_list:
            self.player.events(event_list)
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                if event.key == pg.K_h:
                    if self.show_hitboxes == False:
                        self.show_hitboxes = True
                    elif self.show_hitboxes == True:
                        self.show_hitboxes = False
                if event.key == pg.K_i:
                    if self.invec == False:
                        self.invec = True
                    elif self.invec == True:
                        self.invec = False
                if event.key == pg.K_PLUS and self.contador_volumen <= 1:
                    print(self.contador_volumen)
                    self.contador_volumen += 0.1
                    self.background_music.set_volume(self.contador_volumen)
                if event.key == pg.K_MINUS and self.contador_volumen > 0:
                    print(self.contador_volumen)
                    self.contador_volumen -=0.1
                    self.background_music.set_volume(self.contador_volumen)

    
    def update(self, total_time, pause_time, flag, tries):
        
        if flag == False:
            self.time = int(pg.time.get_ticks()/1000) - total_time
        if flag == True:
            self.time = int(pg.time.get_ticks()/1000) - total_time + pause_time
        self.world.update()
        alive = self.player.update(self.invec, self.ground_level, self.platform_rect, self.creature_rect,self.frog_rect,self.teemo_rect,self.boss_rect)
        self.creature.update(self.screen,self.time)
        self.frog.update(self.screen,self.time)
        self.teemo.update(self.screen,self.time)
        self.boss.update(self.screen,self.time)

        #score
        self.score_surf = self.font.render(f'Time: {self.time}/40',False,'Black')
        self.score_rect = self.score_surf.get_rect(topleft = (0,0))
        #intentos
        self.tries_surf = self.font.render(f'Tries: {tries}',False,'Black')
        self.tries_rect = self.tries_surf.get_rect(topleft = (0,30))
        
        #win
        if self.time == 40:
            self.playing = False
            return 1

        #dead or not
        if alive == False:
            self.playing = False
            return 2

        return 3

    def draw(self):

        self.world.draw(self.screen)

        if self.show_hitboxes == True:
            pg.draw.rect(self.screen,'Pink',self.player_rect)
            pg.draw.rect(self.screen,'Pink',self.creature_rect)
            pg.draw.rect(self.screen,'Pink',self.frog_rect)
            pg.draw.rect(self.screen,'Pink',self.teemo_rect)
            pg.draw.rect(self.screen,'Pink',self.boss_rect)

        self.player.draw(self.screen,self.invec)
        self.creature.draw(self.screen)
        self.frog.draw(self.screen)
        self.teemo.draw(self.screen)
        self.boss.draw(self.screen)

        #draw score
        self.screen.blit(self.score_surf,self.score_rect)
        self.screen.blit(self.tries_surf,self.tries_rect)
        if self.invec == True:
                self.screen.blit(self.inven_surf, self.inven_rect)

        pg.display.update()

    def set_start(self, music_flag):

        self.game_state = True
        self.show_hitboxes = False
        self.invec = False

        #WORLD STUFF
        #ambiente
        self.sky_surf = pg.image.load('data/sky.png').convert_alpha()
        self.ground_surf = pg.image.load('data/floor.png').convert_alpha()

        #platform
        self.platform_surf = pg.Surface((200,20))
        self.platform_surf.fill('Orange')
        self.platform_rect = self.platform_surf.get_rect(topleft = (200,210))

        #PLAYER STUFF
        player_walk_1 = pg.image.load('data/Amongus.png').convert_alpha()
        player_walk_2 = pg.image.load('data/Amongus_flip.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]

        player_index = 0
        self.player_surf = self.player_walk[player_index]
        self.ground_level = 288
        self.player_rect = self.player_surf.get_rect(topleft = (50,self.ground_level))

        #music
        if music_flag == False:
            self.background_music = pg.mixer.Sound('data/Arcade.mp3')
        self.jump_sound = pg.mixer.Sound('data/jump.wav')
        self.death_sound = pg.mixer.Sound('data/death.mp3')
        self.laugh_sound = pg.mixer.Sound('data/laugh.ogg')
        self.teemo_laugh_sound = pg.mixer.Sound('data/teemo_laugh.mp3')


        #ENEMY STUFF
        self.creature_surf = pg.image.load('data/bicho.png').convert_alpha()
        self.creature_position_x = 600
        self.creature_position_y = 288
        self.creature_rect = self.creature_surf.get_rect(topleft = (self.creature_position_x,self.creature_position_y))# 352 - 60
        self.creat_mov_x = 5#int(random.randrange(3,8))
        self.creat_mov_y = 0

        self.frog_surf = pg.image.load('data/rana.png').convert_alpha()
        self.frog_position_x = 100
        self.frog_position_y = 500
        self.frog_outbounds_x = -100
        self.frog_outbounds_y = 600
        self.frog_rect = self.frog_surf.get_rect(topleft = (self.frog_position_x,self.frog_position_y))
        self.frog_mov_x = -5
        self.frog_mov_y = -5

        self.teemo_surf = pg.image.load('data/teemo.png').convert_alpha()
        self.teemo_position_x = 450
        self.teemo_position_y = 500
        self.teemo_outbounds_x = 650
        self.teemo_outbounds_y = 600
        self.teemo_rect = self.teemo_surf.get_rect(topleft = (self.teemo_position_x,self.teemo_position_y))
        self.teemo_mov_x = 5
        self.teemo_mov_y = -5

        self.boss_surf = pg.image.load('data/boss.png').convert_alpha()
        self.boss_position_x = -100
        self.boss_position_y = 288
        self.boss_rect = self.boss_surf.get_rect(topleft = (self.boss_position_x,self.boss_position_y))
        self.boss_mov_x = -2
        self.boss_mov_y = 0

        # world
        self.world = World(self.sky_surf, self.ground_surf, self.platform_surf, self.platform_rect)
        # player
        self.player = Player(self.player_walk, self.player_surf, self.player_rect, self.jump_sound, self.death_sound, self.laugh_sound, self.teemo_laugh_sound)
        #enemy
        self.creature = Enemy(0,self.creature_position_x, self.creature_position_y, self.creat_mov_x, self.creat_mov_y, self.creature_surf, self.creature_rect,0,0, True, True, 0, 288)
        self.frog = Enemy(10,self.frog_position_x,self.frog_position_y,self.frog_mov_x,self.frog_mov_y,self.frog_surf,self.frog_rect,self.frog_outbounds_x,self.frog_outbounds_y,False,False,0,0)
        self.teemo = Enemy(20,self.teemo_position_x,self.teemo_position_y,self.teemo_mov_x,self.teemo_mov_y,self.teemo_surf,self.teemo_rect,self.teemo_outbounds_x,self.teemo_outbounds_y,False,False,0,0)
        self.boss = Enemy(30,self.boss_position_x,self.boss_position_y,self.boss_mov_x,self.boss_mov_y,self.boss_surf,self.boss_rect,0,0,False,True,0,288)