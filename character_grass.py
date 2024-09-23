from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=90
degree = 20
radius = 20
radian = degree * math.pi / 180
X = 200 + math.cos(radius * math.cos(radian))
Y = 200 + math.sin(radius * math.cos(radian))

while (True):
    while (x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x += 2

    while (y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x-=1.5
        y+=2

    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x-=1.5
        y-=2



close_canvas()
