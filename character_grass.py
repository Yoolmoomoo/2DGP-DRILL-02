from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
while (x < 800):
    # 렌더링
    # 상호작용의 결과를 그린다
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    
    # 게임 로직
    # 객체의 상호작용을 시뮬레이션
    x = x+2
    
    delay(0.01)

close_canvas()
