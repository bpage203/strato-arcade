# Import Everything
import pygame, sys, time, numpy, pandas
from game_code import *
from userinterface import *

# Initialize Everything! *This is the front end*
pygame.init()
pygame.joystick.init()  # main joystick device system
# Any variables and looping counters

homeScreen()
pygame.display.update()
# This is the back end
key_press = 0
directions = data_read('backend/ddr_file.txt')




# MAIN MENU
#     isMainMenu = False
#     homeScreen()

# END OF MAIN MENU

# GAME SCREEN AND LOOP  

# AUDIO GOES HERE

# CATCHER ANIMATION GOES HERE

# ARROW SPAWNING GOES HERE

