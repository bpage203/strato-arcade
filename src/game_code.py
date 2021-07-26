import sys, pygame, time, playsound, numpy
from userinterface import homeScreen


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
    print('count = ' + str(count))
    if arrow == 0:
        if players == 1:
            count = count + 2
        if players == 2:
            count = count + 1

        arrow = dic_arrows[direction]
        arrow_rect = arrow.get_rect() #hit box? find out what looks like to define start position
        arrow_rect.top = height + int(num*height/num_arrows) #define start pos right
        if player == 1:
            arrow_rect.left = int(direction*width/8)
        if player == 2:
            arrow_rect.left = int(width/2 + direction*width/8)

    print('ypos = ' + str(arrow_rect.top))

  #  if arrow_rect.top < size[1]:
      #  screen.blit(arrow, arrow_rect)

    next_arrow = False
    arrow_rect = arrow_rect.move(speed)
    print('ypos2 = ' + str(arrow_rect.top))
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







