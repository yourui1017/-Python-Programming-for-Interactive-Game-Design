import pygame
import os

FPS = 60
BLACK = (0,0,0)
pygame.init()
clock = pygame.time.Clock()

class Scroll():
    def __init__(self):
        self.width = 1000
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background_image = pygame.image.load(os.path.join("images", "scroll.jpg"))
        self.backgroundY = 0
    
    def update(self):
        if self.backgroundY >= -2350:
            self.backgroundY -= 0.5
        self.screen.blit(self.background_image, (0, self.backgroundY))

'''scroll = Scroll()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scroll.update()

    pygame.display.update()
pygame.quit()'''
