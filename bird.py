class Bird:
    def __init__(self, x, y, speed, phase=0.0):
        self.x = float(x)
        self.y = y
        self.speed = speed
        self.phase = phase
        self.direction = 1

    def update(self, dt, width):
        # Reflect overshoot so speed and position remain correct at an edge.
        left, right = 45.0, width - 45.0
        span = right - left
        progress = self.x - left if self.direction == 1 else 2 * span - (self.x - left)
        progress = (progress + self.speed * dt) % (2 * span)
        if progress < span:
            self.x, self.direction = left + progress, 1
        else:
            self.x, self.direction = right - (progress - span), -1
