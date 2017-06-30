import pygame
from pygame.locals import *
pygame.mixer.init()
import time
win=pygame.display.set_mode((640,600))
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

pygame.init()

#pygame.mixer.init()
#s=pygame.mixer.sound(Jump4.wav)
#s.play()
pygame.mixer.music.load('01 Aaramaage Iddenaanu_2.mp3')

pygame.mixer.music.play(-1)
