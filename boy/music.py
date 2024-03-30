import pygame
from boy.setting import *

class Music:
    def __init__(self):
        self.sound = None
        self.music = None

    def play_sound(self, sound):
        self.sound = pygame.mixer.Sound(sound)
        self.sound.set_volume(0.3)
        self.sound.play()

    def play_sound1(self, sound):
        self.sound = pygame.mixer.Sound(sound)
        self.sound.set_volume(0.2)
        self.sound.play()

    def play_music(self, music ):
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def play_music1(self, music ):
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(1.3)
        pygame.mixer.music.play(-1)

    def play_music2(self, music ):
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def play_music3(self, music ):
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play(-1)

    def stop_music(self, music):
        pygame.mixer.music.load(music)
        pygame.mixer.music.stop()

    def continue_music(self, music):
        pygame.mixer.music.load(music)
        pygame.mixer.music.unpause()

    '''def play_sound1(self, sound):
        self.sound = pygame.mixer.Sound(sound)
        self.sound.set_volume(0.05)
        self.sound.play()'''