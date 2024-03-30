from __future__ import annotations
from boy.game_map import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from boy.model import Player

class Get_location:
    def __init__(self, player : Player):
        
        self.player = player
        self.map = self.player.get_in_which_map()
        self.map_block = self.player.get_in_which_map_block()

    def get_location(self, map , which : int):          # which是物品代號
        x = 0
        y = 0
        location = []
        for i in map:
            for j in i:
                if j == which:
                    location.append([x, y])  
                    x += 50
                else:
                    x += 50
            x = 0
            y += 50  
        return location
#################################################################################################################   以下為障礙物的位置
    
    def get_block_location(self):                       #獲得障礙物的位置
        self.map_block = self.player.get_in_which_map_block()
        return self.get_location(self.map_block, 1) 

#################################################################################################################    以下為門的位置

    def get_door1_object_location(self):                        #門1物件的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 90)
   
    def get_door1_location(self):                               #觸發門1對話的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 91)  

    '''def get_door1_object_location_1(self):                      #門1物件的位置_1
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 94)'''

    def get_door2_object_location(self):                        #門2物件的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 92)

    def get_door2_location(self):                               #觸發門2對話的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 93)

    '''def get_door2_object_location_1(self):                      #觸發門2物件位置_1
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 95)'''

    def get_door3_object_location(self):                        #門3物件的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 94)
        
    def get_door3_location(self):                               #觸發門3對話的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 95)
################################################################################################################   以下為自己對話位置

    def get_murmur1(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 50)

    def get_murmur2(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 51)

###################################################################################################################   MAP1開始線

#################################################################################################################     以下為博士的位置

    def get_DR_object_location(self):                       #博士物件的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 3)

    def get_DR_location(self):                              #觸發博士對話的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 6)

#################################################################################################################    以下為鑰匙的位置

    def get_key_object_location(self):                 #鑰匙物件的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 5)

    def get_key_location(self):                        #觸發鑰匙對話的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 9)

#################################################################################################################  以下為石頭的位置


    def get_rock_object_location(self):                 #石頭物件的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 10)

    def get_rock_location(self):                        #觸發石頭對話的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 11)

#################################################################################################################  MAP1 終止線  MAP2開始線

################################################################################################################   以下為小丑的位置

    def get_joker_object_location(self):                        #小丑物件的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 2)

    def get_joker_object_location_1(self):                      #小丑物件的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 3)

    def get_joker_location(self):                           #觸發和小丑對話的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 4)

#################################################################################################################    以下為鼻子的位置

    def get_nose_object_location(self):                        #鼻子物件的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 11)

    def get_nose_location(self):                      #觸發和鼻子對話的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 12)

##################################################################################################################   以下為觸發遊戲的位置

    def get_game_location(self):                        #觸發和遊戲對話的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 6)

##############################################################################################################        以下為觸發病毒的位置

    def get_virus_object_location(self):                #病毒物件的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 13)

    def get_virus_location(self):                      #觸發和病毒對話的位置
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 14)

##############################################################################################################         MAP2終止線 MAP3開始線

#############################################################################################################       以下為觸發藍色矮人對話的位置

    def get_blue_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 2)

#############################################################################################################       以下為觸發黃色矮人對話的位置

    def get_yellow_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 3)

#############################################################################################################       以下為觸發紅色矮人對話的位置

    def get_red_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 4)

#############################################################################################################       以下為觸發綠色矮人對話的位置

    def get_green_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 5)

#############################################################################################################       以下為觸發灰色矮人對話的位置

    def get_gray_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 6)

#############################################################################################################       以下為觸發紫色矮人對話的位置

    def get_purple_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 7)

#############################################################################################################       以下為觸發公告1對話的位置

    def get_sign1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 8)

#############################################################################################################       以下為觸發公告2對話的位置

    def get_sign2_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 9)

############################################################################################################       以下為觸發鑰匙對話的位置

    def get_key1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 11)

#########################################################################################################      MAP3終止線  MAP4開始線

##########################################################################################################     以下為觸發書櫃對話的位置

    def get_shelf_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 2)

##########################################################################################################     以下為觸發時鐘對話的位置

    def get_clock_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 3)

##########################################################################################################     以下為觸發老鷹對話的位置

    def get_eagle_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 4)

##########################################################################################################     以下為觸發地板對話的位置

    def get_floor_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 6)

##########################################################################################################     以下為觸發花瓶對話的位置

    def get_vase_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 7)

##########################################################################################################     以下為觸發沙發對話的位置

    def get_sofa_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 8)

##########################################################################################################     以下為觸發燈對話的位置

    def get_light_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 9)

##########################################################################################################     以下為觸發貓頭鷹對話的位置

    def get_owl_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 10)

##########################################################################################################     以下為觸發烏鴉對話的位置

    def get_crow_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 11)

##########################################################################################################     以下為觸發病毒對話的位置 map4

    def get_virus_1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 14)

    def get_virus_1_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 13)

##########################################################################################################    以下為觸發鑰匙對話的位置 map4

    def get_key2_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 2)

##########################################################################################################    以下為觸發書櫃1對話的位置 map4

    def get_shelf1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 17)

##########################################################################################################    以下為觸發公告3對話的位置 map4

    def get_sign3_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 18)

##########################################################################################################    MAP4終止線    MAP5開始線

##########################################################################################################    以下為觸發寶箱對話的位置 map5

    def get_treasure_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 3)

##########################################################################################################    以下為觸發燈管對話的位置 map5

    def get_light1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 4)

##########################################################################################################    以下為觸發牆壁對話的位置 map5

    def get_wall_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 5)

##########################################################################################################    以下為觸發電線對話的位置 map5

    def get_ele_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 6)

    def get_ele_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 7)

##########################################################################################################    以下為觸發鏡子對話的位置 map5

    def get_mirror_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 8)

    def get_mirror_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 9)

##########################################################################################################    以下為觸發祭壇對話的位置 map5

    def get_altar_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 10)

    def get_altar_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 11)

#########################################################################################################    以下為觸發酒桶對話的位置 map5

    def get_urn_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 12)

#########################################################################################################    以下為觸發酒桶1對話的位置 map5

    def get_urn1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 15)

#########################################################################################################    以下為觸發酒桶2對話的位置 map5

    def get_urn2_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 16)

#########################################################################################################    以下為觸發陷阱對話的位置 map5

    def get_trap_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 13)

    def get_trap_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 14)

#########################################################################################################    以下為觸發公告對話的位置 map5

    def get_sign4_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 17)

#########################################################################################################    以下為觸發梯子對話的位置 map5

    def get_ladder_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 18)

#########################################################################################################    以下為觸發女生衣服對話的位置 map5

    def get_cloth_g_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 19)

#########################################################################################################    以下為觸發男生衣服對話的位置 map5

    def get_cloth_b_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 20)

#########################################################################################################    以下為觸發小櫥櫃對話的位置 map5

    def get_small_shelf_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 21)

##################################################################################################################     MAP5終止線   MAP6開始線

#########################################################################################################    以下為觸發電風扇對話的位置 map6

    def get_fan_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 4)

#########################################################################################################    以下為觸發毒氣對話的位置 map6

    def get_gas_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 6)

    def get_gas_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 5)

#########################################################################################################    以下為觸發檯燈對話的位置 map6

    def get_lamp_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 7)

#########################################################################################################    以下為觸發板凳對話的位置 map6

    def get_bench_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 8)

#########################################################################################################    以下為觸發壁爐對話的位置 map6

    def get_fireplace_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 9)

#########################################################################################################    以下為觸發盆栽對話的位置 map6

    def get_grass_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 10)

#########################################################################################################    以下為觸發密碼寶箱對話的位置 map6

    def get_treasure2_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 2)



#########################################################################################################    MAP6終止線  MAP7開始線

#####################################################################################################    以下為觸發laser前面對話的位置 map7

    def get_front_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 16)   

#####################################################################################################    以下為觸發槌子對話的位置 map7

    def get_hammer_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 2)

    def get_hammer_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 3)    

#####################################################################################################    以下為觸發石頭對話的位置 map7

    def get_rock1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 8)   

#####################################################################################################    以下為觸發工具箱對話的位置 map7

    def get_box_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 9)   

#####################################################################################################    以下為觸發鉗子對話的位置 map7

    def get_pliers_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 10)  

#####################################################################################################    以下為觸發櫥櫃對話的位置 map7

    def get_shelf2_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 11)    

#####################################################################################################    以下為觸發小相框對話的位置 map7

    def get_frame_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 13) 

#####################################################################################################    以下為觸發雷射光對話的位置 map7

    def get_laser_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 14)  

#####################################################################################################    以下為觸發骷髏頭對話的位置 map7

    def get_dead_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 15)      

#########################################################################################################    MAP7終止線  MAP8開始線

#########################################################################################################    以下為觸發冰箱對話的位置 map8

    def get_refri_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 2)

#########################################################################################################    以下為觸發相框對話的位置 map8

    def get_paint_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 3)

#########################################################################################################    以下為觸發水對話的位置 map8

    def get_water_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 5)

    def get_water_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 4)

#########################################################################################################    以下為冰的位置

    def get_ice_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 10)

#########################################################################################################    以下為觸發按鈕對話的位置 map8   / 冰的位置

    def get_btn_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 9)

#########################################################################################################    以下為觸發長笛對話的位置 map8   

    def get_flute_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 11)

#########################################################################################################    以下為觸發小提琴盒子對話的位置 map8   

    def get_violin_box_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 12)

#########################################################################################################    以下為觸發小提琴對話的位置 map8   

    def get_violin_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 13)

#########################################################################################################    以下為觸發鋼琴對話的位置 map8   

    def get_piano_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 14)

#########################################################################################################    以下為觸發大提琴對話的位置 map8   

    def get_cello_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 15)

#########################################################################################################    以下為觸發法國號對話的位置 map8   

    def get_trumpet_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 16)

######################################################################################################

#########################################################################################################    MAP8終止線  MAP9開始線

#########################################################################################################    以下為觸發櫥櫃對話的位置 map9   

    def get_cabinet_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 2)

#########################################################################################################    以下為觸發機器1對話的位置 map9   

    def get_mashine1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 3)

#########################################################################################################    以下為觸發機器2對話的位置 map9   

    def get_mashine2_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 4)

#########################################################################################################    以下為觸發機器3對話的位置 map9   

    def get_mashine3_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 5)

#########################################################################################################    以下為觸發顯微鏡對話的位置 map9   

    def get_micro_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 6)

#########################################################################################################    以下為觸發螢幕對話的位置 map9   

    def get_screen_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 7)

#########################################################################################################    以下為觸發濃縮器對話的位置 map9   

    def get_concentrator_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 8)

#########################################################################################################    以下為觸發酒精對話的位置 map9   

    def get_alcohol_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 9)

#########################################################################################################    以下為觸發氯化鈉對話的位置 map9   

    def get_nacl_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 18)

#########################################################################################################    以下為觸發NPC1對話的位置 map9   

    def get_NPC1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 10)

#########################################################################################################    以下為觸發NPC2對話的位置 map9   

    def get_NPC2_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 11)

#########################################################################################################    以下為觸發NPC3對話的位置 map9   

    def get_NPC3_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 12)

#########################################################################################################    以下為觸發NPC4對話的位置 map9   

    def get_NPC4_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 13)

#########################################################################################################    以下為觸發NPC5對話的位置 map9   

    def get_NPC5_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 14)

#########################################################################################################    以下為觸發NPC6對話的位置 map9   

    def get_NPC6_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 15)

#########################################################################################################    以下為觸發NPC7對話的位置 map9   

    def get_NPC7_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 16)

#########################################################################################################    以下為觸發DR對話的位置 map9   

    def get_DR1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 17)

#########################################################################################################    以下為觸發氯化鎂對話的位置 map9_1  

    def get_mgcl_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 2)

#########################################################################################################    以下為觸發沙發對話的位置 map9_1  

    def get_virus1_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 3)

    def get_virus1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 4)

#########################################################################################################    以下為觸發沙發對話的位置 map9_1  

    def get_sofa1_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 5)

#########################################################################################################    以下為觸發電視對話的位置 map9_1  

    def get_tv_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 6)

#########################################################################################################    以下為觸發沖淋設備對話的位置 map9_1  

    def get_shower_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 7)

#########################################################################################################    以下為觸發水桶對話的位置 map9_1  

    def get_bucket_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 8)

#########################################################################################################    以下為觸發蔗糖對話的位置 map9_1  

    def get_sugar_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 9)

#########################################################################################################    以下為觸發edta對話的位置 map9_1  

    def get_edta_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 12)

#########################################################################################################    以下為觸發80對話的位置 map9_1  

    def get_d80_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 13)

#########################################################################################################    以下為觸發妹妹對話的位置 map9_1  

    def get_sis_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 26)

    def get_sis_object_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 25)

#########################################################################################################    以下為觸發博士對話的位置 map9_1  

    def get_DR2_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 31)

#########################################################################################################    以下為觸發寶箱對話的位置 map10  

    def get_final_location(self):
        self.map = self.player.get_in_which_map()
        return self.get_location(self.map, 2)





