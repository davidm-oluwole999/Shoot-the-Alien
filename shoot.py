import pgzrun
from random import randint

WIDTH= 500
HEIGHT= 500

TITLE= "Shoot the Alien"

message= ""

alien= Actor("alien")


def draw():
    screen.fill(color=(204,43,178))
    alien.draw()
    screen.draw.text(message,center=(300,30), fontsize=30)

def place_alien():
    alien.x= randint(50, WIDTH -50)
    alien.y= randint(50, HEIGHT -50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="Good Shot"
        place_alien()
    else:
        message="Missed Shot"

pgzrun.go()