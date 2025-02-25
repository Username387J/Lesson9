from random import randint
import pgzrun
from time import time

WIDTH = 600
HEIGHT = 600
TITLE= "SPACE GAME"

satellites = []
number_of_satellites = 12
next_satellite = 0
lines = []
start_time = 0
total_time = 0
end_time = 0

def createSatellite():
    global start_time
    for i in range (0,number_of_satellites):
        satellite=Actor("satellite")
        satellite.pos= randint(50,550), randint(50,550)
        satellites.append(satellite)

    start_time=time()


def draw():
    global total_time
    screen.blit("sky",(0,0))
    num=1
    
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(num), (satellite.pos[0], satellite.pos[1]+20))
        num= num+1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_satellite < number_of_satellites:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)

    if next_satellite == 12:
        screen.draw.text("Good Job", (300,300), fontsize=30)

def update():
    pass

def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite < number_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite = next_satellite + 1   
        else:
            lines = []
            next_satellite = 0










createSatellite()
pgzrun.go()
