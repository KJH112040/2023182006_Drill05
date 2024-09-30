from pico2d import *

open_canvas()

tuk = load_image('TUK_GROUND.png')
sheet = load_image('retro-character-sprite-sheet.png')

def handle_events():
    global run, dir, frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            run = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                run = False
            elif event.key == SDLK_DOWN:
                dir = 3
            elif event.key == SDLK_UP:
                dir = 0
            elif event.key == SDLK_LEFT:
                dir = 1
            elif event.key == SDLK_RIGHT:
                dir = 2

run = True;
frame = 1
dir = 3
pos_x = 800//2
pos_y = 600//2

while run:
    clear_canvas()
    tuk.draw(400,300,800,600)
    sheet.clip_draw(frame*188//4,dir*245//4,188//4,245//4,pos_x,pos_y,70,80)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    delay(0.05)

close_canvas()
