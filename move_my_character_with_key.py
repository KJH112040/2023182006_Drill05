from pico2d import *

open_canvas()

tuk = load_image('TUK_GROUND.png')
sheet = load_image('retro-character-sprite-sheet.png')

def handle_events():
    global run
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            run = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                run = False

run = True;

while run:
    clear_canvas()
    tuk.draw(400,300,800,600)
    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()
