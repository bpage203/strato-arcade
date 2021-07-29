import sys, pygame, time, playsound, numpy
from userinterface import homeScreen

# Graphics Function
def graphics_init():
    pass

# Music Function
def music_init():
    #initialize music
    #tracks = ['music1.mp3','music2.mp3','music3.mp3']
    bpms = [1,2,3]
    track_lengths = [10,20,30]
    track = int(input("Enter track number:\n"))
    bpm = bpms[track]
    track_length = track_lengths[track]
    wait_time = 10000000*60/bpm #tiks between beats
    #playsound.playsound(tracks[track])
    t_end = time.time() + track_length
    return t_end, wait_time

# Read data:
def data_read(fid):
    file = open(fid,'r')
    data = file.read()
    file.close()
    return data

# Show Points:
def show_points(msg,pts):
    if msg == 'MISS':
        pygame.display.something(msg)
    else:
        pygame.display.something(msg and pts)



# Update Arrow
def update_arrow(arrow,arrow_rect,directions,speed,player,count,num):
    target_pos = 10 #where the arrow outline will be 
    direction = int(directions[count]) - 1
    #print('count = ' + str(count))
    if arrow == 0:
        if players == 1:
            count = count + 2
        if players == 2:
            count = count + 1

        arrow = dic_arrows[direction]
        arrow_rect = arrow.get_rect() #hit box? find out what looks like to define start position
        if count <= 10:
            arrow_rect.top = height + int(num*height/num_arrows) #define start pos
        else:
            arrow_rect.top = height + int(height/num_arrows)

        if player == 1:
            arrow_rect.left = int(direction*width/8)
        if player == 2:
            arrow_rect.left = int(width/2 + direction*width/8)

    print('ypos = ' + str(arrow_rect.top))

    if arrow_rect.top < height:
        screen.blit(arrow, arrow_rect)

    next_arrow = False
    arrow_rect = arrow_rect.move(speed)
    #print('ypos2 = ' + str(arrow_rect.top))
    if arrow_rect.top < height/num_arrows:
        next_arrow = True
    if key_press!=0 and next_arrow:
        if key_press == direction:
            diff = numpy.abs(arrow_rect.top - target_pos)
            if diff <= 20:
                points = 5
                show_points('GOOD',points)
            if diff <= 10:
                points = 10
                show_points('GREAT',points)
            if diff <= 5:
                points = 20
                show_points('EXCELLENT',points)
            if diff <= 1:
                points = 50
                show_points('PERFECT',points)
            else:
                points = 0
                show_points('MISS',points)
        else: 
            points = 0
            show_points('MISS',points)
        next_arrow = False
        total_points[player] = total_points[player] + points

    if arrow_rect.top <= 0:
        arrow = None 
        arrow = 0

    return arrow,arrow_rect,count


pygame.init()
pygame.display.init()

#info = pygame.display.Info()
#print(info)

dic_arrows = [pygame.image.load('images/left_arrow.png'),pygame.image.load('images/up_arrow.png'),pygame.image.load('images/down_arrow.png'),pygame.image.load('images/right_arrow.png')]
num_arrows = 5
width = 300
height = 200
size = [width, height]
black = 0, 0, 0
screen = pygame.display.set_mode((width, height))
screen.fill('white')
pygame.display.set_caption("Strato-Arcade")
pygame.display.flip() # what does this do?

key_press = 0
directions = data_read('src/ddr_file.txt')

stuff = graphics_init()
#main menu, get choices
game_mode = int(input("Enter game difficulty level:\n")) #difficulty level 1 or 2, can easily add more if needed
players = int(input("Enter number of players:\n")) #number of players 1 or 2
total_points = [0 for i in range(players)]

if game_mode == 1:
    speed = [0, -1]
if game_mode == 2:
    speed = [0, -2]

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
ar2_1 = 0
ar2_1_rect = 0
ar2_2 = 0
ar2_2_rect = 0
ar2_3 = 0
ar2_3_rect = 0
ar2_4 = 0
ar2_4_rect = 0
ar2_5 = 0
ar2_5_rect = 0
t_end, wait_time = music_init()


while time.time() < t_end:
    #time.sleep(1) #use this for easier debugging
    #print('arrow 1 = ' + str(ar1_1))
    ar1_1,ar1_1_rect,count = update_arrow(ar1_1,ar1_1_rect,directions,speed,0,count,1) #player 1
    if players == 2:
        ar2_1,ar2_1_rect,count = update_arrow(ar2_1,ar2_1_rect,directions,speed,1,count,1) #player 2
    
    ar1_2,ar1_2_rect,count = update_arrow(ar1_2,ar1_2_rect,directions,speed,0,count,2) 
    if players == 2:
        ar2_2,ar2_2_rect,count = update_arrow(ar2_2,ar2_2_rect,directions,speed,1,count,2)
    
    ar1_3,ar1_3_rect,count = update_arrow(ar1_3,ar1_3_rect,directions,speed,0,count,3) 
    if players == 2:
        ar2_3,ar2_3_rect,count = update_arrow(ar2_3,ar2_3_rect,directions,speed,1,count,3) 
    
    ar1_4,ar1_4_rect,count = update_arrow(ar1_4,ar1_4_rect,directions,speed,0,count,4) 
    if players == 2:
        ar2_4,ar2_4_rect,count = update_arrow(ar2_4,ar2_4_rect,directions,speed,1,count,4) 

    ar1_5,ar1_5_rect,count = update_arrow(ar1_5,ar1_5_rect,directions,speed,0,count,5) 
    if players == 2:
        ar2_5,ar2_5_rect,count = update_arrow(ar2_5,ar2_5_rect,directions,speed,1,count,5) 

#pygame.display(total_points)
print('End Game')






