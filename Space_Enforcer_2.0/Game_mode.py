from Settings import *
from Handle_movement import *
from button import *

#Draw
def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health,red_score_text,yellow_score_text,Yellow_player,Red_player,Round):
    DISPLAYSURF.blit(back_opt,(0,0))
    pygame.draw.rect(DISPLAYSURF,Black,Border)
    red_health_text = Health_font.render("Health: " + str(red_health),1,Red)
    yellow_health_text = Health_font.render("Health: " + str(yellow_health),1,Yellow)
    red_score_text = Health_font.render(str(Red_player),1,Red)
    yellow_score_text = Health_font.render("-Score-" + str(Yellow_player),1,Yellow)
    DISPLAYSURF.blit(yellow_health_text,(DISPLAYSURF.get_width() - yellow_health_text.get_width() - 10,10))
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
def draw_winner(text,wineer_color,Round):
    draw_text = Winner_font.render(text, 1, wineer_color)
    DISPLAYSURF.blit(draw_text, (DISPLAYSURF.get_width()//2 - draw_text.get_width()/2,DISPLAYSURF.get_height()//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)
    Explosion_sound.stop()
    pygame.display.update()
def draw_kill(kill_pos):
    DISPLAYSURF.blit(Space_End,((kill_pos).x, (kill_pos).y))
    pygame.display.update()
    Explosion_sound.play()
    Explosion_sound.set_volume(2)

def main(): 
    DISPLAYSURF = pygame.display.set_mode((DISPLAYSURF.get_width(), DISPLAYSURF.get_height()))
    pygame.display.set_caption("Space Games")

    background = pygame.Surface(DISPLAYSURF.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    joysticks = []
    clock = pygame.time.Clock()
    keepPlaying = True
    clock.tick(60)
def main2(): 
    DISPLAYSURF = pygame.display.set_mode((DISPLAYSURF.get_width(), DISPLAYSURF.get_height()))
    pygame.display.set_caption("Space Games")

    background = pygame.Surface(DISPLAYSURF.get_size())
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

def draw_reset(Round,Start1):
    print(DISPLAYSURF.get_width(),DISPLAYSURF.get_height())
    while Start1:
        CVP =True
        DISPLAYSURF.blit(Menu_image,(0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS,DISPLAYSURF)
            button.update(DISPLAYSURF)
       
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("play",MENU_MOUSE_POS,PLAY_BUTTON.checkForInput(MENU_MOUSE_POS))
                    draw_play(Round,Start1)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("option",MENU_MOUSE_POS,OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS))
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Quit",MENU_MOUSE_POS,QUIT_BUTTON.checkForInput(MENU_MOUSE_POS))
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def draw_play(Round,Start1):
    while Start1:
        CVP =True
        DISPLAYSURF.blit(Game_mode_image,(0,0))
        GAME_MODE_MOUSE_POS = pygame.mouse.get_pos()
        for button in [ONE_PLAYER_BUTTON, TWO_PLAYER_BUTTON, MENU_BUTTON]:
            button.changeColor(GAME_MODE_MOUSE_POS,DISPLAYSURF)
            button.update(DISPLAYSURF)
        pygame.display.update()
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(GAME_MODE_MOUSE_POS)
                if MENU_BUTTON.checkForInput(GAME_MODE_MOUSE_POS):
                    print("Menu clicked")
                    draw_reset(Round,Start1)
                if ONE_PLAYER_BUTTON.checkForInput(GAME_MODE_MOUSE_POS):
                    print("CVP") #Left
                    CVP=True
                    game_version = Winner_font.render("Player vs CPU",1,White)
                    DISPLAYSURF.fill(Black)
                    pygame.display.update()
                    while CVP:
                        pygame.mixer.Channel(0).fadeout(13000)
                        DISPLAYSURF.fill(Black)
                        pygame.display.update()
                        DISPLAYSURF.blit(game_version,(20,DISPLAYSURF.get_height()//2))
                        pygame.display.update()
                        pygame.time.delay(3000)
                        DISPLAYSURF.fill(Black)
                        pygame.display.update()
                        Round+=1
                        Levels=Round*50
                        print(Round)
                        pygame.display.update()
                        rounds = Winner_font.render("Round " + str(Round),1,White)
                        DISPLAYSURF.blit(rounds,(DISPLAYSURF.get_width()//3,DISPLAYSURF.get_height()//2))
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
                if TWO_PLAYER_BUTTON.checkForInput(GAME_MODE_MOUSE_POS):
                    print("PVP") #Right
                    PVP=True
                    game_version=Health_font.render("Plaver vs Player",1,White)
                    pygame.display.update()
                    DISPLAYSURF.fill(Black)
                    pygame.display.update()
                    while PVP:
                        pygame.mixer.Channel(0).fadeout(13000)
                        DISPLAYSURF.fill(Black)
                        pygame.display.update()
                        DISPLAYSURF.blit(game_version,(20,DISPLAYSURF.get_height()//2))
                        pygame.time.delay(8000)
                        DISPLAYSURF.fill(Black)
                        pygame.display.update()
                        Round+=1
                        Levels=Round*50
                        print(Round)
                        pygame.display.update()
                        rounds = Winner_font.render("Round " + str(Round),1,White)
                        DISPLAYSURF.blit(rounds,(DISPLAYSURF.get_width()//3,DISPLAYSURF.get_height()//2))
                        pygame.display.update()
                        pygame.time.delay(5000)
                        Main_PvP(Round,Champ,red_score_text,yellow_score_text,Levels,Red_player,Yellow_player,main)
                        pygame.display.update()
                        DISPLAYSURF.fill(Black)
                        score = Winner_font.render(str(Red_player)+" Score " + str(Yellow_player),1,White)
                        DISPLAYSURF.blit(score,(200,300))
                        pygame.display.update()
                        
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
                    DISPLAYSURF.blit(game_version,(20,DISPLAYSURF.get_height()//2))
                    pygame.time.delay(3000)
                    DISPLAYSURF.fill(Black)
                    pygame.display.update()
                    Round+=1
                    Levels=Round*50
                    print(Round)
                    pygame.display.update()
                    rounds = Winner_font.render("Round " + str(Round),1,White)
                    DISPLAYSURF.blit(rounds,(DISPLAYSURF.get_width()//3,DISPLAYSURF.get_height()//2))
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

    
def Champ_win(Champ_color,Red_player,Yellow_player):
    if Red_player>2:
        Champ_color =Red
        Champ = "RED IS THE CHAMPION"   
    if Yellow_player>2:
        Champ ='YELLOW IS THE CHAMPION'
        Champ_color=Yellow
def draw_Champion(Champ):
    Champ_win(Champ_color)
    draw_text = Winner_font.render(Champ, 1, White)
    DISPLAYSURF.blit(draw_text, (DISPLAYSURF.get_width()//2 - draw_text.get_width()/2,DISPLAYSURF.get_height()//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)
    Explosion_sound.stop()
    pygame.display.update()

#Main game loop P1vsp2
def main_PVP(Round,Champ,red_score_text,yellow_score_text):
    pygame.mixer.Channel(0).fadeout(3000)
    pygame.time.delay(2000)
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
    pygame.time.delay(6000)
    pygame.mixer.Channel(0).pause
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join('Space_Enforcer_2.0/Asset Project 1', 'new.mp3')),loops=-1,fade_ms=3000)
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
                if event.key==pygame.K_m :
                    PVP=False
                    break
                if event.key==pygame.K_v and len(red_bullets)< Max_bullets:
                    bullet_r = pygame.Rect(red.x + red.width, red.y + (red.height//2) -2,DISPLAYSURF.get_width()//90,DISPLAYSURF.get_height()//100)
                    red_bullets.append(bullet_r)
                    Spaceship_guns_sound.play()

                if event.key==pygame.K_b and len(yellow_bullets)< Max_bullets:
                    bullet_y = pygame.Rect(yellow.x, yellow.y + (yellow.height//2) -2,DISPLAYSURF.get_width()//90,DISPLAYSURF.get_height()//100)
                    yellow_bullets.append(bullet_y)
                    Spaceship_guns_sound.play()
            if event.type == pygame.JOYAXISMOTION and len(yellow_bullets)< Max_bullets:
                joy=joy+1
                if joy==7:
                    bullet_y = pygame.Rect(yellow.x, yellow.y + (yellow.height//2) -2,DISPLAYSURF.get_width()//90,DISPLAYSURF.get_height()//100)
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
    pygame.time.delay(6000)
    pygame.mixer.Channel(0).pause
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join('Space_Enforcer_2.0/Asset Project 1', 'new.mp3')),loops=-1,fade_ms=3000)
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

                if event.key==pygame.K_SPACE and len(yellow_bullets)< Max_bullets:
                    bullet_y = pygame.Rect(yellow.x, yellow.y + (yellow.height//2) -2,10,5)
                    yellow_bullets.append(bullet_y)
                    Spaceship_guns_sound.play().set_volume(2.0)

            if event.type ==  CPU_hit:
                Spaceship_guns_sound.play().set_volume(2.0)
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
    pygame.time.delay(3000)
    pygame.mixer.Channel(0).pause
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join('Space_Enforcer_2.0/Asset Project 1', 'new.mp3')),loops=-1,fade_ms=3000)
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
