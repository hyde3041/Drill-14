from pico2d import close_canvas, open_canvas

WIDTH, HEIGHT = 1600, 600

def main():
    open_canvas(WIDTH, HEIGHT)
    try:
        pass
    finally:
        close_canvas()

if __name__ == '__main__':
    main()
