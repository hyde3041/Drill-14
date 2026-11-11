import unittest
from unittest.mock import Mock
from bird import Bird, FRAME_COUNT
from flock import create_flock


class FlightTests(unittest.TestCase):
    def test_flock_has_ten_birds(self):
        self.assertEqual(len(create_flock(1600, 600)), 10)

    def test_reflection_preserves_overshoot(self):
        bird = Bird(1545, 200, 100)
        bird.update(0.2, 1600)
        self.assertAlmostEqual(bird.x, 1545)
        self.assertEqual(bird.direction, -1)

    def test_large_step_stays_inside_bounds(self):
        bird = Bird(45, 200, 100)
        bird.update(1000, 1600)
        self.assertTrue(45 <= bird.x <= 1555)

    def test_animation_wraps_and_flips(self):
        bird = Bird(100, 200, 0, FRAME_COUNT - 0.5)
        bird.direction = -1
        bird.update(0.1, 1600)
        self.assertTrue(0 <= bird.phase < FRAME_COUNT)
        image = Mock()
        bird.draw(image)
        self.assertEqual(image.clip_composite_draw.call_args.args[5], 'h')


if __name__ == '__main__':
    unittest.main()
