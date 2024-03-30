import pygame 
from boy.game_map import *   # 載入地圖
from boy.get_location import Get_location
from boy.game2 import Game
from girl.setting import *
from boy.music import Music
'''from all_event_in_game import Item
from all_dialogue_in_game import Dialogue'''




class Player:
    def __init__(self):
        self.image = player_down_image
        self.music = Music()
        self.bg_map1 = start_bg
        self.bg_map2 = bg_map2
        self.bg_map3 = bg_map3
        self.bg_map4 = bg_map4
        self.bg_map5 = bg_map5
        self.bg_map9 = bg_map9
        self.bg_map10 = bg_map10
        self.door_close = door_close
        self.tl = tl

        #self.foot = foot_sound

        self.surface = pygame.Surface(( 50, 50 ), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.x = 100       # 100
        self.rect.y = 250       # 250
        self.speed = 50
        self.next_x_position = 150    # 暫存下一個即將前往的x座標
        self.next_y_position = 100    # 暫存下一個即將前往的y座標
        self.player_in_which_map = MAP1                    # MAP1
        self.player_in_which_map_block = MAP1_BLOCK         # MAP1_BLOCK
        self.location = Get_location(self) 
        #self.location = location
        self.door1 = self.location.get_door1_object_location()  # 取得第一個門的位置
        #self.door2 = self.location.get_door2_location()  # 取得第二個門的位置
        self.game = [50, 200]    
        self.code_game_main = Game()
        self.change_value = False
        self.change_value_1 = False
    
    def update(self):
        self.rect.x = self.next_x_position   # 確認沒有障礙物，才更新此時的x座標
        self.rect.y = self.next_y_position   # 確認沒有障礙物，才更新此時的x座標
        #self.music.play_sound1(self.foot)
       
    def up(self):                            # 往上走
        self.next_x_position = self.rect.x
        self.next_y_position = self.rect.y - self.speed
        
    def down(self):                          # 往下走
        self.next_x_position = self.rect.x 
        self.next_y_position = self.rect.y + self.speed 
    
    def left(self):                          # 往左走
        self.next_x_position = self.rect.x - self.speed
        self.next_y_position = self.rect.y
        
    def right(self):                         # 往右走
        self.next_x_position = self.rect.x + self.speed     
        self.next_y_position = self.rect.y

    '''def draw(self, screen):                  #畫出主角
        screen.blit(self.image, (self.rect.x, self.rect.y))'''

    '''and self.game_open.get_success == False'''
    def play_game(self):                     #玩小遊戲
        self.game = self.location.get_game_location()    
        if self.code_game_main.get_success() == False:
            if self.player_in_which_map == MAP2 and [self.rect.x, self.rect.y] in self.game :       #判斷位置和地圖
                self.code_game_main.game_run()
            
                

    def change(self):                        #改變地圖
        self.door1 = self.location.get_door1_object_location()  # 取得第一個門的位置
        #self.door1_1 = self.location.get_door1_object_location_1()  # 取得第一個門的位置_1
        self.door2 = self.location.get_door2_object_location()  # 取得第二個門的位置
        #self.door2_1 = self.location.get_door2_object_location_1()  # 取得第二個門的位置_1
        self.door3 = self.location.get_door3_object_location()
        #print(self.door1)
        if self.player_in_which_map == MAP1:                                        #當主角在MAP1且下一個位置是第一個門
            if [self.next_x_position, self.next_y_position] in self.door1:     #就將地圖換到MAP2
                self.player_in_which_map = MAP2
                self.player_in_which_map_block = MAP2_BLOCK
                [self.next_x_position, self.next_y_position] = [700, 100]
                self.change_value = True
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map1)
                self.music.play_music(self.bg_map2)

            else:
                self.change_value = False

        elif self.player_in_which_map == MAP2:                                      #當主角在MAP2且下一個位置是第一個門
            if [self.next_x_position, self.next_y_position] in self.door1:     #就將地圖換到MAP1
                self.player_in_which_map = MAP1
                self.player_in_which_map_block = MAP1_BLOCK
                [self.next_x_position, self.next_y_position] = [100, 500]
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map2)
                self.music.play_music(self.bg_map1)
                self.change_value = True

            elif [self.next_x_position, self.next_y_position] in self.door2:    #當主角在MAP2且下一個位置是第二個門
                self.player_in_which_map = MAP3                                      #就將地圖換到MAP3
                self.player_in_which_map_block = MAP3_BLOCK
                [self.next_x_position, self.next_y_position] = [50, 300]
                self.change_value = True
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map2)
                self.music.play_music(self.bg_map3)
                
                    
            else:
                self.change_value = False

        elif self.player_in_which_map == MAP3:                                       #當主角在MAP3且下一個位置是第一個門
            if [self.next_x_position, self.next_y_position] in self.door1 :      #就將地圖換到MAP2
                self.player_in_which_map = MAP2
                self.player_in_which_map_block = MAP2_BLOCK
                [self.next_x_position, self.next_y_position] = [800, 250]
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map3)
                self.music.play_music(self.bg_map2)

                self.change_value = True

            elif [self.next_x_position, self.next_y_position] in self.door2:    #當主角在MAP3且下一個位置是第二個門
                self.player_in_which_map = MAP4                                      #就將地圖換到MAP4
                self.player_in_which_map_block = MAP4_BLOCK
                [self.next_x_position, self.next_y_position] = [50, 500]
                self.change_value = True
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map3)
                self.music.play_music1(self.bg_map4)

            else:
                self.change_value = False

        elif self.player_in_which_map == MAP4:                                       #當主角在MAP4且下一個位置是第一個門
            if [self.next_x_position, self.next_y_position] in self.door1 :      #就將地圖換到MAP3
                self.player_in_which_map = MAP3
                self.player_in_which_map_block = MAP3_BLOCK
                [self.next_x_position, self.next_y_position] = [900, 300]
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map4)
                self.music.play_music(self.bg_map3)

                self.change_value = True

            elif [self.next_x_position, self.next_y_position] in self.door2 :      #當主角在MAP4且下一個位置是第二個門
                if MAP7[5][1] == 50:
                    self.player_in_which_map = MAP7                                    #就將地圖換到MAP7
                    self.player_in_which_map_block = MAP7_BLOCK
                    [self.next_x_position, self.next_y_position] = [50, 250]
                    self.image = player_down_1_image
                    self.change_value_1 = True
                    self.music.play_sound(self.door_close)
                    self.music.stop_music(self.bg_map4)
                    self.music.play_music2(self.bg_map5)

                elif MAP7[5][1] == 0:
                    self.player_in_which_map = MAP5                                    #就將地圖換到MAP5
                    self.player_in_which_map_block = MAP5_BLOCK
                    [self.next_x_position, self.next_y_position] = [50, 300]
                    self.music.play_sound(self.door_close)
                    self.change_value = True
                    self.music.stop_music(self.bg_map4)
                    self.music.play_music2(self.bg_map5)
                

            elif [self.next_x_position, self.next_y_position] in self.door3:    #當主角在MAP4且下一個位置是第3個門
                self.player_in_which_map = MAP4_1                                      #就將地圖換到MAP4_1
                self.player_in_which_map_block = MAP4_1_BLOCK
                [self.next_x_position, self.next_y_position] = [50, 50]
                self.change_value = True
                #self.music.play_sound(self.door_close)
                self.music.play_sound(self.tl)

            else: 
                self.change_value = False
                self.change_value_1 = False

        elif self.player_in_which_map == MAP4_1:                                       #當主角在MAP4_1且下一個位置是第一個門
            if [self.next_x_position, self.next_y_position] in self.door1 :      #就將地圖換到MAP4
                self.player_in_which_map = MAP4
                self.player_in_which_map_block = MAP4_BLOCK
                [self.next_x_position, self.next_y_position] = [750, 50]
                #self.music.play_sound(self.door_close)
                self.music.play_sound(self.tl)
                self.change_value = True
            else:
                self.change_value = False

        elif self.player_in_which_map == MAP5:                                  #當主角在MAP5且下一個位置是第一個門
            if [self.next_x_position, self.next_y_position] in self.door1:     #就將地圖換到MAP4
                self.player_in_which_map = MAP4
                self.player_in_which_map_block = MAP4_BLOCK
                [self.next_x_position, self.next_y_position] = [900, 500]
                self.change_value = True
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map5)
                self.music.play_music1(self.bg_map4)

            elif [self.next_x_position, self.next_y_position] in self.door2:     #當主角在MAP5且下一個位置是第二個門
                self.player_in_which_map = MAP6                                 #就將地圖換到MAP6
                self.player_in_which_map_block = MAP6_BLOCK
                [self.next_x_position, self.next_y_position] = [50, 250]
                self.change_value = True
                self.music.play_sound(self.door_close)

            elif [self.next_x_position, self.next_y_position] in self.door3:     #當主角在MAP5且下一個位置是第3個門
                self.player_in_which_map = MAP7                                  #就將地圖換到MAP7
                self.player_in_which_map_block = MAP7_BLOCK
                [self.next_x_position, self.next_y_position] = [50, 250]
                self.image = player_down_1_image
                self.change_value = True
                #self.music.play_sound(self.door_close)
                self.music.play_sound(self.tl)

            else:
                self.change_value = False

        elif self.player_in_which_map == MAP6:
            if [self.next_x_position, self.next_y_position] in self.door1:      #當主角在MAP6且下一個位置是第1個門
                self.player_in_which_map = MAP5                                 #就將地圖換到MAP5
                self.player_in_which_map_block = MAP5_BLOCK
                [self.next_x_position, self.next_y_position] = [900, 250]
                self.change_value = True
                self.music.play_sound(self.door_close)

            elif [self.next_x_position, self.next_y_position] in self.door2:      #當主角在MAP6且下一個位置是第2個門
                self.player_in_which_map = MAP9                                 #就將地圖換到MAP9
                self.player_in_which_map_block = MAP9_BLOCK
                [self.next_x_position, self.next_y_position] = [50, 150]
                self.change_value = True
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map5)
                self.music.play_music3(self.bg_map9)
            
            else:
                self.change_value = False
            
            

        elif self.player_in_which_map == MAP7:
            if [self.next_x_position, self.next_y_position] in self.door1:      #當主角在MAP7且下一個位置是第1個門
                self.player_in_which_map = MAP5                                 #就將地圖換到MAP5
                self.player_in_which_map_block = MAP5_BLOCK
                [self.next_x_position, self.next_y_position] = [450, 450]
                self.image = player_down_image
                self.change_value = True
                #self.music.play_sound(self.door_close)
                self.music.play_sound(self.tl)

            elif [self.next_x_position, self.next_y_position] in self.door2:      #當主角在MAP7且下一個位置是第2個門
                self.player_in_which_map = MAP8                                 #就將地圖換到MAP8
                self.player_in_which_map_block = MAP8_BLOCK
                [self.next_x_position, self.next_y_position] = [50, 250]
                self.change_value = True
                self.music.play_sound(self.door_close)

            else:
                self.change_value = False

        elif self.player_in_which_map == MAP8:
            if [self.next_x_position, self.next_y_position] in self.door1:      #當主角在MAP8且下一個位置是第1個門
                self.player_in_which_map = MAP7                                 #就將地圖換到MAP7
                self.player_in_which_map_block = MAP7_BLOCK
                [self.next_x_position, self.next_y_position] = [900, 250]
                self.change_value = True
                self.music.play_sound(self.door_close)
            
            else:
                self.change_value = False

        elif self.player_in_which_map == MAP9:

            if [self.next_x_position, self.next_y_position] in self.door1:      #當主角在MAP9且下一個位置是第1個門

                self.player_in_which_map = MAP6                                 #就將地圖換到MAP6
                self.player_in_which_map_block = MAP6_BLOCK
                [self.next_x_position, self.next_y_position] = [900, 50]
                self.change_value = True
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map9)
                self.music.play_music2(self.bg_map5)

            elif [self.next_x_position, self.next_y_position] in self.door2:      #當主角在MAP9且下一個位置是第2個門
                if MAP9_1[5][17] == 50: 
                    self.player_in_which_map = MAP9_1                                 #就將地圖換到MAP6
                    self.player_in_which_map_block = MAP9_1_BLOCK
                    [self.next_x_position, self.next_y_position] = [850, 250]
                    self.change_value = True
                    self.music.play_sound(self.door_close)
                    self.music.stop_music(self.bg_map9)

                else:
                    self.player_in_which_map = MAP9_1                                 #就將地圖換到MAP9_1
                    self.player_in_which_map_block = MAP9_1_BLOCK
                    [self.next_x_position, self.next_y_position] = [50, 200]
                    self.change_value = True
                    self.music.play_sound(self.door_close)
            
            else:
                self.change_value = False

        elif self.player_in_which_map == MAP9_1:
            if [self.next_x_position, self.next_y_position] in self.door1:      #當主角在MAP9_1且下一個位置是第1個門
                self.player_in_which_map = MAP9                                 #就將地圖換到MAP9
                self.player_in_which_map_block = MAP9_BLOCK
                [self.next_x_position, self.next_y_position] = [900, 200]
                self.change_value = True
                self.music.play_sound(self.door_close)

            elif [self.next_x_position, self.next_y_position] in self.door2:      #當主角在MAP10且下一個位置是第2個門
                self.player_in_which_map = MAP10                                 #就將地圖換到MAP10
                self.player_in_which_map_block = MAP10_BLOCK
                [self.next_x_position, self.next_y_position] = [300, 300]
                self.change_value = True
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map9)
                self.music.play_music(self.bg_map10)
            
            else:
                self.change_value = False

        elif self.player_in_which_map == MAP10:                                #當主角在MAP10且下一個位置是第一個門
            if [self.next_x_position, self.next_y_position] in self.door1:     #就將地圖換到MAP9_1
                self.player_in_which_map = MAP9_1
                self.player_in_which_map_block = MAP9_1_BLOCK
                [self.next_x_position, self.next_y_position] = [900, 300]
                self.change_value = True
                self.music.play_sound(self.door_close)
                self.music.stop_music(self.bg_map10)
                self.music.play_music3(self.bg_map9)

            else:
                self.change_value = False



    def get_change(self):
        return self.change_value

    def get_in_which_map_block(self):
        return self.player_in_which_map_block

    def get_in_which_map(self):                          #回傳主角在哪個地圖
        #print(self.player_in_which_map)
        return self.player_in_which_map
    
    def get_role_next_location(self):                   #回傳主角的下個位置
        return [self.next_x_position, self.next_y_position]

    def get_role_location(self):                        #回傳主角目前位置
        return [self.rect.x, self.rect.y]

    def get_role_image(self):
        return self.image

    def start_dialogue(self):                           #開始對話
        pass        

    def get_change_1(self):
        return self.change_value_1
