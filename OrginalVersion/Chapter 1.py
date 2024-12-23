#IMPORTS
#from _typeshed import Self
from types import NoneType
import pygame, sys
import os
import time
import random
from pygame import draw
from pygame import joystick
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(frequency=44100, size=0, channels=1, buffer=512)
Width = 900
Height = 500
DISPLAYSURF = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Space Games')
Start1=True
#Color
White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)
Yellow=(255,255,0)
wineer_color = None
Champ_color = None
Champ = ""

FPS =70
VEL=8
bullets_Vel=Width//100
Max_bullets=5
Spaceship_width, Spaceship_height = Width/16.3636364, Height/12.5
Yellow_hit = pygame.USEREVENT +1
Red_hit = pygame.USEREVENT +2
CPU_hit = pygame.USEREVENT +3
Round=0
Red_player=int(0)
Yellow_player=int(0)
red_score_text=""
yellow_score_text=""
b=''

#Border
Border = pygame.Rect((Width//2 , 0, 10, Height))

Health_font = pygame.font.SysFont('comicsans',40)
Winner_font = pygame.font.SysFont('comicsans',100)
Reset_font = pygame.font.SysFont('comicsans',60)

import pygame
pygame.init()


def main(): 
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Joystick Testing / XBOX360 Controller")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    joysticks = []
    clock = pygame.time.Clock()
    keepPlaying = True

    # for al the connected joysticks
    for i in range(0, pygame.joystick.get_count()):
        # create an Joystick object in our list
        joysticks.append(pygame.joystick.Joystick(i))
        # initialize them all (-1 means loop forever)
        joysticks[-1].init()
        # print a statement telling what the name of the controller is
        print ("Detected joystick '",joysticks[-1].get_name(),"'")
    while keepPlaying:
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print ("Received event 'Quit', exiting.")
                    keepPlaying = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    print ("Escape key pressed, exiting.")
                    keepPlaying = False
                elif event.type == pygame.KEYDOWN:
                    print ("Keydown,", event.key)
                elif event.type == pygame.KEYUP:
                    print ("Keyup,", event.key)
                ###elif event.type == pygame.MOUSEMOTION:
                    #print "Mous
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print ("Mouse button",event.button,"down at",pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    print ("Mouse button",event.button,"up at",pygame.mouse.get_pos())
                elif event.type == pygame.JOYAXISMOTION:
                    print ("Joystick '",joysticks[event.joy].get_name(),"' 12axis",event.axis,"motion.")
                    pygame.joystick.Joystick.get_axis()
                    if joystick:
                        axis_x, axis_y = (event.axis(0),event.axis(1))
                        if abs(axis_x) > 0.1:
                            print('here')
                        if abs(axis_y) > 0.1:
                            print('here')
                elif event.type == pygame.JOYBUTTONDOWN:
                    print ("Joystick '",joysticks[event.joy].get_name(),"' butto2n",event.button,"down.")
                    if event.button == 0:
                        background.fill((255, 0, 0))
                    elif event.button == 1:
                        background.fill((0, 0, 255))
                elif event.type == pygame.JOYBUTTONUP:
                    print ("Joystick ",joysticks[event.joy].get_name(),"' b3utton")
                    
#Draw
def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health,red_score_text,yellow_score_text,Yellow_player,Red_player,Round):
    DISPLAYSURF.blit(back_opt,(0,0))
    pygame.draw.rect(DISPLAYSURF,Black,Border)
    red_health_text = Health_font.render("Health: " + str(red_health),1,Red)
    yellow_health_text = Health_font.render("Health: " + str(yellow_health),1,Yellow)
    red_score_text = Health_font.render(str(Red_player),1,Red)
    yellow_score_text = Health_font.render("-Score-" + str(Yellow_player),1,Yellow)
    DISPLAYSURF.blit(yellow_health_text,(Width - yellow_health_text.get_width() - 10,10))
    DISPLAYSURF.blit(red_health_text,(10,10))
    DISPLAYSURF.blit(Yellow_spaceship,(yellow.x, yellow.y))
    DISPLAYSURF.blit(Red_spaceship,(red.x, red.y))
    DISPLAYSURF.blit(red_score_text,(330,0))
    DISPLAYSURF.blit(yellow_score_text,(370,0))
    pygame.display.update()
    for bullet in red_bullets:
        pygame.draw.rect(DISPLAYSURF,Red,bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(DISPLAYSURF,Yellow,bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VEL> Border.x + Border.width: #Left
        yellow.x -= VEL
        #Shaceship_eng_sound.play()
        #Shaceship_eng_sound.stop()
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < Width: #Right
        yellow.x += VEL
        #Shaceship_eng_sound.play()
        #Shaceship_eng_sound.stop()
    if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0: #Up
        yellow.y -= VEL
        #Shaceship_eng_sound.play()
        #Shaceship_eng_sound.stop()

    if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height < Height-10: #Down
        yellow.y += VEL
        Shaceship_eng_sound.play()
        Shaceship_eng_sound.stop()
        

def red_handle_movement(keys_pressed, red):
    if (keys_pressed[pygame.K_a]) and red.x -VEL > 0: #Left
        red.x -= VEL
    if keys_pressed[pygame.K_d] and red.x + VEL + red.width < Border.x: #Right
        red.x += VEL
    if keys_pressed[pygame.K_w] and red.y - VEL > 0: #Up
        red.y -= VEL
    if keys_pressed[pygame.K_s] and red.y + VEL + red.height < Height-10: #Down
        red.y += VEL
def CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow):
    up_down=['','3',]
    side=['1','2']
    ally_lis=[1,0]
    Ally=random.choice(ally_lis)
    #if Ally==1:
    cpu_decision=random.choice(up_down)
    #if Ally==0:
    cpu_direction=random.choice(side)
    #for d in c:
    d=1
    #if handle_bullets(yellow_bullets,red_bullets,yellow,red,cpu_paddle):
        #c=0
    

    if d==1:
        for a in b:
            if c==1:
                b.remove(a)
                c=0
                continue
            if red.y - VEL > 0:
                if a=='1':#Left
                    if yellow.y==red.y:
                        red.x -= VEL*0
                        if len(red_bullets)< 1:
                            bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                            if bullet_r.x== (red.x + 2):
                                red_bullets.append(bullet_r)
                                Spaceship_guns_sound.play()
                    if yellow.y!=red.y:
                        red.x -= VEL
                    pygame.display.update()
                    if red.x < 15:
                        red.y += VEL
                        b.append(cpu_decision)
                        b.remove(a)
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x== (red.x + 2):
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                            CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
                        

                if a=='2':#Right
                    if yellow.y==red.y:
                        red.x += VEL*0
                        if len(red_bullets)< 1:
                            bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                            if bullet_r.x== (red.x + 2):
                                red_bullets.append(bullet_r)
                                Spaceship_guns_sound.play()
                    if yellow.y!=red.y:
                        red.x += VEL
                    pygame.display.update()
                    if red.x > Border.x-100:
                        red.y -= VEL*0
                        b.append(cpu_decision)
                        b.remove(a)
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x== (red.x + 2):
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                            CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
                    
            if a=='3'and red.y - VEL > 0:#Up
                if yellow.y==red.y:
                    red.y -= VEL*0
                    if len(red_bullets)< 1:
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x== (red.x + 2):
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                if yellow.y!=red.y:
                    red.y += VEL
                pygame.display.update()
                if red.y < 15:
                    b.append(cpu_direction)
                    b.remove(a)
                    bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                    red_bullets.append(bullet_r)
                    Spaceship_guns_sound.play()
                    if bullet_r.x== (red.x + 2):
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)

            if a==''and red.y + VEL + red.height < Height-10 :
                if yellow.y==red.y:
                    red.y += VEL*0
                    if len(red_bullets)< 1:
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x== (red.x + 2):
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                if yellow.y!=red.y:
                    red.y += VEL
                if red.y>445:
                    print('Line 273')
                    red.y -= VEL
                    b.append('3')
                    b.remove(a)
                    pygame.display.update()
                    CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
            if red.y + VEL + red.height < Height-10: #Down
                if a=='1':#Left
                    if yellow.y==red.y:
                        red.x -= VEL*0
                        if len(red_bullets)< 1:
                            bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                            if bullet_r.x== (red.x + 2):
                                red_bullets.append(bullet_r)
                                Spaceship_guns_sound.play()
                    if yellow.y!=red.y:
                        red.x -= VEL
                        #red.y -= VEL
                    pygame.display.update()
                    if red.x < 15:
                        b.clear()
                        b.append(cpu_decision)
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x== (red.x + 2):
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                            CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)


                if a=='2':#Right
                    if yellow.y==red.y:
                        red.x += VEL*0
                        if len(red_bullets)< 1 or bullet_r.x== (red.x + 2):
                            bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                            if bullet_r.x== (red.x + 2):
                                red_bullets.append(bullet_r)
                                Spaceship_guns_sound.play()
                    if yellow.y!=red.y:
                        red.x += VEL
                    pygame.display.update()
                    if red.x > Border.x-100:
                        b.clear()
                        b.append(cpu_decision)
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x== (red.x + 2):
                            print('338 speed')
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                            CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)

def CPU_yellow_handle_movement(red,e,f,cpu_paddle2,yellow_bullets,red_bullets,yellow):
    yup_down=['3','',]
    yside=['2','1']
    cpuy_decision=random.choice(yup_down)
    cpuy_direction=random.choice(yside)
    d=1
    if d==1:
        for g in e:
            if f==1:
                e.remove(g)
                f=0
                continue
            if yellow.y - VEL > 0:
                if g=='1':#Left
                    print(e,'h1')
                    if yellow.y==red.y:
                        yellow.x -= VEL*0
                        if len(yellow_bullets)< 1:
                            bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                            yellow_bullets.append(bullet_y)
                            Spaceship_guns_sound.play()
                            if bullet_y.x== (yellow.x - 2):
                                yellow_bullets.append(bullet_y)
                                Spaceship_guns_sound.play()
                    if yellow.y!=red.y:
                        yellow.x -= VEL
                        yellow.y-= VEL
                    pygame.display.update()
                    if yellow.x > 875:
                        e.append(cpuy_decision)
                        e.remove(g)
                        bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                        yellow_bullets.append(bullet_y)
                        Spaceship_guns_sound.play()
                        if bullet_y.x== (yellow.x + 2):
                            yellow_bullets.append(bullet_y)
                            Spaceship_guns_sound.play()
                            CPU_yellow_handle_movement(red,e,f,cpu_paddle2,yellow_bullets,red_bullets,yellow) 
                if g=='2':#Right
                    print(e,'h2')
                    if yellow.y==red.y:
                        yellow.x += VEL*0
                        if len(yellow_bullets)< 1:
                            bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                            yellow_bullets.append(bullet_y)
                            Spaceship_guns_sound.play()
                            if bullet_y.x== (yellow.x + 2):
                                yellow_bullets.append(bullet_y)
                                Spaceship_guns_sound.play()
                    if yellow.y!=red.y:
                        yellow.x += VEL
                        yellow.y += VEL
                    pygame.display.update()
                    if yellow.x < Border.x-100:
                        e.append(cpuy_decision)
                        e.remove(g)
                        bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                        yellow_bullets.append(bullet_y)
                        Spaceship_guns_sound.play()
                        if bullet_y.x== (yellow.x + 2):
                            yellow_bullets.append(bullet_y)
                            Spaceship_guns_sound.play()
                            CPU_yellow_handle_movement(red,e,f,cpu_paddle2,yellow_bullets,red_bullets,yellow)
                    
            if g=='3'and yellow.y - VEL > 0:
                print(e,'h3') #Up
                if yellow.y==red.y:
                    yellow.y -= VEL*0
                    if len(yellow_bullets)< 1:
                        bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                        yellow_bullets.append(bullet_y)
                        Spaceship_guns_sound.play()
                        if bullet_y.x== (yellow.x + 2):
                            yellow_bullets.append(bullet_y)
                            Spaceship_guns_sound.play()
                if yellow.y!=red.y:
                    yellow.y -= VEL
                pygame.display.update()
                if red.y < 15:
                    e.append(cpuy_direction)
                    e.remove(g)
                    bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                    yellow_bullets.append(bullet_y)
                    Spaceship_guns_sound.play()
                    if bullet_y.x== (yellow.x + 2):
                        yellow_bullets.append(bullet_y)
                        Spaceship_guns_sound.play()
                        CPU_yellow_handle_movement(red,e,f,cpu_paddle2,yellow_bullets,red_bullets,yellow)

            if g==''and yellow.y + VEL + yellow.height < Height-10 :
                print(e,'h4')
                if yellow.y==red.y:
                    yellow.y += VEL*0
                    if len(yellow_bullets)< 1:
                        bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                        yellow_bullets.append(bullet_y)
                        Spaceship_guns_sound.play()
                        if bullet_y.x== (yellow.x + 2):
                            yellow_bullets.append(bullet_y)
                            Spaceship_guns_sound.play()
                if yellow.y!=red.y:
                    yellow.y += VEL
                if yellow.y>445:
                    e.append('3')
                    e.remove(g)
                    pygame.display.update()
                    CPU_red_handle_movement(red,e,f,cpu_paddle2,yellow_bullets,red_bullets,yellow)
            if red.y + VEL + red.height < Height-10: #Down
                if g=='1':#Left
                    print(e,'h5')
                    if yellow.y==red.y:
                        yellow.x -= VEL*0
                        if len(yellow_bullets)< 1:
                            bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                            red_bullets.append(bullet_y)
                            Spaceship_guns_sound.play()
                            if bullet_y.x== (yellow.x + 2):
                                yellow_bullets.append(bullet_y)
                                Spaceship_guns_sound.play()
                    if yellow.y!=red.y:
                        yellow.x -= VEL
                        yellow.y -= VEL
                    pygame.display.update()
                    if red.x > 855:
                        e.clear()
                        e.append(cpuy_decision)
                        bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                        yellow_bullets.append(bullet_y)
                        Spaceship_guns_sound.play()
                        if bullet_y.x== (yellow.x + 2):
                            yellow_bullets.append(bullet_y)
                            Spaceship_guns_sound.play()
                            CPU_red_handle_movement(red,e,f,cpu_paddle2,yellow_bullets,red_bullets,yellow)


                if g=='2':#Right
                    print(e,'h6')
                    if yellow.y==red.y:
                        red.x += VEL*0
                        if len(yellow_bullets)< 1: #or bullet_y.x== (yellow.x + 2):
                            bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                            yellow_bullets.append(bullet_y)
                            Spaceship_guns_sound.play()
                            if bullet_y.x== (red.x + 2):
                                yellow_bullets.append(bullet_y)
                                Spaceship_guns_sound.play()
                    if yellow.y!=red.y:
                        yellow.x += VEL
                        yellow.y -= VEL
                    pygame.display.update()
                    if red.x > Border.x:
                        e.clear()
                        e.append(cpuy_decision)
                        bullet_y = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height//2) -2,10,5)
                        yellow_bullets.append(bullet_y)
                        Spaceship_guns_sound.play()
                        if bullet_y.x== (yellow.x + 2):
                            print('338 speed')
                            yellow_bullets.append(bullet_y)
                            Spaceship_guns_sound.play()
                            CPU_red_handle_movement(red,e,f,cpu_paddle2,yellow_bullets,red_bullets,yellow)
def handle_bullets(yellow_bullets,red_bullets,yellow,red,cpu_paddle,Levels,a,b):
    for bullet in yellow_bullets:
        bullet.x -= bullets_Vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)

        if cpu_paddle.colliderect(bullet):
            lim=random.choice(range(10,450,Levels//5))
            Clip=[1,2,3,4,5]
            if Round > 5:
                Dodge_speed=VEL
            else:
                Dodge_speed = (float(VEL)*4) #- float(Round) *.75

            if red.y <lim: #and red.y + VEL + red.height > Height-50: #Down
                red.y=red.y+Dodge_speed
                for ws in b:
                    k=1
                    b.remove(ws)
                    b.append('')
                    print('271here')
                    c=1
                    #CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
                    lim=lim+Width//2
                if len(red_bullets)< Max_bullets-4:
                        bullet.x= Round+bullets_Vel
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x== (red.x + 2):
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
            if red.y >= lim: # and red.y - VEL < 0:#UP 
                red.y =red.y - Dodge_speed
                lim=lim-10
                for ws in b:
                    k=1
                    b.remove(ws)
                    b.append('3')
                    print('289here')
                    c=1
                    #CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
                    lim=lim+Width//2
                if len(red_bullets)< Max_bullets-4:
                        bullet.x= Round+bullets_Vel
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x == (red.x + 20):
                            print('338 speed')
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()

    for bullet in red_bullets:
        bullet.x += bullets_Vel     
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x > Width:
            red_bullets.remove(bullet)


def handle_Comp(yellow_bullets,Dogde,Comp_Move):
        for bullet in yellow_bullets:
            bullet.x += bullets_Vel     
            if Border.colliderect(bullet):
                random.choice(Dogde)
                pygame.display.update()
            else:
                random.choice(Comp_Move)
                pygame.display.update()

def Comp_R(red):
    red.x += VEL
def Comp_L(red):
    red.x -= VEL
def Comp_Up(red):
    red.y -= VEL
def Comp_Dn(red):
    red.y += VEL
def Computer_player(red,keys_pressed,yellow_bullets,red_bullets,yellow):
    Comp_Dn(red)
    Comp_Up(red)
    Comp_L(red)
    Comp_R(red)
    Dogde=[]
    Dogde.append(Comp_Dn)
    Dogde.append(Comp_Up)
    Comp_Move=[]
    Comp_Move.append(Comp_Up(red))
    Comp_Move.append(Comp_Dn(red))
    Comp_Move.append(Comp_R(red))
    Comp_Move.append(Comp_L(red))    
    handle_Comp(yellow_bullets,Dogde,Comp_Move)
    pygame.display.update() 
class paddle():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.rect= pygame.Rect(x, y, Spaceship_width +10, Spaceship_height +10)
		self.speed = 5
		self.ai_speed = 5

	def move(self):
		key = pygame.key.get_pressed()
		if self==1 and self.rect.top > Height-10:
			self.rect.move_ip(0, -1 * self.speed)
		if self==2 and self.rect.bottom < 0:
			self.rect.move_ip(0, self.speed)

	def draw(cpu_paddle):
		pygame.draw.rect(DISPLAYSURF, Red, cpu_paddle)
 
def draw_winner(text,wineer_color,Round):
    draw_text = Winner_font.render(text, 1, wineer_color)
    DISPLAYSURF.blit(draw_text, (Width//2 - draw_text.get_width()/2,Height//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)
    Explosion_sound.stop()
    pygame.display.update()
def draw_kill(kill_pos):
    DISPLAYSURF.blit(Space_End,((kill_pos).x, (kill_pos).y))
    pygame.display.update()
    Explosion_sound.play()
    Explosion_sound.set_volume(2)
    

def draw_reset(Round,Start1):
    while Start1:
        CVP =True
        text1 =Health_font.render("Plaver vs Player *Press p",1,White)
        text2=Health_font.render(    "Player vs CPU *Press c",1,White)
        text3=Health_font.render(    "CPU vs CPU *Press v",1,White)
        DISPLAYSURF.blit(text1,(250,150))
        DISPLAYSURF.blit(text2,(250,250))
        DISPLAYSURF.blit(text3,(250,325))
        pygame.display.update()
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_c]:
                print("CVP") #Left
                CVP=True
                game_version = Winner_font.render("Player vs CPU",1,White)
                DISPLAYSURF.fill(Black)
                pygame.display.update()
                while CVP:
                    DISPLAYSURF.fill(Black)
                    pygame.display.update()
                    DISPLAYSURF.blit(game_version,(20,Height//2))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    DISPLAYSURF.fill(Black)
                    pygame.display.update()
                    Round+=1
                    Levels=Round*50
                    print(Round)
                    pygame.display.update()
                    rounds = Winner_font.render("Round " + str(Round),1,White)
                    DISPLAYSURF.blit(rounds,(Width//3,Height//2))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    main_CVP(Round,Champ,red_score_text,yellow_score_text,Levels,Red_player,Yellow_player)
                    pygame.display.update()
                    DISPLAYSURF.fill(Black)
                    score = Winner_font.render(str(Red_player)+" Score " + str(Yellow_player),1,White)
                    DISPLAYSURF.blit(score,(200,300))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    print(Red_player)
                    print(Yellow_player)
                

            if keys_pressed[pygame.K_p]:
                print("PVP") #Right
                PVP=True
                game_version=Health_font.render("Plaver vs Player",1,White)
                pygame.display.update()
                DISPLAYSURF.fill(Black)
                pygame.display.update()
                while PVP:
                    DISPLAYSURF.fill(Black)
                    pygame.display.update()
                    DISPLAYSURF.blit(game_version,(20,Height//2))
                    pygame.time.delay(3000)
                    DISPLAYSURF.fill(Black)
                    pygame.display.update()
                    Round+=1
                    Levels=Round*50
                    print(Round)
                    pygame.display.update()
                    rounds = Winner_font.render("Round " + str(Round),1,White)
                    DISPLAYSURF.blit(rounds,(Width//3,Height//2))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    Main_PvP(Round,Champ,red_score_text,yellow_score_text,Levels,Red_player,Yellow_player,main)
                    pygame.display.update()
                    DISPLAYSURF.fill(Black)
                    score = Winner_font.render(str(Red_player)+" Score " + str(Yellow_player),1,White)
                    DISPLAYSURF.blit(score,(200,300))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    print(Red_player)
                    print(Yellow_player)

            if keys_pressed[pygame.K_v]:
                print("CVC") #Right
                CVC=True
                game_version=Health_font.render("Computer vs Computer",1,White)
                pygame.display.update()
                DISPLAYSURF.fill(Black)
                pygame.display.update()
                while CVC:
                    DISPLAYSURF.fill(Black)
                    pygame.display.update()
                    DISPLAYSURF.blit(game_version,(20,Height//2))
                    pygame.time.delay(3000)
                    DISPLAYSURF.fill(Black)
                    pygame.display.update()
                    Round+=1
                    Levels=Round*50
                    print(Round)
                    pygame.display.update()
                    rounds = Winner_font.render("Round " + str(Round),1,White)
                    DISPLAYSURF.blit(rounds,(Width//3,Height//2))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    main_CVC(Round,Champ,red_score_text,yellow_score_text,Levels,Red_player,Yellow_player)
                    pygame.display.update()
                    DISPLAYSURF.fill(Black)
                    score = Winner_font.render(str(Red_player)+" Score " + str(Yellow_player),1,White)
                    DISPLAYSURF.blit(score,(200,300))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    print(Red_player)
                    print(Yellow_player)
            
    
def draw_Champion(Champ):
    Champ_win(Champ_color)
    draw_text = Winner_font.render(Champ, 1, White)
    DISPLAYSURF.blit(draw_text, (Width//2 - draw_text.get_width()/2,Height//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)
    Explosion_sound.stop()
    pygame.display.update()

def Champ_win(Champ_color,Red_player,Yellow_player):
    if Red_player>2:
        Champ_color =Red
        Champ = "RED IS THE CHAMPION"   
    if Yellow_player>2:
        Champ ='YELLOW IS THE CHAMPION'
        Champ_color=Yellow

    

    
#Imported image
Space_background = pygame.transform.scale(pygame.image.load(os.path.abspath('Asset_Project_1/Play.png')),(Width,Height))
Space_background1 = pygame.transform.scale(pygame.image.load(os.path.abspath('Asset_Project_1/space.png')),(Width,Height))
Yellow_spaceship_Image = pygame.image.load(os.path.abspath('Asset_Project_1/spaceship_yellow.png'))
Yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(Yellow_spaceship_Image,(Spaceship_width,Spaceship_height)),270)
Red_spaceship_Image = pygame.image.load(os.path.abspath('Asset_Project_1/spaceship_red.png'))
Red_spaceship = pygame.transform.rotate(pygame.transform.scale(Red_spaceship_Image,(Spaceship_width,Spaceship_height)),90)
Spaceship_guns_sound =pygame.mixer.Sound(os.path.abspath('Asset_Project_1/Assets_Gun+Silencer.mp3'))
Spaceship_hits_sound =pygame.mixer.Sound(os.path.abspath('Asset_Project_1/Assets_Grenade+1.mp3'))
Space_End_image = pygame.image.load(os.path.abspath('Asset_Project_1/Explosion_ship.png'))
Space_End = pygame.transform.scale(Space_End_image,(Spaceship_width,Spaceship_height))
Explosion_sound =pygame.mixer.Sound(os.path.abspath('Asset_Project_1/ES_Sci Fi Explosion 4 - SFX Producer.mp3'))
Shaceship_eng_sound =pygame.mixer.Sound(os.path.abspath('Asset_Project_1/Rocket-sound-effect.mp3'))
Loaded_up_sound=pygame.mixer.Sound(os.path.abspath('Asset_Project_1/mixkit-clock-countdown-bleeps-916.wav'))
back=[Space_background1,Space_background]
if Round>2:
    back_opt=back[1]
else:
    back_opt=back[Round-1]

#Main game loop P1vsp2
def main_PVP(Round,Champ,red_score_text,yellow_score_text):
    pygame.display.update()
    red = pygame.Rect(100,100,Spaceship_width,Spaceship_height)
    yellow = pygame.Rect(700,100,Spaceship_width,Spaceship_height)
    yellow_bullets =[]
    red_bullets =[]
    cpu_paddle = pygame.Rect(red.x +20,red.y,50,50)
    red_health = 10
    yellow_health =10
    clock = pygame.time.Clock()
    run = True
    S = run
    while run :
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health,red_score_text,yellow_score_text,Yellow_player,Red_player,Round)
        clock.tick(FPS)
        for event in pygame.event.get():
            pygame.display.update()  
            pygame.display.update()   
            if event.type ==pygame.QUIT:
                run = False
                Start = False
                Start1 =False
                pygame.quit
                sys.exit()
            pygame.display.update()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(red_bullets)< Max_bullets:
                    bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                    red_bullets.append(bullet_r)
                    Spaceship_guns_sound.play()

                if event.key==pygame.K_RCTRL and len(yellow_bullets)< Max_bullets:
                    bullet_y = pygame.Rect(yellow.x, yellow.y + (yellow.height//2) -2,10,5)
                    yellow_bullets.append(bullet_y)
                    Spaceship_guns_sound.play()

            if event.type ==  CPU_hit:
                Spaceship_guns_sound.play()
            if event.type == Red_hit:
                red_health -= 1
                Spaceship_hits_sound.play()

            if event.type == Yellow_hit:
                yellow_health -=1
                Spaceship_hits_sound.play()

        winner_text = ""
        wineer_color = None
        Champ_color = None
        #if Round <4 :

        if red_health <= -1:
            wineer_color = Yellow
            winner_text = "YELLOW WINS!"
            kill_pos = red

        if yellow_health <= -1:
            wineer_color = Red
            winner_text = "RED WINS!"
            kill_pos = yellow

        if winner_text !="":
            draw_kill(kill_pos)
            draw_winner(winner_text,wineer_color,Round)
            break
        #if Round >3:
            #Champ_win(Champ_color)
            #draw_Champion(Champ)
            #break
        


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow,cpu_paddle)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        #Computer_player(red,keys_pressed,yellow_bullets,red_bullets,yellow)
        pygame.display.update()
#Main game loop CPUvsP1
def Main_PvP(Round,Champ,red_score_text,yellow_score_text,Levels,Red_player,Yellow_player,main):
    pygame.display.update()
    red = pygame.Rect(100,100,Spaceship_width,Spaceship_height)
    yellow = pygame.Rect(700,100,Spaceship_width,Spaceship_height)
    yellow_bullets =[]
    red_bullets =[]
    red_health = 10
    yellow_health =10
    clock = pygame.time.Clock()
    run = True
    dog =False
    S = run
    b=['']
    c=['']
    joysticks = []
    a=None
    c=None
    joy=6
    while run :
        #main()
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health,red_score_text,yellow_score_text,Yellow_player,Red_player,Round)
        clock.tick(FPS)
        cpu_paddle = pygame.Rect(0,0,2,2)
        #paddle.draw(cpu_paddle)
        pygame.display.update()
        for i in range(0, pygame.joystick.get_count()):
        # create an Joystick object in our list
            joysticks.append(pygame.joystick.Joystick(i))
        # initialize them all (-1 means loop forever)
            joysticks[-1].init()
        for event in pygame.event.get():
            pygame.display.update()     
            if event.type ==pygame.QUIT:
                run = False
                Start = False
                Start1 =False
                pygame.quit
                sys.exit()
            pygame.display.update()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(red_bullets)< Max_bullets:
                    bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,Width//90,Height//100)
                    red_bullets.append(bullet_r)
                    Spaceship_guns_sound.play()

                if event.key==pygame.K_RCTRL and len(yellow_bullets)< Max_bullets:
                    bullet_y = pygame.Rect(yellow.x, yellow.y + (yellow.height//2) -2,Width//90,Height//100)
                    yellow_bullets.append(bullet_y)
                    Spaceship_guns_sound.play()
            if event.type == pygame.JOYAXISMOTION and len(yellow_bullets)< Max_bullets:
                joy=joy+1
                if joy==7:
                    bullet_y = pygame.Rect(yellow.x, yellow.y + (yellow.height//2) -2,Width//90,Height//100)
                    yellow_bullets.append(bullet_y)
                    Spaceship_guns_sound.play()
                    joy=0

            if event.type ==  CPU_hit:
                Spaceship_guns_sound.play()
            if event.type == Red_hit:
                red_health -= 1
                Spaceship_hits_sound.play()

            if event.type == Yellow_hit:
                yellow_health -=1
                Spaceship_hits_sound.play()

        winner_text = ""
        wineer_color = None
        Champ_color = None
        #if Round <4 :

        if red_health <= -1:
            Yellow_player+=1
            print(Yellow_player)
            wineer_color = Yellow
            winner_text = "YELLOW WINS!"
            kill_pos = red

        if yellow_health <= -1:
            Red_player+=1
            wineer_color = Red
            winner_text = "RED WINS!"
            kill_pos = yellow
            Round-=1
            

        if winner_text !="":
            draw_kill(kill_pos)
            draw_winner(winner_text,wineer_color,Round)
            if winner_text == "YELLOW WINS!":
                Red_player=Red_player+1
                pygame.display.update()
            if winner_text == "YELLOW WINS!":
                Yellow_player=Yellow_player+1
                pygame.display.update()
            break
        #if Round >3:
            #Champ_win(Champ_color,Red_player,Yellow_player)
            #draw_Champion(Champ)
            #break
        

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        #Red_AI(sense,red)
        #if Round>-1:
        #    CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red,cpu_paddle,Levels,c,b)
        #Computer_player(red,keys_pressed,yellow_bullets,red_bullets,yellow)
        pygame.display.update()
def main_CVP(Round,Champ,red_score_text,yellow_score_text,Levels,Red_player,Yellow_player):
    pygame.display.update()
    red = pygame.Rect(100,100,Spaceship_width,Spaceship_height)
    yellow = pygame.Rect(700,100,Spaceship_width,Spaceship_height)
    yellow_bullets =[]
    red_bullets =[]
    red_health = 10
    yellow_health =10
    clock = pygame.time.Clock()
    run = True
    dog =False
    S = run
    b=['']
    c=['']
    a=None
    c=None
    while run :
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health,red_score_text,yellow_score_text,Yellow_player,Red_player,Round)
        clock.tick(FPS)
        cpu_paddle = pygame.Rect(red.x+10,red.y - (red.height//2),Levels+2,100)
        #paddle.draw(cpu_paddle)
        pygame.display.update()
        for event in pygame.event.get():
            pygame.display.update()     
            if event.type ==pygame.QUIT:
                run = False
                Start = False
                Start1 =False
                pygame.quit
                sys.exit()
            pygame.display.update()
            if event.type== pygame.KEYDOWN:

                if event.key==pygame.K_LCTRL and len(yellow_bullets)< Max_bullets:
                    bullet_y = pygame.Rect(yellow.x, yellow.y + (yellow.height//2) -2,10,5)
                    yellow_bullets.append(bullet_y)
                    Spaceship_guns_sound.play()

            if event.type ==  CPU_hit:
                Spaceship_guns_sound.play()
            if event.type == Red_hit:
                red_health -= 1
                Spaceship_hits_sound.play()

            if event.type == Yellow_hit:
                yellow_health -=1
                Spaceship_hits_sound.play()

        winner_text = ""
        wineer_color = None
        Champ_color = None
        #if Round <4 :

        if red_health <= -1:
            Yellow_player+=1
            print(Yellow_player)
            wineer_color = Yellow
            winner_text = "YELLOW WINS!"
            kill_pos = red

        if yellow_health <= -1:
            Red_player+=1
            wineer_color = Red
            winner_text = "RED WINS!"
            kill_pos = yellow
            Round-=1
            

        if winner_text !="":
            draw_kill(kill_pos)
            draw_winner(winner_text,wineer_color,Round)
            if winner_text == "YELLOW WINS!":
                Red_player=Red_player+1
                pygame.display.update()
            if winner_text == "YELLOW WINS!":
                Yellow_player=Yellow_player+1
                pygame.display.update()
            break
        #if Round >3:
            #Champ_win(Champ_color,Red_player,Yellow_player)
            #draw_Champion(Champ)
            #break
        

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        #Red_AI(sense,red)
        if Round>-1:
            CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
        #red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red,cpu_paddle,Levels,c,b)
        #Computer_player(red,keys_pressed,yellow_bullets,red_bullets,yellow)
        pygame.display.update()
def main_CVC(Round,Champ,red_score_text,yellow_score_text,Levels,Red_player,Yellow_player):
    pygame.display.update()
    red = pygame.Rect(100,100,Spaceship_width,Spaceship_height)
    yellow = pygame.Rect(700,100,Spaceship_width,Spaceship_height)
    yellow_bullets =[]
    red_bullets =[]
    red_health = 10
    yellow_health =10
    clock = pygame.time.Clock()
    run = True
    dog =False
    S = run
    b=['']
    c=['']
    e=['']
    f=['']
    a=None
    c=None
    while run :
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health,red_score_text,yellow_score_text,Yellow_player,Red_player,Round)
        clock.tick(FPS)
        cpu_paddle = pygame.Rect(red.x+10,red.y - (red.height//2),Levels+2,100)
        cpu_paddle2 = pygame.Rect(yellow.x+10,yellow.y - (yellow.height//2),Levels+2,100)
        #paddle.draw(cpu_paddle)
        pygame.display.update()
        for event in pygame.event.get():
            pygame.display.update()     
            if event.type ==pygame.QUIT:
                run = False
                Start = False
                Start1 =False
                pygame.quit
                sys.exit()
            pygame.display.update()
            if event.type== pygame.KEYDOWN:

                if event.key==pygame.K_LCTRL and len(yellow_bullets)< Max_bullets:
                    bullet_y = pygame.Rect(yellow.x, yellow.y + (yellow.height//2) -2,10,5)
                    yellow_bullets.append(bullet_y)
                    Spaceship_guns_sound.play()

            if event.type ==  CPU_hit:
                Spaceship_guns_sound.play()
            if event.type == Red_hit:
                red_health -= 1
                Spaceship_hits_sound.play()

            if event.type == Yellow_hit:
                yellow_health -=1
                Spaceship_hits_sound.play()

        winner_text = ""
        wineer_color = None
        Champ_color = None
        #if Round <4 :

        if red_health <= -1:
            Yellow_player+=1
            print(Yellow_player)
            wineer_color = Yellow
            winner_text = "YELLOW WINS!"
            kill_pos = red

        if yellow_health <= -1:
            Red_player+=1
            wineer_color = Red
            winner_text = "RED WINS!"
            kill_pos = yellow
            Round-=1
            

        if winner_text !="":
            draw_kill(kill_pos)
            draw_winner(winner_text,wineer_color,Round)
            if winner_text == "YELLOW WINS!":
                Red_player=Red_player+1
                pygame.display.update()
            if winner_text == "YELLOW WINS!":
                Yellow_player=Yellow_player+1
                pygame.display.update()
            break
        #if Round >3:
            #Champ_win(Champ_color,Red_player,Yellow_player)
            #draw_Champion(Champ)
            #break
        

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        #Red_AI(sense,red)
        if Round>-1:
            CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
            CPU_yellow_handle_movement(red,e,f,cpu_paddle2,yellow_bullets,red_bullets,yellow)
        #red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red,cpu_paddle,Levels,c,b)
        #Computer_player(red,keys_pressed,yellow_bullets,red_bullets,yellow)
        pygame.display.update()

loading=[5,4,3,2,1]
DISPLAYSURF.fill(Black)
pygame.display.update()
Loaded_up_sound.play
Loaded_up_sound.set_volume(2)
for countdown in loading:
    count_d=Winner_font.render(str(countdown),1,White)
    DISPLAYSURF.blit(count_d,(450,150))
    pygame.display.update()
    pygame.time.delay(1000)
    DISPLAYSURF.fill(Black)
    pygame.display.update()
pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.abspath('Asset_Project_1/new.mp3')),loops=-1)
draw_reset(Round,Start1)
pygame.display.update()
