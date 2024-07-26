# IMPORTS
# from _typeshed import Self
from types import NoneType
import pygame, sys
import os
import time
import random
from pygame import draw
from pygame import joystick
from pygame.locals import *
import cv2

#Global Variable
global Width
global Height
global DISPLAYSURF
global Start1
global White
global Black
global Red
global Yellow
global Winner_color
global Champ_color
global Champ
global FPS
global VEL
global bullets_Vel
global Max_bullets
global Spaceship_width
global Spaceship_height
global Yellow_hit
global Red_hit
global CPU_hit
global Round
global Red_player
global Yellow_player
global red_score_text
global yellow_score_text
global b 
global Border
global Health_font
global Winner_font
global Reset_font
global Space_background
global Space_background1
global Yellow_spaceship_Image
global Yellow_spaceship
global Red_spaceship_Image
global Red_spaceship
global Spaceship_guns_sound
global Spaceship_hits_sound
global Space_End_image 
global Space_End
global Explosion_sound
global Shaceship_eng_sound
global Loaded_up_sound
global back

#Pygame Setup
pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(frequency=44100, size=0, channels=1, buffer=512)
pygame.display.set_caption("Space Games")
Width = 900
Height = 500
DISPLAYSURF = pygame.display.set_mode((Width, Height))
Start1 = True

#Colors
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
wineer_color = None
Champ_color = None
Champ = ""

#Game Settings
FPS = 70
VEL = 8
bullets_Vel = Width // 100
Max_bullets = 5
Spaceship_width, Spaceship_height = Width / 16.3636364, Height / 12.5
Yellow_hit = pygame.USEREVENT + 1
Red_hit = pygame.USEREVENT + 2
CPU_hit = pygame.USEREVENT + 3
Round = 0
Red_player = int(0)
Yellow_player = int(0)
red_score_text = ""
yellow_score_text = ""
b = ""

#Border
Border = pygame.Rect((Width // 2, 0, 10, Height))

#Fonts
Health_font = pygame.font.SysFont("Roboto", 40)
Winner_font = pygame.font.SysFont("Roboto", 100)
Reset_font = pygame.font.SysFont("Roboto", 60)

#Imported images
Space_background = pygame.transform.scale(pygame.image.load(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/Play.png')),(Width,Height))
Space_background1 = pygame.transform.scale(pygame.image.load(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/space.png')),(Width,Height))
Yellow_spaceship_Image = pygame.image.load(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/spaceship_yellow.png'))
Yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(Yellow_spaceship_Image,(Spaceship_width,Spaceship_height)),270)
Red_spaceship_Image = pygame.image.load(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/spaceship_red.png'))
Red_spaceship = pygame.transform.rotate(pygame.transform.scale(Red_spaceship_Image,(Spaceship_width,Spaceship_height)),90)
Spaceship_guns_sound =pygame.mixer.Sound(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/Assets_Gun+Silencer.mp3'))
Spaceship_hits_sound =pygame.mixer.Sound(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/Assets_Grenade+1.mp3'))
Space_End_image = pygame.image.load(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/Explosion_ship.png'))
Space_End = pygame.transform.scale(Space_End_image,(Spaceship_width,Spaceship_height))
Explosion_sound =pygame.mixer.Sound(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/ES_Sci Fi Explosion 4 - SFX Producer.mp3'))
Shaceship_eng_sound =pygame.mixer.Sound(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/Rocket-sound-effect.mp3'))
Loaded_up_sound=pygame.mixer.Sound(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/mixkit-clock-countdown-bleeps-916.wav'))
Loaded_up_music=pygame.mixer.Sound(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/shuttlelaunch-24467.mp3'))
Space_image = pygame.image.load(os.path.abspath('Space_Enforcer_2.0/Asset Project 1/SPACE ENFORCER.png'))
#Space_video = moviepy.editor.VideoFileClip('Space_Enforcer_2.0/Asset Project 1/SPACE ENFORCER.mp4')
video = cv2.VideoCapture('Space_Enforcer_2.0/Asset Project 1/SPACE ENFORCER.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
clock = pygame.time.Clock()
clock.tick(fps)
success, video_image = video.read()
video_surf = pygame.image.frombuffer(video_image, video_image.shape[1::-1], "BGR")

back=[Space_background1,Space_background]
if Round>2:
    back_opt=back[1]
else:
    back_opt=back[Round-1]
