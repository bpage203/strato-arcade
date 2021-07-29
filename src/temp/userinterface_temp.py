import pygame, sys
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
    background = pygame.image.load('images/Strato-Arcade.png')
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
def setBackground(level, num_players):
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.flip()
    #if num_players == 1:
        # Creates background
    background = pygame.image.load('images/Strato-Arcade.png')
    background = pygame.transform.scale(background, (1000,500))
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
        #dic_arrows['left1'] = left_arrow
       # dic_arrows['right1'] = right_arrow
      #  dic_arrows['up1'] = up_arrow
      #  dic_arrows['down1'] = down_arrow
    

    #########TO DO!!!!!!!!!##############
    #if num_players == 2:
    return dic_arrows


def singlePlayerUI():
    players = 1
    run = True
    screen = pygame.display.set_mode((1000, 500))
    while run:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             run= False

        # Fill the background
        background = pygame.image.load('images/Strato-Arcade.png').convert_alpha()
        background = pygame.transform.scale(background, (1000,500))
        screen.blit(background,(0,0))

        # Draw 4 arrows if players = 1
        left_arrow = pygame.image.load('images/left_arrow.png')
        down_arrow = pygame.image.load('images/down_arrow.png')
        up_arrow = pygame.image.load('images/up_arrow.png')
        right_arrow = pygame.image.load('images/right_arrow.png')
        screen.blit(background,(0,0))
        screen.blit(left_arrow,(300,20))
        screen.blit(down_arrow,(450,10))
        screen.blit(up_arrow,(575,10))
        screen.blit(right_arrow,(700,20))
       

        # Moving Arrows:
        left_arrow_move = pygame.image.load('images/left_arrow_hit.png')
        down_arrow_move = pygame.image.load('images/down_arrow_hit.png')
        up_arrow_move = pygame.image.load('images/up_arrow_hit.png')
        right_arrow_move = pygame.image.load('images/right_arrow_hit.png')

        left_pos = left_arrow_move.get_rect(center = (350, 400))
        down_pos = down_arrow_move.get_rect(center = (490, 400))
        up_pos = up_arrow_move.get_rect(center = (620, 400))
        right_pos = right_arrow_move.get_rect(center = (750,400))

        for i in range(200): # this is going to be the length of the file
            left_pos = left_pos.move(0,-2) # figure out the speed functionality
            down_pos = down_pos.move(0,-2)
            up_pos = up_pos.move(0,-2)
            right_pos = right_pos.move(0,-2)
            
            screen.blit(left_arrow_move, left_pos)
            screen.blit(down_arrow_move, down_pos)
            screen.blit(up_arrow_move, up_pos)
            screen.blit(right_arrow_move, right_pos)
            pygame.display.update()
            pygame.time.delay(100)

        pygame.display.update()
        # Flip the display
        pygame.display.flip()
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
        background = pygame.image.load('images/Strato-Arcade.png').convert_alpha()
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
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.flip()

     # Load Button Images
    single_img = pygame.image.load('images/single_button/single_button1.png').convert_alpha()
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

    single_button = Button(180, 280, single_img, 0.3)
    double_button = Button(600, 290, double_img, 0.3)

    while run:
        
        # Sets stuff for loops of buttons
        count = 0
        wl = [300,310,320]
        hl = [25,30,35]

        background = pygame.image.load('images/space/frame_00_delay-0.07s.gif').convert_alpha()
        background = pygame.transform.scale(background, (1000,500))
        screen.blit(background,(0,0))

        logo = pygame.image.load('images/Strato.png')
        logo = pygame.transform.scale(logo, (375,150))
        screen.blit(logo,(wl[count],hl[count]))

        if single_button.draw() == True:
            players = 1
            print("Single")
            #Calling the other methods
            singlePlayerUI()
        
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

    

    
