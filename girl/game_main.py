import pygame 
from boy.game_map import *   # 載入地圖
from girl.control import GameControl
from girl.model import Player
from girl.view import Draw
from girl.dialogue import Dialogue
from boy.get_location import Get_location
from boy.fadein import Fader
from boy.music import Music
from scroll import Scroll


WIN_WIDTH = 1000
WIN_HEIGHT = 600
FPS = 60

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.init()
clock = pygame.time.Clock()


class Game_girl:
    def game_run(self):
        music = Music()
        player = Player()
        get_location = Get_location(player)
        dialogue = Dialogue(player, music)
        draw = Draw(screen, player, dialogue)
        scroll = Scroll()
                  
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA) 
        surface.fill(BLACK)
        fader1 = Fader(screen, surface, WIN_WIDTH, WIN_HEIGHT)
        
        #surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA) 
        control = GameControl(player, draw, dialogue, get_location, music)
        control.update_view()
        fader = Fader(screen, screen, WIN_WIDTH, WIN_HEIGHT)
        fader.fade()

        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            control = GameControl(player, draw, dialogue, get_location , music)
            control.receive_request()
            control.update_model()
            control.update_view()
            
            if control.get_over():
                running = False
            
            pygame.display.update()

        fader1.fade()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            scroll.update()

            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    m = Game_girl()
    m.game_run()