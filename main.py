from random import randint
import pgzrun
from time import time

WIDTH=300
HEIGHT=300
TITLE="CONNECT THE DOTS"

dots = []
num_of_dots = 8
next_dot = 0
lines = []
game_over=False


def createDot():
    global start_time
    for i in range (0,num_of_dots):
        dot=Actor("dot")
        dot.pos= randint(50,250), randint(50,250)
        dots.append(dot)

def time_up():
    global game_over
    game_over=True 


def draw():

    screen.blit("square",(0,0))
    num=1
    
    for dot in dots:
        dot.draw()
        screen.draw.text(str(num), (dot.pos[0], dot.pos[1]-3))
        num= num+1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

        if game_over:
             screen.fill("white")
             screen.draw.text("Time's Up ! You connected : "+str(next_dot),"dots together", center=(50,50), fontsize=35, color="black")
    
       


def update():
    pass

clock.schedule(time_up, 60.0)
createDot()
pgzrun.go()
