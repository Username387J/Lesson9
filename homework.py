from random import randint
import pgzrun


WIDTH = 300
HEIGHT = 300
TITLE = "CONNECT THE DOTS"
dots = []
num_of_dots = 5
next_dot = 0
lines = []
game_over = False
time_left=60
time = 30.0


def create_dot():
    for i in range(0, num_of_dots):
        dot = Actor("dot")
        dot.pos = randint(50, 250), randint(50, 250)
        dots.append(dot)


def draw():
    screen.blit("square", (0, 0))
    num = 1  
    for dot in dots:
        dot.draw()
        screen.draw.text(str(num), (dot.pos[0], dot.pos[1]-7))
        num += 1  

    for line in lines:
        screen.draw.line(line[0], line[1], (0, 255, 255))

    if next_dot == 5:
        screen.fill("white")
        screen.draw.text("Congratulations", center=(150, 150), fontsize=30, color="black")

    if game_over==True:
        screen.fill("white")
        screen.draw.text("Time's Up! You got to dot number",str(next_dot), center=(150, 150), fontsize=30, color="black")

    

def update():
    pass


def on_mouse_down(pos):
    global next_dot, lines
    if next_dot < num_of_dots:
        if dots[next_dot].collidepoint(pos):
            if next_dot:
                lines.append((dots[next_dot - 1].pos , dots[next_dot].pos))
            next_dot = next_dot+1
        else:
            lines = []  
            next_dot = 0  


def time_up():
    global game_over
    game_over = True



clock.schedule(time_up,time)

create_dot()
pgzrun.go()
