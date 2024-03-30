import pygame
from boy.game_main import Game_boy
from boy.fadein import Fader
from boy.setting import *
from girl.game_main import Game_girl
from girl.setting import *

#sys.setrecursionlimit(1000000)

#set parameter

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS_CHA = 3
FPS = 60
#load image
girl_front1 = pygame.transform.scale(pygame.image.load("images/girl/girl1.png"), (GIRL_WIDTH, GIRL_HEIGHT) )
girl_front2 = pygame.transform.scale(pygame.image.load("images/girl/girl2.png"), (GIRL_WIDTH, GIRL_HEIGHT) )
girl_front3 = pygame.transform.scale(pygame.image.load("images/girl/girl3.png"), (GIRL_WIDTH, GIRL_HEIGHT) )

boy_front1 = pygame.transform.scale(pygame.image.load("images/boy/boy1.png"), (BOY_WIDTH, BOY_HEIGHT) )
boy_front2 = pygame.transform.scale(pygame.image.load("images/boy/boy2.png"), (BOY_WIDTH, BOY_HEIGHT) )
boy_front3 = pygame.transform.scale(pygame.image.load("images/boy/boy3.png"), (BOY_WIDTH, BOY_HEIGHT) )

background = pygame.transform.scale(pygame.image.load("images/choose_bak.png"), (WIN_WIDTH,WIN_HEIGHT) )

i = 0
class Charactor:
    def __init__(self):
        self.charactor_list = []
        self.surface_posx = 300
        self.surface_posy = 350
        self.cha_surface = pygame.Surface(( 300, 350 ), pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.mouse_on = False
        self.rect = self.cha_surface.get_rect()
        self.rect.center = (300, 325)
        self.frame = None

    def print(self, win):
        #print(self.mouse_on)
        self.cha_surface = pygame.Surface((300, 350), pygame.SRCALPHA)
        #self.cha_surface.fill(WHITE)
        self.cha_surface.blit(self.charactor_list[1], (50, 75))
        win.blit(self.cha_surface,( self.surface_posx, self.surface_posy ))

    def move(self, win):
        global i
        self.cha_surface = pygame.Surface(( 300, 350 ), pygame.SRCALPHA)
        #self.cha_surface.fill(WHITE)
        self.cha_surface.blit(self.charactor_list[i%3], (50, 75))
        win.blit(self.cha_surface,( self.surface_posx, self.surface_posy ))
        self.clock.tick(FPS_CHA)
        pygame.display.flip()  # 重新整理視窗
        i += 1
    
    def draw(self, win):
        if self.mouse_on:
            self.move(win)
        else:
            self.print(win)

    def if_mouse_on(self, x : int, y : int):
        if self.rect.collidepoint(x, y):
            self.mouse_on = True
        else:
            self.mouse_on = False

    def create_frame(self, x: int, y: int):
        """if cursor position is on the button, create button frame"""
        if self.mouse_on:
            x, y, w, h = self.rect
            self.frame = pygame.Rect(x - 5, y - 5, w + 10, h + 10)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame is not None:
            pygame.draw.rect(win, BLACK, self.frame, 10)

    def get(self):
        return self.mouse_on

class Girl(Charactor):
    def __init__(self):
        super().__init__()
        self.charactor_list = [girl_front1, girl_front2, girl_front3]
        self.surface_posx = 150
        self.surface_posy = 150
        self.rect.center = (300, 325)
    
    def move(self,win):
        super().move(win)

    def draw(self, win):
        super().draw(win)
    
    def if_mouse_on(self, x : int, y : int):
        return super().if_mouse_on(x, y)

    def create_frame(self, x: int, y: int):
        return super().create_frame(x, y)

    def draw_frame(self, win):
        return super().draw_frame(win)
    
    def get(self):
        return super().get()

class Boy(Charactor):
    def __init__(self):
        super().__init__()
        self.charactor_list = [boy_front1, boy_front2, boy_front3]
        self.surface_posx = 550
        self.surface_posy = 150
        self.rect.center = (700, 325)

    def move(self,win):
        super().move(win)

    def draw(self, win):
        super().draw(win)

    def if_mouse_on(self, x : int, y : int):
        return super().if_mouse_on(x, y)

    def create_frame(self, x: int, y: int):
        return super().create_frame(x, y)

    def draw_frame(self, win):
        return super().draw_frame(win)

    def get(self):
        return super().get()



class Choose:
    def __init__(self):
        self.win = pygame.display.set_mode((1000, 600))
        self.cha = Charactor()
        self.girl = Girl()
        self.boy = Boy()

    def game_run(self):
        clock = pygame.time.Clock()
        pygame.display.set_caption("game")
        
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        surface.blit(background, (0, 0))
        self.girl.draw(surface)
        self.boy.draw(surface)
        fader = Fader(self.win, surface, WIN_WIDTH, WIN_HEIGHT)
        fader.fade()

        run1 = True
        while run1:
            #set mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clock.tick(FPS)
            self.win.blit(background, (0, 0))
            
            self.girl.if_mouse_on(mouse_x, mouse_y)
            self.boy.if_mouse_on(mouse_x, mouse_y)

            for(event) in pygame.event.get():
                if event.type == pygame.QUIT:
                   run1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.girl.get():
                        game = Game_girl()
                        game.game_run()
                        run1 = False
                    if self.boy.get():
                        game = Game_boy()
                        game.game_run()
                        run1 = False
                        
            
            self.girl.draw(self.win)
            self.boy.draw(self.win)
            self.girl.create_frame(mouse_x, mouse_y)
            self.girl.draw_frame(self.win)
            self.boy.create_frame(mouse_x, mouse_y)
            self.boy.draw_frame(self.win)


            pygame.display.update()
        pygame.quit()

        
