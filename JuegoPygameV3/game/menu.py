import pygame as pg
import sys
# from .utils import *

class StartMenu:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.screen_size = self.screen.get_size()

    def run(self):
        self.menu_running = True
        while self.menu_running:
            self.clock.tick(60)
            self.update()
            self.draw()
        return True

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.menu_running = False
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
    
    def draw(self):
        font = pg.font.Font(None, 50)
        startmes_surf = font.render('DODGE THE GAME', False, 'White')
        startmes_rect = startmes_surf.get_rect(center = (300,250))
        intromes_surf = font.render('Press Enter to play',False,'White')
        intromes_rect = intromes_surf.get_rect(center = (300,350))

        self.screen.fill('Blue')
        self.screen.blit(startmes_surf,startmes_rect)
        self.screen.blit(intromes_surf,intromes_rect)

        pg.display.update()

class GameMenu:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.screen_size = self.screen.get_size()
        self.playing = True

    def run(self):
        self.menu_running = True
        while self.menu_running:
            self.clock.tick(60)
            self.update()
            self.draw()
        return self.playing

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.playing = True
                    self.menu_running = False
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                    self.menu_running = False
    
    def draw(self):
        font = pg.font.Font(None, 50)
        pausemes_surf = font.render('PAUSE', False, 'BLACK')
        pausemes_rect = pausemes_surf.get_rect(center = (300,300))

        control_surf = font.render('A/S/D/SpaceBar -> Movement',False,'Black')
        control_rect = control_surf.get_rect(bottomleft = (0,600))
        h_surf = font.render('H -> ShowHitboxes',False,'Black')
        h_rect = h_surf.get_rect(bottomleft = (0,550))
        i_surf = font.render('I -> Invencibility',False,'Black')
        i_rect = i_surf.get_rect(bottomleft = (0,500))
        volumen_surf = font.render('-/+ -> Volumen',False,'Black')
        volumen_rect = volumen_surf.get_rect(bottomleft =(0,450))

        self.screen.blit(pausemes_surf,pausemes_rect)
        self.screen.blit(control_surf,control_rect)
        self.screen.blit(h_surf,h_rect)
        self.screen.blit(i_surf,i_rect)
        self.screen.blit(volumen_surf,volumen_rect)

        pg.display.update()

class DeathMenu:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.screen_size = self.screen.get_size()
        self.playing = True

    def run(self, current_time):
        self.menu_running = True
        stop = False
        self.draw(current_time, stop)
        while self.menu_running:
            self.clock.tick(60)
            self.update()
        return self.playing

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.playing = True
                    self.menu_running = False
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                    self.menu_running = False
    
    def draw(self, current_time, stop):
        font = pg.font.Font(None, 50)
        pausemes_surf = font.render('YOU DIED', False, 'BLACK')
        pausemes_rect = pausemes_surf.get_rect(center = (300,250))
        score = int(pg.time.get_ticks()/1000)- current_time
        score_surf = font.render(f'Score: {score}',False,'BLACK')
        score_rect = score_surf.get_rect(center =(300,350))

        self.screen.fill('Red')
        self.screen.blit(pausemes_surf,pausemes_rect)
        self.screen.blit(score_surf,score_rect)

        pg.display.update()

class WinMenu:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.win_sound = pg.mixer.Sound('data/win_sound.wav')
        self.screen_size = self.screen.get_size()
        self.playing = True

    def run(self):
        self.win_sound.play()
        self.menu_running = True
        while self.menu_running:
            self.clock.tick(60)
            self.update()
            self.draw()
        return self.playing

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.playing = True
                    self.menu_running = False
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                    self.menu_running = False
    
    def draw(self):
        font = pg.font.Font(None, 50)
        pausemes_surf = font.render('YOU WIN!!', False, 'BLACK')
        pausemes_rect = pausemes_surf.get_rect(center = (300,250))
        player_surf = pg.image.load('data/Amongus.png').convert_alpha()
        player_rect = player_surf.get_rect(center = (300,350))

        self.screen.fill('Green')
        self.screen.blit(pausemes_surf,pausemes_rect)
        self.screen.blit(player_surf, player_rect)

        pg.display.update()