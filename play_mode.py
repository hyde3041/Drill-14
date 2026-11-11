from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from flock import create_flock

boy = None
font = None
birds = []
bird_image = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy, font, birds, bird_image

    boy = Boy()
    font = load_font('ENCR10B.TTF', 24)
    bird_image = load_image('bird_animation.png')
    birds = create_flock(get_canvas_width(), get_canvas_height())
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy, birds, bird_image
    game_world.clear()
    boy = None
    birds = []
    bird_image = None


def update():
    game_world.update()
    for bird in birds:
        bird.update(game_framework.frame_time, get_canvas_width())

def render():
    clear_canvas()
    game_world.render()
    for bird in birds:
        bird.draw(bird_image)
    frame_time = game_framework.frame_time
    fps = 1.0 / frame_time if frame_time > 0 else 0.0
    font.draw(10, 570, f'Frame Time: {frame_time:.4f}s  FPS: {fps:.1f}', (255, 255, 255))
    update_canvas()









