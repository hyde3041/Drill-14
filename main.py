import time
from pathlib import Path
from pico2d import (SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE, clear_canvas,
                    close_canvas, get_events, load_image, open_canvas, update_canvas)
from flock import create_flock

WIDTH, HEIGHT = 1600, 600


def main():
    open_canvas(WIDTH, HEIGHT)
    try:
        image = load_image(str(Path(__file__).resolve().parent / 'bird_animation.png'))
        birds = create_flock(WIDTH, HEIGHT)
        previous = time.perf_counter()
        running = True
        while running:
            for event in get_events():
                if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                    running = False
            if not running:
                break
            now = time.perf_counter()
            dt, previous = now - previous, now
            for bird in birds:
                bird.update(dt, WIDTH)
            clear_canvas()
            for bird in birds:
                bird.draw(image)
            update_canvas()
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
