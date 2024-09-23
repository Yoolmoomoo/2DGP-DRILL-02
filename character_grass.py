from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=90
degree = 20
radius = 200
radian = degree * math.pi / 180
X = 200 + radius * math.cos(radian)
Y = 200 + radius * math.sin(radian)

while (True):
    while (x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x += 2

        delay(0.001)

    while (y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x-=1.5
        y+=2

        delay(0.001)

    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x-=1.5
        y-=2

        delay(0.001)

    while (degree < 360):
        clear_canvas_now()
        radian = degree * math.pi / 180
        X = 400 + radius * math.cos(radian)
        Y = 300 + radius * math.sin(radian)
        grass.draw_now(400,30)
        character.draw_now(X,Y)

        degree += 1
        delay(0.001)
    degree = 20
    

close_canvas()
