import pygame
import os

HALF_WIDTH = 25
HALF_HEIGHT = 25    

WIDTH= 50
HEIGHT = 50

WIDTH_1 = 100
HEIGHT_1 =100

JOKER_WIDTH = 75
JOKER_HEIGHT = 100

WIN_WIDTH = 1000
WIN_HEIGHT = 600
GIRL_WIDTH = 200
GIRL_HEIGHT = 200
BOY_WIDTH = 200
BOY_HEIGHT = 200

FPS = 60

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
WHITE_APRICOT = (255, 235, 205)
ORANGE = (255, 97, 0)
GOLD = (255, 215, 0)
YELLOW = (255, 255, 0)
BROWN = (94, 38, 18)
DARK_BROWN = (128, 42, 42)
OTHER_BROWN = (94, 38, 18)
SHIT = (115, 74, 18)
DARK_BLUE = (25, 25, 112)
RICE = (163, 148, 128)
EGG = (252, 230, 201)
OTHER_GREEN = (35, 60, 5)

shower = os.path.join("music/map9/shower.mp3")
ck = os.path.join("music/map3/ck.mp3")
tl = os.path.join("music/map5/transport.mp3")
shelf = os.path.join("music/map5/shelf.mp3")
light = os.path.join("music/map5/light.mp3")
rock = os.path.join("music/map0/rock.mp3")
space_sound = os.path.join("music/space1.mp3")
door_lock = os.path.join("music/doorlock.mp3")
laugh_sound = os.path.join("music/map1/laugh1.wav")
door_close = os.path.join("music/door_close.mp3")
start_bg = os.path.join("music/bak1.wav")
bg_map2 = os.path.join("music/map1/bg.mp3")
bg_map3 = os.path.join("music/map2/bg.mp3")
bg_map4 = os.path.join("music/map3/bg.mp3")
bg_map5 = os.path.join("music/map5/bg.mp3")
bg_map9 = os.path.join("music/map9/bg.mp3")
bg_map10 = os.path.join("music/map10/bg.mp3")

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
font_name = os.path.join("font.ttf")

background_image = pygame.transform.scale(pygame.image.load("images/background2.png"), (WIN_WIDTH, WIN_HEIGHT))

player_down_image = pygame.image.load(os.path.join("images/boy/boy1.png")).convert()
player_down_image = pygame.transform.scale(player_down_image, (50,50))
player_down_image.set_colorkey(BLACK)

player_down_1_image = pygame.image.load(os.path.join("images/girl/girl2.png")).convert()
player_down_1_image = pygame.transform.scale(player_down_1_image, (50,50))
player_down_1_image.set_colorkey(BLACK)

dialogue_outline_map1_image = pygame.image.load(os.path.join("images/object/map0.png"))
dialogue_outline_map1_image = pygame.transform.scale(dialogue_outline_map1_image, (800, 150))

dialogue_outline_map2_image = pygame.image.load(os.path.join("images/object/map1.png"))
dialogue_outline_map2_image = pygame.transform.scale(dialogue_outline_map2_image, (800, 150))

dialogue_outline_map3_image = pygame.image.load(os.path.join("images/object/map2.png"))
dialogue_outline_map3_image = pygame.transform.scale(dialogue_outline_map3_image, (800, 150))

dialogue_outline_map4_image = pygame.image.load(os.path.join("images/object/map3.png"))
dialogue_outline_map4_image = pygame.transform.scale(dialogue_outline_map4_image, (800, 150))

dialogue_outline_map5_image = pygame.image.load(os.path.join("images/object/map4.png"))
dialogue_outline_map5_image = pygame.transform.scale(dialogue_outline_map5_image, (800, 150))

dialogue_outline_map6_image = pygame.image.load(os.path.join("images/object/map5.png"))
dialogue_outline_map6_image = pygame.transform.scale(dialogue_outline_map6_image, (800, 150))

dialogue_outline_map10_image = pygame.image.load(os.path.join("images/object/map10.png"))
dialogue_outline_map10_image = pygame.transform.scale(dialogue_outline_map10_image, (800, 150))


'''test_image = pygame.image.load(os.path.join("images", "123.jpg"))
test_image = pygame.transform.scale(test_image, (200, 200))'''

#################################################################################################以下為MAP1

door_image = pygame.image.load(os.path.join("images/map0/door1.png")).convert()
door_image = pygame.transform.scale(door_image, (50, 50))

dr_image = pygame.image.load(os.path.join("images/map0/DR.png"))
dr_image = pygame.transform.scale(dr_image, (50, 50))

rock_image = pygame.image.load(os.path.join("images/map0/rock.png"))
rock_image = pygame.transform.scale(rock_image, (50, 50))

bg_map1_image = pygame.image.load(os.path.join("images/map0/bg3.png"))
bg_map1_image = pygame.transform.scale(bg_map1_image, (WIN_WIDTH, WIN_HEIGHT))

key_image = pygame.image.load(os.path.join("images/map0/key.png")).convert()
key_image = pygame.transform.scale(key_image, (50,50))

################################################################################################ 以下為MAP2

bg_map2_image = pygame.image.load(os.path.join("images/map1/bg.png"))
bg_map2_image = pygame.transform.scale(bg_map2_image, (WIN_WIDTH, WIN_HEIGHT))

joker_image = pygame.image.load(os.path.join("images/map1/joker.png"))
joker_image = pygame.transform.scale(joker_image, (JOKER_WIDTH, JOKER_HEIGHT))

nose_image = pygame.image.load(os.path.join("images/map1/nose.png"))
nose_image = pygame.transform.scale(nose_image, (WIDTH, HEIGHT))

virus_image = pygame.image.load(os.path.join("images/map1/virus3.png"))
virus_image = pygame.transform.scale(virus_image, (WIDTH, HEIGHT))

###############################################################################################   以下為MAP3

bg_map3_image = pygame.image.load(os.path.join("images/map2/bg1.jpg"))
bg_map3_image = pygame.transform.scale(bg_map3_image, (WIN_WIDTH, WIN_HEIGHT))

################################################################################################   以下為MAP4

bg_map4_image = pygame.image.load(os.path.join("images/map3/bg1.png"))
bg_map4_image = pygame.transform.scale(bg_map4_image, (WIN_WIDTH, WIN_HEIGHT))

bg_map4_1_image = pygame.image.load(os.path.join("images/map3/bg_1_1.png"))
bg_map4_1_image = pygame.transform.scale(bg_map4_1_image, (WIN_WIDTH, WIN_HEIGHT))

virus_1_image = pygame.image.load(os.path.join("images/map3/virus2.png"))
virus_1_image = pygame.transform.scale(virus_1_image, (WIDTH, HEIGHT))
virus_1_image.set_colorkey(WHITE)

num_image = pygame.image.load(os.path.join("images/map3/number_1_green1.png"))
num_image = pygame.transform.scale(num_image, (WIDTH_1, HEIGHT_1))

##############################################################################################   以下為MAP5

bg_map5_image = pygame.image.load(os.path.join("images/map4/bg.png"))
bg_map5_image = pygame.transform.scale(bg_map5_image, (WIN_WIDTH, WIN_HEIGHT))

trap_image = pygame.image.load(os.path.join("images/map4/trap.png"))
trap_image = pygame.transform.scale(trap_image, (WIDTH, HEIGHT))

ele_f_image = pygame.image.load(os.path.join("images/map4/ele_f.jpg"))
ele_f_image = pygame.transform.scale(ele_f_image, (WIDTH, HEIGHT))

ele_s_image = pygame.image.load(os.path.join("images/map4/ele_s.jpg"))
ele_s_image = pygame.transform.scale(ele_s_image, (WIDTH, HEIGHT))

ball1_image = pygame.image.load(os.path.join("images/map4/ball1.png"))
ball1_image = pygame.transform.scale(ball1_image, (WIDTH, HEIGHT))

ball2_image = pygame.image.load(os.path.join("images/map4/ball2.png"))
ball2_image = pygame.transform.scale(ball2_image, (WIDTH, HEIGHT))

ball3_image = pygame.image.load(os.path.join("images/map4/ball3.png"))
ball3_image = pygame.transform.scale(ball3_image, (WIDTH, HEIGHT))

ball4_image = pygame.image.load(os.path.join("images/map4/ball4.png"))
ball4_image = pygame.transform.scale(ball4_image, (WIDTH, HEIGHT))

##############################################################################################   以下為MAP6

bg_map6_image = pygame.image.load(os.path.join("images/map5/bg.jpg"))
bg_map6_image = pygame.transform.scale(bg_map6_image, (WIN_WIDTH, WIN_HEIGHT))

gas_image = pygame.image.load(os.path.join("images/map5/gas.png"))
gas_image = pygame.transform.scale(gas_image, (WIDTH*3, HEIGHT*3))

##############################################################################################   以下為MAP7

bg_map7_image = pygame.image.load(os.path.join("images/map6/bg.jpg"))
bg_map7_image = pygame.transform.scale(bg_map7_image, (WIN_WIDTH, WIN_HEIGHT))

hammer_image = pygame.image.load(os.path.join("images/map6/hammer3.png"))
hammer_image = pygame.transform.scale(hammer_image, (WIDTH, HEIGHT))
hammer_image.set_colorkey(WHITE)

laser1_image = pygame.image.load(os.path.join("images/map6/laser1.png"))
laser1_image = pygame.transform.scale(laser1_image, (WIDTH, HEIGHT))

laser2_image = pygame.image.load(os.path.join("images/map6/laser2.png"))
laser2_image = pygame.transform.scale(laser2_image, (WIDTH, HEIGHT))

laser3_image = pygame.image.load(os.path.join("images/map6/laser3.png"))
laser3_image = pygame.transform.scale(laser3_image, (WIDTH, HEIGHT))



##############################################################################################   以下為MAP8

bg_map8_image = pygame.image.load(os.path.join("images/map7/bg.jpg"))
bg_map8_image = pygame.transform.scale(bg_map8_image, (WIN_WIDTH, WIN_HEIGHT))

'''ele_f_image = pygame.image.load(os.path.join("images/map7/ele_f.png"))
ele_f_image = pygame.transform.scale(ele_f_image, (WIDTH, HEIGHT))

ele_s_image = pygame.image.load(os.path.join("images/map7/ele_s.png"))
ele_s_image = pygame.transform.scale(ele_s_image, (WIDTH, HEIGHT))'''

paint_image = pygame.image.load(os.path.join("images/map7/paint1.jpg"))
paint_image = pygame.transform.scale(paint_image, (WIDTH*18, HEIGHT*9))

water_image = pygame.image.load(os.path.join("images/map7/water.png"))
water_image = pygame.transform.scale(water_image, (WIDTH, HEIGHT))

ice_image = pygame.image.load(os.path.join("images/map7/ice.png"))
ice_image = pygame.transform.scale(ice_image, (WIDTH, HEIGHT))

ele_f_1_image = pygame.image.load(os.path.join("images/map7/ele_f.jpg"))
ele_f_1_image = pygame.transform.scale(ele_f_1_image, (WIDTH, HEIGHT))

ele_s_1_image = pygame.image.load(os.path.join("images/map7/ele_s.jpg"))
ele_s_1_image = pygame.transform.scale(ele_s_1_image, (WIDTH, HEIGHT))


###################################################################################################   以下為 MAP9

bg_map9_image = pygame.image.load(os.path.join("images/map8/bg.jpg"))
bg_map9_image = pygame.transform.scale(bg_map9_image, (WIN_WIDTH, WIN_HEIGHT))


bg_map9_1_image = pygame.image.load(os.path.join("images/map8_1/bg1.png"))
bg_map9_1_image = pygame.transform.scale(bg_map9_1_image, (WIN_WIDTH, WIN_HEIGHT))

virus_2_image = pygame.image.load(os.path.join("images/map8_1/virus1.png"))
virus_2_image = pygame.transform.scale(virus_2_image, (WIDTH, HEIGHT))

star_image = pygame.image.load(os.path.join("images/map8_1/star.png"))
star_image = pygame.transform.scale(star_image, (WIDTH, HEIGHT))

moon_image = pygame.image.load(os.path.join("images/map8_1/moon.png"))
moon_image = pygame.transform.scale(moon_image, (WIDTH*3, HEIGHT*3))

###################################################################################################   以下為MAP10

bg_map10_image = pygame.image.load(os.path.join("images/map9/bg.png"))
bg_map10_image = pygame.transform.scale(bg_map10_image, (WIN_WIDTH, WIN_HEIGHT))

