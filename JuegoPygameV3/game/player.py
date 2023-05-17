import pygame as pg
import sys

class Player:

    def __init__(self, player_walk, player_surf, player_rect, jump_sound, death_sound, laugh_sound, teemo_laugh_sound):
        self.player_walk = player_walk
        self.player_surf = player_surf
        self.player_rect = player_rect
        self.player_gravity = 0
        self.jump_sound = jump_sound
        self.death_sound = death_sound
        self.laugh_sound = laugh_sound
        self.teemo_laugh_sound = teemo_laugh_sound
        self.player_x = 50
        self.on_platform = False
        self.pressed_d = False
        self.pressed_a = False
        self.pressed_s = False
        self.direction = pg.math.Vector2(0,0)


    def update(self, invec, ground_level, platform_rect, creature_rect,frog_rect,teemo_rect,boss_rect):
        #player gravity and jump
        self.player_rect.y += self.player_gravity
        self.player_gravity += 1
        self.player_rect.x = self.player_x

        #player map limits
        if self.player_rect.bottom >= 352: self.player_rect.bottom = 352
        if self.player_rect.left <= 0: 
            self.player_rect.left = 0
            self.player_x = 0
        if self.player_rect.right >600: 
            self.player_rect.right=600
            self.player_x = 551
        #movement
        if self.pressed_d: self.player_x += 10
        if self.pressed_a: self.player_x -= 10
        #animation
        if self.pressed_d == True:
            self.player_surf = self.player_walk[0]
        if self.pressed_a == True:
            self.player_surf = self.player_walk[1]
                
        #collisions
        if self.player_rect.colliderect(platform_rect):
            #colisiona por abajo
            if self.player_gravity <= 0 and self.pressed_s == True:
                self.on_platform = False
            #colisiona por arriba
            if self.player_gravity > 0 and self.pressed_s == False:
                self.on_platform = True
                self.player_gravity = 0
        else:
            self.on_platform = False
        # key s
        if self.player_rect.y == ground_level-4:
            self.pressed_s = False
        if invec == False:
            if creature_rect.colliderect(self.player_rect) or frog_rect.colliderect(self.player_rect) or teemo_rect.colliderect(self.player_rect) or boss_rect.colliderect(self.player_rect):
                if boss_rect.colliderect(self.player_rect):
                    self.laugh_sound.play()
                if teemo_rect.colliderect(self.player_rect):
                    self.teemo_laugh_sound.play()
                else:
                    self.death_sound.play()
                self.alive = False
                return self.alive
            else:
                self.alive = True
                return self.alive

    def events(self, event_list):
        for event in event_list:
                if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE and self.player_rect.bottom >= 352:
                            self.player_gravity = -20
                            self.jump_sound.play()
                        if event.key == pg.K_SPACE and self.on_platform == True and self.pressed_s == False:
                            self.player_gravity = -20
                            self.jump_sound.play()
                        if event.key == pg.K_d:
                            self.pressed_d = True
                        if event.key == pg.K_a:
                            self.pressed_a = True
                        if event.key == pg.K_s:
                            self.pressed_s = True
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_d:
                        self.pressed_d = False
                    if event.key == pg.K_a:
                        self.pressed_a = False
                    #if event.key == pg.K_s:
                    #    self.pressed_s = False
            
    def draw(self,screen,invec):
        screen.blit(self.player_surf,self.player_rect)