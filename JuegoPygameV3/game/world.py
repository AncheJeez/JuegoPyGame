import pygame as pg
import sys

class World:

    def __init__(self, sky_surf, ground_surf, platform_surf, platform_rect):
        self.sky_surf = sky_surf
        self.ground_surf = ground_surf
        self.platform_surf = platform_surf
        self.platform_rect = platform_rect
        
    
    def update(self):
        mouse_pos = pg.mouse.get_pos()
        mouse_action = pg.mouse.get_pressed()

    def draw(self,screen):
        screen.blit(self.sky_surf,(0,0))
        screen.blit(self.ground_surf,(0,352))
        screen.blit(self.platform_surf,(200,210))