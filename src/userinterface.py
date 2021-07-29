import pygame, sys, numpy, playsound
from pygame.locals import *
import time
import glob, os


# Adding comment
# I'm using this main function to test/demonstrate, but eventually should be phased out in use of defined functions 
def main():
    # Creates screen
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.flip()
    # Creates background
    background = pygame.image.load('images/Strato.png')
   # background = pygame.transform.scale(background, (1920,1080))
    # Sets arrows for background 
    left_arrow = pygame.image.load('images/left_arrow.png')
    down_arrow = pygame.image.load('images/down_arrow.png')
    up_arrow = pygame.image.load('images/up_arrow.png')
    right_arrow = pygame.image.load('images/right_arrow.png')
    screen.blit(background,(0,0))
    screen.blit(left_arrow,(300,20))
    screen.blit(down_arrow,(450,0))
    screen.blit(up_arrow,(575,0))
    screen.blit(right_arrow,(700,20))
    pygame.display.update()

    time.sleep(10)

# Call this function from the backend to set up the background UI depending upon the level and number of players 
# @param level: 1-2
# @param num_players: 1-2
# @return dic_arrows[]
def setBackground(level, background):
    height = pygame.display.Info().current_h 
    width = pygame.display.Info().current_w
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    #if num_players == 1:
        # Creates background
   # background = pygame.image.load('images/Strato-Arcade.png')
    background = pygame.transform.scale(background, (width,height))
        # Sets arrows for background 
    left_arrow = pygame.image.load('images/left_arrow.png')
    down_arrow = pygame.image.load('images/down_arrow.png')
    up_arrow = pygame.image.load('images/up_arrow.png')
    right_arrow = pygame.image.load('images/right_arrow.png')
    dic_arrows = [left_arrow,down_arrow,up_arrow,right_arrow]
    screen.blit(background,(0,0))
    screen.blit(left_arrow,(300-45,20))
    screen.blit(down_arrow,(450-45,0))
    screen.blit(up_arrow,(575-45,0))
    screen.blit(right_arrow,(700-45,20))
    pygame.display.update()
        #dic_arrows['left1'] = left_arrow
       # dic_arrows['right1'] = right_arrow
      #  dic_arrows['up1'] = up_arrow
      #  dic_arrows['down1'] = down_arrow
    

    #########TO DO!!!!!!!!!##############
    #if num_players == 2:
    return dic_arrows

# Music Function
def music_init(track):
    #initialize music
    tracks = os.listdir('tracks')
    for t in tracks[:]:
        if not(t.endswith('.mp3')):
            tracks.remove(t)
    info_id = open('tracks/info.txt','r')
    lines = info_id.readlines()
    bpms = [0 for i in range(len(lines)-1)]
    track_lengths = [0 for i in range(len(lines)-1)]
    track_delays = [0 for i in range(len(lines)-1)]
    line_num = 0
    for line in lines:
        if line_num!=0:
            bpms[line_num-1] = int(line[0:3])
            track_lengths[line_num-1] = int(line[6:9])
            track_delays[line_num-1] = int(line[12:15])
        line_num = line_num + 1

    #track = 0 #minjaj is 23
    bpm = bpms[track]
    track_length = track_lengths[track]
    track_delay = 1000*track_delays[track]
    wait_time = 60/bpm #tiks between beats #sec = 10000000 tiks  
    pygame.mixer.init()
    pygame.mixer.music.load('tracks/' + tracks[track])
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()    
    t_end = time.time() + track_length
    return t_end, wait_time, track_delay

# Read data:
def data_read(fid):
    file = open(fid,'r')
    data = file.read()
    file.close()
    return data

# Show Points:
def show_points(msg,pts):
    if disp_count<100:
        if msg == 'MISS':
            screen.blit(miss,(300-35,40))
        elif msg == 'GOOD':
            screen.blit(good,(300-35,40))
        elif msg == 'GREAT':
            screen.blit(great,(300-35,40))
        elif msg == 'EXCELLENT':
            screen.blit(excellent,(300-35,40))
        elif msg == 'PERFECT':
            screen.blit(perfect,(300-35,40))
    else:
        msg = None
    pygame.display.update()



# Update Arrow
def update_arrow(arrow,arrow_rect,directions,speed,player,num,count,key_press,msg):
    #print(key_press)
    width = size[0]
    height = size[1]

    target_pos = 10 #where the arrow outline will be 
    direction = int(directions[count]) - 1

    if arrow == 0:
        if players == 1:
            count = count + 2
        if players == 2:
            count = count + 1

        arrow = dic_arrows[direction]
        arrow_rect = arrow.get_rect() #hit box? find out what looks like to define start position
        if count <= 10:
            top = height + int(num*height/num_arrows) #define start pos
        else:
            top = height + int(height/num_arrows)

        if players == 1:
            #left = int(direction*width/4)
            lefts = [300,450,575,700] 
            left = lefts[direction]
        else:
            if player == 1:
                left = int(direction*width/8)
            if player == 2:
                left = int(width/2 + direction*width/8)

        arrow_rect = arrow.get_rect(center = (left,top)) 

    next_arrow = False
    arrow_rect = arrow_rect.move(speed)

    if arrow_rect.center[1] < height/num_arrows:
        next_arrow = True
    if key_press>=0 and next_arrow:
        if key_press == direction:
            disp_count = 0
            diff = numpy.abs(arrow_rect.top - target_pos)
            if diff <= 1:
                points = 50
                msg = 'PERFECT'
                #show_points('PERFECT',points)
            elif diff <= 5:
                points = 20
                msg = 'EXCELLENT'
                #show_points('EXCELLENT',points)
            elif diff <= 10:
                points = 10
                msg = 'EXCELLENT'
                #show_points('GREAT',points)
            elif diff <= 20:
                points = 5
                msg = 'GOOD'
                #show_points('GOOD',points)
            else:
                points = 0
                msg = 'MISS'
                #show_points('MISS',points)
        else: 
            points = 0
            msg = 'MISS'
            #show_points('MISS',points)
        next_arrow = False
        total_points[player] = total_points[player] + points

    if arrow_rect.top <= 0:
        disp_count = 0
        msg = 'MISS' 
        arrow = 0

    return arrow,arrow_rect,count,msg

def singlePlayerUI(game_mode,track,j):
    global players
    players = 1
    run = True
    height = pygame.display.Info().current_h 
    width = pygame.display.Info().current_w
    global size
    size = [width,height]
    global screen
    screen = pygame.display.set_mode((width, height))
    global total_points
    total_points = [0 for i in range(players)]
    if game_mode == 1:
        speed = [0, -1]
    if game_mode == 2:
        speed = [0, -2]

    global miss
    global good
    global great
    global excellent
    global perfect
    miss = pygame.image.load('images/miss.png')
    good = pygame.image.load('images/good.png')
    great = pygame.image.load('images/great.png')
    excellent = pygame.image.load('images/excellent.png')
    perfect = pygame.image.load('images/perfect.png')

    global directions
    directions = data_read('src/ddr_file.txt')

    # Fill the background
    background = pygame.image.load('images/game_background.png').convert_alpha()
    background = pygame.transform.scale(background, (width,height))
    screen.blit(background,(0,0))

    global dic_arrows
    dic_arrows = setBackground(game_mode,background)
    global num_arrows
    num_arrows = 5
    count = 0 #initialize arrow stuff
    ar1_1 = 0
    ar1_1_rect = 0
    ar1_2 = 0
    ar1_2_rect = 0
    ar1_3 = 0
    ar1_3_rect = 0
    ar1_4 = 0
    ar1_4_rect = 0
    ar1_5 = 0
    ar1_5_rect = 0
    global disp_count
    disp_count = 100
    key_press = -1
    t_end, wait_time, track_delay = music_init(track)
    pygame.time.delay(track_delay)

    while time.time()<t_end and run:
        disp_count = disp_count + 1
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             run = False
        if event.type == pygame.JOYBUTTONDOWN:
            disp_count = 0
            if j.get_button(0):
                key_press = 0
            elif j.get_button(1):
                key_press = 1
            elif j.get_button(2):
                key_press = 2
            elif j.get_button(3):
                key_press = 3
                #0,1,2,3 = left, down, up, right

        disp_msg = None
        msg = None

        ar1_1,ar1_1_rect,count,msg = update_arrow(ar1_1,ar1_1_rect,directions,speed,0,1,count,key_press,msg) 
        ar1_2,ar1_2_rect,count,msg = update_arrow(ar1_2,ar1_2_rect,directions,speed,0,2,count,key_press,msg) 
        ar1_3,ar1_3_rect,count,msg = update_arrow(ar1_3,ar1_3_rect,directions,speed,0,3,count,key_press,msg) 
        ar1_4,ar1_4_rect,count,msg = update_arrow(ar1_4,ar1_4_rect,directions,speed,0,4,count,key_press,msg)
        ar1_5,ar1_5_rect,count,msg = update_arrow(ar1_5,ar1_5_rect,directions,speed,0,5,count,key_press,msg) 
        
        key_press = -1

        screen.blit(background,(0,0))
        screen.blit(logo,(int(3*width/4),int(height/5)))
        screen.blit(dic_arrows[0],(300-45,20))
        screen.blit(dic_arrows[1],(450-45,0))
        screen.blit(dic_arrows[2],(575-45,0))
        screen.blit(dic_arrows[3],(700-45,20))

        if ar1_1 and ar1_1_rect.center[1] < height:
            screen.blit(ar1_1, ar1_1_rect)
        if ar1_2 and ar1_2_rect.center[1] < height:
            screen.blit(ar1_2, ar1_2_rect)
        if ar1_3 and ar1_3_rect.center[1] < height:
            screen.blit(ar1_3, ar1_3_rect)
        if ar1_4 and ar1_4_rect.center[1] < height:
            screen.blit(ar1_4, ar1_4_rect)
        if ar1_5 and ar1_5_rect.center[1] < height:
            screen.blit(ar1_5, ar1_5_rect)

        if disp_count<=100:
            disp_msg = msg
            if disp_msg == 'MISS':
                screen.blit(miss,(300-35,40))
            elif disp_msg == 'GOOD':
                screen.blit(good,(300-35,40))
            elif disp_msg == 'GREAT':
                screen.blit(great,(300-35,40))
            elif disp_msg == 'EXCELLENT':
                screen.blit(excellent,(300-35,40))
            elif disp_msg == 'PERFECT':
                screen.blit(perfect,(300-35,40))

        pygame.display.update()
        pygame.time.delay(3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()   

    return players   

def multiPlayerUI():
    players = 2
    run = True
    screen = pygame.display.set_mode((1000, 500))
    while run:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             run= False

        # Fill the background
        background = pygame.image.load('images/game_background.png').convert_alpha()
        background = pygame.transform.scale(background, (1000,500))
        screen.blit(background,(0,0))

        # Draw 8 arrows for 2 players
        left_arrow1 = pygame.image.load('images/left_arrow.png')
        left_arrow1 = pygame.transform.scale(left_arrow1, (75, 75))
        down_arrow1 = pygame.image.load('images/down_arrow.png')
        down_arrow1 = pygame.transform.scale(down_arrow1, (75, 75))
        up_arrow1 = pygame.image.load('images/up_arrow.png')
        up_arrow1 = pygame.transform.scale(up_arrow1, (75, 75))
        right_arrow1 = pygame.image.load('images/right_arrow.png')
        right_arrow1 = pygame.transform.scale(right_arrow1, (75, 75))

        left_arrow2 = pygame.image.load('images/left_arrow.png')
        left_arrow2 = pygame.transform.scale(left_arrow2, (75, 75))
        down_arrow2 = pygame.image.load('images/down_arrow.png')
        down_arrow2 = pygame.transform.scale(down_arrow2, (75, 75))
        up_arrow2 = pygame.image.load('images/up_arrow.png')
        up_arrow2 = pygame.transform.scale(up_arrow2, (75, 75))
        right_arrow2 = pygame.image.load('images/right_arrow.png')
        right_arrow2 = pygame.transform.scale(right_arrow2, (75, 75))


        screen.blit(background,(0,0))
        screen.blit(left_arrow1,(150,20))
        screen.blit(down_arrow1,(250,10))
        screen.blit(up_arrow1,(350,10))
        screen.blit(right_arrow1,(450,20))
        
        screen.blit(left_arrow2,(600,20))
        screen.blit(down_arrow2,(700,10))
        screen.blit(up_arrow2,(800,10))
        screen.blit(right_arrow2,(900,20))
        pygame.display.update()

        # Flip the display
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit() 
    return players

# For splitting up gifs into separate images
# https://ezgif.com/split/ezgif-7-8624e5747d03.gif
def homeScreen():
    run = True

    # Creates screen
    height = pygame.display.Info().current_h 
    width = pygame.display.Info().current_w
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()

    pygame.joystick.init()  # main joystick device system
    try:
        j = pygame.joystick.Joystick(0) # create a joystick instance
        j.init() # init instance
        print ("Enabled joystick: {0}".format(j.get_name())) 
        
    except pygame.error:
        print ("no joystick found.")

     # Load Button Images
    single_img = pygame.image.load('images/single_button1.png').convert_alpha()
    double_img = pygame.image.load('images/double.png').convert_alpha()


    class Button():
        def __init__(self, x, y, image, scale):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), (int(height * scale))))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False


            screen.blit(self.image, (self.rect.x, self.rect.y))
            return action

    single_button = Button(int(2*width/4), int(2*height/5), single_img, 0.3)
    double_button = Button(int(3*width/4), int(2*height/5), double_img, 0.3)

    while run:
        
        # Sets stuff for loops of buttons
        count = 0
        wl = [300,310,320] #?
        hl = [25,30,35]

        background = pygame.image.load('images/space/frame_00_delay-0.07s.gif').convert_alpha()
        background = pygame.transform.scale(background, (width,height))
        screen.blit(background,(0,0))

        global logo
        logo = pygame.image.load('images/Strato.png')
        logo = pygame.transform.scale(logo, (375,150))
        screen.blit(logo,(int(width/2),int(height/5)))

        if single_button.draw() == True:
            players = 1
            print("Single")
            #Calling the other methods
            game_mode = 1
            track = 25
            singlePlayerUI(game_mode,track,j)
        
        if double_button.draw() == True:
            players = 2
            print("Double")
            #Calling the other methods
            multiPlayerUI()
      
        
        pygame.display.update()
        
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()   
        
       


    
    
    

def doneScreen():
    pass

    

    
