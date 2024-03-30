import pygame
import os

WIDTH = 1000
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
pygame.display.set_caption("password")
clock = pygame.time.Clock()
win = pygame.display.set_mode((WIDTH, HEIGHT))

font_name = os.path.join("font.ttf")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

class Lock_treasure:
    def __init__(self):
        
        self.font = pygame.font.Font(font_name, 20)
        self.clock = pygame.time.Clock()
        self.input_box = pygame.Rect(450, 300, 100, 30)
        self.text = ""
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.success = True 
        self.ok = False

    def run(self):
        running = True
        while running:
            clock.tick(FPS)
            win.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.text != "":
                            num = int(self.text)
                            if num == 6198:
                                self.ok = True
                                running = False
                            else:
                                self.success = False
                        self.text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
            pygame.draw.rect(win, WHITE, [300, 150, 400, 200], 0)
            draw_text(win, "請輸入4位數字的寶箱密碼", 20, 500, 200)
            draw_text(win, "(按右上角叉叉可退出)", 20, 500, 230)
            if not self.success:
                draw_text(win, "密碼錯誤", 20, 500, 270)
            self.txt_surface = self.font.render(self.text, True, (0,0,0))
            win.blit(self.txt_surface, (self.input_box.x+30, self.input_box.y+5))
            pygame.draw.rect(win, RED, self.input_box, 2)
            pygame.display.update()

    def get_ok(self):
        return self.ok

#Lock_treasure().run()
