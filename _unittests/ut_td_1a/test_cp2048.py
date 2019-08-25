"""
@brief      test log(time=1s)
"""
import unittest
from ensae_teaching_cs.td_1a.cp2048 import Game2048


class TestCp2048(unittest.TestCase):

    def test_2048(self):
        game = Game2048.create_game()
        self.assertEqual(game.game.shape, (4, 4))
        game.next_turn()
        s = str(game)
        self.assertIn('[', s)
        r = game.process_line([0, 2, 2, 4])
        self.assertEqual(r, [8, 0, 0, 0])

        game = Game2048.create_game()
        for i in range(0, 5):
            game.next_turn()
            direction = i % 4
            game.play(direction)
        self.assertEqual(game.game.shape, (4, 4))

    def test_random_2048(self):
        game = Game2048.create_game()
        scores = list(game.evaluate_strategy())
        self.assertEqual(len(scores), 10)
        self.assertGreater(min(scores), 4)


if __name__ == "__main__":
    unittest.main()
