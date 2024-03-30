#from tkinter.constants import W
import pygame 
from charactor import Choose
from boy.setting import *
from boy.music import Music


# initialization
pygame.init()
pygame.mixer.init()

class Start:
    def __init__(self):
        # window
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.background_image = background_image
        self.start_btn = Buttons(558, 370, 287, 76)
        self.buttons = [self.start_btn]
        self.music = Music()
        self.bg = start_bg
        

    def game_run(self):
        #count time
        clock = pygame.time.Clock()
        pygame.display.set_caption("game")
        self.music.play_music(self.bg)

        run = True
        while run:
            
            #set mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clock.tick(FPS)
            self.win.blit(self.background_image, (0, 0))
            
            for(event) in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_btn.clicked(mouse_x, mouse_y):
                        choose = Choose()
                        #self.start_sound()
                        choose.game_run()
                        run = False

            for obj in self.buttons:
                if obj.clicked(mouse_x, mouse_y):
                    obj.create_frame(mouse_x, mouse_y)
                    obj.draw_frame(self.win)

            pygame.display.update()
        pygame.quit()

    '''def start_sound(self):
        start_sound = pygame.mixer.Sound("music/start1.wav")
        start_sound.set_volume(0.5)
        start_sound.play()'''

    '''def play_music(self):
        pygame.mixer.music.load("D:/project/music/bak1.wav")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)'''


class Buttons:
    def __init__(self, x : int, y : int, width : int, height : int):
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = None

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False

    def create_frame(self, x: int, y: int):
        """if cursor position is on the button, create button frame"""
        if self.clicked(x, y):
            x, y, w, h = self.rect
            self.frame = pygame.Rect(x - 5, y - 5, w + 10, h + 10)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame is not None:
            pygame.draw.rect(win, WHITE, self.frame, 10)


















        '''if self.change == False:
            self.win.blit(background_image, (0, 0) ) 
            note_text = pygame.font.Font('word/mnjzbh.ttf',40)
            position_supply = (590, ( WIN_HEIGHT * 3 ) / 4)
            self.win.blit( note_text.render( "按任意鍵繼續...", True, WHITE ), position_supply )

            note_text1 = pygame.font.Font('word/mnjzbh.ttf',100)
            position_title = ( 520, WIN_HEIGHT / 6 )
            self.win.blit( note_text1.render( "逃出升天", True, WHITE ), position_title )'''

    '''def second(self):
        if self.change == True:
            self.win.fill(BLACK)
            note_text1 = pygame.font.Font('word/mnjzbh.ttf',60)
            position_select = ( 310, WIN_HEIGHT / 7 )
            self.win.blit( note_text1.render( "選擇最初的角色", True, WHITE ), position_select )

            self.girl.draw( self.win )
            self.boy.draw( self.win)'''
            
        
    '''def music_stop(self):
        if self.change == True:
            pygame.mixer.music.stop()

    def keydown(self):
        self.change = True

    def whether_girl_mouse_is_on(self, x, y):
        self.girl.if_mouse_on(x, y)

    def whether_boy_mouse_is_on(self, x, y):
        self.boy.if_mouse_on(x, y)       ''' 

