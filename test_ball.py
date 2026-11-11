import unittest
from unittest.mock import patch

import game_framework
import game_world
from ball import Ball


class BallTests(unittest.TestCase):
    def setUp(self):
        game_world.clear()
        self.addCleanup(game_world.clear)
        self.enterContext(patch('ball.load_image'))
        self.enterContext(patch('ball.get_canvas_width', return_value=1600))
        self.enterContext(patch.object(Ball, 'images', {}))
        self.enterContext(patch.object(game_framework, 'frame_time', 0.0))

    def advance(self, ball, seconds, steps):
        game_framework.frame_time = seconds / steps
        for _ in range(steps):
            ball.update()

    def test_flight_is_independent_of_frame_rate(self):
        slow = Ball(400, 90, 1)
        fast = Ball(400, 90, 1)
        self.advance(slow, 1.0, 30)
        self.advance(fast, 1.0, 144)
        self.assertAlmostEqual(slow.x, fast.x)
        self.assertAlmostEqual(slow.y, fast.y)
        self.assertAlmostEqual(slow.velocity_y, fast.velocity_y)
        self.assertAlmostEqual(slow.x, 700)
        self.assertAlmostEqual(slow.y, 226.6666666667)

    def test_both_directions_rise_then_fall(self):
        for direction in (-1, 1):
            with self.subTest(direction=direction):
                ball = Ball(800, 90, direction)
                self.advance(ball, 0.5, 30)
                self.assertGreater(ball.y, 90)
                self.assertGreater(ball.velocity_y, 0)
                self.assertAlmostEqual(ball.x, 800 + direction * 150)
                raised_y = ball.y
                self.advance(ball, 1.0, 60)
                self.assertLess(ball.velocity_y, 0)
                self.assertLess(ball.y, raised_y)

    def test_ground_contact_uses_each_ball_size(self):
        for ball_type, radius in ((1, 10.5), (2, 20.5)):
            with self.subTest(ball_type=ball_type):
                ball = Ball(800, 40 + radius + 1, 1, ball_type)
                ball.velocity_y = -100
                game_world.add_oject(ball)
                self.advance(ball, 0.02, 1)
                self.assertNotIn(ball, game_world.world[1])

    def test_removal_waits_until_ball_is_fully_off_screen(self):
        for ball_type, radius in ((1, 10.5), (2, 20.5)):
            for edge, direction in ((0, -1), (1600, 1)):
                with self.subTest(ball_type=ball_type, direction=direction):
                    ball = Ball(edge, 200, direction, ball_type)
                    game_world.add_oject(ball)
                    self.advance(ball, radius / 600, 1)
                    self.assertIn(ball, game_world.world[1])
                    self.advance(ball, radius / 300, 1)
                    self.assertNotIn(ball, game_world.world[1])


if __name__ == '__main__':
    unittest.main()
