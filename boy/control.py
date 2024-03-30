from __future__ import annotations
import pygame
from boy.setting import *
from boy.game_map import *
from boy.fadein import Fader

from boy.dialogue_list import *

from boy.fadein import Fader
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from boy.model import Player
    from boy.get_location import Get_location
    from boy.dialogue import Dialogue
    from boy.view import Draw
    from boy.music import Music

pygame.init()

#player = Player()
#dialogue = Dialogue(player)

temp_time = 0
open_dialogue = False
open_plot_dialogue = False
dark = False
dark_b = False
paint = False
laser_value = False
laser1_value = False
finish = False

class GameControl:
    def __init__(self, player : Player, draw : Draw, dialogue : Dialogue, location : Get_location , music : Music):
        self.player = player
        self.draw = draw
        self.dialogue = dialogue
        self.location = location
        #self.music = music
        #self.foot = foot_sound

        self.block1 = self.location.get_block_location()
        self.map = self.player.get_in_which_map()
        self.player_change = self.player.get_change()
        self.player_change_1 = self.player.get_change_1()

        self.can_move = False
        self.role_next_location = []        
    def receive_request(self):
        
        """receive user input from the events"""
        #self.value = self.draw.get_value()
        key_pressed = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()   # 隨時抓取經過的時間
        #pressed_time = pygame.time.get_ticks()
        global temp_time
        global open_dialogue
        global open_plot_dialogue
        global dark
        global dark_b
        global paint
        global laser_value
        global laser1_value
        global finish
          
        
        if key_pressed[pygame.K_UP]:
            if current_time - temp_time >= 125:    # 至少經過150毫秒，才能再上下左右移動
                temp_time = current_time
                self.player.up()
                self.role_next_location = self.player.get_role_next_location()
                self.if_hit_wall()
                
        elif key_pressed[pygame.K_DOWN]:
            if current_time - temp_time >= 125:    # 至少經過150毫秒，才能再上下左右移動
                temp_time = current_time
                self.player.down()
                self.role_next_location = self.player.get_role_next_location()
                self.if_hit_wall()
                  

        elif key_pressed[pygame.K_LEFT]:
            if current_time - temp_time >= 125:    # 至少經過150毫秒，才能再上下左右移動
                temp_time = current_time
                self.player.left()
                self.role_next_location = self.player.get_role_next_location()
                self.if_hit_wall()

        elif key_pressed[pygame.K_RIGHT]:
            if current_time - temp_time >= 125:    # 至少經過150毫秒，才能再上下左右移動
                temp_time = current_time
                self.player.right()
                self.role_next_location = self.player.get_role_next_location()
                self.if_hit_wall()

        elif key_pressed[pygame.K_SPACE]:
            if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                temp_time = current_time 
                open_dialogue = self.dialogue.whether_open_dialogue() 

                '''if open_dialogue:
                    self.music.play_sound(self.space_sound)   '''

        open_plot_dialogue = self.dialogue.open_plot_dialogue()

        dark = self.dialogue.get_dark()
        dark_b = self.dialogue.get_dark_b()
        paint = self.dialogue.get_paint_value()
        laser_value = self.dialogue.get_laser_value()
        laser1_value = self.dialogue.get_laser1_value()
        finish = self.dialogue.get_finish()

    '''def if_hit_wall(self):            #判斷是否有撞到牆
        if self.role_next_location not in self.virus and self.role_next_location not in self.game_object and self.role_next_location not in self.treasure_object:
            self.can_move = True'''

    def if_hit_wall(self):            #判斷是否有撞到牆
        if self.role_next_location not in self.block1 :
            self.can_move = True

    def update_model(self):
        '''if self.player_change :
            self.can_move = False
        
        if self.player_change_1 :
            self.can_move = False'''
        
        if open_dialogue: 
            self.can_move = False      
            self.dialogue.open_dialogue = True

        elif open_plot_dialogue:
            self.can_move = False
            self.dialogue.open_dialogue = True
        
        if self.can_move:        #沒有撞到牆就更新目前位置 
            self.player.change()
            self.player.update()

        

    def update_view(self):
        self.draw.draw_night()
        self.draw.draw_map() 
        self.draw.draw_charactor(self.player)

        if dark_b:
            self.draw.draw_dark()

        if dark:
            self.draw.draw_night()

        '''if self.player_change_1 :
            self.move = False
            #self.draw.draw_fade1(self.player)

        if self.player_change :
            self.can_move = False
            #self.draw.draw_fade(self.player)'''
            
            
        #print(self.can_move)
        if paint:
            self.draw.draw_paint()

        if laser_value and self.player.get_in_which_map() == MAP7:
            self.draw.draw_laser1()

        if laser1_value == True and self.player.get_in_which_map() == MAP5:
            self.draw.draw_laser2()
            self.draw.draw_laser3()

        self.draw.draw_dialogue(self.dialogue)

    def get_over(self):
        return finish

       
        
