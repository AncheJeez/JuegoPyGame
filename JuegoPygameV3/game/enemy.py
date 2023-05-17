import pygame as pg
import sys
import random

class Enemy:

    def __init__(self, segundos, position_x, position_y, mov_x, mov_y, enemy_surf, enemy_rect,outbounds_x,outbounds_y, comeback, random, random_min, random_max):
        self.position_x = position_x
        self.position_y = position_y
        self.segundos = segundos
        self.mov_x = mov_x
        self.mov_y = mov_y
        self.enemy_surf = enemy_surf
        self.enemy_rect = enemy_rect
        self.outbounds_x = outbounds_x
        self.outbounds_y = outbounds_y
        self.comeback = comeback
        self.random = random
        self.random_min = random_min
        self.random_max = random_max

    def update(self,screen, time):
        if time >= self.segundos:
            self.enemy_rect.x -= self.mov_x
            self.enemy_rect.y += self.mov_y
        #print(self.enemy_rect.x, " ", self.enemy_rect.y, id(self))
        if self.enemy_rect.x <= -100 or self.enemy_rect.x >= 700 or self.enemy_rect.y >= 700 or self.enemy_rect.y <= -100:
            if self.comeback == True:
                self.mov_x = -self.mov_x
                self.mov_y = -self.mov_y
            else:
                if self.outbounds_x > 0 or self.outbounds_y > 0:
                    self.enemy_rect.x = self.outbounds_x
                    self.enemy_rect.y = self.outbounds_y
                else:
                    self.enemy_rect.x = self.position_x
                    self.enemy_rect.y = self.position_y
            if self.random == True:
                self.enemy_rect.y = int(random.randrange(self.random_min,self.random_max))
        

    def draw(self, screen):
        screen.blit(self.enemy_surf,self.enemy_rect)