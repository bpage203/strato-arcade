import pygame, sys
from pygame.locals import *
import time
import glob, os
pygame.init()
# Adding comment
# I'm using this main function to test/demonstrate, but eventually should be phased out in use of defined functions 
def main():
    # Creates screen
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.flip()
    # Creates background
    background = pygame.image.load(r'front-end\Strato-Arcade.png')
    background = pygame.transform.scale(background, (1000,500))
    # Sets arrows for background 
    left_arrow = pygame.image.load(r'front-end\left_arrow.png')
    down_arrow = pygame.image.load(r'front-end\down_arrow.png')
    up_arrow = pygame.image.load(r'front-end\up_arrow.png')
    right_arrow = pygame.image.load(r'front-end\right_arrow.png')
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
def setBackground(level, num_players):
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.flip()
    if num_players == 1:
        # Creates background
        background = pygame.image.load(r'front-end\backgrounds\game_background.png')
        background = pygame.transform.scale(background, (1000,500))
        # Sets logo on left side 
        logo = pygame.image.load(r'front-end\logos\Vertical_Strato.png')
        ##################Not sure if this is in a good location?
        screen.blit(logo,(50,500))
        # Sets arrows for background 
        left_arrow = pygame.image.load(r'front-end\arrows\left_gray.png')
        down_arrow = pygame.image.load(r'front-end\arrows\down_gray.png')
        up_arrow = pygame.image.load(r'front-end\arrows\up_gray.png')
        right_arrow = pygame.image.load(r'front-end\arrows\right_gray.png')
        screen.blit(background,(0,0))
        screen.blit(left_arrow,(300,20))
        screen.blit(down_arrow,(450,0))
        screen.blit(up_arrow,(575,0))
        screen.blit(right_arrow,(700,20))
        pygame.display.update()
        # Adds arrows to dictionary
        dic_arrows['left1'] = left_arrow
        dic_arrows['right1'] = right_arrow
        dic_arrows['up1'] = up_arrow
        dic_arrows['down1'] = down_arrow
    

    #########TO DO!!!!!!!!!##############
    #if num_players == 2:
    return dic_arrows

# For splitting up gifs into separate images
# https://ezgif.com/split/ezgif-7-8624e5747d03.gif
def homeScreen():
    run = True
    # Gets all the picture names from the given file
    pic_names = []
    for filename in glob.iglob('C:/Users/missa/Desktop/t1-stratoarcade/images/spiral/**'):
        pic_names.append(filename)
    # Creates screen
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.flip()
    # Creates background
    #first = pic_names[0]
    while run:
        
        # Sets stuff for loops of buttons
        count = 0
        # location of single button along x axis
        ws = [240,250,260]
        # location of single button along y axis
        hs = [215,220,225]
        # location of double button along x axis
        wd = [520,530,540]
        # location of double button along y axis
        hd = [225,230,235]
        # location of logo along x axis
        wl = [300,310,320]
        # location of logo along y axis 
        hl = [25,30,35]
        # Loops through the background pictures and displays them to the screen
        for x in pic_names:
            background = pygame.image.load(x)
            background = pygame.transform.scale(background, (1000,500))
            screen.blit(background,(0,0))
            
            logo = pygame.image.load('C:/Users/missa/Desktop/t1-stratoarcade/images/Strato.png').convert_alpha()
            #logo = pygame.transform.scale(logo, (75,75))
            screen.blit(logo,(wl[count],hl[count]))
            single_button = pygame.image.load('C:/Users/missa/Desktop/t1-stratoarcade/images/single_button/single_button1.png').convert_alpha()
            single_button = pygame.transform.scale(single_button, (175,75))
            screen.blit(single_button,(ws[count],hs[count]))
            double_button = pygame.image.load('C:/Users/missa/Desktop/t1-stratoarcade/images/double.png').convert_alpha()
            double_button = pygame.transform.scale(double_button, (175,62))
            screen.blit(double_button,(wd[count],hd[count]))
            count += 1
            if count > 2:
                count -= 1
            if count < 0:
                count += 1

            pygame.display.update()
            time.sleep(.09)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

homeScreen()

    
    
    

    

    
