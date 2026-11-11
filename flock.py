from bird import Bird


def create_flock(width, height):
    # Two rows keep all ten birds visible without stacking them at one point.
    return [Bird(width * (0.12 + (i % 5) * 0.18),
                 height * (0.35 + (i // 5) * 0.35),
                 85 + (i % 5) * 7, i * 1.4)
            for i in range(10)]
