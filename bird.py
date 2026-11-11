class Bird:
    def __init__(self, x, y, speed, phase=0.0):
        self.x = float(x)
        self.y = y
        self.speed = speed
        self.phase = phase
        self.direction = 1
