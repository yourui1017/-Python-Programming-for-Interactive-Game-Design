import pygame
from boy.setting import *

class Fader:

    def __init__(self, screen, image, WIN_WIDTH : int, WIN_HEIGHT : int):
        self.width = WIN_WIDTH
        self.height = WIN_HEIGHT
        self.screen = screen
        self.image = image
        self.fade_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.current_time = pygame.time.get_ticks()
        self.temp_time = 0


    def fade(self):
        self.fade_surface.blit(self.image, (0, 0))
        alpha = 0
        while alpha <= 300:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.temp_time >= 50:
                self.temp_time = self.current_time
                alpha += 10
                self.fade_surface.set_alpha(alpha)
                self.redrawWindow()
                self.screen.blit(self.fade_surface, (0, 0))
                pygame.display.update()
    '''def fade(self):
        self.fade_surface.blit(self.image, (0, 0))
        for alpha in range(0, 300):
            self.fade_surface.set_alpha(alpha)
            self.redrawWindow()
            self.screen.blit(self.fade_surface, (0, 0))
            pygame.display.update()'''

    
    def fade1(self):
        self.fade_surface.blit(self.image, (0, 0))
        alpha = 0
        while alpha <= 300:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.temp_time >= 50:
                self.temp_time = self.current_time
                alpha += 10
                self.fade_surface.set_alpha(alpha)
                self.redrawWindow()
                self.screen.blit(self.fade_surface, (0, 0))
                pygame.display.update()
    
    def fade2(self):
        self.fade_surface.blit(self.image, (0, 0))
        alpha = 0
        while alpha <= 300:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.temp_time >= 50:
                self.temp_time = self.current_time
                alpha += 10
                self.fade_surface.set_alpha(alpha)
                self.redrawWindow()
                self.screen.blit(self.fade_surface, (0, 0))
                pygame.display.update()


    def redrawWindow(self):
        self.screen.fill(BLACK)
