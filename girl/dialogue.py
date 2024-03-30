from __future__ import annotations
from girl.setting import *
import pygame
from boy.game_map import *
from girl.dialogue_list import *
from boy.get_location import Get_location
from boy.lock_treasure import Lock_treasure
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from girl.model import Player
    from boy.music import Music


#player = Player()
count = 0
temp_time = 0

class Dialogue:
    def __init__(self, player : Player, music : Music):
        
        self.player = player

        self.open_dialogue = False

        self.finish = False

        self.dark = False

        self.dark_b = True

        self.paint_value = False

        self.laser_value = False

        self.laser1_value = False

        self.music = music

        self.door_lock = door_lock

        self.space_sound = space_sound

        self.laugh_sound = laugh_sound

        self.rock_m = rock

        self.light_m = light

        self.shelf_m = shelf

        self.ck = ck

        self.shower_m = shower

        self.map = self.player.get_in_which_map()

        self.lock = Lock_treasure()

        self.location = Get_location(self.player)   

        self.dr = self.location.get_DR_location()                   # 取得博士的位置
        self.dr_dialogue_in_map1 = Jonny_DR_dialogue1_in_map1       # 取得觸發博士對話的位置

        self.rock = self.location.get_rock_location()               # 取得石頭的位置
        self.rock_dialogue_in_map1 = Jonny_rock_dialogue1_in_map1   # 取得石頭的位置

        self.door1 = self.location.get_door1_location()             # 取得門的位置
        self.door1_dialogue_in_map1 = Jonny_door_dialogue4_in_map1  # 取得觸發門的對話位置

        self.key = self.location.get_key_location()                 # 取得觸發鑰匙的位置
        self.key1_dialogue_in_map1= Jonny_key_dialogue1_in_map1     #取得鑰匙對話

        self.murmur1 = [100, 250]                           # 取得觸發自己對話1的位置
        self.murmur_dialogue_in_map1 = Jonny_self_dialogue1_in_map1  #取得和自己的對話 map1

        self.murmur2 = [850, 300]                            # 取得觸發自己對話2的位置
        self.murmur_dialogue_in_map2 = Jonny_self_dialogue1_in_map2  #取得和自己的對話 map2

        self.murmur_dialogue_in_map3 = Jonny_self_dialogue1_in_map3  #取得和自己的對話 map3

        self.murmur_dialogue_in_map4 = Jonny_self_dialogue1_in_map4  #取得和自己的對話 map4

        self.murmur_dialogue_in_map5 = Jonny_self_dialogue1_in_map5 #取得和自己的對話 map5

        self.murmur_dialogue_in_map6 = Jonny_self_dialogue1_in_map6 #取得和自己的對話map6

        self.murmur_dialogue_in_map7 = Vivian_self_dialogue1_in_map7  #取得和自己的對話 map7

        self.murmur_dialogue_in_map9 = Jonny_self_dialogue1_in_map9  #取得和自己的對話 map9

        self.murmur_dialogue_in_map9_1 = Jonny_self_dialogue1_in_map9_1  #取得和自己的對話 map9_1

        self.murmur_dialogue_in_map10 = Jonny_self_dialogue1_in_map10  #取得和自己的對話 map10


        self.joker = [750, 500]                                     # 取得觸發小丑對話的位置
        self.joker_dialogue_in_map2 = Jonny_joker_dialogue1_in_map2  #取得和小丑的對話

        self.nose = [500, 350]                                     # 取得觸發鼻子對話的位置
        self.nose_dialogue_in_map2 = Jonny_nose_dialogue1_in_map2  #取得和鼻子的對話

        self.game = [50, 200]                                     # 取得觸發遊戲對話的位置
        self.game_dialogue_in_map2 = Jonny_game_dialogue1_in_map2  #取得和遊戲的對話

        self.virus = [550, 150]                                     # 取得觸發病毒對話的位置
        self.virus_dialogue_in_map2 = Jonny_virus_dialogue1_in_map2  #取得和病毒的對話

        self.sign1 = [50, 200]                                     # 取得觸發公告1對話的位置
        self.sign1_dialogue_in_map3 = Jonny_sign1_dialogue_in_map3  #取得和公告1的對話

        self.sign2 = [900, 200]                                     # 取得觸發公告2對話的位置
        self.sign2_dialogue_in_map3 = Jonny_sign2_dialogue_in_map3  #取得和公告2的對話

        self.blue = [200, 150]                                     # 取得觸發藍色矮人對話的位置
        self.blue_dialogue_in_map3 = Jonny_blue_dialogue1_in_map3  #取得和藍色矮人的對話

        self.yellow = [450, 150]                                     # 取得觸發黃色矮人對話的位置
        self.yellow_dialogue_in_map3 = Jonny_yellow_dialogue1_in_map3  #取得和黃色矮人的對話

        self.red = [600, 150]                                     # 取得觸發紅色矮人對話的位置
        self.red_dialogue_in_map3 = Jonny_red_dialogue1_in_map3  #取得和紅色矮人的對話

        self.green = [200, 400]                                      # 取得觸發綠色矮人對話的位置
        self.green_dialogue_in_map3 = Jonny_green_dialogue1_in_map3    #取得綠色矮人對話

        self.gray = [450, 400]                                      # 取得觸發灰色矮人對話的位置
        self.gray_dialogue_in_map3 = Jonny_gray_dialogue1_in_map3    #取得灰色矮人對話

        self.purple = [600, 400]                                      # 取得觸發紫色矮人對話的位置
        self.purple_dialogue_in_map3 = Jonny_purple_dialogue1_in_map3    #取得紫色矮人對話

        self.key1 = [350, 500]                                      # 取得觸發鑰匙對話的位置
        self.key_dialogue_in_map3 = Jonny_key_dialogue_in_map3      #取得鑰匙對話

        self.door2 = [900, 250]                                      # 取得觸發和門2對話的位置 map3
        self.door_dialogue_in_map3 = Jonny_door_dialogue1_in_map3    #取得門2的對話 map3
######################################################################################################
        self.door_dialogue_in_map4 = Jonny_door_dialogue1_in_map4    #取得門2的對話 map4

        self.vase = [50, 250]                                      # 取得觸發和花瓶對話的位置 map4
        self.vase_dialogue_in_map4 = Jonny_vase_dialogue_in_map4    #取得花瓶的對話 

        self.shelf = [50, 150]                                      #取得觸發和書櫃對話的位置
        self.shelf_dialogue_in_map4 = Jonny_shelf_dialogue_in_map4   #取得書櫃的對話

        self.clock = [300, 100]                                     #取得觸發和時鐘對話的位置
        self.clock_dialogue_in_map4 = Jonny_clock_dialogue1_in_map4   #取得時鐘的對話

        self.eagle = [600, 100]                                     #取得觸發和老鷹對話的位置
        self.eagle_dialogue_in_map4 = Jonny_eagle_dialogue1_in_map4  #取得老鷹的對話

        self.virus_dialogue_in_map4 = Jonny_virus_dialogue1_in_map4  #取得病毒的對話

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

        self.virus_1 = [900, 50]                                     #取得觸發和病毒對話的位置
        self.virus_dialogue_in_map4 = Jonny_virus_dialogue1_in_map4  #取得病毒的對話

        self.key2 = [750, 400]                                     #取得觸發和花對話的位置
        self.key_dialogue_in_map4 = Jonny_flower_dialogue_in_map4  #取得花的對話

        self.sign3 = [150, 150]                                     #取得觸發和公告對話的位置   map4
        self.sign_dialogue_in_map4 = Jonny_sign_dialogue_in_map4   #取得公告的對話

        self.shelf1 = [600, 100]                                    #取得觸發和書櫃1對話的位置   map4
        self.shelf1_dialogue_in_map4 = Jonny_shelf1_dialogue_in_map4    #取得書櫃1的對話


######################################################################################################

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
        self.trap_dialogue_in_map5 = Jonny_trap_dialogue1_in_map5   #取得陷阱的對話

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
####################################################################################################

        self.treasure_dialogue_in_map6 = Jonny_treasure_dialogue1_in_map6    #取得寶箱的對話 map6

        self.fan = [850, 50]                                                #取得觸發風扇對話的位置 map6
        self.fan_dialogue_in_map6 = Jonny_fan_dialogue1_in_map6             #取得風扇的對話 map6

        self.gas = [850, 50]                                                #取得觸發毒氣對話的位置 map6
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

####################################################################################################

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

        self.dead = [900, 50]                                             #取得觸發和骷髏頭對話的位置   map7
        self.dead_dialogue_in_map7 = Vivian_dead_dialogue_in_map7           #取得骷髏頭的對話

        self.front = [700, 150]
        self.laser1_dialogue_in_map7 = Vivian_laser_dialogue_in_map7           #取得雷射光的對話
####################################################################################################

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

####################################################################################################

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
        self.NPC6_dialogue_in_map9 = Jonny_NPC6_dialogue1_in_map9        #取得NPC6的對話

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

        self.dr2 = [500, 100]
        self.dr_dialogue_in_map9_1 = Jonny_dr_dialogue_in_map9_1

        self.sis = [550, 50]                                            #取得和妹妹對話的位置
        self.sis_dialogue_in_map9_1 = Jonny_sis_dialogue_in_map9_1      #取得妹妹的位置

        self.final = [650, 200]                                         #取得觸發和final對話的位置   map10
        self.final_dialogue_in_map10 = Jonny_final_dialogue1_in_map10       #取得和final的對話   map10

        self.sis_dialogue_in_map10 = Jonny_sis_dialogue_in_map10    #取得和妹妹的對話   map10

        self.dr_dialogue_in_map10 = Jonny_dr_dialogue_in_map10    #取得和Dr博士的對話   map10

####################################################################################################

        self.role_location_x = 0
        self.role_loaction_y = 0 

        self.count = 0
    
    def open_plot_dialogue(self):
        [self.role_loaction_x, self.role_loaction_y] = self.player.get_role_location()
        self.map = self.player.get_in_which_map()

        key_pressed = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()   # 隨時抓取經過的時間

        global temp_time
        
        self.murmur1 = self.location.get_murmur1()  # 取得自我對話的位置
        self.murmur2 = self.location.get_murmur2()  # 取得自我對話的位置

##############################################################################################  以下為MAP1的自我對話

        if MAP1_BLOCK[11][19] == 0:
            self.murmur_dialogue_in_map1 = Jonny_self_dialogue2_in_map1

        if MAP5[6][1] == 0:
            self.murmur_dialogue_in_map7 = Vivian_self_dialogue2_in_map7

        if [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP1:
            if self.count < len( self.murmur_dialogue_in_map1 ) :
                self.open_dialogue = True   
                #print(self.murmur_dialogue_in_map1)


                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        self.count += 1
                return True

            else:
                self.open_dialogue = False
                self.count = 0
                MAP1_BLOCK[11][19] = 0
                MAP1[5][2] = 0
                return False

        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur2 and self.map == MAP1:
            if self.count < len( self.murmur_dialogue_in_map1 ) :
                self.open_dialogue = True

                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        self.count += 1
                        
                return True
            else:
                self.open_dialogue = False
                self.count = 0
                MAP1[6][17] = 0
                return False

########################################################################################################  以下為MAP2的自我對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP2:
            if self.count < len( self.murmur_dialogue_in_map2 ) :
                self.open_dialogue = True

                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        self.count += 1
                        
                return True
            else:
                self.open_dialogue = False
                self.count = 0
                MAP2[2][14] = 0
                return False

########################################################################################################  以下為MAP3的自我對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP3:
            if self.count < len( self.murmur_dialogue_in_map3 ) :
                self.open_dialogue = True

                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        self.count += 1
                        
                return True
            else:
                self.open_dialogue = False
                self.count = 0
                MAP3[5][1] = 0
                MAP3[6][1] = 0
                return False

########################################################################################################  以下為MAP4的自我對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP4:
            if self.count < len( self.murmur_dialogue_in_map4 ) :
                self.open_dialogue = True

                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        self.count += 1
                        
                return True
            else:
                self.open_dialogue = False
                self.count = 0
                MAP4[10][1] = 0
                return False

########################################################################################################  以下為MAP5的自我對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP5:
            if self.count < len( self.murmur_dialogue_in_map5 ) :
                self.open_dialogue = True

                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        self.count += 1
                        
                return True
            else:
                self.open_dialogue = False
                self.count = 0
                [self.player.rect.x, self.player.rect.y] = [50, 250]
                self.player.player_in_which_map = MAP7
                self.player.image = player_down_1_image
                MAP5[6][1] = 0
                return False        

########################################################################################################  以下為MAP6的自我對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP6:
            if self.count < len( self.murmur_dialogue_in_map6 ) :
                self.open_dialogue = True

                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        if self.count == 1:
                            MAP6[1][17] = 25
                        self.count += 1
                        
                return True
            else:
                self.open_dialogue = False
                self.count = 0
                MAP6[1][17] = 0
                MAP6[1][18] = 0
                return False
            
        
########################################################################################################  以下為MAP7的自我對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP7:
            if self.count < len( self.murmur_dialogue_in_map7 ) :
                self.open_dialogue = True
                #self.dark_b = True

                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        self.count += 1
                        
                return True

            else:
                self.open_dialogue = False
                self.count = 0
                [self.player.rect.x, self.player.rect.y] = [50, 300]
                self.player.player_in_which_map = MAP5
                self.player.image = player_down_image
                MAP7[5][1] = 51
                return False

        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur2 and self.map == MAP7:
            if self.count < len( self.murmur_dialogue_in_map7 ) :
                self.open_dialogue = True

                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        self.count += 1
                        
                return True

            else:
                self.open_dialogue = False
                self.count = 0
                MAP7[5][1] = 0
                return False

########################################################################################################  以下為MAP9的自我對話


        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP9:
            if self.count < len( self.murmur_dialogue_in_map9 ) :
                self.open_dialogue = True
                MAP9[3][2] = 25
                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        
                        if self.count == len(self.murmur_dialogue_in_map9) - 1:
                            MAP9[3][2] = 0
                        self.count += 1
                        
                return True
            else:
                self.open_dialogue = False
                self.count = 0
                MAP9[3][1] = 0
                return False

########################################################################################################  以下為MAP9_1的自我對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP9_1:
            if self.count < len( self.murmur_dialogue_in_map9_1 ) :
                self.open_dialogue = True

                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        self.count += 1
                        
                return True
            else:
                self.open_dialogue = False
                self.count = 0
                MAP9_1[5][17] = 0
                MAP10[0][0] = 0
                return False

########################################################################################################  以下為MAP10的自我對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.murmur1 and self.map == MAP10:
            if self.count < len( self.murmur_dialogue_in_map10 ) :
                self.open_dialogue = True

                if key_pressed[pygame.K_SPACE]:
                    if current_time - temp_time >= 250:    # 至少經過150毫秒，才能再上下左右移動
                        self.music.play_sound(self.space_sound)
                        temp_time = current_time
                        self.count += 1
                        
                return True
            else:
                self.open_dialogue = False
                self.count = 0
                MAP10[4][9] = 0
                MAP10[5][9] = 0
                MAP10[6][9] = 0
                MAP10[7][9] = 0
                return False

            
        

################################################################################################################


    def whether_open_dialogue(self):
        [self.role_loaction_x, self.role_loaction_y] = self.player.get_role_location()

        self.map = self.player.get_in_which_map()

        self.door1 = self.location.get_door1_location()  # 取得第一個門對話的位置

        self.door2 = self.location.get_door2_location()  # 取得第二個門對話的位置

        self.rock = self.location.get_rock_location()  # 取得石頭對話的位置

        self.dr = self.location.get_DR_location()  # 取得DR對話的位置

        self.key = self.location.get_key_location()    # 取得觸發鑰匙對話的位置

        self.nose = self.location.get_nose_location()  #取得觸發鼻子對話的位置

        self.joker = self.location.get_joker_location()  #取得觸發小丑對話的位置

        self.game = self.location.get_game_location()   #取得觸發遊戲對話的位置

        self.virus = self.location.get_virus_location()   #取得觸發病毒對話的位置

        self.sign1 = self.location.get_sign1_location()   #取得觸發公告1對話的位置

        self.sign2 = self.location.get_sign2_location()   #取得觸發公告2對話的位置

        self.blue = self.location.get_blue_location()   #取得觸發藍色矮人對話的位置

        self.yellow = self.location.get_yellow_location()   #取得觸發黃色矮人對話的位置

        self.red = self.location.get_red_location()   #取得觸發紅色矮人對話的位置

        self.green = self.location.get_green_location()   #取得觸發綠色矮人對話的位置

        self.gray = self.location.get_gray_location()   #取得觸發灰色矮人對話的位置

        self.purple = self.location.get_purple_location()   #取得觸發紫色矮人對話的位置

        self.key1 = self.location.get_key1_location()   #取得觸發鑰匙對話的位置

        self.vase = self.location.get_vase_location()              # 取得觸發和花瓶對話的位置 map4

        self.shelf = self.location.get_shelf_location()            #取得觸發和書櫃對話的位置

        self.clock = self.location.get_clock_location()          #取得觸發和時鐘對話的位置

        self.eagle = self.location.get_eagle_location()            #取得觸發和老鷹對話的位置

        self.sofa = self.location.get_sofa_location()             #取得觸發和沙發對話的位置

        self.floor = self.location.get_floor_location()             #取得觸發和地板對話的位置

        self.light = self.location.get_light_location()             # 取得觸發和燈對話的位置 

        self.owl = self.location.get_owl_location()                  #取得觸發和貓頭鷹對話的位置

        self.crow = self.location.get_crow_location()                #取得觸發和烏鴉對話的位置
        
        self.virus_1 = self.location.get_virus_1_location()                #取得觸發和病毒對話的位置  map4

        self.key2 = self.location.get_key2_location()                #取得觸發和花對話的位置  map4

        self.sign3 = self.location.get_sign3_location()                #取得觸發和公告3對話的位置  map4

        self.shelf1 = self.location.get_shelf1_location()                #取得觸發和書櫃1對話的位置  map4

        self.treasure1 = self.location.get_treasure_location()              #取得觸發和寶箱1對話的位置   map5 

        self.light1 = self.location.get_light1_location()                  #取得觸發和燈管對話的位置   map5

        self.ele = self.location.get_ele_location()                         #取得觸發和電線對話的位置   map5  

        self.mirror = self.location.get_mirror_location()                   #取得觸發和鏡子對話的位置   map5  
    
        self.altar = self.location.get_altar_location()                  #取得觸發和祭壇對話的位置   map5 

        self.urn = self.location.get_urn_location()                    #取得觸發和酒桶對話的位置   map5  

        self.wall = self.location.get_wall_location()                   #取得觸發和牆壁對話的位置   map5

        self.trap = self.location.get_trap_location()                   #取得觸發和陷阱對話的位置   map5

        self.urn1 = self.location.get_urn1_location()                   #取得觸發和酒桶1對話的位置   map5

        self.urn2 = self.location.get_urn2_location()                   #取得觸發和酒桶2對話的位置   map5

        self.sign4 = self.location.get_sign4_location()                   #取得觸發和公告4對話的位置   map5

        self.ladder = self.location.get_ladder_location()                   #取得觸發和梯子對話的位置   map5

        self.cloth_g = self.location.get_cloth_g_location()                   #取得觸發和女生衣服對話的位置   map5

        self.cloth_b = self.location.get_cloth_b_location()                   #取得觸發和男生衣服對話的位置   map5

        self.small_shelf = self.location.get_small_shelf_location()             #取得觸發和小櫥櫃對話的位置   map5

        self.fan = self.location.get_fan_location()                   #取得觸發和風扇對話的位置   map6

        self.gas = self.location.get_gas_location()                   #取得觸發和毒氣對話的位置   map6

        self.lamp = self.location.get_lamp_location()                   #取得觸發和檯燈對話的位置   map6

        self.bench = self.location.get_bench_location()                   #取得觸發和板凳對話的位置   map6

        self.fireplace = self.location.get_fireplace_location()           #取得觸發和壁爐對話的位置   map6

        self.grass = self.location.get_grass_location()                   #取得觸發和盆栽對話的位置   map6

        self.treasure2 = self.location.get_treasure2_location()            #取得觸發和密碼寶箱對話的位置   map6

        self.front = self.location.get_front_location()

        self.hammer = self.location.get_hammer_location()                   #取得觸發和槌子對話的位置   map7

        self.rock1 = self.location.get_rock1_location()                 #取得觸發和石頭對話的位置   map7

        self.box = self.location.get_box_location()                 #取得觸發和工具箱對話的位置   map7

        self.pliers = self.location.get_pliers_location()               #取得觸發和鉗子對話的位置   map7

        self.shelf2 = self.location.get_shelf2_location()                 #取得觸發和櫥櫃對話的位置   map7

        self.frame = self.location.get_frame_location()              #取得觸發和相框對話的位置   map7

        self.laser = self.location.get_laser_location()                 #取得觸發和雷射光對話的位置   map7

        self.dead = self.location.get_dead_location()                    #取得觸發和骷髏頭對話的位置   map7

        self.refri = self.location.get_refri_location()                 #取得觸發和冰箱對話的位置   map8

        self.paint = self.location.get_paint_location()                #取得觸發和相框對話的位置   map8

        self.water = self.location.get_water_location()                 #取得觸發和水對話的位置   map8

        self.btn = self.location.get_btn_location()                     #取得觸發和按鈕對話的位置   map8

        self.flute = self.location.get_flute_location()                 #取得觸發和長笛對話的位置   map8

        self.violin_box = self.location.get_violin_box_location()        #取得觸發和小提琴箱子對話的位置   map8

        self.violin = self.location.get_violin_location()               #取得觸發和小提琴對話的位置   map8

        self.piano = self.location.get_piano_location()              #取得觸發和鋼琴對話的位置   map8

        self.cello = self.location.get_cello_location()            #取得觸發和大提琴對話的位置   map8

        self.trumpet = self.location.get_trumpet_location()         #取得觸發和法國號對話的位置   map8

        self.cabinet = self.location.get_cabinet_location()            #取得觸發和櫃子對話的位置   map9

        self.mashine1 = self.location.get_mashine1_location()          #取得觸發和機器1對話的位置   map9

        self.mashine2 = self.location.get_mashine2_location()                   #取得觸發和機器2對話的位置   map9

        self.mashine3 = self.location.get_mashine3_location()              #取得觸發和機器3對話的位置   map9

        self.micro = self.location.get_micro_location()           #取得觸發和顯微鏡對話的位置   map9

        self.screen1 = self.location.get_screen_location()             #取得觸發和螢幕對話的位置   map9

        self.alcohol = self.location.get_alcohol_location()                 #取得觸發和酒精對話的位置   map9

        self.nacl = self.location.get_nacl_location()                   #取得觸發和氯化鈉對話的位置   map9

        self.concentrator = self.location.get_concentrator_location()      #取得觸發和濃縮器對話的位置   map9

        self.NPC1 = self.location.get_NPC1_location()                    #取得觸發和NPC1對話的位置   map9

        self.NPC2 = self.location.get_NPC2_location()               #取得觸發和NPC2對話的位置   map9

        self.NPC3 = self.location.get_NPC3_location()              #取得觸發和NPC3對話的位置   map9

        self.NPC4 = self.location.get_NPC4_location()             #取得觸發和NPC4對話的位置   map9

        self.NPC5 = self.location.get_NPC5_location()           #取得觸發和NPC5對話的位置   map9

        self.NPC6 = self.location.get_NPC6_location()              #取得觸發和NPC6對話的位置   map9

        self.NPC7 = self.location.get_NPC7_location()          #取得觸發和NPC7對話的位置   map9

        self.DR1 = self.location.get_DR1_location()             #取得觸發和DR博士對話的位置   map9

        self.sofa1 = self.location.get_sofa1_location()             #取得觸發和沙發對話的位置   map9_1

        self.tv = self.location.get_tv_location()             #取得觸發和電視對話的位置   map9_1

        self.bucket = self.location.get_bucket_location()             #取得觸發和沙發對話的位置   map9_1

        self.shower = self.location.get_shower_location()             #取得觸發和淋浴設備對話的位置   map9_1

        self.virus1 = self.location.get_virus1_location()             #取得觸發和病毒對話的位置   map9_1

        self.sugar = self.location.get_sugar_location()             #取得觸發和蔗糖對話的位置   map9_1

        self.d80 = self.location.get_d80_location()             #取得觸發和80對話的位置   map9_1

        self.edta = self.location.get_edta_location()             #取得觸發和edta對話的位置   map9_1

        self.mgcl = self.location.get_mgcl_location()             #取得觸發和氯化鎂對話的位置   map9_1

        self.sis = self.location.get_sis_location()                 #取得和妹妹對話的位置     map9_1

        self.dr2 = self.location.get_DR2_location()

        self.final = self.location.get_final_location()             #取得觸發和final對話的位置   map10

##################################################################################################      下面為MAP1的鑰匙的對話

        if [self.role_loaction_x, self.role_loaction_y] in self.key and self.map == MAP1:
            if self.count < len(self.key1_dialogue_in_map1):
                self.music.play_sound(self.space_sound)
                self.count += 1
                self.open_dialogue = True
                return True
            else:
                self.open_dialogue = False
                self.count = 0
                MAP1[2][15] = 0
                MAP1[2][16] = 0
                MAP1_BLOCK[2][15] = 0
                return False

##########################################################################################   

            '''elif [self.role_loaction_x, self.role_loaction_y] in self.game and self.map == MAP1:
            if self.game1_dialogue_in_map1 == game1_list_in_map1_0:
                if self.count < len(self.game1_dialogue_in_map1):
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.game1_dialogue_in_map1 = game1_list_in_map1_1
                    self.open_dialogue = False
                    return False

            elif self.game1_dialogue_in_map1 == game1_list_in_map1_1:
                if self.count < len(self.game1_dialogue_in_map1):
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False
                    '''

##########################################################################################   下面為MAP1的門的對話
        elif [self.role_loaction_x, self.role_loaction_y] in self.door1 and self.map == MAP1 :
                    
                    if MAP1[1][3] == 0:
                        self.door1_dialogue_in_map1 = Jonny_door_dialogue1_in_map1

                        if MAP1_BLOCK[0][0] == 0:
                            self.door1_dialogue_in_map1 = Jonny_door_dialogue2_in_map1

                            if MAP1[2][15] == 0:
                                self.door1_dialogue_in_map1 = Jonny_door_dialogue3_in_map1

                    

                    if self.door1_dialogue_in_map1 == Jonny_door_dialogue4_in_map1:
                        if self.count < len(self.door1_dialogue_in_map1):
                            self.music.play_sound(self.space_sound)
                            self.count += 1
                            self.open_dialogue = True
                            return True
                        else:
                            self.count = 0
                            self.open_dialogue = False
                            return False

                    elif self.door1_dialogue_in_map1 == Jonny_door_dialogue1_in_map1:
                        if self.count < len(self.door1_dialogue_in_map1):
                            self.music.play_sound(self.space_sound)
                            self.count += 1
                            self.open_dialogue = True
                            return True
                        else:
                            self.count = 0
                            self.open_dialogue = False
                            MAP1_BLOCK[0][0] = 0
                            return False

                    elif self.door1_dialogue_in_map1 == Jonny_door_dialogue2_in_map1:
                        if self.count < len(self.door1_dialogue_in_map1):
                            self.music.play_sound(self.space_sound)
                            self.count += 1
                            self.open_dialogue = True
                            return True
                        else:
                            self.count = 0
                            self.open_dialogue = False
                            return False
                    
                    elif self.door1_dialogue_in_map1 == Jonny_door_dialogue3_in_map1:
                        if self.count == len(self.door1_dialogue_in_map1) - 1:
                                self.music.play_sound(self.door_lock)

                        if self.count < len(self.door1_dialogue_in_map1):
                            self.music.play_sound(self.space_sound)
                            self.count += 1
                            self.open_dialogue = True
                            
                            return True
                        else:
                            self.count = 0
                            MAP1_BLOCK[11][2] = 0
                            MAP1[10][2] = 0
                            self.open_dialogue = False
                            return False

##########################################################################################   下面為MAP1的dr的對話
        

        elif [self.role_loaction_x, self.role_loaction_y] in self.dr and self.map == MAP1:
            if self.dr_dialogue_in_map1 == Jonny_DR_dialogue1_in_map1:
                
                if self.count < len(self.dr_dialogue_in_map1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    MAP1[1][3] = 0
                    MAP1_BLOCK[1][3] = 0
                    MAP1[1][2] = 0
                    MAP1[1][4] = 0
                    MAP1[2][3] = 0
                    self.open_dialogue = False
                    return False


##########################################################################################   下面為MAP1的石頭的對話


        elif [self.role_loaction_x, self.role_loaction_y] in self.rock and self.map == MAP1:  
                if MAP1_BLOCK[0][0] == 0:
                    self.rock_dialogue_in_map1 = Jonny_rock_dialogue2_in_map1

                if self.rock_dialogue_in_map1 == Jonny_rock_dialogue1_in_map1:
                    if self.count < len(self.rock_dialogue_in_map1):
                        self.music.play_sound(self.space_sound)
                        self.count += 1
                        self.open_dialogue = True
                        return True
                    else:
                        self.open_dialogue = False
                        self.count = 0
                        return False
                
                elif self.rock_dialogue_in_map1 == Jonny_rock_dialogue2_in_map1:
                    if self.count < len(self.rock_dialogue_in_map1):
                        self.music.play_sound(self.space_sound)
                        self.count += 1
                        self.open_dialogue = True
                        return True
                    else:
                        self.open_dialogue = False
                        self.count = 0
                        self.music.play_sound(self.rock_m)
                        MAP1_BLOCK[6][14] = 0
                        MAP1[6][14] = 0
                        MAP1[5][14] = 0
                        MAP1[6][13] = 0
                        return False

##########################################################################################          以下為MAP2和鼻子的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.nose and self.map == MAP2:
            if self.nose_dialogue_in_map2 == Jonny_nose_dialogue1_in_map2:
                
                if self.count < len(self.nose_dialogue_in_map2):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    MAP2[7][10] = 0
                    MAP2[8][10] = 0
                    MAP2_BLOCK[8][10] = 0
                    self.open_dialogue = False
                    return False


##########################################################################################          以下為MAP2和小丑的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.joker and self.map == MAP2:
            if MAP2_BLOCK[11][19] == 0:
                self.joker_dialogue_in_map2 = Jonny_joker_dialogue2_in_map2
            
            if MAP2_BLOCK[8][10] == 0:
                self.joker_dialogue_in_map2 = Jonny_joker_dialogue3_in_map2

            if self.joker_dialogue_in_map2 == Jonny_joker_dialogue1_in_map2:
                
                if self.count < len(self.joker_dialogue_in_map2):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    MAP2_BLOCK[2][12] = 0
                    MAP2_BLOCK[11][19] = 0
                    self.open_dialogue = False
                    return False

            elif self.joker_dialogue_in_map2 == Jonny_joker_dialogue2_in_map2:
                
                if self.count < len(self.joker_dialogue_in_map2):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.joker_dialogue_in_map2 == Jonny_joker_dialogue3_in_map2:

                if self.count == len(self.joker_dialogue_in_map2)-1 :
                    self.music.play_sound(self.laugh_sound)
                
                if self.count < len(self.joker_dialogue_in_map2):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                    
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP2[10][14] = 0
                    MAP2[9][15] = 0
                    MAP2_BLOCK[10][15] = 0
                    return False
        
            
                        


##########################################################################################   以下為MAP2和遊戲的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.game and self.map == MAP2:
            
            if self.player.code_game_main.get_success():
                self.game_dialogue_in_map2 = Jonny_game_dialogue2_in_map2
            
            if MAP2_BLOCK[0][1] == 0:
                self.game_dialogue_in_map2 = Jonny_game_dialogue3_in_map2
            
        
            if self.game_dialogue_in_map2 == Jonny_game_dialogue1_in_map2:
                
                if self.count < len(self.game_dialogue_in_map2):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    self.player.play_game()
                    return False

            elif self.game_dialogue_in_map2 == Jonny_game_dialogue2_in_map2:
                if self.count == 0 :
                    self.music.play_sound(self.door_lock)
                
                if self.count < len(self.game_dialogue_in_map2):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP2_BLOCK[0][1] = 0
                    MAP2_BLOCK[0][0] = 0
                    return False

            elif self.game_dialogue_in_map2 == Jonny_game_dialogue3_in_map2:
                
                if self.count < len(self.game_dialogue_in_map2):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

#################################################################################################   以下為MAP2和病毒對話的位置


        elif [self.role_loaction_x, self.role_loaction_y] in self.virus and self.map == MAP2:
            if MAP2_BLOCK[0][0] == 0 :
                self.virus_dialogue_in_map2 = Jonny_virus_dialogue2_in_map2

            if self.virus_dialogue_in_map2 == Jonny_virus_dialogue1_in_map2:
                
                if self.count < len(self.virus_dialogue_in_map2):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.virus_dialogue_in_map2 == Jonny_virus_dialogue2_in_map2:
                
                if self.count < len(self.virus_dialogue_in_map2):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP2[3][11] = 0
                    MAP2[4][11] = 0
                    MAP2_BLOCK[4][11] = 0
                    return False

####################################################################################################   MAP2終止線  MAP3開始線

####################################################################################################   以下為和公告1對話的位置

        elif [self.role_loaction_x, self.role_loaction_y] in self.sign1 and self.map == MAP3:
            if self.sign1_dialogue_in_map3 == Jonny_sign1_dialogue_in_map3:
                
                if self.count < len(self.sign1_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

######################################################################################################  以下為和公告2對話的位置

        elif [self.role_loaction_x, self.role_loaction_y] in self.sign2 and self.map == MAP3:
            if self.sign2_dialogue_in_map3 == Jonny_sign2_dialogue_in_map3:
                
                if self.count < len(self.sign2_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

######################################################################################################  以下為和藍色矮人對話的位置

        elif [self.role_loaction_x, self.role_loaction_y] in self.blue and self.map == MAP3:
            if MAP3_BLOCK[0][19] == 0:
                self.blue_dialogue_in_map3 = Jonny_blue_dialogue2_in_map3

            if self.blue_dialogue_in_map3 == Jonny_blue_dialogue1_in_map3:
                
                if self.count < len(self.blue_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.blue_dialogue_in_map3 == Jonny_blue_dialogue2_in_map3:
                
                if self.count < len(self.blue_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

######################################################################################################  以下為和黃色矮人對話的位置

        elif [self.role_loaction_x, self.role_loaction_y] in self.yellow and self.map == MAP3:
            if MAP3_BLOCK[0][19] == 0:
                self.yellow_dialogue_in_map3 = Jonny_yellow_dialogue2_in_map3

            if self.yellow_dialogue_in_map3 == Jonny_yellow_dialogue1_in_map3:
                
                if self.count < len(self.yellow_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.yellow_dialogue_in_map3 == Jonny_yellow_dialogue2_in_map3:
                
                if self.count < len(self.yellow_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

######################################################################################################  以下為和紅色矮人對話的位置

        elif [self.role_loaction_x, self.role_loaction_y] in self.red and self.map == MAP3:
            if MAP3_BLOCK[0][19] == 0:
                self.red_dialogue_in_map3 = Jonny_red_dialogue2_in_map3

            if self.red_dialogue_in_map3 == Jonny_red_dialogue1_in_map3:
                
                if self.count < len(self.red_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.red_dialogue_in_map3 == Jonny_red_dialogue2_in_map3:
                
                if self.count < len(self.red_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

######################################################################################################  以下為和綠色矮人對話的位置

        elif [self.role_loaction_x, self.role_loaction_y] in self.green and self.map == MAP3:
            if MAP3_BLOCK[0][19] == 0:
                self.green_dialogue_in_map3 = Jonny_green_dialogue2_in_map3

            if self.green_dialogue_in_map3 == Jonny_green_dialogue1_in_map3:
                
                if self.count < len(self.green_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.green_dialogue_in_map3 == Jonny_green_dialogue2_in_map3:
                
                if self.count < len(self.green_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

######################################################################################################  以下為和灰色矮人對話的位置

        elif [self.role_loaction_x, self.role_loaction_y] in self.gray and self.map == MAP3:
            if MAP3_BLOCK[0][19] == 0:
                self.gray_dialogue_in_map3 = Jonny_gray_dialogue2_in_map3

            if self.gray_dialogue_in_map3 == Jonny_gray_dialogue1_in_map3:
                
                if self.count < len(self.gray_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.gray_dialogue_in_map3 == Jonny_gray_dialogue2_in_map3:
                
                if self.count < len(self.gray_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

######################################################################################################  以下為和紫色矮人對話的位置

        elif [self.role_loaction_x, self.role_loaction_y] in self.purple and self.map == MAP3:
            if MAP3_BLOCK[0][19] == 0:
                self.purple_dialogue_in_map3 = Jonny_purple_dialogue2_in_map3

            if self.purple_dialogue_in_map3 == Jonny_purple_dialogue1_in_map3:
                
                if self.count < len(self.purple_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.purple_dialogue_in_map3 == Jonny_purple_dialogue2_in_map3:
                
                if self.count < len(self.purple_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

######################################################################################################  以下為和鑰匙對話的位置

        elif [self.role_loaction_x, self.role_loaction_y] in self.key1 and self.map == MAP3:
            if self.key_dialogue_in_map3 == Jonny_key_dialogue_in_map3:
                
                if self.count < len(self.key_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP3_BLOCK[0][0] = 0
                    MAP3[10][7] = 0
                    return False

######################################################################################################  以下為和門2對話的位置 map3

        elif [self.role_loaction_x, self.role_loaction_y] in self.door2 and self.map == MAP3:
            if MAP3_BLOCK[0][0] == 0:
                self.door_dialogue_in_map3 = Jonny_door_dialogue2_in_map3
                #print("VVVV")

            if self.door_dialogue_in_map3 == Jonny_door_dialogue1_in_map3:
                
                if self.count < len(self.door_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.door_dialogue_in_map3 == Jonny_door_dialogue2_in_map3:
                if self.count == len(self.door_dialogue_in_map3) - 1:
                    self.music.play_sound(self.door_lock)
                
                if self.count < len(self.door_dialogue_in_map3):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP3_BLOCK[5][19] = 0
                    MAP3_BLOCK[6][19] = 0
                    MAP3_BLOCK[0][19] = 0
                    MAP3[5][18] = 0
                    MAP3[6][18] = 0
                    
                    return False


#########################################################################################################  MAP3終止線 MAP4開始線

##################################################################################################### 以下為和花瓶的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.vase and self.map == MAP4:
            if self.vase_dialogue_in_map4 == Jonny_vase_dialogue_in_map4:
                
                if self.count < len(self.vase_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和書櫃的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.shelf and self.map == MAP4:
            if self.shelf_dialogue_in_map4 == Jonny_shelf_dialogue_in_map4:
                
                if self.count < len(self.shelf_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和書櫃1的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.shelf1 and self.map == MAP4:
            if self.shelf1_dialogue_in_map4 == Jonny_shelf1_dialogue_in_map4:
                
                if self.count < len(self.shelf1_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和公告3的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.sign3 and self.map == MAP4:
            if self.sign_dialogue_in_map4 == Jonny_sign_dialogue_in_map4:
                
                if self.count < len(self.sign_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和時鐘的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.clock and self.map == MAP4:
            if MAP4_BLOCK[0][12] == 0:
                self.clock_dialogue_in_map4 = Jonny_clock_dialogue2_in_map4

            if MAP4_BLOCK[0][13] == 0:
                self.clock_dialogue_in_map4 = Jonny_clock_dialogue3_in_map4

            if MAP4_BLOCK[0][14] == 0:
                self.clock_dialogue_in_map4 = Jonny_clock_dialogue1_in_map4

            if self.clock_dialogue_in_map4 == Jonny_clock_dialogue1_in_map4:
                
                if self.count < len(self.clock_dialogue_in_map4):
                    if self.count == 0:
                        self.music.play_sound(self.ck)
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    self.dark = True
                    MAP4_BLOCK[0][12] = 0
                    MAP4_BLOCK[0][13] = 1
                    MAP4_BLOCK[0][14] = 1
                    return False

            elif self.clock_dialogue_in_map4 == Jonny_clock_dialogue2_in_map4:
                
                if self.count < len(self.clock_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    self.dark = True
                    MAP4_BLOCK[0][12] = 1
                    MAP4_BLOCK[0][13] = 0
                    MAP4_BLOCK[0][14] = 1
                    return False

            elif self.clock_dialogue_in_map4 == Jonny_clock_dialogue3_in_map4:
                
                if self.count < len(self.clock_dialogue_in_map4):
                    if self.count == 0:
                        self.music.play_sound(self.ck)
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    self.dark = False
                    MAP4_BLOCK[0][12] = 1
                    MAP4_BLOCK[0][13] = 1
                    MAP4_BLOCK[0][14] = 0
                    return False

##################################################################################################### 以下為和老鷹的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.eagle and self.map == MAP4:
            if self.dark:
                self.eagle_dialogue_in_map4 = Jonny_eagle_dialogue2_in_map4
            else:
                self.eagle_dialogue_in_map4 = Jonny_eagle_dialogue1_in_map4

            if self.eagle_dialogue_in_map4 == Jonny_eagle_dialogue1_in_map4:
                
                if self.count < len(self.eagle_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.eagle_dialogue_in_map4 == Jonny_eagle_dialogue2_in_map4:
                
                if self.count < len(self.eagle_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和病毒的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.virus_1 and self.map == MAP4:
            if MAP4[10][8] == 0 :
                self.virus_dialogue_in_map4 = Jonny_virus_dialogue2_in_map4

            if self.virus_dialogue_in_map4 == Jonny_virus_dialogue1_in_map4:
                
                if self.count < len(self.virus_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.virus_dialogue_in_map4 == Jonny_virus_dialogue2_in_map4:
                
                if self.count < len(self.virus_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP4[1][17] = 0
                    MAP4[1][18] = 0
                    MAP4_BLOCK[1][17] = 0
                    return False


##################################################################################################### 以下為和沙發的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.sofa and self.map == MAP4:
            if self.sofa_dialogue_in_map4 == Jonny_sofa_dialogue_in_map4:
                
                if self.count < len(self.sofa_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和花的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.key2 and self.map == MAP4_1:
            if self.key_dialogue_in_map4 == Jonny_flower_dialogue_in_map4:
                
                if self.count < len(self.key_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP4_BLOCK[0][0] = 0
                    MAP4_1[8][15] = 0
                    return False

##################################################################################################### 以下為和地板的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.floor and self.map == MAP4:
            if self.floor_dialogue_in_map4 == Jonny_floor_dialogue_in_map4:
                
                if self.count < len(self.floor_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP4[10][8] = 0
                    MAP4[10][9] = 0
                    return False

##################################################################################################### 以下為和燈的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.light and self.map == MAP4:
            if self.light_dialogue_in_map4 == Jonny_light_dialogue_in_map4:
                
                if self.count < len(self.light_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和門的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.door2 and self.map == MAP4:
            if MAP4_BLOCK[0][0] == 0:
                self.door_dialogue_in_map4 = Jonny_door_dialogue2_in_map4

            if self.door_dialogue_in_map4 == Jonny_door_dialogue1_in_map4:
                
                if self.count < len(self.door_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.door_dialogue_in_map4 == Jonny_door_dialogue2_in_map4:
                if self.count == len(self.door_dialogue_in_map4) - 1:
                    self.music.play_sound(self.door_lock)
                
                if self.count < len(self.door_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP4[10][18] = 0
                    MAP4_BLOCK[10][19] = 0
                    return False

##################################################################################################### 以下為和貓頭鷹的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.owl and self.map == MAP4:
            if self.dark:
                self.owl_dialogue_in_map4 = Jonny_owl_dialogue2_in_map4
            else:
                self.owl_dialogue_in_map4 = Jonny_owl_dialogue1_in_map4

            if self.owl_dialogue_in_map4 == Jonny_owl_dialogue1_in_map4:
                
                if self.count < len(self.owl_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.owl_dialogue_in_map4 == Jonny_owl_dialogue2_in_map4:
                
                if self.count < len(self.owl_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和烏鴉的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.crow and self.map == MAP4:
            if self.dark:
                self.crow_dialogue_in_map4 = Jonny_crow_dialogue2_in_map4
            else:
                self.crow_dialogue_in_map4 = Jonny_crow_dialogue1_in_map4

            if self.crow_dialogue_in_map4 == Jonny_crow_dialogue1_in_map4:
                
                if self.count < len(self.crow_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.crow_dialogue_in_map4 == Jonny_crow_dialogue2_in_map4:
                
                if self.count < len(self.crow_dialogue_in_map4):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##########################################################################################################  MAP4 終止線   MAP5開始線

##################################################################################################### 以下為和燈管的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.light1 and self.map == MAP5:
            if MAP5[1][18] == 22 and MAP8[10][1] == 17 :
                if MAP5_BLOCK[0][0] == 1:
                    self.light_dialogue_in_map5 = Jonny_light_dialogue2_in_map5
                else: 
                    self.light_dialogue_in_map5 = Jonny_light_dialogue3_in_map5
            else:
                self.light_dialogue_in_map5 = Jonny_light_dialogue1_in_map5

            if self.light_dialogue_in_map5 == Jonny_light_dialogue1_in_map5:
                
                if self.count < len(self.light_dialogue_in_map5):
                    if self.count == 0:
                        self.music.play_sound(self.light_m)
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5_BLOCK[0][0] = 1
                    
                    return False

            elif self.light_dialogue_in_map5 == Jonny_light_dialogue2_in_map5:
                
                if self.count < len(self.light_dialogue_in_map5):
                    if self.count == 0:
                        self.music.play_sound(self.light_m)
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    self.dark_b = False
                    MAP5_BLOCK[0][0] = 0
                    #self.music.play_sound(self.light_m)
                    return False

            elif self.light_dialogue_in_map5 == Jonny_light_dialogue3_in_map5:
                
                if self.count < len(self.light_dialogue_in_map5):
                    if self.count == 0:
                        self.music.play_sound(self.light_m)
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    self.dark_b = True
                    MAP5_BLOCK[0][0] = 1
                    #self.music.play_sound(self.light_m)
                    return False

##################################################################################################### 以下為和寶箱的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.treasure1 and self.map == MAP5:
            if MAP5_BLOCK[1][0] == 0:
                self.treasure_dialogue_in_map5 = Jonny_treasure_dialogue2_in_map5

            if self.treasure_dialogue_in_map5 == Jonny_treasure_dialogue1_in_map5:
                
                if self.count < len(self.treasure_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5_BLOCK[1][0] = 0
                    MAP5[9][1] = 31
                    return False

            elif self.treasure_dialogue_in_map5 == Jonny_treasure_dialogue2_in_map5:
                
                if self.count < len(self.treasure_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和牆壁的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.wall and self.map == MAP5:
            if self.wall_dialogue_in_map5 == Jonny_wall_dialogue1_in_map5:
                
                if self.count < len(self.wall_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和電線的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.ele and self.map == MAP5:
            if MAP5[1][18] == 22:
                self.ele_dialogue_in_map5 = Jonny_ele_dialogue2_in_map5
            if MAP5[1][18] == 6:
                self.ele_dialogue_in_map5 = Jonny_ele_dialogue1_in_map5

            if self.ele_dialogue_in_map5 == Jonny_ele_dialogue1_in_map5:
                
                if self.count < len(self.ele_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5[1][18] = 22
                    return False

            elif self.ele_dialogue_in_map5 == Jonny_ele_dialogue2_in_map5:
                
                if self.count < len(self.ele_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5[1][18] = 6
                    return False

##################################################################################################### 以下為和鏡子的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.mirror and self.map == MAP5:
            if self.mirror_dialogue_in_map5 == Jonny_mirror_dialogue_in_map5:
                
                if self.count < len(self.mirror_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和門的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.door2 and self.map == MAP5:
            if MAP5_BLOCK[11][18] == 0:
                self.door_dialogue_in_map5 = Jonny_door_dialogue2_in_map5

            if self.door_dialogue_in_map5 == Jonny_door_dialogue1_in_map5:
                
                if self.count < len(self.door_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.door_dialogue_in_map5 == Jonny_door_dialogue2_in_map5:
                
                if self.count < len(self.door_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5[5][18] = 0
                    MAP5_BLOCK[5][19] = 0
                    return False

##################################################################################################### 以下為和祭壇的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.altar and self.map == MAP5:
            if MAP5_BLOCK[8][1] == 0:
                self.altar_dialogue_in_map5 = Jonny_altar_dialogue2_in_map5

            if MAP5[8][2] == 30 and MAP5[9][1] == 31 and MAP5[9][3] == 32 and MAP5[10][2] == 33:
                self.altar_dialogue_in_map5 = Jonny_altar_dialogue3_in_map5

            if MAP6_BLOCK[1][19] == 0:
                self.altar_dialogue_in_map5 = Jonny_altar_dialogue4_in_map5

            if self.altar_dialogue_in_map5 == Jonny_altar_dialogue1_in_map5:
                
                if self.count < len(self.altar_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5_BLOCK[8][1] = 0
                    return False

            elif self.altar_dialogue_in_map5 == Jonny_altar_dialogue2_in_map5:
                
                if self.count < len(self.altar_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.altar_dialogue_in_map5 == Jonny_altar_dialogue3_in_map5:
                
                if self.count < len(self.altar_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP6_BLOCK[1][19] = 0
                    MAP6[1][18] = 50
                    self.music.play_sound(self.door_lock)

                    return False

            elif self.altar_dialogue_in_map5 == Jonny_altar_dialogue4_in_map5:
                
                if self.count < len(self.altar_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和酒桶的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.urn and self.map == MAP5:
            if MAP5_BLOCK[10][19] == 0:
                self.urn_dialogue_in_map5 = Jonny_urn_dialogue2_in_map5

            if self.urn_dialogue_in_map5 == Jonny_urn_dialogue1_in_map5:
                
                if self.count < len(self.urn_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5_BLOCK[10][19] = 0
                    MAP5[8][2] = 30
                    return False

            elif self.urn_dialogue_in_map5 == Jonny_urn_dialogue2_in_map5:
                
                if self.count < len(self.urn_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和陷阱的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.trap and self.map == MAP5:
            if self.trap_dialogue_in_map5 == Jonny_trap_dialogue1_in_map5:
                
                if self.count < len(self.trap_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和酒桶1的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.urn1 and self.map == MAP5:
            if self.urn1_dialogue_in_map5 == Jonny_urn1_dialogue1_in_map5:
                
                if self.count < len(self.urn1_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和酒桶2的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.urn2 and self.map == MAP5:
            if MAP9_BLOCK[1][1] == 0 :
                self.urn2_dialogue_in_map5 = Jonny_urn2_dialogue2_in_map5

            if MAP5_BLOCK[5][12] == 0 :
                self.urn2_dialogue_in_map5 = Jonny_urn2_dialogue3_in_map5

            if self.urn2_dialogue_in_map5 == Jonny_urn2_dialogue1_in_map5:
                
                if self.count < len(self.urn2_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.urn2_dialogue_in_map5 == Jonny_urn2_dialogue2_in_map5:
                
                if self.count < len(self.urn2_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5_BLOCK[5][12] = 0
                    return False

            elif self.urn2_dialogue_in_map5 == Jonny_urn2_dialogue3_in_map5:
                
                if self.count < len(self.urn2_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和公告4的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.sign4 and self.map == MAP5:
            if self.sign4_dialogue_in_map5 == Jonny_sign4_dialogue_in_map5:
                
                if self.count < len(self.sign4_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和梯子的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.ladder and self.map == MAP5:
            if self.ladder_dialogue_in_map5 == Jonny_ladder_dialogue_in_map5:
                
                if self.count < len(self.ladder_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和女生衣服的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.cloth_g and self.map == MAP5:
            if self.cloth_g_dialogue_in_map5 == Jonny_cloth_g_dialogue_in_map5:
                
                if self.count < len(self.cloth_g_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和男生衣服的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.cloth_b and self.map == MAP5:
            if self.cloth_b_dialogue_in_map5 == Jonny_cloth_b_dialogue_in_map5:
                
                if self.count < len(self.cloth_b_dialogue_in_map5):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和小櫥櫃的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.small_shelf and self.map == MAP5:
            if self.small_shelf_dialogue_in_map5 == Jonny_small_shelf_dialogue_in_map5:
                
                if self.count < len(self.small_shelf_dialogue_in_map5):
                    if self.count == 0:
                        self.music.play_sound(self.shelf_m)
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    #self.music.play_sound(self.shelf_m)
                    return False

##########################################################################################################  MAP5終止線    MAP6開始線

##################################################################################################### 以下為和寶箱的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.treasure1 and self.map == MAP6:
            if MAP6_BLOCK[10][19] == 0:
                self.treasure_dialogue_in_map6 = Jonny_treasure_dialogue2_in_map6

            if self.treasure_dialogue_in_map6 == Jonny_treasure_dialogue1_in_map6:
                
                if self.count < len(self.treasure_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP6_BLOCK[10][19] = 0
                    MAP5[10][2] = 33
                    return False

            if self.treasure_dialogue_in_map6 == Jonny_treasure_dialogue2_in_map6:
                
                if self.count < len(self.treasure_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和風扇的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.fan and self.map == MAP6:
            if MAP5[1][18] == 22 and MAP8[10][1] == 17 :
                if MAP6_BLOCK[0][0] == 1:
                    self.fan_dialogue_in_map6 = Jonny_fan_dialogue2_in_map6
                else: 
                    self.fan_dialogue_in_map6 = Jonny_fan_dialogue3_in_map6
            else:
                self.fan_dialogue_in_map6 = Jonny_fan_dialogue1_in_map6

            if self.fan_dialogue_in_map6 == Jonny_fan_dialogue1_in_map6:
                
                if self.count < len(self.fan_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP6_BLOCK[0][0] = 1
                    return False

            elif self.fan_dialogue_in_map6 == Jonny_fan_dialogue2_in_map6:
                
                if self.count < len(self.fan_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP6_BLOCK[0][0] = 0
                    MAP6[7][16] = 0
                    MAP6[7][17] = 0
                    MAP6[7][18] = 0
                    MAP6[8][16] = 0
                    MAP6[8][15] = 0
                    MAP6[9][15] = 0
                    MAP6[10][15] = 0
                    MAP6_BLOCK[8][16] = 0
                    MAP6_BLOCK[8][17] = 0
                    MAP6_BLOCK[8][18] = 0
                    MAP6_BLOCK[9][16] = 0
                    MAP6_BLOCK[10][16] = 0
                    return False

            elif self.fan_dialogue_in_map6 == Jonny_fan_dialogue3_in_map6:
                
                if self.count < len(self.fan_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP6_BLOCK[0][0] = 1
                    return False

##################################################################################################### 以下為和毒氣的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.gas and self.map == MAP6:
            if self.gas_dialogue_in_map6 == Jonny_gas_dialogue_in_map6:
                
                if self.count < len(self.gas_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和密碼寶箱的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.treasure2 and self.map == MAP6:
            if MAP5_BLOCK[9][19] == 0:
                self.treasure2_dialogue_in_map6 = Jonny_treasure2_dialogue2_in_map6

            if MAP5[9][3] == 32:
                self.treasure2_dialogue_in_map6 = Jonny_treasure2_dialogue3_in_map6

            if self.treasure2_dialogue_in_map6 == Jonny_treasure2_dialogue1_in_map6:
                
                if self.count < len(self.treasure2_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    if self.lock.get_ok() == False:
                        self.lock.run()
                        if self.lock.get_ok():
                            MAP5_BLOCK[9][19] = 0
                    return False

            elif self.treasure2_dialogue_in_map6 == Jonny_treasure2_dialogue2_in_map6:
                
                if self.count < len(self.treasure2_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    if self.count == 1:
                        self.music.play_sound(self.door_lock)
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5[9][3] = 32
                    return False

            elif self.treasure2_dialogue_in_map6 == Jonny_treasure2_dialogue3_in_map6:
                
                if self.count < len(self.treasure2_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和檯燈的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.lamp and self.map == MAP6:
            if self.lamp_dialogue_in_map6 == Jonny_lamp_dialogue_in_map6:
                
                if self.count < len(self.lamp_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和板凳的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.bench and self.map == MAP6:
            if self.bench_dialogue_in_map6 == Jonny_bench_dialogue_in_map6:
                
                if self.count < len(self.bench_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和壁爐的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.fireplace and self.map == MAP6:
            if self.fireplace_dialogue_in_map6 == Jonny_fireplace_dialogue_in_map6:
                
                if self.count < len(self.fireplace_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和盆栽的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.grass and self.map == MAP6:
            if self.grass_dialogue_in_map6 == Jonny_grass_dialogue_in_map6:
                
                if self.count < len(self.grass_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和門的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.door2 and self.map == MAP6:
            if self.door_dialogue_in_map6 == Jonny_door_dialogue_in_map6:
                
                if self.count < len(self.door_dialogue_in_map6):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False



############################################################################################################     MAP6終止線 MAP7開始線

##################################################################################################### 以下為和槌子的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.hammer and self.map == MAP7:

            if self.hammer_dialogue_in_map7 == Vivian_hammer_dialogue_in_map7:
                
                if self.count < len(self.hammer_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP7_BLOCK[1][1] = 0
                    MAP7[1][1] = 0
                    MAP7[1][2] = 0
                    return False

##################################################################################################### 以下為和電線的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.ele and self.map == MAP7:
            if self.ele_dialogue_in_map7 == Vivian_ele_dialogue1_in_map7:
                
                if self.count < len(self.ele_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和牆壁的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.wall and self.map == MAP7:
            '''if self.laser_value == True and MAP7_BLOCK[11][0] == 0 :
                #print(self.laser1_value)
                self.laser1_value = True
            else:
                self.laser1_value = False'''

            if MAP7[1][1] == 0:
                self.wall_dialogue_in_map7 = Vivian_wall_dialogue2_in_map7

            if MAP7_BLOCK[11][0] == 0:   #############    到這裡
                self.wall_dialogue_in_map7 = Vivian_wall_dialogue3_in_map7

            if self.wall_dialogue_in_map7 == Vivian_wall_dialogue1_in_map7:
                
                if self.count < len(self.wall_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False
            

            elif self.wall_dialogue_in_map7 == Vivian_wall_dialogue2_in_map7:
                
                if self.count < len(self.wall_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP7_BLOCK[11][0] = 0
                    return False

            elif self.wall_dialogue_in_map7 == Vivian_wall_dialogue3_in_map7:
                
                if self.count < len(self.wall_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和石頭的對話  map7

        elif [self.role_loaction_x, self.role_loaction_y] in self.rock1 and self.map == MAP7:
            if self.rock_dialogue_in_map7 == Vivian_rock_dialogue_in_map7:
                
                if self.count < len(self.rock_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和工具箱的對話  map7

        elif [self.role_loaction_x, self.role_loaction_y] in self.box and self.map == MAP7:
            if self.box_dialogue_in_map7 == Vivian_box_dialogue_in_map7:
                
                if self.count < len(self.box_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和鉗子的對話  map7

        elif [self.role_loaction_x, self.role_loaction_y] in self.pliers and self.map == MAP7:
            if self.pliers_dialogue_in_map7 == Vivian_pliers_dialogue_in_map7:
                
                if self.count < len(self.pliers_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

                    
##################################################################################################### 以下為和櫥櫃的對話  map7

        elif [self.role_loaction_x, self.role_loaction_y] in self.shelf2 and self.map == MAP7:
            if self.shelf_dialogue_in_map7 == Vivian_shelf_dialogue_in_map7:
                
                if self.count < len(self.shelf_dialogue_in_map7):
                    if self.count == 0:
                        self.music.play_sound(self.shelf_m)
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    #self.music.play_sound(self.shelf_m)
                    return False

##################################################################################################### 以下為和小相框的對話  map7

        elif [self.role_loaction_x, self.role_loaction_y] in self.frame and self.map == MAP7:
            if self.frame_dialogue_in_map7 == Vivian_frame_dialogue_in_map7:
                
                if self.count < len(self.frame_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和雷射光前面的對話  map7

        elif [self.role_loaction_x, self.role_loaction_y] in self.front and self.map == MAP7:
            if self.laser1_dialogue_in_map7 == Vivian_laser_dialogue_in_map7:
                
                if self.count < len(self.laser1_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和骷髏頭的對話  map7

        elif [self.role_loaction_x, self.role_loaction_y] in self.dead and self.map == MAP7:
            if self.dead_dialogue_in_map7 == Vivian_dead_dialogue_in_map7:
                
                if self.count < len(self.dead_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和雷射光的對話  map7

        elif [self.role_loaction_x, self.role_loaction_y] in self.laser and self.map == MAP7:
            if MAP5[1][18] == 22 and MAP8[10][1] == 17 :
                if MAP7_BLOCK[0][0] == 1:
                    self.laser_dialogue_in_map7 = Vivian_laser_dialogue2_in_map7
                else: 
                    self.laser_dialogue_in_map7 = Vivian_laser_dialogue3_in_map7
            else:
                self.laser_dialogue_in_map7 = Vivian_laser_dialogue1_in_map7


            if self.laser_dialogue_in_map7 == Vivian_laser_dialogue1_in_map7:
                
                if self.count < len(self.laser_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP7_BLOCK[0][0] =  1
                    self.laser_value = False
                    return False

            elif self.laser_dialogue_in_map7 == Vivian_laser_dialogue2_in_map7:
                
                if self.count < len(self.laser_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    self.laser_value = True
                    MAP7_BLOCK[0][0] =  0
                    return False

            elif self.laser_dialogue_in_map7 == Vivian_laser_dialogue3_in_map7:
                
                if self.count < len(self.laser_dialogue_in_map7):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    self.laser_value = False
                    MAP7_BLOCK[0][0] =  1
                    return False







############################################################################################################     MAP7終止線 MAP8開始線

##################################################################################################### 以下為和水的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.water and self.map == MAP8:
            if self.water_dialogue_in_map8 == Vivian_water_dialogue_in_map8:
                
                if self.count < len(self.water_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和電線的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.ele and self.map == MAP8:
            if MAP8[10][1] == 6:
                self.ele_dialogue_in_map8 = Vivian_ele_dialogue1_in_map8
            if MAP8[10][1] == 17:
                self.ele_dialogue_in_map8 = Vivian_ele_dialogue2_in_map8

            if self.ele_dialogue_in_map8 == Vivian_ele_dialogue1_in_map8:
                
                if self.count < len(self.ele_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP8[10][1] = 17
                    return False

            elif self.ele_dialogue_in_map8 == Vivian_ele_dialogue2_in_map8:
                
                if self.count < len(self.ele_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP8[10][1] = 6
                    return False

##################################################################################################### 以下為和按鈕的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.btn and self.map == MAP8:
            if MAP5_BLOCK[2][2]:
                self.btn_dialogue_in_map8 = Vivian_btn_dialogue1_in_map8
            else:
                self.btn_dialogue_in_map8 = Vivian_btn_dialogue2_in_map8

            if self.btn_dialogue_in_map8 == Vivian_btn_dialogue1_in_map8:
                
                if self.count < len(self.btn_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5[2][2] = 0
                    MAP5[3][2] = 0
                    MAP5_BLOCK[2][2] = 0
                    return False

            elif self.btn_dialogue_in_map8 == Vivian_btn_dialogue2_in_map8:
                
                if self.count < len(self.btn_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP5[2][2] = 13
                    MAP5[3][2] = 14
                    MAP5_BLOCK[2][2] = 1
                    return False

##################################################################################################### 以下為和相框的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.paint and self.map == MAP8:
            if self.paint_dialogue_in_map8 == Vivian_paint_dialogue1_in_map8:
                
                if self.count < len(self.paint_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.paint_value = True
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    self.paint_value = False
                    return False

##################################################################################################### 以下為和冰箱的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.refri and self.map == MAP8:
            if MAP5[1][18] == 22 and MAP8[10][1] == 17 :
                if MAP8_BLOCK[0][0] == 1:
                    self.refri_dialogue_in_map8 = Vivian_refri_dialogue2_in_map8
                else: 
                    self.refri_dialogue_in_map8 = Vivian_refri_dialogue3_in_map8
            else:
                self.refri_dialogue_in_map8 = Vivian_refri_dialogue1_in_map8

            if self.refri_dialogue_in_map8 == Vivian_refri_dialogue1_in_map8:
                
                if self.count < len(self.refri_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP8_BLOCK[0][0] = 1
                    return False
            
            elif self.refri_dialogue_in_map8 == Vivian_refri_dialogue2_in_map8:
                
                if self.count < len(self.refri_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP8_BLOCK[0][0] = 0
                    MAP8[7][15] = 10
                    MAP8[7][16] = 10     #水的位置
                    MAP8[7][17] = 10
                    MAP8[7][18] = 10
                    MAP8[8][15] = 10
                    MAP8[8][16] = 10
                    MAP8[8][17] = 10
                    MAP8[8][18] = 10
                    MAP8[9][15] = 10
                    MAP8[9][16] = 10
                    MAP8[10][15] = 10
                    MAP8[10][16] = 10
                    MAP8[9][17] = 10

                    MAP8[6][15] = 0
                    MAP8[6][16] = 0     #水的對話位置
                    MAP8[6][17] = 0
                    MAP8[6][18] = 0
                    MAP8[7][14] = 0
                    MAP8[8][14] = 0
                    MAP8[9][14] = 0
                    MAP8[10][14] = 0

                    MAP8_BLOCK[7][15] = 0
                    MAP8_BLOCK[7][16] = 0     #水的位置
                    MAP8_BLOCK[7][17] = 0
                    MAP8_BLOCK[7][18] = 0
                    MAP8_BLOCK[8][15] = 0
                    MAP8_BLOCK[8][16] = 0
                    MAP8_BLOCK[8][17] = 0
                    MAP8_BLOCK[8][18] = 0
                    MAP8_BLOCK[9][15] = 0
                    MAP8_BLOCK[9][16] = 0
                    MAP8_BLOCK[10][15] = 0
                    MAP8_BLOCK[10][16] = 0
                    return False

            elif self.refri_dialogue_in_map8 == Vivian_refri_dialogue3_in_map8:
                
                if self.count < len(self.refri_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP8_BLOCK[0][0] = 1

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
                    return False

##################################################################################################### 以下為和長笛的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.flute and self.map == MAP8:
            if self.flute_dialogue_in_map8 == Vivian_flute_dialogue_in_map8:
                
                if self.count < len(self.flute_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和小提琴盒子的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.violin_box and self.map == MAP8:
            if self.violin_box_dialogue_in_map8 == Vivian_violin_box_dialogue_in_map8:
                
                if self.count < len(self.violin_box_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和小提琴的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.violin and self.map == MAP8:
            if self.violin_dialogue_in_map8 == Vivian_violin_dialogue_in_map8:
                
                if self.count < len(self.violin_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和鋼琴的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.piano and self.map == MAP8:
            if self.piano_dialogue_in_map8 == Vivian_piano_dialogue_in_map8:
                
                if self.count < len(self.piano_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和大提琴的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.cello and self.map == MAP8:
            if self.cello_dialogue_in_map8 == Vivian_cello_dialogue_in_map8:
                
                if self.count < len(self.cello_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和法國號的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.trumpet and self.map == MAP8:
            if self.trumpet_dialogue_in_map8 == Vivian_trumpet_dialogue_in_map8:
                
                if self.count < len(self.trumpet_dialogue_in_map8):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

############################################################################################################     MAP8終止線 MAP9開始線

##################################################################################################### 以下為和櫥櫃的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.cabinet and self.map == MAP9:
            if self.cabinet_dialogue_in_map9 == Jonny_cabinet_dialogue_in_map9:
                
                if self.count < len(self.cabinet_dialogue_in_map9):
                    if self.count == 0:
                        self.music.play_sound(self.shelf_m)
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    
                    return False

##################################################################################################### 以下為和機器1的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.mashine1 and self.map == MAP9:
            if self.mashine1_dialogue_in_map9 == Jonny_mashine1_dialogue_in_map9:
                
                if self.count < len(self.mashine1_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和機器2的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.mashine2 and self.map == MAP9:
            if self.mashine2_dialogue_in_map9 == Jonny_mashine2_dialogue_in_map9:
                
                if self.count < len(self.mashine2_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和機器3的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.mashine3 and self.map == MAP9:
            if self.mashine3_dialogue_in_map9 == Jonny_mashine3_dialogue_in_map9:
                
                if self.count < len(self.mashine3_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和顯微鏡的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.micro and self.map == MAP9:
            if self.micro_dialogue_in_map9 == Jonny_micro_dialogue_in_map9:
                
                if self.count < len(self.micro_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和螢幕的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.screen1 and self.map == MAP9:
            if self.screen_dialogue_in_map9 == Jonny_screen_dialogue_in_map9:
                
                if self.count < len(self.screen_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和酒精的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.alcohol and self.map == MAP9:
            if MAP9_BLOCK[11][19] == 0:
                self.alcohol_dialogue_in_map9 = Jonny_alcohol_dialogue2_in_map9

            if self.alcohol_dialogue_in_map9 == Jonny_alcohol_dialogue1_in_map9:
                
                if self.count < len(self.alcohol_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_BLOCK[11][19] = 0
                    return False

            elif self.alcohol_dialogue_in_map9 == Jonny_alcohol_dialogue2_in_map9:
                
                if self.count < len(self.alcohol_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False



##################################################################################################### 以下為和氯化鈉的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.nacl and self.map == MAP9:
            if MAP9_BLOCK[0][0] == 0:
                self.nacl_dialogue_in_map9 = Jonny_nacl_dialogue2_in_map9

            if self.nacl_dialogue_in_map9 == Jonny_nacl_dialogue1_in_map9:
                
                if self.count < len(self.nacl_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_BLOCK[0][0] = 0
                    return False

            elif self.nacl_dialogue_in_map9 == Jonny_nacl_dialogue2_in_map9:
                
                if self.count < len(self.nacl_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和濃縮器的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.concentrator and self.map == MAP9:
            if MAP9_BLOCK[11][19] == 0:
                self.concentrator_dialogue_in_map9 = Jonny_concentrator_dialogue2_in_map9

            if MAP9_BLOCK[0][18] == 0:
                self.concentrator_dialogue_in_map9 = Jonny_concentrator_dialogue3_in_map9

            if self.concentrator_dialogue_in_map9 == Jonny_concentrator_dialogue1_in_map9:
                
                if self.count < len(self.concentrator_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.concentrator_dialogue_in_map9 == Jonny_concentrator_dialogue2_in_map9:
                
                if self.count < len(self.concentrator_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_BLOCK[0][18] = 0
                    return False

            elif self.concentrator_dialogue_in_map9 == Jonny_concentrator_dialogue3_in_map9:
                
                if self.count < len(self.concentrator_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和NPC1的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.NPC1 and self.map == MAP9:
            if self.dark:
                self.NPC1_dialogue_in_map9 = Jonny_NPC1_dialogue2_in_map9
            else:
                self.NPC1_dialogue_in_map9 = Jonny_NPC1_dialogue1_in_map9

            if self.NPC1_dialogue_in_map9 == Jonny_NPC1_dialogue1_in_map9:
                
                if self.count < len(self.NPC1_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.NPC1_dialogue_in_map9 == Jonny_NPC1_dialogue2_in_map9:
                
                if self.count < len(self.NPC1_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和NPC2的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.NPC2 and self.map == MAP9:
            if self.dark:
                self.NPC2_dialogue_in_map9 = Jonny_NPC2_dialogue2_in_map9
            else:
                self.NPC2_dialogue_in_map9 = Jonny_NPC2_dialogue1_in_map9

            if self.NPC2_dialogue_in_map9 == Jonny_NPC2_dialogue1_in_map9:
                
                if self.count < len(self.NPC2_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.NPC2_dialogue_in_map9 == Jonny_NPC2_dialogue2_in_map9:
                
                if self.count < len(self.NPC2_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和NPC3的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.NPC3 and self.map == MAP9:
            if self.dark:
                self.NPC3_dialogue_in_map9 = Jonny_NPC3_dialogue2_in_map9
            else:
                self.NPC3_dialogue_in_map9 = Jonny_NPC3_dialogue1_in_map9

            if self.NPC3_dialogue_in_map9 == Jonny_NPC3_dialogue1_in_map9:
                
                if self.count < len(self.NPC3_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.NPC3_dialogue_in_map9 == Jonny_NPC3_dialogue2_in_map9:
                
                if self.count < len(self.NPC3_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和NPC4的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.NPC4 and self.map == MAP9:
            if self.dark:
                self.NPC4_dialogue_in_map9 = Jonny_NPC4_dialogue2_in_map9
            else:
                self.NPC4_dialogue_in_map9 = Jonny_NPC4_dialogue1_in_map9

            if self.NPC4_dialogue_in_map9 == Jonny_NPC4_dialogue1_in_map9:
                
                if self.count < len(self.NPC4_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.NPC4_dialogue_in_map9 == Jonny_NPC4_dialogue2_in_map9:
                
                if self.count < len(self.NPC4_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和NPC5的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.NPC5 and self.map == MAP9:
            if self.dark:
                self.NPC5_dialogue_in_map9 = Jonny_NPC5_dialogue2_in_map9
            else:
                self.NPC5_dialogue_in_map9 = Jonny_NPC5_dialogue1_in_map9

            if self.NPC5_dialogue_in_map9 == Jonny_NPC5_dialogue1_in_map9:
                
                if self.count < len(self.NPC5_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.NPC5_dialogue_in_map9 == Jonny_NPC5_dialogue2_in_map9:
                
                if self.count < len(self.NPC5_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和NPC6的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.NPC6 and self.map == MAP9:
            if self.dark:
                self.NPC6_dialogue_in_map9 = Jonny_NPC6_dialogue2_in_map9
            else:
                self.NPC6_dialogue_in_map9 = Jonny_NPC6_dialogue1_in_map9

            if self.NPC6_dialogue_in_map9 == Jonny_NPC6_dialogue1_in_map9:
                
                if self.count < len(self.NPC6_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.NPC6_dialogue_in_map9 == Jonny_NPC6_dialogue2_in_map9:
                
                if self.count < len(self.NPC6_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和NPC7的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.NPC7 and self.map == MAP9:
            if self.dark:
                self.NPC7_dialogue_in_map9 = Jonny_NPC7_dialogue2_in_map9
            else:
                self.NPC7_dialogue_in_map9 = Jonny_NPC7_dialogue1_in_map9

            if self.NPC7_dialogue_in_map9 == Jonny_NPC7_dialogue1_in_map9:
                
                if self.count < len(self.NPC7_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.NPC7_dialogue_in_map9 == Jonny_NPC7_dialogue2_in_map9:
                
                if self.count < len(self.NPC7_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和DR的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.DR1 and self.map == MAP9:
            if MAP9_BLOCK[7][19] == 0:
                self.DR_dialogue_in_map9 = Jonny_DR_dialogue2_in_map9

            if MAP9_BLOCK[0][0] == 0 and MAP9_BLOCK[11][19] == 0 and MAP9_1_BLOCK[0][4] == 0 and MAP9_1_BLOCK[0][0] == 0 and MAP9_1_BLOCK[11][0] == 0 and MAP9_1_BLOCK[0][19] == 0 :
                self.DR_dialogue_in_map9 = Jonny_DR_dialogue3_in_map9

            if MAP9_BLOCK[1][1] == 0:
                self.DR_dialogue_in_map9 = Jonny_DR_dialogue4_in_map9

            if MAP5_BLOCK[5][12] == 0 :
                self.DR_dialogue_in_map9 = Jonny_DR_dialogue5_in_map9

            if MAP9_BLOCK[0][9] == 0:
                self.DR_dialogue_in_map9 = Jonny_DR_dialogue6_in_map9

            if self.DR_dialogue_in_map9 == Jonny_DR_dialogue1_in_map9:
                
                if self.count < len(self.DR_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_BLOCK[7][19] = 0
                    return False

            elif self.DR_dialogue_in_map9 == Jonny_DR_dialogue2_in_map9:
                
                if self.count < len(self.DR_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.DR_dialogue_in_map9 == Jonny_DR_dialogue3_in_map9:
                
                if self.count < len(self.DR_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_BLOCK[1][1] = 0
                    return False

            elif self.DR_dialogue_in_map9 == Jonny_DR_dialogue4_in_map9:
                
                if self.count < len(self.DR_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.DR_dialogue_in_map9 == Jonny_DR_dialogue5_in_map9:
                
                if self.count < len(self.DR_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_BLOCK[0][9] = 0
                    MAP9_1[5][17] = 50
                    return False

            elif self.DR_dialogue_in_map9 == Jonny_DR_dialogue6_in_map9:
                
                if self.count < len(self.DR_dialogue_in_map9):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False





############################################################################################################     MAP9終止線 MAP9_1開始線

##################################################################################################### 以下為和沙發的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.sofa1 and self.map == MAP9_1:
            if self.sofa_dialogue_in_map9_1 == Jonny_sofa_dialogue_in_map9_1:
                
                if self.count < len(self.sofa_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和電視的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.tv and self.map == MAP9_1:
            if self.tv_dialogue_in_map9_1 == Jonny_tv_dialogue_in_map9_1:
                
                if self.count < len(self.tv_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和水桶的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.bucket and self.map == MAP9_1:
            if self.bucket_dialogue_in_map9_1 == Jonny_bucket_dialogue_in_map9_1:
                
                if self.count < len(self.bucket_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和淋浴工具的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.shower and self.map == MAP9_1:
            if self.shower_dialogue_in_map9_1 == Jonny_shower_dialogue_in_map9_1:
                
                if self.count < len(self.shower_dialogue_in_map9_1):
                    '''if self.count == 0 :
                        self.music.play_sound(self.shower_m)'''
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和病毒的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.virus1 and self.map == MAP9_1:
            if MAP9_BLOCK[0][18] == 0:
                self.virus_dialogue_in_map9_1 = Jonny_virus_dialogue2_in_map9_1

            if self.virus_dialogue_in_map9_1 == Jonny_virus_dialogue1_in_map9_1:
                
                if self.count < len(self.virus_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            if self.virus_dialogue_in_map9_1 == Jonny_virus_dialogue2_in_map9_1:
                
                if self.count < len(self.virus_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_1[1][15] = 0
                    MAP9_1[1][16] = 0
                    MAP9_1[2][14] = 0
                    MAP9_1[2][16] = 0
                    MAP9_1[2][17] = 0
                    MAP9_1[3][15] = 0
                    MAP9_1[3][16] = 0
                    MAP9_1[3][18] = 0
                    MAP9_1[4][16] = 0
                    MAP9_1[4][17] = 0
                    MAP9_1_BLOCK[1][15] = 0
                    MAP9_1_BLOCK[1][16] = 0
                    MAP9_1_BLOCK[2][14] = 0
                    MAP9_1_BLOCK[2][16] = 0
                    MAP9_1_BLOCK[2][17] = 0
                    MAP9_1_BLOCK[3][15] = 0
                    MAP9_1_BLOCK[3][16] = 0
                    MAP9_1_BLOCK[3][18] = 0
                    MAP9_1_BLOCK[4][16] = 0
                    MAP9_1_BLOCK[4][17] = 0
                    MAP9_1[1][14] = 0
                    MAP9_1[2][13] = 0
                    MAP9_1[3][14] = 0
                    MAP9_1[4][15] = 0
                    MAP9_1[5][16] = 0
                    MAP9_1[5][17] = 0
                    MAP9_1[4][17] = 0
                    MAP9_1[3][18] = 0
                    MAP9_1[4][18] = 0
                    return False

##################################################################################################### 以下為和蔗糖的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.sugar and self.map == MAP9_1:
            if MAP9_1_BLOCK[0][4] == 0:
                self.sugar_dialogue_in_map9_1 = Jonny_sugar_dialogue2_in_map9_1

            if self.sugar_dialogue_in_map9_1 == Jonny_sugar_dialogue1_in_map9_1:
                
                if self.count < len(self.sugar_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_1_BLOCK[0][4] = 0
                    return False

            elif self.sugar_dialogue_in_map9_1 == Jonny_sugar_dialogue2_in_map9_1:
                
                if self.count < len(self.sugar_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和edta的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.edta and self.map == MAP9_1:
            if MAP9_1_BLOCK[0][0] == 0 :
                self.edta_dialogue_in_map9_1 = Jonny_edta_dialogue2_in_map9_1

            if self.edta_dialogue_in_map9_1 == Jonny_edta_dialogue1_in_map9_1:
                
                if self.count < len(self.edta_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_1_BLOCK[0][0] = 0
                    return False

            elif self.edta_dialogue_in_map9_1 == Jonny_edta_dialogue2_in_map9_1:
                
                if self.count < len(self.edta_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和80的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.d80 and self.map == MAP9_1:
            if MAP9_1_BLOCK[11][0] == 0 :
                self.d80_dialogue_in_map9_1 = Jonny_d80_dialogue2_in_map9_1

            if self.d80_dialogue_in_map9_1 == Jonny_d80_dialogue1_in_map9_1:
                
                if self.count < len(self.d80_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_1_BLOCK[11][0] = 0
                    return False

            elif self.d80_dialogue_in_map9_1 == Jonny_d80_dialogue2_in_map9_1:
                
                if self.count < len(self.d80_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和mgcl的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.mgcl and self.map == MAP9_1:
            if MAP9_1_BLOCK[0][19] == 0:
                self.mgcl_dialogue_in_map9_1 = Jonny_mgcl_dialogue2_in_map9_1

            if self.mgcl_dialogue_in_map9_1 == Jonny_mgcl_dialogue1_in_map9_1:
                
                if self.count < len(self.mgcl_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_1_BLOCK[0][19] = 0
                    return False

            elif self.mgcl_dialogue_in_map9_1 == Jonny_mgcl_dialogue2_in_map9_1:
                
                if self.count < len(self.mgcl_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和NPC1的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.NPC1 and self.map == MAP9_1:
            if self.dark:
                self.NPC1_dialogue_in_map9_1 = Jonny_NPC1_dialogue1_in_map9_1
            else:
                self.NPC1_dialogue_in_map9_1 = Jonny_NPC1_dialogue_in_map9_1

            if self.NPC1_dialogue_in_map9_1 == Jonny_NPC1_dialogue_in_map9_1:
                
                if self.count < len(self.NPC1_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.NPC1_dialogue_in_map9_1 == Jonny_NPC1_dialogue1_in_map9_1:
                
                if self.count < len(self.NPC1_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和NPC2的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.NPC2 and self.map == MAP9_1:
            if self.dark:
                self.NPC2_dialogue_in_map9_1 = Jonny_NPC2_dialogue1_in_map9_1
            else:
                self.NPC2_dialogue_in_map9_1 = Jonny_NPC2_dialogue_in_map9_1

            if self.NPC2_dialogue_in_map9_1 == Jonny_NPC2_dialogue_in_map9_1:
                
                if self.count < len(self.NPC2_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.NPC2_dialogue_in_map9_1 == Jonny_NPC2_dialogue1_in_map9_1:
                
                if self.count < len(self.NPC2_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和Dr的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.dr2 and self.map == MAP9_1:
            if self.dr_dialogue_in_map9_1 == Jonny_dr_dialogue_in_map9_1:
                
                if self.count < len(self.dr_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和sis的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.sis and self.map == MAP9_1:
            if MAP10[0][0] == 0 :
                self.sis_dialogue_in_map9_1 = Jonny_sis_dialogue1_in_map9_1

            '''if self.dark:
                self.sis_dialogue_in_map9_1 = Jonny_sis_dialogue2_in_map9_1
            else:
                self.sis_dialogue_in_map9_1 = Jonny_sis_dialogue_in_map9_1'''

            if self.sis_dialogue_in_map9_1 == Jonny_sis_dialogue_in_map9_1:
                
                if self.count < len(self.sis_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.sis_dialogue_in_map9_1 == Jonny_sis_dialogue1_in_map9_1:
                
                if self.count < len(self.sis_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    if self.count == 6:
                        MAP9_1[2][10] = 30
                        MAP9_1[3][10] = 31
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP10[0][1] = 0
                    MAP9_1[1][11] = 0
                    MAP9_1[2][11] = 0
                    MAP9_1_BLOCK[1][11] = 0
                    MAP9_1_BLOCK[2][10] = 1
                    return False

            '''elif self.sis_dialogue_in_map9_1 == Jonny_sis_dialogue2_in_map9_1:
                
                if self.count < len(self.sis_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False'''




##################################################################################################### 以下為和門2的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.door2 and self.map == MAP9_1:
            if MAP9_BLOCK[0][9] == 0:
                self.door2_dialogue_in_map9_1 = Jonny_door2_dialogue2_in_map9_1

            if MAP10[0][1] == 0:
                self.door2_dialogue_in_map9_1 = Jonny_door2_dialogue3_in_map9_1

            if self.door2_dialogue_in_map9_1 == Jonny_door2_dialogue1_in_map9_1:
                
                if self.count < len(self.door2_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.door2_dialogue_in_map9_1 == Jonny_door2_dialogue2_in_map9_1:
                
                if self.count < len(self.door2_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

            elif self.door2_dialogue_in_map9_1 == Jonny_door2_dialogue3_in_map9_1:
                
                if self.count < len(self.door2_dialogue_in_map9_1):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP9_1_BLOCK[5][19] = 0
                    MAP9_1_BLOCK[6][19] = 0
                    MAP9_1[5][18] = 0
                    MAP9_1[6][18] = 0
                    MAP10[4][9] = 50
                    MAP10[5][9] = 50
                    MAP10[6][9] = 50
                    MAP10[7][9] = 50
                    self.music.play_sound(self.door_lock)
                    return False

############################################################################################################     MAP9_1終止線 MAP10開始線

##################################################################################################### 以下為和final的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.final and self.map == MAP10:
            if MAP10_BLOCK[11][19] == 0:
                self.final_dialogue_in_map10 = Jonny_final_dialogue2_in_map10

            if self.final_dialogue_in_map10 == Jonny_final_dialogue1_in_map10:
                
                if self.count < len(self.final_dialogue_in_map10):
                    if self.count == 0:
                        MAP10[5][12] = 25
                        MAP10_BLOCK[5][12] = 1
                        MAP10[6][12] = 26
                    if self.count == 17:
                        MAP10[5][11] = 30
                        MAP10_BLOCK[5][11]= 1
                        MAP10[6][11] = 31
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    MAP10_BLOCK[11][19] = 0
                    self.finish = True
                    return False

            elif self.final_dialogue_in_map10 == Jonny_final_dialogue2_in_map10:
                
                if self.count < len(self.final_dialogue_in_map10):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和妹妹的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.sis and self.map == MAP10:
            if self.sis_dialogue_in_map10 == Jonny_sis_dialogue_in_map10:
                
                if self.count < len(self.sis_dialogue_in_map10):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

##################################################################################################### 以下為和Dr的對話

        elif [self.role_loaction_x, self.role_loaction_y] in self.dr2 and self.map == MAP10:
            if self.dr_dialogue_in_map10 == Jonny_dr_dialogue_in_map10:
                
                if self.count < len(self.dr_dialogue_in_map10):
                    self.music.play_sound(self.space_sound)
                    self.count += 1
                    self.open_dialogue = True
                    return True
                else:
                    self.count = 0
                    self.open_dialogue = False
                    return False

############################################################################################################     MAP10終止線 



        else:
            return False


    def get_open_dialogue(self):
        return self.open_dialogue

    def get_count(self):
        return self.count

    def get_dark(self):
        return self.dark

    def get_dark_b(self):
        return self.dark_b

    def get_paint_value(self):
        return self.paint_value

    def get_laser_value(self):
        return self.laser_value

    def get_laser1_value(self):
        return self.laser1_value

    def get_finish(self):
        return self.finish
