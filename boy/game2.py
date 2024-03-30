import pygame
import os
from random import randint

WIDTH = 1000
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background_image = pygame.image.load(os.path.join("images/game2", "background.png")).convert()
background_image = pygame.transform.scale(background_image, (1000, 600))

button_image = pygame.image.load(os.path.join("images/game2", "button.png")).convert()
button_image = pygame.transform.scale(button_image, (250, 80))

font_name = os.path.join("font.ttf")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((1000, 600))
        self.font = pygame.font.Font(font_name, 40)
        self.clock = pygame.time.Clock()
        self.input_box = pygame.Rect(600, 300, 200, 50)
        self.start_btn = Buttons(500, 300, 250, 80)
        self.second_btn = Buttons(500, 250, 200, 100)
        self.buttons = [self.start_btn]
        self.active = False
        self.text = ""
        self.done = False
        self.color_inactive = pygame.Color('aquamarine1')
        self.color_active = pygame.Color('black')
        self.color = self.color_inactive
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.width = max(200, self.txt_surface.get_width()+10)
        self.input_box.w = self.width
        self.open_first_page = True
        self.open_second_page = False
        self.open_last_page = False
        self.min = 0
        self.max = 100
        self.ans=randint(self.min,self.max)
        self.success = False

    def game_run(self):
        running = True
        while running:
            clock.tick(FPS)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(background_image, (0, 0)) 

            if self.open_first_page:
                draw_text(self.win, "請輸入1~100之間的數字", 40, 600, 100)
                screen.blit(button_image, (500, 300))
                if self.start_btn.clicked(mouse_x, mouse_y):
                    self.start_btn.create_frame(mouse_x, mouse_y)
                    self.start_btn.draw_frame(self.win)

            if self.open_second_page:
                draw_text(self.win, "輸入框", 40, 530, 300)
                draw_text(self.win, f"請輸入{self.min}到{self.max}的數字", 40, 600, 150)
                draw_text(self.win, "(點擊輸入框能切換顏色，黑色才能輸入數字)", 20, 600, 400)
                self.txt_surface = self.font.render(self.text, True, (0,0,0))
                self.width = max(200, self.txt_surface.get_width()+10)
                self.input_box.w = self.width
                self.win.blit(self.txt_surface, (self.input_box.x+10, self.input_box.y))
                pygame.draw.rect(self.win, self.color, self.input_box, 2)

            if self.open_last_page:
                draw_text(self.win, "恭喜過關", 40, 600, 100)
                pygame.draw.rect(self.win, YELLOW,(500, 250, 200, 100),0)
                if self.second_btn.clicked(mouse_x, mouse_y):
                    self.second_btn.create_frame(mouse_x, mouse_y)
                    self.second_btn.draw_frame(self.win)
                draw_text(self.win, "離開遊戲", 40, 600, 270)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("loser")
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if 500 <= mouse_x <= 750 and 300 <= mouse_y <= 380 and self.open_first_page:
                        self.open_first_page = False
                        self.open_second_page = True

                    if 500 <= mouse_x <= 700 and 250 <= mouse_y <= 350 and self.open_last_page:
                        self.open_last_page = False
                        self.success = True
                        running = False

                    if self.input_box.collidepoint(event.pos):
                        self.active = not self.active
                    else:
                        self.active = False
                    # Change the current color of the input box.
                    self.color = self.color_active if self.active else self.color_inactive

                if event.type ==pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            if self.text != "":
                                num = int(self.text)
                                if self.ans < num < self.max:
                                    self.max = num
                                elif self.min < num < self.ans:
                                    self.min = num
                                elif num == self.ans:
                                    self.open_second_page = False
                                    self.open_last_page = True
                                self.text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
            


            pygame.display.update()
        #pygame.quit()

    def get_success(self):
        return self.success


class Buttons:
    def __init__(self, x, y, width, height):
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
            pygame.draw.rect(win, RED, self.frame, 10)

#Game().game_run()

