from Settings import *

#Player Handle Movements
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VEL> Border.x + Border.width: #Left
        yellow.x -= VEL
        #Shaceship_eng_sound.play()
        #Shaceship_eng_sound.stop()
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < DISPLAYSURF.get_width(): #Right
        yellow.x += VEL
        #Shaceship_eng_sound.play()
        #Shaceship_eng_sound.stop()
    if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0: #Up
        yellow.y -= VEL
        #Shaceship_eng_sound.play()
        #Shaceship_eng_sound.stop()

    if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height < DISPLAYSURF.get_height()-10: #Down
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
    if keys_pressed[pygame.K_s] and red.y + VEL + red.height < DISPLAYSURF.get_height()-10: #Down
        red.y += VEL

#CPU Handle Movements
def CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow):
    up_down=['','3',]
    side=['1','2']
    ally_lis=[1,0]
    Ally=random.choice(ally_lis)
    print("Ally: ",Ally)
    if Ally==1:
        cpu_decision=random.choice(up_down)
        print("cpu_decision: ",cpu_decision)
        if cpu_decision=='3'and red.y - VEL > 0:#Up
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
        if cpu_decision==' 'and red.y + VEL + red.height < DISPLAYSURF.get_height()-10: #Down
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
    if Ally==0:
        cpu_direction=random.choice(side)
        print("cpu_direction: ",cpu_direction)
        if cpu_direction=='1':#Left
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
        if cpu_direction=='2':#Right
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
                        b.append(cpu_direction)
                        b.remove(a)
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x== (red.x + 2):
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
                            CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)     
    #for d in c:
    d=1
    #if handle_bullets(yellow_bullets,red_bullets,yellow,red,cpu_paddle):
        #c=0
    if d==1:
        for a in b:
            print("a:",a)
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
            if a=='3'and red.y + VEL + red.height < DISPLAYSURF.get_height()-10 :
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
            if red.y + VEL + red.height < DISPLAYSURF.get_height()-10: #Down
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

            if g==''and yellow.y + VEL + yellow.height < DISPLAYSURF.get_height()-10 :
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
            if red.y + VEL + red.height < DISPLAYSURF.get_height()-10: #Down
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
def handle_Comp(yellow_bullets,Dogde,Comp_Move, bullets_Vel, Border):
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

#Ammo Movements
def handle_bullets(yellow_bullets,red_bullets,yellow,red,cpu_paddle,Levels,a,b):
    for bullet in yellow_bullets:
        bullet.x -= bullets_Vel+20
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)
        if cpu_paddle.colliderect(bullet):
            lim=random.choice(range(10,450,Levels//5))
            ally_lis=[1,2]
            Dodge_Direction=random.choice(ally_lis)
            Clip=[1,2,3,4,5]
            if Round > 5:
                Dodge_speed=VEL
            else:
                Dodge_speed = (float(VEL)*4) #- float(Round) *.75
            
            if Dodge_Direction == 2 and (red.y <lim or red.y + VEL + red.height < DISPLAYSURF.get_height()-100): #Down
                red.y=red.y+Dodge_speed
                for ws in b:
                    k=1
                    b.remove(ws)
                    b.append('')
                    print('Down_Red: ',red)
                    print('Down_B: ',b)
                    c=1
                    #CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
                    lim=lim+DISPLAYSURF.get_width()//2
                if len(red_bullets)< Max_bullets-4:
                        bullet.x= Round+bullets_Vel
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x== (red.x + 2):
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()
            if Dodge_Direction == 1 and (red.y >lim or red.y - VEL < 100): #UP
                red.y=red.y-Dodge_speed
                for ws in b:
                    k=1
                    b.remove(ws)
                    b.append('')
                    print('Down_Red: ',red)
                    print('Down_B: ',b)
                    c=1
                    #CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
                    lim=lim+DISPLAYSURF.get_width()//2
                if len(red_bullets)< Max_bullets-4:
                        bullet.x= Round+bullets_Vel
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x== (red.x + 2):
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()

            if Dodge_Direction == 3 and (red.y >= lim or red.y - VEL < 0):#UP 
                red.y =red.y - Dodge_speed
                lim=lim-20
                for ws in b:
                    k=1
                    b.remove(ws)
                    b.append('3')
                    print('UP_Red: '+red)
                    print('Up_B: '+b)
                    c=1
                    #CPU_red_handle_movement(red,b,c,cpu_paddle,yellow_bullets,red_bullets,yellow)
                    lim=lim+DISPLAYSURF.get_width()//2
                if len(red_bullets)< Max_bullets-4:
                        bullet.x= Round+bullets_Vel
                        bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,10,5)
                        red_bullets.append(bullet_r)
                        Spaceship_guns_sound.play()
                        if bullet_r.x == (red.x + 20): 
                            red_bullets.append(bullet_r)
                            Spaceship_guns_sound.play()

    for bullet in red_bullets:
        bullet.x += bullets_Vel + 5    
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x > DISPLAYSURF.get_width():
            red_bullets.remove(bullet)

#CPU Movements
def Cpu_Handle(red,yellow,sign_y,sign_x,red_bullets,Max_bullets):
    
    if red.y == yellow.y and red.x < DISPLAYSURF.get_width()//2:
        red.x=red.x+2
        if len(red_bullets)< 1: #Max_bullets:
            bullet_y = pygame.Rect(red.x, red.y + (red.height//2) -2,10,5)
            red_bullets.append(bullet_y)
    if red.y  < 20: #UP
            sign_y = sign_y  *-1
    if red.y > DISPLAYSURF.get_height()-20: #DOWN
        sign_y  = sign_y  *-1
    if red.x  < 0: #UP
        sign_x = sign_x *-1
    if red.x > DISPLAYSURF.get_width()//2: #DOWN
        sign_x = sign_x *-1
    else:
        red.y=red.y-1*sign_y 
        red.x=red.x-1*sign_x