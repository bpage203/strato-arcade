import pygame
import sys

pygame.init()  
pygame.joystick.init()  # main joystick device system

try:
	j = pygame.joystick.Joystick(0) # create a joystick instance
	j.init() # init instance
	print ("Enabled joystick: {0}".format(j.get_name())) 
    
except pygame.error:
	print ("no joystick found.")


display_width = 800
display_height = 600



# Joystick information
joystick_count = pygame.joystick.get_count()
print("Joystick Count: " + str(joystick_count))
joystick_buttons = pygame.joystick.Joystick(0).get_numbuttons()
print("Number of Buttons: " + str(joystick_buttons))
joystick_axes =  pygame.joystick.Joystick(0).get_numaxes()
print("Number of Axes: " + str(joystick_axes))
hats = j.get_numhats()
print("Number of hats: {}".format(hats))


# Game Display Test
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Strato-Arcade Joystick Test')

def gameLoop():
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('goodbye')
                pygame.quit()
                sys.exit()
                quit()
             
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(0):
                    print("LEFT ARROW PRESSED")
                elif j.get_button(1):
                    print("DOWN ARROW")
                elif j.get_button(2):
                    print("UP ARROW")
                elif j.get_button(3):
                    print("RIGHT ARROW")
                elif j.get_button(4):
                    print("TRIANGLE")
                elif j.get_button(5):
                    print("SQUARE")
                elif j.get_button(6):
                    print("X")
                elif j.get_button(7):
                    print("CIRCLE")
                elif j.get_button(8):
                    print("SELECT")
                elif j.get_button(9):
                    print("START")
                               
    pygame.display.update()


gameLoop()
pygame.quit()
#test