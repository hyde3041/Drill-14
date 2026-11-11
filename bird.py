FRAME_COUNT = 14
ANIMATION_FPS = 14.0

class Bird:
    def __init__(self, x, y, speed, phase=0.0):
        self.x = float(x)
        self.y = y
        self.speed = speed
        self.phase = phase % FRAME_COUNT
        self.direction = 1

    def update(self, dt, width):
        self.phase = (self.phase + ANIMATION_FPS * dt) % FRAME_COUNT
        # Reflect overshoot so speed and position remain correct at an edge.
        left, right = 45.0, width - 45.0
        span = right - left
        progress = self.x - left if self.direction == 1 else 2 * span - (self.x - left)
        progress = (progress + self.speed * dt) % (2 * span)
        if progress < span:
            self.x, self.direction = left + progress, 1
        else:
            self.x, self.direction = right - (progress - span), -1

    def draw(self, image):
        frame = int(self.phase)
        column, row = frame % 5, frame // 5
        # pico2d source coordinates start at the bottom of the image.
        x0, x1 = column * 918 // 5, (column + 1) * 918 // 5
        y0, y1 = 506 - (row + 1) * 506 // 3, 506 - row * 506 // 3
        image.clip_composite_draw(x0, y0, x1 - x0, y1 - y0,
                                  0, 'h' if self.direction < 0 else '',
                                  self.x, self.y, 90, 83)
