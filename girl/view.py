from __future__ import annotations
import pygame 
from boy.game_map import *
from girl.dialogue_list import *
from boy.get_location import Get_location
from boy.fadein import Fader
from girl.setting import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from girl.model import Player
    from girl.dialogue import Dialogue




pygame.init()

class Draw:
    def __init__(self, screen, player :Player , dialogue : Dialogue):
        self.surface = pygame.Surface(( 50, 50 ), pygame.SRCALPHA)
        self.screen = screen
        self.player = player
        self.image = player_down_image
        self.dialogue = dialogue
        self.map = self.player.get_in_which_map()
        self.location = Get_location(self.player)

        self.font = pygame.font.Font(font_name, 24)                                  # 設定文字

        self.night_surface = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        transparency1 = 140
        pygame.draw.rect(self.night_surface, (0, 0, 0, transparency1), [0, 0, WIN_WIDTH, WIN_HEIGHT])

        self.dark_surface = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        transparency2 = 140
        pygame.draw.rect(self.dark_surface, (0, 0, 0, transparency2), [0, 0, WIN_WIDTH, WIN_HEIGHT])

        transparency3 = 140
        self.laser_surface1 = pygame.Surface(( WIDTH, HEIGHT*9 ), pygame.SRCALPHA)                # MAP7直的雷射光
        pygame.draw.line(self.laser_surface1, (255, 0, 0, transparency3), (25, 0 ), (25, 450), 5 )

        self.laser_surface2 = pygame.Surface(( WIDTH, HEIGHT*6 ), pygame.SRCALPHA)                # MAP8 直的雷射光
        pygame.draw.line(self.laser_surface2, (255, 0, 0, transparency3), (25, 0 ), (25, 275), 5 )

        self.laser_surface3 = pygame.Surface(( WIDTH*6, HEIGHT ), pygame.SRCALPHA)                #MAP8 橫的雷射光
        pygame.draw.line(self.laser_surface3, (255, 0, 0, transparency3), (25, 25 ), (300, 25), 5)


        self.bg_surface_map1 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map1.blit(bg_map1_image, (0, 0))

        self.bg_surface_map2 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map2.blit(bg_map2_image, (0, 0))

        self.bg_surface_map3 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map3.blit(bg_map3_image, (0, 0))

        self.bg_surface_map4 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map4.blit(bg_map4_image, (0, 0))

        self.bg_surface_map4_1 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map4_1.blit(bg_map4_1_image, (0, 0))

        self.bg_surface_map5 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map5.blit(bg_map5_image, (0, 0))

        self.bg_surface_map6 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map6.blit(bg_map6_image, (0, 0))

        self.bg_surface_map7 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map7.blit(bg_map7_image, (0, 0))

        self.hammer_surface_map7 = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.hammer_surface_map7.blit(hammer_image, (0, 0))

        self.bg_surface_map8 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map8.blit(bg_map8_image, (0, 0))

        self.bg_surface_map9 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map9.blit(bg_map9_image, (0, 0))

        self.bg_surface_map9_1 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map9_1.blit(bg_map9_1_image, (0, 0))

        self.bg_surface_map10 = pygame.Surface(( WIN_WIDTH, WIN_HEIGHT ), pygame.SRCALPHA)
        self.bg_surface_map10.blit(bg_map10_image, (0, 0))

        self.key_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.key_surface.blit(key_image, (0, 0))

        self.floor_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.floor_surface.fill(BLACK)

        self.rock_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.rock_surface.blit(rock_image, (0, 0))

        self.door_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.door_surface.blit(door_image, (0, 0))

        self.dr_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.dr_surface.blit(dr_image, (0, 0))

        self.joker_surface_map2 = pygame.Surface(( JOKER_WIDTH, JOKER_HEIGHT ), pygame.SRCALPHA)
        self.joker_surface_map2.blit(joker_image, (0, 0))

        self.nose_surface_map2 = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.nose_surface_map2.blit(nose_image, (0, 0))

        self.virus_surface_map2 = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.virus_surface_map2.blit(virus_image, (0, 0))

        self.virus_surface_map4 = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.virus_surface_map4.blit(virus_1_image, (0, 0))

        self.num_surface = pygame.Surface(( WIDTH_1, HEIGHT_1 ), pygame.SRCALPHA)
        self.num_surface.blit(num_image, (0, 0))

        self.trap_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.trap_surface.blit(trap_image, (0, 0))

        self.gas_surface = pygame.Surface(( WIDTH*3, HEIGHT*3), pygame.SRCALPHA)
        self.gas_surface.blit(gas_image, (0, 0))

        self.ele_f_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.ele_f_surface.blit(ele_f_image, (0, 0))

        self.ele_s_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.ele_s_surface.blit(ele_s_image, (0, 0))

        self.ele_f_1_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.ele_f_1_surface.blit(ele_f_1_image, (0, 0))

        self.ele_s_1_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.ele_s_1_surface.blit(ele_s_1_image, (0, 0))

        self.paint_surface = pygame.Surface(( WIDTH*18, HEIGHT*9 ), pygame.SRCALPHA)
        self.paint_surface.blit(paint_image, (0, 0))

        self.ball1_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.ball1_surface.blit(ball1_image, (0, 0))

        self.ball2_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.ball2_surface.blit(ball2_image, (0, 0))

        self.ball3_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.ball3_surface.blit(ball3_image, (0, 0))

        self.ball4_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.ball4_surface.blit(ball4_image, (0, 0))

        self.water_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.water_surface.blit(water_image, (0, 0))

        self.ice_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.ice_surface.blit(ice_image, (0, 0))

        self.virus_surface_map9_1 = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.virus_surface_map9_1.blit(virus_2_image, (0, 0))

        self.star_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.star_surface.blit(star_image, (0, 0))

        self.moon_surface = pygame.Surface(( WIDTH*3, HEIGHT*3 ), pygame.SRCALPHA)
        self.moon_surface.blit(moon_image, (0, 0))

        self.girl_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.girl_surface.blit(player_down_1_image, (0, 0))
        
        self.door1 = self.location.get_door1_location()  # 取得門1的位置
        self.door2 = self.location.get_door2_location()  # 取得門2的位置

        self.door1_dialogue_in_map1 = Jonny_door_dialogue4_in_map1  #取得門1對話 map1

        self.dr = self.location.get_DR_location()  # 取得觸發DR對話的位置
        self.dr_dialogue_in_map1 = Jonny_DR_dialogue1_in_map1  #取得DR對話

        self.rock = self.location.get_rock_location()  # 取得觸發石頭對話的位置
        self.rock_dialogue_in_map1 = Jonny_rock_dialogue1_in_map1  #取得石頭對話

        self.key = self.location.get_key_location()    # 取得觸發鑰匙對話的位置
        self.key_dialogue_in_map1= Jonny_key_dialogue1_in_map1    #取得鑰匙對話

        self.murmur1 = [100, 250]                               # 取得觸發自己對話1的位置
        self.murmur2 = [850, 300]                                     # 取得觸發自己對話2的位置

        self.murmur_dialogue_in_map1 = Jonny_self_dialogue1_in_map1   #取得和自己的對話map1
        self.murmur_dialogue_in_map2 = Jonny_self_dialogue1_in_map2   #取得和自己的對話map2
        self.murmur_dialogue_in_map3 = Jonny_self_dialogue1_in_map3   #取得和自己的對話map3
        self.murmur_dialogue_in_map4 = Jonny_self_dialogue1_in_map4   #取得和自己的對話map4
        self.murmur_dialogue_in_map5 = Jonny_self_dialogue1_in_map5    #取得和自己的對話map5
        self.murmur_dialogue_in_map6 = Jonny_self_dialogue1_in_map6    #取得和自己的對話map6
        self.murmur_dialogue_in_map7 = Vivian_self_dialogue1_in_map7   #取得和自己的對話map7
        self.murmur_dialogue_in_map9 = Jonny_self_dialogue1_in_map9  #取得和自己的對話 map9
        self.murmur_dialogue_in_map9_1 = Jonny_self_dialogue1_in_map9_1  #取得和自己的對話 map9_1
        self.murmur_dialogue_in_map10 = Jonny_self_dialogue1_in_map10  #取得和自己的對話 map9_1



        self.nose = [500, 350]                                   # 取得觸發鼻子對話的位置
        self.nose_dialogue_in_map2 = Jonny_nose_dialogue1_in_map2    #取得鼻子對話

        self.joker = [750, 500]                                      # 取得觸發小丑對話的位置
        self.joker_dialogue_in_map2 = Jonny_joker_dialogue1_in_map2    #取得小丑對話

        self.game = [50, 200]                                      # 取得觸發遊戲對話的位置
        self.game_dialogue_in_map2 = Jonny_game_dialogue1_in_map2    #取得遊戲對話

        self.virus = [550, 150]                                      # 取得觸發病毒對話的位置
        self.virus_dialogue_in_map2 = Jonny_virus_dialogue1_in_map2    #取得病毒對話

        self.sign1 = [50, 200]                                      # 取得觸發公告1對話的位置
        self.sign1_dialogue_in_map3 = Jonny_sign1_dialogue_in_map3    #取得公告1對話

        self.sign2 = [900, 200]                                      # 取得觸發公告2對話的位置
        self.sign2_dialogue_in_map3 = Jonny_sign2_dialogue_in_map3    #取得公告2對話

        self.blue = [200, 150]                                      # 取得觸發藍色矮人對話的位置
        self.blue_dialogue_in_map3 = Jonny_blue_dialogue1_in_map3    #取得藍色矮人對話

        self.yellow = [450, 150]                                      # 取得觸發黃色矮人對話的位置
        self.yellow_dialogue_in_map3 = Jonny_yellow_dialogue1_in_map3    #取得黃色矮人對話

        self.red = [600, 150]                                      # 取得觸發紅色矮人對話的位置
        self.red_dialogue_in_map3 = Jonny_red_dialogue1_in_map3    #取得紅色矮人對話

        self.green = [200, 400]                                      # 取得觸發綠色矮人對話的位置
        self.green_dialogue_in_map3 = Jonny_green_dialogue1_in_map3    #取得綠色矮人對話

        self.gray = [450, 400]                                      # 取得觸發灰色矮人對話的位置
        self.gray_dialogue_in_map3 = Jonny_gray_dialogue1_in_map3    #取得灰色矮人對話

        self.purple = [600, 400]                                      # 取得觸發紫色矮人對話的位置
        self.purple_dialogue_in_map3 = Jonny_purple_dialogue1_in_map3    #取得紫色矮人對話

        self.key1 = [350, 500]                                      # 取得觸發鑰匙對話的位置
        self.key_dialogue_in_map3 = Jonny_key_dialogue_in_map3      #取得鑰匙對話

        self.door_dialogue_in_map3 = Jonny_door_dialogue1_in_map3    # 取得門2的對話 map3

        self.door_dialogue_in_map4 = Jonny_door_dialogue1_in_map4    #取得門2的對話 map4

        self.vase = [50, 250]                                      # 取得觸發和花瓶對話的位置 map4
        self.vase_dialogue_in_map4 = Jonny_vase_dialogue_in_map4    #取得花瓶的對話 

        self.shelf = [50, 150]                                      #取得觸發和書櫃對話的位置
        self.shelf_dialogue_in_map4 = Jonny_shelf_dialogue_in_map4   #取得書櫃的對話

        self.clock = [300, 100]                                     #取得觸發和時鐘對話的位置
        self.clock_dialogue_in_map4 = Jonny_clock_dialogue1_in_map4   #取得時鐘的對話

        self.eagle = [600, 100]                                     #取得觸發和老鷹對話的位置
        self.eagle_dialogue_in_map4 = Jonny_eagle_dialogue1_in_map4  #取得老鷹的對話

        self.sofa = [250, 250]                                     #取得觸發和沙發對話的位置
        self.sofa_dialogue_in_map4 = Jonny_sofa_dialogue_in_map4  #取得沙發的對話

        self.floor = [250, 250]                                     #取得觸發和地板對話的位置
        self.floor_dialogue_in_map4 = Jonny_floor_dialogue_in_map4  #取得地板的對話

        self.light = [50, 250]                                      # 取得觸發和燈對話的位置 map3
        self.light_dialogue_in_map4 = Jonny_light_dialogue_in_map4    #取得燈的對話 

        self.owl = [250, 250]                                     #取得觸發和貓頭鷹對話的位置
        self.owl_dialogue_in_map4 = Jonny_owl_dialogue1_in_map4  #取得貓頭鷹的對話

        self.crow = [850, 350]                                     #取得觸發和烏鴉對話的位置
        self.crow_dialogue_in_map4 = Jonny_crow_dialogue1_in_map4  #取得烏鴉的對話

        self.virus_1 = [900, 50]                                    #取得觸發和病毒對話的位置
        self.virus_dialogue_in_map4 = Jonny_virus_dialogue1_in_map4  #取得病毒的對話

        self.key2 = [750, 400]                                    #取得觸發和花對話的位置
        self.key_dialogue_in_map4 = Jonny_flower_dialogue_in_map4  #取得花的對話

        self.sign3 = [150, 150]                                     #取得觸發和公告對話的位置   map4
        self.sign_dialogue_in_map4 = Jonny_sign_dialogue_in_map4   #取得公告的對話

        self.shelf1 = [600, 100]                                    #取得觸發和書櫃1對話的位置   map4
        self.shelf1_dialogue_in_map4 = Jonny_shelf1_dialogue_in_map4    #取得書櫃1的對話

        self.treasure1 = [50, 50]                                   #取得觸發和寶箱1對話的位置   map5
        self.treasure_dialogue_in_map5 = Jonny_treasure_dialogue1_in_map5   #取得寶箱1的對話   

        self.light1 = [450, 50]                                   #取得觸發和燈管對話的位置   map5
        self.light_dialogue_in_map5 = Jonny_light_dialogue1_in_map5   #取得燈管的對話   

        self.ele = [900, 50]                                   #取得觸發和電線對話的位置   map5
        self.ele_dialogue_in_map5 = Jonny_ele_dialogue1_in_map5   #取得電線的對話   

        self.mirror = [650, 200]                                   #取得觸發和鏡子對話的位置   map5
        self.mirror_dialogue_in_map5 = Jonny_mirror_dialogue_in_map5   #取得鏡子的對話

        self.door_dialogue_in_map5 = Jonny_door_dialogue1_in_map5   #取得門的對話   
   
        self.altar = [50, 350]                                   #取得觸發和祭壇對話的位置   map5
        self.altar_dialogue_in_map5 = Jonny_altar_dialogue1_in_map5   #取得祭壇的對話 

        self.urn = [900, 500]                                   #取得觸發和酒桶對話的位置   map5
        self.urn_dialogue_in_map5 = Jonny_urn_dialogue1_in_map5   #取得酒桶的對話   

        self.wall = [700, 50]                                       #取得觸發和牆壁對話的位置   map5
        self.wall_dialogue_in_map5 = Jonny_wall_dialogue1_in_map5   #取得牆壁的對話

        self.trap = [100, 50]                                       #取得觸發和陷阱對話的位置   map5
        self.wall_dialogue_in_map5 = Jonny_wall_dialogue1_in_map5   #取得陷阱的對話

        self.urn1 = [850, 400]                                       #取得觸發和酒桶1對話的位置   map5
        self.urn1_dialogue_in_map5 = Jonny_urn1_dialogue1_in_map5   #取得酒桶1的對話

        self.urn2 = [850, 450]                                       #取得觸發和酒桶2對話的位置   map5
        self.urn2_dialogue_in_map5 = Jonny_urn2_dialogue1_in_map5   #取得酒桶2的對話

        self.sign4 = [200, 150]                                       #取得觸發和公告4對話的位置   map5
        self.sign4_dialogue_in_map5 = Jonny_sign4_dialogue_in_map5   #取得公告4的對話

        self.ladder = [300, 150]                                       #取得觸發和梯子對話的位置   map5
        self.ladder_dialogue_in_map5 = Jonny_ladder_dialogue_in_map5   #取得梯子的對話

        self.cloth_g = [250, 450]                                       #取得觸發和女生衣服對話的位置   map5
        self.cloth_g_dialogue_in_map5 = Jonny_cloth_g_dialogue_in_map5   #取得女生衣服的對話

        self.cloth_b = [500, 400]                                       #取得觸發和男生衣服對話的位置   map5
        self.cloth_b_dialogue_in_map5 = Jonny_cloth_b_dialogue_in_map5   #取得男生衣服的對話

        self.small_shelf = [750, 500]                                       #取得觸發和小櫥櫃對話的位置   map5
        self.small_shelf_dialogue_in_map5 = Jonny_small_shelf_dialogue_in_map5   #取得小櫥櫃的對話

        self.treasure_dialogue_in_map6 = Jonny_treasure_dialogue1_in_map6    #取得寶箱的對話 map6

        self.fan = [850, 50]                                                #取得觸發風扇對話的位置 map6
        self.fan_dialogue_in_map6 = Jonny_fan_dialogue1_in_map6             #取得風扇的對話 map6

        self.gas = [400, 50]                                                #取得觸發毒氣對話的位置 map6
        self.gas_dialogue_in_map6 = Jonny_gas_dialogue_in_map6             #取得毒氣的對話 map6

        self.gas = [400, 50]                                                #取得觸發毒氣對話的位置 map6
        self.gas_dialogue_in_map6 = Jonny_gas_dialogue_in_map6             #取得毒氣的對話 map6

        self.gas = [400, 50]                                                #取得觸發毒氣對話的位置 map6
        self.gas_dialogue_in_map6 = Jonny_gas_dialogue_in_map6             #取得毒氣的對話 map6

        self.gas = [400, 50]                                                #取得觸發毒氣對話的位置 map6
        self.gas_dialogue_in_map6 = Jonny_gas_dialogue_in_map6             #取得毒氣的對話 map6

        self.lamp = [100, 400]                                                #取得觸發檯燈對話的位置 map6
        self.lamp_dialogue_in_map6 = Jonny_lamp_dialogue_in_map6             #取得檯燈的對話 map6

        self.bench = [300, 500]                                                #取得觸發板凳對話的位置 map6
        self.bench_dialogue_in_map6 = Jonny_bench_dialogue_in_map6             #取得板凳的對話 map6

        self.fireplace = [400, 150]                                                #取得觸發壁爐對話的位置 map6
        self.fireplace_dialogue_in_map6 = Jonny_fireplace_dialogue_in_map6             #取得壁爐的對話 map6

        self.grass = [650, 50]                                                #取得觸發盆栽對話的位置 map6
        self.grass_dialogue_in_map6 = Jonny_grass_dialogue_in_map6             #取得盆栽的對話 map6

        self.treasure2 = [100, 500]                                           #取得觸發密碼寶箱對話的位置 map6
        self.treasure2_dialogue_in_map6 = Jonny_treasure2_dialogue1_in_map6             #取得密碼寶箱的對話 map6

        self.door_dialogue_in_map6 = Jonny_door_dialogue_in_map6


        self.hammer = [150, 50]                                             #取得觸發和槌子對話的位置   map7
        self.hammer_dialogue_in_map7 = Vivian_hammer_dialogue_in_map7           #取得槌子的對話

        self.ele_dialogue_in_map7 = Vivian_ele_dialogue1_in_map7           #取得電線的對話 map7

        self.wall_dialogue_in_map7 = Vivian_wall_dialogue1_in_map7           #取得牆壁的對話 map7

        self.rock1 = [150, 250]                                             #取得觸發和石頭對話的位置   map7
        self.rock_dialogue_in_map7 = Vivian_rock_dialogue_in_map7           #取得石頭的對話

        self.box = [100, 500]                                             #取得觸發和工具箱對話的位置   map7
        self.box_dialogue_in_map7 = Vivian_box_dialogue_in_map7           #取得工具箱的對話

        self.pliers = [350, 500]                                             #取得觸發和鉗子對話的位置   map7
        self.pliers_dialogue_in_map7 = Vivian_pliers_dialogue_in_map7           #取得鉗子的對話

        self.shelf2 = [400, 150]                                             #取得觸發和櫥櫃對話的位置   map7
        self.shelf_dialogue_in_map7 = Vivian_shelf_dialogue_in_map7           #取得櫥櫃的對話

        self.frame = [600, 500]                                             #取得觸發和相框對話的位置   map7
        self.frame_dialogue_in_map7 = Vivian_frame_dialogue_in_map7           #取得相框的對話

        self.laser = [700, 150]                                             #取得觸發和雷射光對話的位置   map7
        self.laser_dialogue_in_map7 = Vivian_laser_dialogue1_in_map7           #取得雷射光的對話

        self.front = [700, 150]
        self.laser1_dialogue_in_map7 = Vivian_laser_dialogue_in_map7           #取得雷射光的對話

        self.dead = [900, 50]                                             #取得觸發和骷髏頭對話的位置   map7
        self.dead_dialogue_in_map7 = Vivian_dead_dialogue_in_map7           #取得骷髏頭的對話

        self.refri = [50, 150]                                          #取得觸發和冰箱對話的位置   map8
        self.refri_dialogue_in_map8 = Vivian_refri_dialogue1_in_map8        #取得冰箱的對話

        self.paint = [50, 150]                                          #取得觸發和相框對話的位置   map8
        self.paint_dialogue_in_map8 = Vivian_paint_dialogue1_in_map8        #取得相框的對話

        self.ele_dialogue_in_map8 = Vivian_ele_dialogue1_in_map8           #取得電線的對話 map8

        self.water = [900, 400]                                          #取得觸發和水對話的位置   map8
        self.water_dialogue_in_map8 = Vivian_water_dialogue_in_map8        #取得水的對話

        self.btn = [50, 150]                                          #取得觸發和按鈕對話的位置   map8
        self.btn_dialogue_in_map8 = Vivian_btn_dialogue1_in_map8        #取得按鈕的對話

        self.flute = [300, 50]                                          #取得觸發和長笛對話的位置   map8
        self.flute_dialogue_in_map8 = Vivian_flute_dialogue_in_map8        #取得長笛的對話

        self.violin_box = [150, 350]                                          #取得觸發和小提琴箱子對話的位置   map8
        self.violin_box_dialogue_in_map8 = Vivian_violin_box_dialogue_in_map8        #取得小提琴箱子的對話

        self.violin = [500, 150]                                          #取得觸發和小提琴對話的位置   map8
        self.violin_dialogue_in_map8 = Vivian_violin_dialogue_in_map8        #取得小提琴的對話

        self.piano = [300, 500]                                          #取得觸發和鋼琴對話的位置   map8
        self.piano_dialogue_in_map8 = Vivian_piano_dialogue_in_map8        #取得鋼琴的對話

        self.cello = [550, 450]                                          #取得觸發和大提琴對話的位置   map8
        self.cello_dialogue_in_map8 = Vivian_cello_dialogue_in_map8        #取得大提琴的對話

        self.trumpet = [800, 150]                                          #取得觸發和法國號對話的位置   map8
        self.trumpet_dialogue_in_map8 = Vivian_trumpet_dialogue_in_map8        #取得法國號的對話

        self.cabinet = [50, 150]                                          #取得觸發和櫃子對話的位置   map9
        self.cabinet_dialogue_in_map9 = Jonny_cabinet_dialogue_in_map9        #取得櫃子的對話

        self.mashine1 = [150, 50]                                          #取得觸發和機器1對話的位置   map9
        self.mashine1_dialogue_in_map9 = Jonny_mashine1_dialogue_in_map9        #取得機器1的對話

        self.mashine2 = [200, 50]                                          #取得觸發和機器2對話的位置   map9
        self.mashine2_dialogue_in_map9 = Jonny_mashine2_dialogue_in_map9        #取得機器2的對話

        self.mashine3 = [300, 50]                                          #取得觸發和機器3對話的位置   map9
        self.mashine3_dialogue_in_map9 = Jonny_mashine3_dialogue_in_map9        #取得機器3的對話

        self.micro = [400, 50]                                          #取得觸發和顯微鏡對話的位置   map9
        self.micro_dialogue_in_map9 = Jonny_micro_dialogue_in_map9        #取得顯微鏡的對話

        self.screen1 = [550, 50]                                          #取得觸發和螢幕對話的位置   map9
        self.screen_dialogue_in_map9 = Jonny_screen_dialogue_in_map9        #取得螢幕的對話

        self.alcohol = [900, 500]                                          #取得觸發和酒精對話的位置   map9
        self.alcohol_dialogue_in_map9 = Jonny_alcohol_dialogue1_in_map9        #取得酒精的對話

        self.nacl = [100, 500]                                          #取得觸發和氯化鈉對話的位置   map9
        self.nacl_dialogue_in_map9 = Jonny_nacl_dialogue1_in_map9        #取得氯化鈉的對話

        self.concentrator = [900, 100]                                          #取得觸發和濃縮器對話的位置   map9
        self.concentrator_dialogue_in_map9 = Jonny_concentrator_dialogue1_in_map9        #取得濃縮器的對話

        self.NPC1 = [250, 150]                                          #取得觸發和NPC1對話的位置   map9
        self.NPC1_dialogue_in_map9 = Jonny_NPC1_dialogue1_in_map9        #取得NPC1的對話

        self.NPC2 = [250, 300]                                          #取得觸發和NPC2對話的位置   map9
        self.NPC2_dialogue_in_map9 = Jonny_NPC2_dialogue1_in_map9        #取得NPC2的對話

        self.NPC3 = [300, 500]                                          #取得觸發和NPC3對話的位置   map9
        self.NPC3_dialogue_in_map9 = Jonny_NPC3_dialogue1_in_map9        #取得NPC3的對話

        self.NPC4 = [450, 100]                                          #取得觸發和NPC4對話的位置   map9
        self.NPC4_dialogue_in_map9 = Jonny_NPC4_dialogue1_in_map9        #取得NPC4的對話

        self.NPC5 = [650, 350]                                          #取得觸發和NPC5對話的位置   map9
        self.NPC5_dialogue_in_map9 = Jonny_NPC5_dialogue1_in_map9        #取得NPC5的對話

        self.NPC6 = [650, 500]                                          #取得觸發和NPC6對話的位置   map9
        self.NPc6_dialogue_in_map9 = Jonny_NPC6_dialogue1_in_map9        #取得NPC6的對話

        self.NPC7 = [850, 300]                                          #取得觸發和NPC7對話的位置   map9
        self.NPC7_dialogue_in_map9 = Jonny_NPC7_dialogue1_in_map9        #取得NPC7的對話

        self.DR1 = [900, 400]                                          #取得觸發和DR博士對話的位置   map9
        self.DR_dialogue_in_map9 = Jonny_DR_dialogue1_in_map9        #取得DR博士的對話

        self.sofa1 = [200, 100]                                          #取得觸發和沙發對話的位置   map9_1
        self.sofa_dialogue_in_map9_1 = Jonny_sofa_dialogue_in_map9_1        #取得沙發的對話

        self.tv = [300, 100]                                          #取得觸發和電視對話的位置   map9_1
        self.tv_dialogue_in_map9_1 = Jonny_tv_dialogue_in_map9_1        #取得電視的對話

        self.bucket = [250, 250]                                          #取得觸發和水桶對話的位置   map9_1
        self.bucket_dialogue_in_map9_1 = Jonny_bucket_dialogue_in_map9_1        #取得水桶的對話

        self.shower = [900, 400]                                          #取得觸發和淋浴設備對話的位置   map9_1
        self.shower_dialogue_in_map9_1 = Jonny_shower_dialogue_in_map9_1        #取得淋浴設備的對話

        self.virus1 = [900, 400]                                          #取得觸發和病毒對話的位置   map9_1
        self.virus_dialogue_in_map9_1 = Jonny_virus_dialogue1_in_map9_1        #取得病毒的對話

        self.sugar = [600, 250]                                          #取得觸發和蔗糖對話的位置   map9_1
        self.sugar_dialogue_in_map9_1 = Jonny_sugar_dialogue1_in_map9_1        #取得蔗糖的對話

        self.edta = [500, 400]                                          #取得觸發和edta對話的位置   map9_1
        self.edta_dialogue_in_map9_1 = Jonny_edta_dialogue1_in_map9_1        #取得edta的對話

        self.mgcl = [900, 50]                                          #取得觸發和mgcl對話的位置   map9_1
        self.mgcl_dialogue_in_map9_1 = Jonny_mgcl_dialogue1_in_map9_1        #取得mgcl的對話

        self.d80 = [350, 350]                                          #取得觸發和80對話的位置   map9_1
        self.d80_dialogue_in_map9_1 = Jonny_d80_dialogue1_in_map9_1        #取得80的對話

        self.NPC1_dialogue_in_map9_1 = Jonny_NPC1_dialogue_in_map9_1   #取得NPC1的對話      map9_1

        self.NPC2_dialogue_in_map9_1 = Jonny_NPC2_dialogue_in_map9_1    #取得NPC2的對話     map9_1

        self.door2_dialogue_in_map9_1 = Jonny_door2_dialogue1_in_map9_1     #取得和門2的對話        map9_1

        self.sis = [550, 50]                                            #取得和妹妹對話的位置
        self.sis_dialogue_in_map9_1 = Jonny_sis_dialogue_in_map9_1      #取得妹妹的位置

        self.dr2 = [500, 100]
        self.dr2_dialogue_in_map9_1 = Jonny_dr_dialogue_in_map9_1

        self.final = [650, 200]                                         #取得觸發和final對話的位置   map10
        self.final_dialogue_in_map10 = Jonny_final_dialogue1_in_map10       #取得和final的對話   map10

        self.sis_dialogue_in_map10 = Jonny_sis_dialogue_in_map10    #取得和妹妹的對話   map10

        self.dr_dialogue_in_map10 = Jonny_dr_dialogue_in_map10    #取得和Dr博士的對話   map10



        self.count = 0
        

    def draw_fade(self, player : Player):                #轉場動畫
        '''self.fade_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        self.fade_surface.blit(self.screen, (0, 0))'''
        fader = Fader(self.screen, self.screen, WIN_WIDTH, WIN_HEIGHT)
        fader.fade1()
        player.change_value = False

    def draw_fade1(self, player : Player):                #轉場動畫
        '''self.fade_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        self.fade_surface.blit(self.screen, (0, 0))'''
        fader = Fader(self.screen, self.screen, WIN_WIDTH, WIN_HEIGHT)
        fader.fade2()
        player.change_value_1 = False

    def draw_night(self):
        self.screen.blit(self.night_surface, (0, 0))

    def draw_dark(self):
        self.screen.blit(self.dark_surface, (0, 0))

    def draw_num(self, x, y):
        self.screen.blit(self.num_surface, (x, y))

    def draw_ele_f(self, x, y):                                  #畫出失敗的線
        self.screen.blit(self.ele_f_surface, (x, y))

    def draw_ele_s(self, x, y):                                  #畫出成功的線
        self.screen.blit(self.ele_s_surface, (x, y))

    def draw_ele_f_1(self, x, y):                                  #畫出失敗的線
        self.screen.blit(self.ele_f_1_surface, (x, y))

    def draw_ele_s_1(self, x, y):                                  #畫出成功的線
        self.screen.blit(self.ele_s_1_surface, (x, y))

    def draw_laser1(self):
        self.screen.blit(self.laser_surface1, (700, 150))

    def draw_laser2(self):
        self.screen.blit(self.laser_surface2, (700, 0))

    def draw_laser3(self):
        self.screen.blit(self.laser_surface3, (700, 250))

    def draw_ball1(self, x, y):
        self.screen.blit(self.ball1_surface, (x, y))

    def draw_ball2(self, x, y):
        self.screen.blit(self.ball2_surface, (x, y))

    def draw_ball3(self, x, y):
        self.screen.blit(self.ball3_surface, (x, y))

    def draw_ball4(self, x, y):
        self.screen.blit(self.ball4_surface, (x, y))

    

##########################################################################################
##########  X記得要加50
    def draw_map(self):                                 #畫出地圖
        x = 0
        y = 0
        #print(self.map)
        self.map = self.player.get_in_which_map()

        if self.dialogue.get_laser_value() == True and MAP7_BLOCK[11][0] == 0 :
            self.dialogue.laser1_value = True
        else:
            self.dialogue.laser1_value = False

        if MAP5[1][18] == 22 and MAP8[10][1] == 17 and MAP7_BLOCK[0][0] == 0 :
            self.dialogue.laser_value = True
            if MAP7_BLOCK[11][0] == 0:
                MAP5_BLOCK[11][18] = 0
        else:
            MAP7_BLOCK[0][0] = 1
            self.dialogue.laser_value = False

        if self.dialogue.laser_value == True:
            MAP7_BLOCK[3][14] = 1
            MAP7_BLOCK[4][14] = 1
            MAP7_BLOCK[5][14] = 1
            MAP7_BLOCK[6][14] = 1
            MAP7_BLOCK[7][14] = 1
            MAP7_BLOCK[8][14] = 1
            MAP7_BLOCK[9][14] = 1
            MAP7_BLOCK[10][14] = 1
        else :
            MAP7_BLOCK[3][14] = 0
            MAP7_BLOCK[4][14] = 0
            MAP7_BLOCK[5][14] = 0
            MAP7_BLOCK[6][14] = 0
            MAP7_BLOCK[7][14] = 0
            MAP7_BLOCK[8][14] = 0
            MAP7_BLOCK[9][14] = 0
            MAP7_BLOCK[10][14] = 0

        if self.dialogue.laser1_value == True:
            MAP5_BLOCK[1][14] = 1
            MAP5_BLOCK[2][14] = 1
            MAP5_BLOCK[3][14] = 1
            MAP5_BLOCK[4][14] = 1

            MAP5_BLOCK[5][15] = 1
            MAP5_BLOCK[5][16] = 1
            MAP5_BLOCK[5][17] = 1
            MAP5_BLOCK[5][18] = 1
        else :
            MAP5_BLOCK[1][14] = 0
            MAP5_BLOCK[2][14] = 0
            MAP5_BLOCK[3][14] = 0
            MAP5_BLOCK[4][14] = 0

            MAP5_BLOCK[5][15] = 0
            MAP5_BLOCK[5][16] = 0
            MAP5_BLOCK[5][17] = 0
            MAP5_BLOCK[5][18] = 0
            


        if self.map == MAP1:
            self.draw_bg_map1()
            self.dialogue.dark_b = False
            for i in self.map:
                for j in i:
                    #self.draw_floor(x, y)
                    if j == 10 :
                        self.draw_rock(x, y)
                        #x += 50
                    elif j == 5:
                        self.draw_key(x, y)
                        #x += 50
                    elif j == 90:
                        self.draw_door(x, y)
                        #x += 50
                    elif j == 3:
                        self.draw_DR(x, y)
                        #x += 50
                    else :
                        x += 50
                x = 0
                y += 50

        elif self.map == MAP2:
            self.draw_bg_map2()
            self.dialogue.dark_b = False
            for i in self.map:
                for j in i:
                    if j == 13:
                        self.draw_virus(x, y)

                    if j == 11:
                        self.draw_nose(x, y)

                    elif j == 2:
                        self.draw_joker(x, y)
                    else :
                        x += 50
                x = 0
                y += 50

        elif self.map == MAP3:
            self.draw_bg_map3()
            self.dialogue.dark_b = False

        elif self.map == MAP4:
            self.draw_bg_map4()
            self.dialogue.dark_b = False

            for i in self.map:
                for j in i:
                    
                    if j == 15:
                        self.draw_virus_1(x, y)
                    else :
                        x += 50
                x = 0
                y += 50

        elif self.map == MAP4_1:
            self.draw_bg_map4_1()
            for i in self.map:
                for j in i:
                    if j == 3:
                        if self.dialogue.get_dark():
                            self.draw_num(x, y)
                    else :
                        x += 50
                x = 0
                y += 50

        elif self.map == MAP5:
            self.draw_bg_map5()
            if MAP5[1][18] == 6 or MAP8[10][1] == 6:
                self.dialogue.dark_b = True
            else:
                if MAP5_BLOCK[0][0]:
                    self.dialogue.dark_b = True
                else:
                    self.dialogue.dark_b = False

            for i in self.map:
                for j in i:
                    if j == 13:
                        self.draw_trap(x, y)
                        x += 50
                    elif j == 6:
                        self.draw_ele_f(x, y)
                        x += 50
                    elif j == 22:
                        self.draw_ele_s(x, y)  
                        x += 50      
                    elif j == 30:
                        self.draw_ball1(x, y)
                        x += 50  
                    elif j == 31:
                        self.draw_ball2(x, y)  
                        x += 50
                    elif j == 32:
                        self.draw_ball3(x, y) 
                        x += 50 
                    elif j == 33:
                        self.draw_ball4(x, y)  
                        x += 50          
                    else :
                        x += 50
                x = 0
                y += 50

        elif self.map == MAP6:
            self.draw_bg_map6()
            if MAP5[1][18] == 6 or MAP8[10][1] == 6:
                self.dialogue.dark_b = True
            else:
                if MAP5_BLOCK[0][0]:
                    self.dialogue.dark_b = True
                else:
                    self.dialogue.dark_b = False
            for i in self.map:
                for j in i:
                    if j == 6:
                        self.draw_gas(x, y)
                        x += 50
                    elif j ==25:
                        self.draw_girl(x, y)
                        x += 50
                    else :
                        x += 50
                x = 0
                y += 50

        elif self.map == MAP7:
            self.draw_bg_map7()
            if MAP5[1][18] == 6 or MAP8[10][1] == 6:
                self.dialogue.dark_b = True

            else:
                if MAP5_BLOCK[0][0]:
                    self.dialogue.dark_b = True
                else:
                    self.dialogue.dark_b = False

            for i in self.map:
                for j in i:
                    if j == 2:
                        self.draw_hammer(x, y)
                    else :
                        x += 50
                x = 0
                y += 50

        elif self.map == MAP8:
            self.draw_bg_map8()
            if MAP5[1][18] == 6 or MAP8[10][1] == 6:
                self.dialogue.dark_b = True
                MAP8[7][15] = 4
                MAP8[7][16] = 4     #水的位置
                MAP8[7][17] = 4
                MAP8[7][18] = 4
                MAP8[8][15] = 4
                MAP8[8][16] = 4
                MAP8[8][17] = 4
                MAP8[8][18] = 4
                MAP8[9][15] = 4
                MAP8[9][16] = 4
                MAP8[10][15] = 4
                MAP8[10][16] = 4
                MAP8[9][17] = 4

                MAP8[6][15] = 5
                MAP8[6][16] = 5     #水的位置
                MAP8[6][17] = 5
                MAP8[6][18] = 5
                MAP8[7][14] = 5
                MAP8[8][14] = 5
                MAP8[9][14] = 5
                MAP8[10][14] = 5

                MAP8_BLOCK[7][15] = 1
                MAP8_BLOCK[7][16] = 1     #水的位置
                MAP8_BLOCK[7][17] = 1
                MAP8_BLOCK[7][18] = 1
                MAP8_BLOCK[8][15] = 1
                MAP8_BLOCK[8][16] = 1
                MAP8_BLOCK[8][17] = 1
                MAP8_BLOCK[8][18] = 1
                MAP8_BLOCK[9][15] = 1
                MAP8_BLOCK[9][16] = 1
                MAP8_BLOCK[10][15] = 1
                MAP8_BLOCK[10][16] = 1
            else:
                if MAP5_BLOCK[0][0]:
                    self.dialogue.dark_b = True
                else:
                    self.dialogue.dark_b = False
            for i in self.map:
                for j in i:
                    if j == 17:
                        self.draw_ele_s_1(x, y)
                        x += 50
                    elif j == 6 :
                        self.draw_ele_f_1(x, y)
                        x += 50
                    elif j == 4 :
                        self.draw_water(x, y)
                        x += 50
                    elif j == 10 :
                        self.draw_ice(x, y)
                        x += 50
                    
                    else :
                        x += 50
                x = 0
                y += 50

        elif self.map == MAP9:
            self.draw_bg_map9()
            self.dialogue.dark_b = False
            for i in self.map:
                for j in i:
                    if j == 25:
                        self.draw_girl(x, y)
                        x += 50
                    else :
                        x += 50
                x = 0
                y += 50

        elif self.map == MAP9_1:
            self.draw_bg_map9_1()
            self.dialogue.dark_b = False

            for i in self.map:
                for j in i:
                    
                    if j == 3:
                        self.draw_virus_map9_1(x, y)
                        x += 50
                    elif j == 20:
                        if self.dialogue.dark:
                            self.draw_moon(x, y)
                            x += 50
                        else:
                            x += 50
                    elif j == 21:
                        if self.dialogue.dark:
                            self.draw_star(x, y)
                            x += 50
                        else:
                            x += 50
                    elif j ==25:
                        self.draw_girl(x, y)
                        x += 50

                    elif j == 30:
                        self.draw_DR(x, y)
                        x += 50
                    
                    else :
                        x += 50
                x = 0
                y += 50

        elif self.map == MAP10:
            self.draw_bg_map10()
            self.dialogue.dark_b = False
            for i in self.map:
                for j in i:
                    if j == 25:
                        self.draw_girl(x, y)
                        x += 50
                    elif j == 30:
                        self.draw_DR(x, y)
                        x += 50
                    else :
                        x += 50
                x = 0
                y += 50
            
            
    
##################################################################################################

    def draw_paint(self):                               #畫出地圖8的畫像
        self.screen.blit(self.paint_surface, (50, 50))

#############################################################################################################      MAP1開始線

    def draw_bg_map1(self):                      #畫出背景
        #self.surface.blit(bg_image, (0, 0))
        self.screen.blit(self.bg_surface_map1, (0, 0))

########################################################################

    def draw_key(self, x : int, y : int):                      #畫出鑰匙
        self.screen.blit(self.key_surface, (x, y))

########################################################################

    def draw_charactor(self, player : Player):           #畫出角色
        self.image = self.player.get_role_image()
        self.player_down_surface = pygame.Surface(( WIDTH, HEIGHT ), pygame.SRCALPHA)
        self.player_down_surface.blit(self.image, (0, 0))
        self.screen.blit(self.player_down_surface, player.rect)

########################################################################      

    def draw_DR(self, x : int, y : int):                    #畫出博士
        self.screen.blit(self.dr_surface, (x, y))

########################################################################

    def draw_door(self, x : int, y : int):                  #畫出門
        self.screen.blit(self.door_surface, (x, y))
    
########################################################################

    def draw_rock(self, x : int, y : int):                  #畫出石頭
        self.screen.blit(self.rock_surface, (x, y))

###################################################################################################     MAP1終止線    MAP2開始線     

    def draw_bg_map2(self):                                 #畫出地圖2的bg
        self.screen.blit(self.bg_surface_map2, (0, 0))

###################################################################################################     

    def draw_joker(self, x, y):                             #畫出地圖2的小丑
        self.screen.blit(self.joker_surface_map2, (x, y))


##################################################################################################

    def draw_nose(self, x, y):                             #畫出地圖2的鼻子
        self.screen.blit(self.nose_surface_map2, (x, y))

##################################################################################################

    def draw_virus(self, x, y):                             #畫出地圖2的病毒
        self.screen.blit(self.virus_surface_map2, (x, y))

###################################################################################################     MAP2終止線   MAP3開始線

    def draw_bg_map3(self):                                 #畫出地圖3的bg
        self.screen.blit(self.bg_surface_map3, (0, 0))

 ##################################################################################################     MAP3終止線   MAP4開始線

###################################################################################################     
 
    def draw_bg_map4(self):                                 #畫出地圖4的bg1
        self.screen.blit(self.bg_surface_map4, (0, 0))

##################################################################################################

    def draw_bg_map4_1(self):                               #畫出地圖4的bg2
        self.screen.blit(self.bg_surface_map4_1, (0, 0))

##################################################################################################

    def draw_virus_1(self, x, y):                                 #畫出地圖4的病毒
        self.screen.blit(self.virus_surface_map4, (x, y))

###################################################################################################     MAP4終止線   MAP5開始線

##################################################################################################

    def draw_bg_map5(self):                               #畫出地圖5的bg
        self.screen.blit(self.bg_surface_map5, (0, 0))

##################################################################################################

    def draw_trap(self, x, y):                                  #畫出地圖5的尖刺
        self.screen.blit(self.trap_surface, (x, y))

####################################################################################################  MAP5終止線  MAP6開始線

##################################################################################################

    def draw_bg_map6(self):                               #畫出地圖6的bg
        self.screen.blit(self.bg_surface_map6, (0, 0))

##################################################################################################

    def draw_gas(self, x, y):                                  #畫出地圖6的毒氣
        self.screen.blit(self.gas_surface, (x, y))

##################################################################################################

    def draw_girl(self, x, y):                                  #畫出地圖6的妹妹
        self.screen.blit(self.girl_surface, (x, y))


####################################################################################################  MAP6終止線  MAP7開始線

##################################################################################################

    def draw_bg_map7(self):                               #畫出地圖7的bg
        self.screen.blit(self.bg_surface_map7, (0, 0))

    def draw_hammer(self, x, y):                               #畫出地圖7的槌子
        self.screen.blit(self.hammer_surface_map7, (x, y))

##################################################################################################


####################################################################################################  MAP7終止線  MAP8開始線

##################################################################################################

    def draw_bg_map8(self):                               #畫出地圖8的bg
        self.screen.blit(self.bg_surface_map8, (0, 0))

##################################################################################################

    def draw_water(self, x, y):                         #畫出水地板
        self.screen.blit(self.water_surface, (x, y))

##################################################################################################

    def draw_ice(self, x, y):                           #畫出冰地板
        self.screen.blit(self.ice_surface, (x, y))

##################################################################################################

####################################################################################################  MAP8終止線  MAP9開始線

####################################################################################################

    def draw_bg_map9(self):                            # 畫出地圖9 的bg
        self.screen.blit(self.bg_surface_map9, (0, 0))

####################################################################################################

    def draw_bg_map9_1(self):                            # 畫出地圖9_1 的bg
        self.screen.blit(self.bg_surface_map9_1, (0, 0))

###################################################################################################

    def draw_virus_map9_1(self, x, y):                            # 畫出地圖9_1 的病毒
        self.screen.blit(self.virus_surface_map9_1, (x, y))

###################################################################################################

    def draw_star(self, x, y):                            # 畫出地圖9_1 的星星
        self.screen.blit(self.star_surface, (x, y))

###################################################################################################

    def draw_moon(self, x, y):                            # 畫出地圖9_1 的月亮
        self.screen.blit(self.moon_surface, (x, y))



####################################################################################################

####################################################################################################  MAP9終止線  MAP10開始線

###################################################################################################

    def draw_bg_map10(self):                            # 畫出地圖10的bg
        self.screen.blit(self.bg_surface_map10, (0, 0))

####################################################################################################  MAP10終止線  


    def draw_text_map1(self, dialogue : Dialogue, dialogue_list : list ):
        
        self.screen.blit(dialogue_outline_map1_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count() -1 ], True, WHITE)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

###################################################################################################### 

    def draw_text_map2(self, dialogue : Dialogue, dialogue_list : list ):
        
        self.screen.blit(dialogue_outline_map2_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count() -1 ], True, ORANGE)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

########################################################################################################

    def draw_text_map3(self, dialogue : Dialogue, dialogue_list : list ):
        
        self.screen.blit(dialogue_outline_map3_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count() -1 ], True, BROWN)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

########################################################################################################

    def draw_text_map4(self, dialogue : Dialogue, dialogue_list : list ):
        
        self.screen.blit(dialogue_outline_map4_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count() -1 ], True, OTHER_BROWN)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

########################################################################################################

    def draw_text_map5(self, dialogue : Dialogue, dialogue_list : list ):
        
        self.screen.blit(dialogue_outline_map5_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count() -1 ], True, BLACK)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

########################################################################################################

    def draw_text_map6(self, dialogue : Dialogue, dialogue_list : list ):
        
        self.screen.blit(dialogue_outline_map6_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count() -1 ], True, OTHER_GREEN)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

########################################################################################################

    def draw_text_map10(self, dialogue : Dialogue, dialogue_list : list ):
        
        self.screen.blit(dialogue_outline_map10_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count() -1 ], True, BLACK)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)


###########################################################################################################

    def draw_plot_text_map1(self, dialogue : Dialogue, dialogue_list : list):

        self.screen.blit(dialogue_outline_map1_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count()  ], True, WHITE)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

###########################################################################################################

    def draw_plot_text_map2(self, dialogue : Dialogue, dialogue_list : list):

        self.screen.blit(dialogue_outline_map2_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count()  ], True, ORANGE)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

###########################################################################################################

    def draw_plot_text_map3(self, dialogue : Dialogue, dialogue_list : list):
        
        self.screen.blit(dialogue_outline_map3_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count()  ], True, BROWN)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

###########################################################################################################

    def draw_plot_text_map4(self, dialogue : Dialogue, dialogue_list : list):

        self.screen.blit(dialogue_outline_map4_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count()  ], True, OTHER_BROWN)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

###########################################################################################################

    def draw_plot_text_map5(self, dialogue : Dialogue, dialogue_list : list):

        self.screen.blit(dialogue_outline_map5_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count()  ], True, BLACK)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)
    
###########################################################################################################

    def draw_plot_text_map6(self, dialogue : Dialogue, dialogue_list : list):

        self.screen.blit(dialogue_outline_map6_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count()  ], True, OTHER_GREEN)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)

###########################################################################################################

    def draw_plot_text_map10(self, dialogue : Dialogue, dialogue_list : list):

        self.screen.blit(dialogue_outline_map10_image, (200, 450))
        text_surface = self.font.render(  dialogue_list  [dialogue.get_count()  ], True, BLACK)
        text_Rect = text_surface.get_rect()
        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
        self.screen.blit(text_surface, text_Rect)



############################################################################################################

    def draw_dialogue(self, dialogue : Dialogue):                                   #畫出對話

        if dialogue.get_open_dialogue():

            self.map = self.player.get_in_which_map()                               #取得角色在哪個地圖

            self.door1 = self.location.get_door1_location()                          # 取得門2對話的位置

            self.door2 = self.location.get_door2_location()                          # 取得門2對話的位置

            self.door1_dialogue_in_map1 = dialogue.door1_dialogue_in_map1            #取得門1對話 map1
            
            self.rock = self.location.get_rock_location()                            # 取得石頭對話的位置
            self.rock_dialogue_in_map1 = dialogue.rock_dialogue_in_map1              #取得石頭對話

            self.key = self.location.get_key_location()                              # 取得鑰匙對話的位置
            self.key_dialogue_in_map1 = dialogue.key1_dialogue_in_map1               #取得鑰匙對話

            self.murmur1 = self.location.get_murmur1()                              # 取得自我對話的位置1
            self.murmur2 = self.location.get_murmur2()                              #取得自我對話的位置2

            self.murmur_dialogue_in_map1 = dialogue.murmur_dialogue_in_map1          #取得自我對話   map1

            self.murmur_dialogue_in_map7 = dialogue.murmur_dialogue_in_map7          #取得自我對話 map7

            self.murmur_dialogue_in_map10 = dialogue.murmur_dialogue_in_map10       #取得自我對話 map10

################################################################################################################


            self.joker = self.location.get_joker_location()                          # 取得小丑對話的位置
            self.joker_dialogue_in_map2 = dialogue.joker_dialogue_in_map2            #取得小丑對話

            self.nose = self.location.get_nose_location()                          # 取得小丑對話的位置
            self.nose_dialogue_in_map2 = dialogue.nose_dialogue_in_map2            #取得小丑對話

            self.game = self.location.get_game_location()                          # 取得遊戲對話的位置
            self.game_dialogue_in_map2 = dialogue.game_dialogue_in_map2            #取得遊戲對話

            self.virus = self.location.get_virus_location()                          # 取得遊戲對話的位置
            self.virus_dialogue_in_map2 = dialogue.virus_dialogue_in_map2            #取得遊戲對話

################################################################################################################


            self.sign1 = self.location.get_sign1_location()                          # 取得公告1對話的位置
            self.sign1_dialogue_in_map3 = dialogue.sign1_dialogue_in_map3            #取得公告1對話

            self.sign2 = self.location.get_sign2_location()                          # 取得公告2對話的位置
            self.sign2_dialogue_in_map3 = dialogue.sign2_dialogue_in_map3            #取得公告2對話

            self.blue = self.location.get_blue_location()                         #取得觸發藍色矮人對話的位置
            self.blue_dialogue_in_map3 = dialogue.blue_dialogue_in_map3            #取得藍色矮人對話

            self.yellow = self.location.get_yellow_location()                        #取得觸發黃色矮人對話的位置
            self.yellow_dialogue_in_map3 = dialogue.yellow_dialogue_in_map3            #取得黃色矮人對話

            self.red = self.location.get_red_location()                             #取得觸發紅色矮人對話的位置
            self.red_dialogue_in_map3 = dialogue.red_dialogue_in_map3            #取得紅色矮人對話

            self.green = self.location.get_green_location()                         #取得觸發綠色矮人對話的位置
            self.green_dialogue_in_map3 = dialogue.green_dialogue_in_map3            #取得綠色矮人對話

            self.gray = self.location.get_gray_location()                            #取得觸發灰色矮人對話的位置
            self.gray_dialogue_in_map3 = dialogue.gray_dialogue_in_map3            #取得灰色矮人對話

            self.purple = self.location.get_purple_location()                       #取得觸發紫色矮人對話的位置
            self.purple_dialogue_in_map3 = dialogue.purple_dialogue_in_map3            #取得紫色矮人對話

            self.key1 = self.location.get_key1_location()                           #取得觸發鑰匙對話的位置  map3
            self.key_dialogue_in_map3 = dialogue.key_dialogue_in_map3               #取得鑰匙對話       map3

            self.door_dialogue_in_map3 = dialogue.door_dialogue_in_map3            #取得門2對話   map3

################################################################################################################


            self.door_dialogue_in_map4 = dialogue.door_dialogue_in_map4           # 取得門2對話   map4

            self.vase = self.location.get_vase_location()                            # 取得觸發和花瓶對話的位置 map4
            self.vase_dialogue_in_map4 = dialogue.vase_dialogue_in_map4             #取得花瓶對話

            self.shelf = self.location.get_shelf_location()                            #取得觸發和書櫃對話的位置
            self.shelf_dialogue_in_map4 = dialogue.shelf_dialogue_in_map4            #取得書櫃對話

            self.clock = self.location.get_clock_location()                           #取得觸發和時鐘對話的位置
            self.clock_dialogue_in_map4 = dialogue.clock_dialogue_in_map4           #取得時鐘對話

            self.eagle = self.location.get_eagle_location()                           #取得觸發和老鷹對話的位置
            self.eagle_dialogue_in_map4 = dialogue.eagle_dialogue_in_map4            #取得老鷹對話

            self.sofa = self.location.get_sofa_location()                             #取得觸發和沙發對話的位置
            self.sofa_dialogue_in_map4 = dialogue.sofa_dialogue_in_map4             #取得沙發對話

            self.floor = self.location.get_floor_location()                           #取得觸發和地板對話的位置
            self.floor_dialogue_in_map4 = dialogue.floor_dialogue_in_map4           #取得地板對話

            self.light = self.location.get_light_location()                           # 取得觸發和燈對話的位置 
            self.light_dialogue_in_map4 = dialogue.light_dialogue_in_map4            #取得燈對話

            self.owl = self.location.get_owl_location()                               #取得觸發和貓頭鷹對話的位置
            self.owl_dialogue_in_map4 = dialogue.owl_dialogue_in_map4               #取得貓頭鷹對話

            self.crow = self.location.get_crow_location()                             #取得觸發和烏鴉對話的位置
            self.crow_dialogue_in_map4 = dialogue.crow_dialogue_in_map4             #取得烏鴉對話

            self.virus_1 = self.location.get_virus_1_location()                       #取得觸發和病毒對話的位置 map4
            self.virus_dialogue_in_map4 = dialogue.virus_dialogue_in_map4             #取得病毒對話

            self.key2 = self.location.get_key2_location()                           #取得觸發花對話的位置  map4
            self.flower_dialogue_in_map4 = dialogue.key_dialogue_in_map4           #取得花對話

            self.sign3 = self.location.get_sign3_location()                     #取得觸發公告3對話的位置 map4
            self.sign_dialogue_in_map4 = dialogue.sign_dialogue_in_map4         #取得公告3的對話

            self.shelf1 = self.location.get_shelf1_location()                     #取得觸發書櫃1對話的位置 map4
            self.shelf1_dialogue_in_map4 = dialogue.shelf1_dialogue_in_map4         #取得書櫃1的對話

            self.treasure2 = self.location.get_treasure2_location()                     #取得觸發密碼寶箱對話的位置 map4
            self.shelf1_dialogue_in_map6 = dialogue.treasure_dialogue_in_map6         #取得密碼寶箱的對話

################################################################################################################


            self.treasure1 = self.location.get_treasure_location()              #取得觸發和寶箱1對話的位置   map5
            self.treasure_dialogue_in_map5 = dialogue.treasure_dialogue_in_map5   #取得寶箱1的對話   

            self.light1 = self.location.get_light1_location()                  #取得觸發和燈管對話的位置   map5
            self.light_dialogue_in_map5 = dialogue.light_dialogue_in_map5         #取得燈管的對話   

            self.ele = self.location.get_ele_location()                         #取得觸發和電線對話的位置   map5
            self.ele_dialogue_in_map5 = dialogue.ele_dialogue_in_map5             #取得電線的對話   

            self.mirror = self.location.get_mirror_location()                   #取得觸發和鏡子對話的位置   map5
            self.mirror_dialogue_in_map5 = dialogue.mirror_dialogue_in_map5        #取得鏡子的對話

            self.door_dialogue_in_map5 = dialogue.door_dialogue_in_map5           #取得門的對話   
    
            self.altar = self.location.get_altar_location()                  #取得觸發和祭壇對話的位置   map5
            self.altar_dialogue_in_map5 = dialogue.altar_dialogue_in_map5         #取得祭壇的對話 

            self.urn = self.location.get_urn_location()                    #取得觸發和酒桶對話的位置   map5
            self.urn_dialogue_in_map5 = dialogue.urn_dialogue_in_map5             #取得酒桶的對話   

            self.wall = self.location.get_wall_location()                   #取得觸發和牆壁對話的位置   map5
            self.wall_dialogue_in_map5 = dialogue.wall_dialogue_in_map5           #取得牆壁的對話

            self.trap = self.location.get_trap_location()                   #取得觸發和陷阱對話的位置   map5
            self.trap_dialogue_in_map5 = dialogue.trap_dialogue_in_map5           #取得陷阱的對話

            self.urn1 = self.location.get_urn1_location()                   #取得觸發和酒桶1對話的位置   map5
            self.urn1_dialogue_in_map5 = dialogue.urn1_dialogue_in_map5           #取得酒桶1的對話

            self.urn2 = self.location.get_urn2_location()                   #取得觸發和酒桶2對話的位置   map5
            self.urn2_dialogue_in_map5 = dialogue.urn2_dialogue_in_map5           #取得酒桶2的對話

            self.sign4 = self.location.get_sign4_location()                   #取得觸發和公告4對話的位置   map5
            self.sign4_dialogue_in_map5 = dialogue.sign4_dialogue_in_map5           #取得公告4的對話

            self.ladder = self.location.get_ladder_location()                   #取得觸發和梯子對話的位置   map5
            self.ladder_dialogue_in_map5 = dialogue.ladder_dialogue_in_map5           #取得梯子的對話

            self.cloth_g = self.location.get_cloth_g_location()                   #取得觸發和女生衣服對話的位置   map5
            self.cloth_g_dialogue_in_map5 = dialogue.cloth_g_dialogue_in_map5           #取得女生衣服的對話

            self.cloth_b = self.location.get_cloth_b_location()                   #取得觸發和男生衣服對話的位置   map5
            self.cloth_b_dialogue_in_map5 = dialogue.cloth_b_dialogue_in_map5           #取得男生衣服的對話

            self.small_shelf = self.location.get_small_shelf_location()             #取得觸發和小櫥櫃對話的位置   map5
            self.small_shelf_dialogue_in_map5 = dialogue.small_shelf_dialogue_in_map5      #取得小櫥櫃的對話


################################################################################################################

            self.treasure_dialogue_in_map6 = dialogue.treasure_dialogue_in_map6           #取得寶藏的對話 map6

            self.fan = self.location.get_fan_location()                   #取得觸發和風扇對話的位置   map6
            self.fan_dialogue_in_map6 = dialogue.fan_dialogue_in_map6           #取得風扇的對話

            self.gas = self.location.get_gas_location()                   #取得觸發和毒氣對話的位置   map6
            self.gas_dialogue_in_map6 = dialogue.gas_dialogue_in_map6           #取得毒氣的對話

            self.lamp = self.location.get_lamp_location()                   #取得觸發和檯燈對話的位置   map6
            self.lamp_dialogue_in_map6 = dialogue.lamp_dialogue_in_map6           #取得檯燈的對話

            self.bench = self.location.get_bench_location()                   #取得觸發和板凳對話的位置   map6
            self.bench_dialogue_in_map6 = dialogue.bench_dialogue_in_map6           #取得板凳的對話

            self.fireplace = self.location.get_fireplace_location()           #取得觸發和壁爐對話的位置   map6
            self.fireplace_dialogue_in_map6 = dialogue.fireplace_dialogue_in_map6           #取得壁爐的對話

            self.grass = self.location.get_grass_location()                   #取得觸發和盆栽對話的位置   map6
            self.grass_dialogue_in_map6 = dialogue.grass_dialogue_in_map6           #取得盆栽的對話

            self.treasure2 = self.location.get_treasure2_location()                   #取得觸發和密碼寶箱對話的位置   map6
            self.treasure2_dialogue_in_map6 = dialogue.treasure2_dialogue_in_map6           #取得密碼寶箱的對話

            self.front = self.location.get_front_location()
            self.laser1_dialogue_in_map7 = dialogue.laser1_dialogue_in_map7 



################################################################################################################

            self.hammer = self.location.get_hammer_location()                   #取得觸發和槌子對話的位置   map7
            self.hammer_dialogue_in_map7 = dialogue.hammer_dialogue_in_map7           #取得槌子的對話

            self.ele_dialogue_in_map7 = dialogue.ele_dialogue_in_map7           #取得電線的對話 map7

            self.wall_dialogue_in_map7 = dialogue.wall_dialogue_in_map7           #取得牆壁的對話 map7

            self.rock1 = self.location.get_rock1_location()                 #取得觸發和石頭對話的位置   map7
            self.rock1_dialogue_in_map7 = dialogue.rock_dialogue_in_map7           #取得石頭的對話

            self.box = self.location.get_box_location()                 #取得觸發和工具箱對話的位置   map7
            self.box_dialogue_in_map7 = dialogue.box_dialogue_in_map7           #取得工具箱的對話

            self.pliers = self.location.get_pliers_location()               #取得觸發和鉗子對話的位置   map7
            self.pliers_dialogue_in_map7 = dialogue.pliers_dialogue_in_map7           #取得鉗子的對話

            self.shelf2 = self.location.get_shelf2_location()                 #取得觸發和櫥櫃對話的位置   map7
            self.shelf_dialogue_in_map7 = dialogue.shelf_dialogue_in_map7           #取得櫥櫃的對話

            self.frame = self.location.get_frame_location()              #取得觸發和相框對話的位置   map7
            self.frame_dialogue_in_map7 = dialogue.frame_dialogue_in_map7           #取得相框的對話

            self.laser = self.location.get_laser_location()                 #取得觸發和雷射光對話的位置   map7
            self.laser_dialogue_in_map7 = dialogue.laser_dialogue_in_map7           #取得雷射光的對話

            self.dead = self.location.get_dead_location()                    #取得觸發和骷髏頭對話的位置   map7
            self.dead_dialogue_in_map7 = dialogue.dead_dialogue_in_map7           #取得骷髏頭的對話


################################################################################################################

            self.refri = self.location.get_refri_location()                   #取得觸發和冰箱對話的位置   map8
            self.refri_dialogue_in_map8 = dialogue.refri_dialogue_in_map8           #取得冰箱的對話

            self.water = self.location.get_water_location()                   #取得觸發和水對話的位置   map8
            self.water_dialogue_in_map8 = dialogue.water_dialogue_in_map8           #取得水的對話

            self.btn = self.location.get_btn_location()                     #取得觸發和按鈕對話的位置   map8
            self.btn_dialogue_in_map8 = dialogue.btn_dialogue_in_map8           #取得按鈕的對話

            self.paint = self.location.get_paint_location()                     #取得觸發和相框對話的位置   map8
            self.paint_dialogue_in_map8 = dialogue.paint_dialogue_in_map8           #取得相框的對話

            self.ele_dialogue_in_map8 = dialogue.ele_dialogue_in_map8           #取得電線的對話 map8

            self.flute = self.location.get_flute_location()                      #取得觸發和長笛對話的位置   map8
            self.flute_dialogue_in_map8 = dialogue.flute_dialogue_in_map8           #取得長笛的對話

            self.violin_box = self.location.get_violin_box_location()              #取得觸發和小提琴箱子對話的位置   map8
            self.violin_box_dialogue_in_map8 = dialogue.violin_box_dialogue_in_map8           #取得小提琴箱子的對話

            self.violin = self.location.get_violin_location()                   #取得觸發和小提琴對話的位置   map8
            self.violin_dialogue_in_map8 = dialogue.violin_dialogue_in_map8           #取得小提琴的對話

            self.piano = self.location.get_piano_location()                     #取得觸發和鋼琴對話的位置   map8
            self.piano_dialogue_in_map8 = dialogue.piano_dialogue_in_map8           #取得鋼琴的對話

            self.cello = self.location.get_cello_location()                     #取得觸發和大提琴對話的位置   map8
            self.cello_dialogue_in_map8 = dialogue.cello_dialogue_in_map8           #取得大提琴的對話

            self.trumpet = self.location.get_trumpet_location()                 #取得觸發和法國號對話的位置   map8
            self.trumpet_dialogue_in_map8 = dialogue.trumpet_dialogue_in_map8           #取得法國號的對話


################################################################################################################

            self.cabinet = self.location.get_cabinet_location()            #取得觸發和櫃子對話的位置   map9
            self.cabinet_dialogue_in_map9 = dialogue.cabinet_dialogue_in_map9      #取得櫃子的對話

            self.mashine1 = self.location.get_mashine1_location()          #取得觸發和機器1對話的位置   map9
            self.mashine1_dialogue_in_map9 = dialogue.mashine1_dialogue_in_map9      #取得機器1的對話

            self.mashine2 = self.location.get_mashine2_location()                   #取得觸發和機器2對話的位置   map9
            self.mashine2_dialogue_in_map9 = dialogue.mashine2_dialogue_in_map9      #取得機器2的對話

            self.mashine3 = self.location.get_mashine3_location()              #取得觸發和機器3對話的位置   map9
            self.mashine3_dialogue_in_map9 = dialogue.mashine3_dialogue_in_map9      #取得機器3的對話

            self.micro = self.location.get_micro_location()           #取得觸發和顯微鏡對話的位置   map9
            self.micro_dialogue_in_map9 = dialogue.micro_dialogue_in_map9      #取得顯微鏡的對話

            self.screen1 = self.location.get_screen_location()             #取得觸發和螢幕對話的位置   map9
            self.screen_dialogue_in_map9 = dialogue.screen_dialogue_in_map9      #取得櫃螢幕對話

            self.alcohol = self.location.get_alcohol_location()                 #取得觸發和酒精對話的位置   map9
            self.alcohol_dialogue_in_map9 = dialogue.alcohol_dialogue_in_map9      #取得酒精的對話

            self.nacl = self.location.get_nacl_location()                   #取得觸發和氯化鈉對話的位置   map9
            self.nacl_dialogue_in_map9 = dialogue.nacl_dialogue_in_map9      #取得氯化鈉的對話

            self.concentrator = self.location.get_concentrator_location()      #取得觸發和濃縮器對話的位置   map9
            self.concentrator_dialogue_in_map9 = dialogue.concentrator_dialogue_in_map9      #取得濃縮器的對話

            self.NPC1 = self.location.get_NPC1_location()                    #取得觸發和NPC1對話的位置   map9
            self.NPC1_dialogue_in_map9 = dialogue.NPC1_dialogue_in_map9      #取得NPC1的對話

            self.NPC2 = self.location.get_NPC2_location()               #取得觸發和NPC2對話的位置   map9
            self.NPC2_dialogue_in_map9 = dialogue.NPC2_dialogue_in_map9      #取得NPC2的對話

            self.NPC3 = self.location.get_NPC3_location()              #取得觸發和NPC3對話的位置   map9
            self.NPC3_dialogue_in_map9 = dialogue.NPC3_dialogue_in_map9      #取得NPC3的對話

            self.NPC4 = self.location.get_NPC4_location()             #取得觸發和NPC4對話的位置   map9
            self.NPC4_dialogue_in_map9 = dialogue.NPC4_dialogue_in_map9      #取得NPC4的對話

            self.NPC5 = self.location.get_NPC5_location()           #取得觸發和NPC5對話的位置   map9
            self.NPC5_dialogue_in_map9 = dialogue.NPC5_dialogue_in_map9      #取得NPC5的對話

            self.NPC6 = self.location.get_NPC6_location()              #取得觸發和NPC6對話的位置   map9
            self.NPC6_dialogue_in_map9 = dialogue.NPC6_dialogue_in_map9      #取得NPC6的對話

            self.NPC7 = self.location.get_NPC7_location()          #取得觸發和NPC7對話的位置   map9
            self.NPC7_dialogue_in_map9 = dialogue.NPC7_dialogue_in_map9      #取得NPC7的對話

            self.DR1 = self.location.get_DR1_location()             #取得觸發和DR博士對話的位置   map9
            self.DR_dialogue_in_map9 = dialogue.DR_dialogue_in_map9      #取得DR博士的對話

################################################################################################################

            self.sofa1 = self.location.get_sofa1_location()             #取得觸發和沙發對話的位置   map9_1
            self.sofa_dialogue_in_map9_1 = dialogue.sofa_dialogue_in_map9_1      #取得沙發的對話

            self.tv = self.location.get_tv_location()             #取得觸發和電視對話的位置   map9_1
            self.tv_dialogue_in_map9_1 = dialogue.tv_dialogue_in_map9_1      #取得沙發的對話

            self.bucket = self.location.get_bucket_location()             #取得觸發和沙發對話的位置   map9_1
            self.bucket_dialogue_in_map9_1 = dialogue.bucket_dialogue_in_map9_1      #取得沙發的對話

            self.shower = self.location.get_shower_location()             #取得觸發和淋浴設備對話的位置   map9_1
            self.shower_dialogue_in_map9_1 = dialogue.shower_dialogue_in_map9_1      #取得沙發的對話

            self.virus1 = self.location.get_virus1_location()             #取得觸發和病毒對話的位置   map9_1
            self.virus_dialogue_in_map9_1 = dialogue.virus_dialogue_in_map9_1      #取得沙發的對話

            self.sugar = self.location.get_sugar_location()             #取得觸發和蔗糖對話的位置   map9_1
            self.sugar_dialogue_in_map9_1 = dialogue.sugar_dialogue_in_map9_1      #取得沙發的對話

            self.d80 = self.location.get_d80_location()             #取得觸發和80對話的位置   map9_1
            self.d80_dialogue_in_map9_1 = dialogue.d80_dialogue_in_map9_1      #取得沙發的對話

            self.edta = self.location.get_edta_location()             #取得觸發和edta對話的位置   map9_1
            self.edta_dialogue_in_map9_1 = dialogue.edta_dialogue_in_map9_1      #取得沙發的對話

            self.mgcl = self.location.get_mgcl_location()             #取得觸發和氯化鎂對話的位置   map9_1
            self.mgcl_dialogue_in_map9_1 = dialogue.mgcl_dialogue_in_map9_1      #取得沙發的對話

            self.sis = self.location.get_sis_location()                 #取得和妹妹對話的位置     map9_1
            self.sis_dialogue_in_map9_1 = dialogue.sis_dialogue_in_map9_1   #取得妹妹的對話

            self.dr2 = self.location.get_DR2_location()                 #取得和DR對話的位置     map9_1
            self.dr_dialogue_in_map9_1 = dialogue.dr_dialogue_in_map9_1   #取得DR的對話

            self.door2_dialogue_in_map9_1 = dialogue.door2_dialogue_in_map9_1      #取得門2的對話

            self.NPC1_dialogue_in_map9_1 = dialogue.NPC1_dialogue_in_map9_1      #取得NPC1的對話

            self.NPC2_dialogue_in_map9_1 = dialogue.NPC2_dialogue_in_map9_1      #取得NPC2的對話

            self.final = self.location.get_final_location()                 #取得觸發和final對話的位置  map10
            self.final_dialogue_in_map10 = dialogue.final_dialogue_in_map10    #取得final的對話

            self.sis_dialogue_in_map10 = dialogue.sis_dialogue_in_map10

            self.dr_dialogue_in_map10 = dialogue.dr_dialogue_in_map10


################################################################################################################


            [self.role_loaction_x, self.role_loaction_y] = self.player.get_role_location()      #取得角色位置

#########################################################################################       下面為MAP1自己的對話

            if [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP1:
                if dialogue.get_count() < len(self.murmur_dialogue_in_map1 )  : 
                    
                    self.draw_plot_text_map1( dialogue , self.murmur_dialogue_in_map1)

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur2 and self.map == MAP1:

                if dialogue.get_count() < len(self.murmur_dialogue_in_map1 ) : 
                    
                    self.draw_plot_text_map1( dialogue , self.murmur_dialogue_in_map1)


##########################################################################################      下面為MAP1的鑰匙的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.key and self.map == MAP1:      #位置在觸發鑰匙對話且在MAP1
                if dialogue.get_count() <= len(self.key_dialogue_in_map1): 
                    
                    self.draw_text_map1( dialogue , self.key_dialogue_in_map1)
                    

##########################################################################################      

                '''elif [self.role_loaction_x, self.role_loaction_y] in self.game and self.map == MAP1:
                
                if self.game1_dialogue_in_map1 == game1_list_in_map1_0: 
                      
                    if dialogue.get_count() <= len(self.game1_dialogue_in_map1): 
                        self.screen.blit(dialogue_outline_image, (200, 450))
                        text_surface = font.render(self.game1_dialogue_in_map1[dialogue.get_count() -1 ], True, RED)
                        text_Rect = text_surface.get_rect()
                        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
                        self.screen.blit(text_surface, text_Rect)
                        
                        
                elif self.game1_dialogue_in_map1 == game1_list_in_map1_1:
        
                    if dialogue.get_count() <= len(self.game1_dialogue_in_map1): 
                        font = pygame.font.Font(font_name, 24)    # 畫出文字
                        self.screen.blit(dialogue_outline_image, (200, 450))
                        text_surface = font.render(self.game1_dialogue_in_map1[dialogue.get_count() -1 ], True, RED)
                        text_Rect = text_surface.get_rect()
                        text_Rect.midleft=(300 + 25*self.count, 450 + 50)
                        self.screen.blit(text_surface, text_Rect)'''
##########################################################################################    下面為MAP1的石頭的對話


            elif [self.role_loaction_x, self.role_loaction_y] in self.rock and self.map == MAP1:
                            
                #if   self.rock_dialogue_in_map1   == Jonny_rock_dialogue1_in_map1: 
                                
                    if dialogue.get_count() <= len(  self.rock_dialogue_in_map1  ): 

                        self.draw_text_map1( dialogue , self.rock_dialogue_in_map1)
                                    
                                    
                                    
                    '''elif   self.rock_dialogue_in_map1   == Jonny_rock_dialogue2_in_map1:
                            
                    if dialogue.get_count() <= len(  self.rock_dialogue_in_map1  ):
                        self.draw_text( dialogue , self.rock_dialogue_in_map1)'''
                                    

##########################################################################################          下面為MAP1的門的對話 

            elif [self.role_loaction_x, self.role_loaction_y] in self.door1 and self.map == MAP1:
                
                #if   self.door1_dialogue_in_map1   == Jonny_door_dialogue1_in_map1: 
                       
                    if dialogue.get_count() <= len(  self.door1_dialogue_in_map1  ): 
                        self.draw_text_map1( dialogue , self.door1_dialogue_in_map1)                    
                        
                    '''elif   self.door1_dialogue_in_map1   == Jonny_door_dialogue2_in_map1:
                   
                    if dialogue.get_count() <= len(  self.door1_dialogue_in_map1  ): 
                        self.draw_text( dialogue , self.door1_dialogue_in_map1)
                        

                elif   self.door1_dialogue_in_map1   == Jonny_door_dialogue3_in_map1:
                   
                    if dialogue.get_count() <= len(  self.door1_dialogue_in_map1  ): 
                        self.draw_text( dialogue , self.door1_dialogue_in_map1)
                        

                elif   self.door1_dialogue_in_map1   == Jonny_door_dialogue4_in_map1:
                   
                    if dialogue.get_count() <= len(  self.door1_dialogue_in_map1  ):
                        self.draw_text( dialogue , self.door1_dialogue_in_map1) '''
                        

##########################################################################################          下面為MAP1的博士的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.dr and self.map == MAP1:
                            
                #if   self.dr_dialogue_in_map1   == Jonny_DR_dialogue1_in_map1: 
        
                    if dialogue.get_count() <= len(  self.dr_dialogue_in_map1  ): 
                        self.draw_text_map1( dialogue , self.dr_dialogue_in_map1)

##########################################################################################           下面為MAP2的自我對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP2:
                if dialogue.get_count() < len(self.murmur_dialogue_in_map2 )  : 
                    
                    self.draw_plot_text_map2( dialogue , self.murmur_dialogue_in_map2)


############################################################################################       下面為MAP2的鼻子對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.nose and self.map == MAP2:
                #if self.nose_dialogue_in_map2 == Jonny_nose_dialogue1_in_map2:
                    if dialogue.get_count() <= len(self.nose_dialogue_in_map2 ) : 

                        self.draw_text_map2( dialogue , self.nose_dialogue_in_map2)

#############################################################################################      下面為MAP2的小丑對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.joker and self.map == MAP2:

                #if self.joker_dialogue_in_map2 == Jonny_joker_dialogue1_in_map2:

                    if dialogue.get_count() <= len(self.joker_dialogue_in_map2 )  : 

                        self.draw_text_map2( dialogue , self.joker_dialogue_in_map2)

                    '''elif self.joker_dialogue_in_map2 == Jonny_joker_dialogue2_in_map2:

                    if dialogue.get_count() <= len(self.joker_dialogue_in_map2 )  : 
                        
                        self.draw_text( dialogue , self.joker_dialogue_in_map2)

                elif self.joker_dialogue_in_map2 == Jonny_joker_dialogue3_in_map2:

                    if dialogue.get_count() <= len(self.joker_dialogue_in_map2 )  : 
                        
                        self.draw_text( dialogue , self.joker_dialogue_in_map2)'''


###############################################################################################     下面為MAP2的遊戲的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.game and self.map == MAP2:

                    if dialogue.get_count() <= len(self.game_dialogue_in_map2 ) : 

                        self.draw_text_map2( dialogue , self.game_dialogue_in_map2)

                    '''elif dialogue.get_count() <= len(self.game_dialogue_in_map2 ) : 

                        self.draw_text( dialogue , self.game_dialogue_in_map2)

                    elif dialogue.get_count() <= len(self.game_dialogue_in_map2 ) : 

                        self.draw_text( dialogue , self.game_dialogue_in_map2)'''

##################################################################################################    下面為MAP2的病毒的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.virus and self.map == MAP2:

                    if dialogue.get_count() <= len(self.virus_dialogue_in_map2 ) : 

                        self.draw_text_map2( dialogue , self.virus_dialogue_in_map2)

###################################################################################################  MAP2終止線 MAP3開始線

########################################################################################################## 以下為MAP3公告1的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.sign1 and self.map == MAP3:

                    if dialogue.get_count() <= len(self.sign1_dialogue_in_map3 ) : 

                        self.draw_text_map3( dialogue , self.sign1_dialogue_in_map3)

########################################################################################################## 以下為MAP3公告2的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.sign2 and self.map == MAP3:

                    if dialogue.get_count() <= len(self.sign2_dialogue_in_map3 ) : 

                        self.draw_text_map3( dialogue , self.sign2_dialogue_in_map3)

########################################################################################################## 以下為MAP3藍色矮人的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.blue and self.map == MAP3:

                    if dialogue.get_count() <= len(self.blue_dialogue_in_map3 ) : 

                        self.draw_text_map3( dialogue , self.blue_dialogue_in_map3)

########################################################################################################## 以下為MAP3黃色矮人的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.yellow and self.map == MAP3:

                    if dialogue.get_count() <= len(self.yellow_dialogue_in_map3 ) : 

                        self.draw_text_map3( dialogue , self.yellow_dialogue_in_map3)

########################################################################################################## 以下為MAP3紅色矮人的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.red and self.map == MAP3:

                    if dialogue.get_count() <= len(self.red_dialogue_in_map3 ) : 

                        self.draw_text_map3( dialogue , self.red_dialogue_in_map3)


########################################################################################################## 以下為MAP3綠色矮人的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.green and self.map == MAP3:

                    if dialogue.get_count() <= len(self.green_dialogue_in_map3 ) : 

                        self.draw_text_map3( dialogue , self.green_dialogue_in_map3)

########################################################################################################## 以下為MAP3灰色矮人的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.gray and self.map == MAP3:

                    if dialogue.get_count() <= len(self.gray_dialogue_in_map3 ) : 

                        self.draw_text_map3( dialogue , self.gray_dialogue_in_map3)

########################################################################################################## 以下為MAP3紫色矮人的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.purple and self.map == MAP3:

                    if dialogue.get_count() <= len(self.purple_dialogue_in_map3 ) : 

                        self.draw_text_map3( dialogue , self.purple_dialogue_in_map3)

########################################################################################################## 以下為MAP3 鑰匙的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.key1 and self.map == MAP3:

                    if dialogue.get_count() <= len(self.key_dialogue_in_map3 ) : 

                        self.draw_text_map3( dialogue , self.key_dialogue_in_map3)

########################################################################################################## 以下為MAP3 門2的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.door2 and self.map == MAP3:

                    if dialogue.get_count() <= len(self.door_dialogue_in_map3 ) : 

                        self.draw_text_map3( dialogue , self.door_dialogue_in_map3)

##########################################################################################           下面為MAP3的自我對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP3:

                if dialogue.get_count() < len(self.murmur_dialogue_in_map3 )  : 
                    
                    self.draw_plot_text_map3( dialogue , self.murmur_dialogue_in_map3)

##########################################################################################################   MAP3終止線  MAP4開始線

########################################################################################################## 以下為MAP4 花瓶的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.vase and self.map == MAP4:

                    if dialogue.get_count() <= len(self.vase_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.vase_dialogue_in_map4)

########################################################################################################## 以下為MAP4 書櫃的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.shelf and self.map == MAP4:

                    if dialogue.get_count() <= len(self.shelf_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.shelf_dialogue_in_map4)

########################################################################################################## 以下為MAP4 時鐘的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.clock and self.map == MAP4:

                    if dialogue.get_count() <= len(self.clock_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.clock_dialogue_in_map4)

########################################################################################################## 以下為MAP4 老鷹的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.eagle and self.map == MAP4:

                    if dialogue.get_count() <= len(self.eagle_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.eagle_dialogue_in_map4)

########################################################################################################## 以下為MAP4 沙發的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.sofa and self.map == MAP4:

                    if dialogue.get_count() <= len(self.sofa_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.sofa_dialogue_in_map4)

########################################################################################################## 以下為MAP4 地板的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.floor and self.map == MAP4:

                    if dialogue.get_count() <= len(self.floor_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.floor_dialogue_in_map4)

########################################################################################################## 以下為MAP4 燈的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.light and self.map == MAP4:

                    if dialogue.get_count() <= len(self.light_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.light_dialogue_in_map4)

########################################################################################################## 以下為MAP4 貓頭鷹的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.owl and self.map == MAP4:

                    if dialogue.get_count() <= len(self.owl_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.owl_dialogue_in_map4)

########################################################################################################## 以下為MAP4 烏鴉的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.crow and self.map == MAP4:

                    if dialogue.get_count() <= len(self.crow_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.crow_dialogue_in_map4)

########################################################################################################## 以下為MAP4 病毒的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.virus_1 and self.map == MAP4:

                    if dialogue.get_count() <= len(self.virus_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.virus_dialogue_in_map4)

########################################################################################################## 以下為MAP4 花的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.key2 and self.map == MAP4_1:

                    if dialogue.get_count() <= len(self.key_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.key_dialogue_in_map4)

########################################################################################################## 以下為MAP4 門的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.door2 and self.map == MAP4:

                    if dialogue.get_count() <= len(self.door_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.door_dialogue_in_map4)

########################################################################################################## 以下為MAP4 公告3的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.sign3 and self.map == MAP4:

                    if dialogue.get_count() <= len(self.sign_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.sign_dialogue_in_map4)

########################################################################################################## 以下為MAP4 書櫃1的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.shelf1 and self.map == MAP4:

                    if dialogue.get_count() <= len(self.shelf1_dialogue_in_map4 ) : 

                        self.draw_text_map4( dialogue , self.shelf1_dialogue_in_map4)

##########################################################################################           下面為MAP4的自我對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP4:
                if dialogue.get_count() < len(self.murmur_dialogue_in_map4 )  : 
                    
                    self.draw_plot_text_map4( dialogue , self.murmur_dialogue_in_map4)

###########################################################################################################    MAP4終止線   MAP5開始線

##########################################################################################           下面為MAP5的自我對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP5:
                if dialogue.get_count() < len(self.murmur_dialogue_in_map5 )  : 
                    
                    self.draw_plot_text_map5( dialogue , self.murmur_dialogue_in_map5)

########################################################################################################## 以下為MAP5 寶箱的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.treasure1 and self.map == MAP5:

                    if dialogue.get_count() <= len(self.treasure_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.treasure_dialogue_in_map5)

########################################################################################################## 以下為MAP5 燈管的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.light1 and self.map == MAP5:

                    if dialogue.get_count() <= len(self.light_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.light_dialogue_in_map5)

########################################################################################################## 以下為MAP5 牆壁的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.wall and self.map == MAP5:

                    if dialogue.get_count() <= len(self.wall_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.wall_dialogue_in_map5)

########################################################################################################## 以下為MAP5 電線的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.ele and self.map == MAP5:

                    if dialogue.get_count() <= len(self.ele_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.ele_dialogue_in_map5)

########################################################################################################## 以下為MAP5 鏡子的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.mirror and self.map == MAP5:

                    if dialogue.get_count() <= len(self.mirror_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.mirror_dialogue_in_map5)

########################################################################################################## 以下為MAP5 門的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.door2 and self.map == MAP5:

                    if dialogue.get_count() <= len(self.door_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.door_dialogue_in_map5)

########################################################################################################## 以下為MAP5 祭壇的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.altar and self.map == MAP5:

                    if dialogue.get_count() <= len(self.altar_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.altar_dialogue_in_map5)

########################################################################################################## 以下為MAP5 酒桶的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.urn and self.map == MAP5:

                    if dialogue.get_count() <= len(self.urn_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.urn_dialogue_in_map5)

########################################################################################################## 以下為MAP5 陷阱的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.trap and self.map == MAP5:

                    if dialogue.get_count() <= len(self.trap_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.trap_dialogue_in_map5)

########################################################################################################## 以下為MAP5 酒桶1的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.urn1 and self.map == MAP5:

                    if dialogue.get_count() <= len(self.urn1_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.urn1_dialogue_in_map5)

########################################################################################################## 以下為MAP5 酒桶2的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.urn2 and self.map == MAP5:

                    if dialogue.get_count() <= len(self.urn2_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.urn2_dialogue_in_map5)

########################################################################################################## 以下為MAP5 公告4的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.sign4 and self.map == MAP5:

                    if dialogue.get_count() <= len(self.sign4_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.sign4_dialogue_in_map5)

########################################################################################################## 以下為MAP5 梯子的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.ladder and self.map == MAP5:

                    if dialogue.get_count() <= len(self.ladder_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.ladder_dialogue_in_map5)


########################################################################################################## 以下為MAP5 女生衣服的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.cloth_g and self.map == MAP5:

                    if dialogue.get_count() <= len(self.cloth_g_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.cloth_g_dialogue_in_map5)

########################################################################################################## 以下為MAP5 男生衣服的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.cloth_b and self.map == MAP5:

                    if dialogue.get_count() <= len(self.cloth_b_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.cloth_b_dialogue_in_map5)

########################################################################################################## 以下為MAP5 小櫥櫃的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.small_shelf and self.map == MAP5:

                    if dialogue.get_count() <= len(self.small_shelf_dialogue_in_map5 ) : 

                        self.draw_text_map5( dialogue , self.small_shelf_dialogue_in_map5)


###########################################################################################################    MAP5終止線   MAP6開始線

########################################################################################################## 以下為MAP6 寶箱的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.treasure1 and self.map == MAP6:

                    if dialogue.get_count() <= len(self.treasure_dialogue_in_map6 ) : 

                        self.draw_text_map5( dialogue , self.treasure_dialogue_in_map6)

########################################################################################################## 以下為MAP6 毒氣的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.gas and self.map == MAP6:

                    if dialogue.get_count() <= len(self.gas_dialogue_in_map6 ) : 

                        self.draw_text_map5( dialogue , self.gas_dialogue_in_map6)

########################################################################################################## 以下為MAP6 門的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.door2 and self.map == MAP6:

                    if dialogue.get_count() <= len(self.door_dialogue_in_map6 ) : 

                        self.draw_text_map5( dialogue , self.door_dialogue_in_map6)

########################################################################################################## 以下為MAP6 風扇的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.fan and self.map == MAP6:

                    if dialogue.get_count() <= len(self.fan_dialogue_in_map6 ) : 

                        self.draw_text_map5( dialogue , self.fan_dialogue_in_map6)

########################################################################################################## 以下為MAP6 檯燈的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.lamp and self.map == MAP6:

                    if dialogue.get_count() <= len(self.lamp_dialogue_in_map6 ) : 

                        self.draw_text_map5( dialogue , self.lamp_dialogue_in_map6)

########################################################################################################## 以下為MAP6 板凳的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.bench and self.map == MAP6:

                    if dialogue.get_count() <= len(self.bench_dialogue_in_map6 ) : 

                        self.draw_text_map5( dialogue , self.bench_dialogue_in_map6)

########################################################################################################## 以下為MAP6 壁爐的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.fireplace and self.map == MAP6:

                    if dialogue.get_count() <= len(self.fireplace_dialogue_in_map6 ) : 

                        self.draw_text_map5( dialogue , self.fireplace_dialogue_in_map6)

########################################################################################################## 以下為MAP6 盆栽的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.grass and self.map == MAP6:

                    if dialogue.get_count() <= len(self.grass_dialogue_in_map6 ) : 

                        self.draw_text_map5( dialogue , self.grass_dialogue_in_map6)


########################################################################################################## 以下為MAP6 密碼寶箱的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.treasure2 and self.map == MAP6:

                    if dialogue.get_count() <= len(self.treasure2_dialogue_in_map6 ) : 

                        self.draw_text_map5( dialogue , self.treasure2_dialogue_in_map6)

##########################################################################################           下面為MAP6的自我對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP6:
                if dialogue.get_count() < len(self.murmur_dialogue_in_map6 )  : 
                    
                    self.draw_plot_text_map5( dialogue , self.murmur_dialogue_in_map6)


#############################################################################################################    MAP6終止線   MAP7開始線

##########################################################################################           下面為MAP7的自我對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP7:
                if dialogue.get_count() < len(self.murmur_dialogue_in_map7 )  : 
                    
                    self.draw_plot_text_map5( dialogue , self.murmur_dialogue_in_map7)

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur2 and self.map == MAP7:
                if dialogue.get_count() < len(self.murmur_dialogue_in_map7 )  : 
                    
                    self.draw_plot_text_map5( dialogue , self.murmur_dialogue_in_map7)

########################################################################################################## 以下為MAP7 槌子的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.hammer and self.map == MAP7:

                    if dialogue.get_count() <= len(self.hammer_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.hammer_dialogue_in_map7)

########################################################################################################## 以下為MAP7 牆壁的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.wall and self.map == MAP7:

                    if dialogue.get_count() <= len(self.wall_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.wall_dialogue_in_map7)

########################################################################################################## 以下為MAP7 電線的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.ele and self.map == MAP7:

                    if dialogue.get_count() <= len(self.ele_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.ele_dialogue_in_map7)

########################################################################################################## 以下為MAP7 石頭的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.rock1 and self.map == MAP7:

                    if dialogue.get_count() <= len(self.rock_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.rock_dialogue_in_map7)

########################################################################################################## 以下為MAP7 工具箱的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.box and self.map == MAP7:

                    if dialogue.get_count() <= len(self.box_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.box_dialogue_in_map7)

########################################################################################################## 以下為MAP7 鉗子的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.pliers and self.map == MAP7:

                    if dialogue.get_count() <= len(self.pliers_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.pliers_dialogue_in_map7)

########################################################################################################## 以下為MAP7 櫥櫃的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.shelf2 and self.map == MAP7:

                    if dialogue.get_count() <= len(self.shelf_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.shelf_dialogue_in_map7)

########################################################################################################## 以下為MAP7 小相框的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.frame and self.map == MAP7:

                    if dialogue.get_count() <= len(self.frame_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.frame_dialogue_in_map7)

########################################################################################################## 以下為MAP7 骷髏頭的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.dead and self.map == MAP7:

                    if dialogue.get_count() <= len(self.dead_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.dead_dialogue_in_map7)

########################################################################################################## 以下為MAP7 雷射光的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.laser and self.map == MAP7:

                    if dialogue.get_count() <= len(self.laser_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.laser_dialogue_in_map7)

########################################################################################################## 以下為MAP7 雷射光前面的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.front and self.map == MAP7:

                    if dialogue.get_count() <= len(self.laser1_dialogue_in_map7 ) : 

                        self.draw_text_map5( dialogue , self.laser1_dialogue_in_map7)




#############################################################################################################    MAP7終止線   MAP8開始線

########################################################################################################## 以下為MAP8 電線的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.ele and self.map == MAP8:

                    if dialogue.get_count() <= len(self.ele_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.ele_dialogue_in_map8)

########################################################################################################## 以下為MAP8 水的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.water and self.map == MAP8:

                    if dialogue.get_count() <= len(self.water_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.water_dialogue_in_map8)

########################################################################################################## 以下為MAP8 按鈕的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.btn and self.map == MAP8:

                    if dialogue.get_count() <= len(self.btn_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.btn_dialogue_in_map8)

########################################################################################################## 以下為MAP8 冰箱的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.refri and self.map == MAP8:

                    if dialogue.get_count() <= len(self.refri_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.refri_dialogue_in_map8)

########################################################################################################## 以下為MAP8 相框的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.paint and self.map == MAP8:

                    if dialogue.get_count() <= len(self.paint_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.paint_dialogue_in_map8)

########################################################################################################## 以下為MAP8 長笛的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.flute and self.map == MAP8:

                    if dialogue.get_count() <= len(self.flute_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.flute_dialogue_in_map8)

########################################################################################################## 以下為MAP8 小提琴盒子的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.violin_box and self.map == MAP8:

                    if dialogue.get_count() <= len(self.violin_box_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.violin_box_dialogue_in_map8)

########################################################################################################## 以下為MAP8 小提琴的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.violin and self.map == MAP8:

                    if dialogue.get_count() <= len(self.violin_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.violin_dialogue_in_map8)

########################################################################################################## 以下為MAP8 鋼琴的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.piano and self.map == MAP8:

                    if dialogue.get_count() <= len(self.piano_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.piano_dialogue_in_map8)

########################################################################################################## 以下為MAP8 大提琴的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.cello and self.map == MAP8:

                    if dialogue.get_count() <= len(self.cello_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.cello_dialogue_in_map8)

########################################################################################################## 以下為MAP8 法國號的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.trumpet and self.map == MAP8:

                    if dialogue.get_count() <= len(self.trumpet_dialogue_in_map8 ) : 

                        self.draw_text_map5( dialogue , self.trumpet_dialogue_in_map8)


#############################################################################################################    MAP8終止線   MAP9開始線

########################################################################################################## 以下為MAP9 櫥櫃的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.cabinet and self.map == MAP9:

                    if dialogue.get_count() <= len(self.cabinet_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.cabinet_dialogue_in_map9)

########################################################################################################## 以下為MAP9 機器1的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.mashine1 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.mashine1_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.mashine1_dialogue_in_map9)

########################################################################################################## 以下為MAP9 機器2的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.mashine2 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.mashine2_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.mashine2_dialogue_in_map9)

########################################################################################################## 以下為MAP9 機器3的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.mashine3 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.mashine3_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.mashine3_dialogue_in_map9)

########################################################################################################## 以下為MAP9 顯微鏡的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.micro and self.map == MAP9:

                    if dialogue.get_count() <= len(self.micro_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.micro_dialogue_in_map9)

########################################################################################################## 以下為MAP9 螢幕的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.screen1 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.screen_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.screen_dialogue_in_map9)

########################################################################################################## 以下為MAP9 濃縮器的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.concentrator and self.map == MAP9:

                    if dialogue.get_count() <= len(self.concentrator_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.concentrator_dialogue_in_map9)

########################################################################################################## 以下為MAP9 酒精的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.alcohol and self.map == MAP9:

                    if dialogue.get_count() <= len(self.alcohol_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.alcohol_dialogue_in_map9)

########################################################################################################## 以下為MAP9 氯化鈉的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.nacl and self.map == MAP9:

                    if dialogue.get_count() <= len(self.nacl_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.nacl_dialogue_in_map9)

########################################################################################################## 以下為MAP9 NPC1的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.NPC1 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.NPC1_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.NPC1_dialogue_in_map9)

########################################################################################################## 以下為MAP9 NPC2的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.NPC2 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.NPC2_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.NPC2_dialogue_in_map9)

########################################################################################################## 以下為MAP9 NPC3的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.NPC3 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.NPC3_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.NPC3_dialogue_in_map9)

########################################################################################################## 以下為MAP9 NPC4的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.NPC4 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.NPC4_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.NPC4_dialogue_in_map9)

########################################################################################################## 以下為MAP9 NPC5的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.NPC5 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.NPC5_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.NPC5_dialogue_in_map9)

########################################################################################################## 以下為MAP9 NPC6的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.NPC6 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.NPC6_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.NPC6_dialogue_in_map9)

########################################################################################################## 以下為MAP9 NPC7的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.NPC7 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.NPC7_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.NPC7_dialogue_in_map9)

########################################################################################################## 以下為MAP9 DR博士的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.DR1 and self.map == MAP9:

                    if dialogue.get_count() <= len(self.DR_dialogue_in_map9 ) : 

                        self.draw_text_map6( dialogue , self.DR_dialogue_in_map9)

#########################################################################################################    下面為MAP9的自我對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP9:
                if dialogue.get_count() < len(self.murmur_dialogue_in_map9 )  : 
                    
                    self.draw_plot_text_map6( dialogue , self.murmur_dialogue_in_map9)


#############################################################################################################    MAP9終止線   MAP9_1開始線

########################################################################################################## 以下為MAP9_1 沙發的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.sofa1 and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.sofa_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.sofa_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 電視的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.tv and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.tv_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.tv_dialogue_in_map9_1)
                    
########################################################################################################## 以下為MAP9_1 水桶的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.bucket and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.bucket_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.bucket_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 淋浴設備的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.shower and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.shower_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.shower_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 病毒的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.virus1 and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.virus_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.virus_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 蔗糖的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.sugar and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.sugar_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.sugar_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 edta的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.edta and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.edta_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.edta_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 mgcl的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.mgcl and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.mgcl_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.mgcl_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 d80的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.d80 and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.d80_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.d80_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 NPC1的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.NPC1 and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.NPC1_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.NPC1_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 NPC2的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.NPC2 and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.NPC2_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.NPC2_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 門2的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.door2 and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.door2_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.door2_dialogue_in_map9_1)

########################################################################################################## 以下為MAP9_1 妹妹的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.sis and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.sis_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.sis_dialogue_in_map9_1)

######################################################################################################### 以下為MAP9_1 DR的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.dr2 and self.map == MAP9_1:

                    if dialogue.get_count() <= len(self.dr_dialogue_in_map9_1 ) : 

                        self.draw_text_map6( dialogue , self.dr_dialogue_in_map9_1)

#########################################################################################################    下面為MAP9_1的自我對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP9_1:
                if dialogue.get_count() < len(self.murmur_dialogue_in_map9_1 )  : 
                    
                    self.draw_plot_text_map6( dialogue , self.murmur_dialogue_in_map9_1)

#############################################################################################################    MAP9_1終止線   MAP10開始線


########################################################################################################## 以下為MAP10 final的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.final and self.map == MAP10:

                    if dialogue.get_count() <= len(self.final_dialogue_in_map10 ) : 

                        self.draw_text_map10( dialogue , self.final_dialogue_in_map10)


########################################################################################################## 以下為MAP10 DR博士的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.dr2 and self.map == MAP10:

                    if dialogue.get_count() <= len(self.dr_dialogue_in_map10 ) : 

                        self.draw_text_map10( dialogue , self.dr_dialogue_in_map10)


########################################################################################################## 以下為MAP10 妹妹的對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.sis and self.map == MAP10:

                    if dialogue.get_count() <= len(self.sis_dialogue_in_map10 ) : 

                        self.draw_text_map10( dialogue , self.sis_dialogue_in_map10)

#########################################################################################################    下面為MAP10的自我對話

            elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP10:
                if dialogue.get_count() < len(self.murmur_dialogue_in_map10 )  : 
                    
                    self.draw_plot_text_map10( dialogue , self.murmur_dialogue_in_map10)


#############################################################################################################    MAP10終止線   

