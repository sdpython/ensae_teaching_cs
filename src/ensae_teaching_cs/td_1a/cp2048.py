"""
@file
@brief Simple strategy for 2048.
"""
import random
import numpy


class GameOverException(Exception):
    """
    Raised when the game is over.
    """
    pass


class Game2048:
    """
    Implements the logic of the game :epkg:`2048`.
    """

    def __init__(self, game):
        """
        :param game: matrix 4x4
        """
        self.game = game

    def __str__(self):
        "Displays the game as a string."
        return str(self.game)

    def gameover(self):
        "Checks the game is over or not. Returns True in that case."
        return numpy.ma.masked_not_equal(self.game, 0).count() == 0

    def copy(self):
        "Makes a copy of the game."
        return Game2048(self.game.copy())

    def next_turn(self):
        "Adds a number in the game."
        if self.gameover():
            raise GameOverException("Game Over\n" + str(self.game))
        else:
            while True:
                i = random.randint(0, self.game.shape[0] - 1)
                j = random.randint(0, self.game.shape[1] - 1)
                if self.game[i, j] == 0:
                    n = random.randint(0, 3)
                    self.game[i, j] = 4 if n == 0 else 2
                    break

    @staticmethod
    def create_game():
        "Creates an empty matrix."
        return Game2048(numpy.zeros((4, 4), dtype=int))

    @staticmethod
    def process_line(line):
        """
        Moves numbers inside a vector whether this vector represents
        a row or a column.

        .. runpython::
            :showcode:

            from ensae_teaching_cs.td_1a.cp2048 import Game2048
            print(Game2048.process_line([0, 2, 2, 4]))
        """
        res = []
        for n in line:
            if n == 0:
                # Zero: skipped.
                continue
            if len(res) == 0:
                # First number: add.
                res.append(n)
            else:
                prev = res[-1]
                if prev == n:
                    # The number is identical: combine.
                    res[-1] = 2 * n
                else:
                    # Otherwise: add.
                    res.append(n)
        while len(res) < len(line):
            res.append(0)
        return res

    def play(self, direction):
        "Updates the game after a direction was chosen."
        if direction == 0:
            lines = [Game2048.process_line(self.game[i, :])
                     for i in range(self.game.shape[0])]
            self.game = numpy.array(lines)
        elif direction == 1:
            lines = [Game2048.process_line(self.game[:, i])
                     for i in range(self.game.shape[1])]
            self.game = numpy.array(lines).T
        elif direction == 2:
            lines = [list(reversed(Game2048.process_line(self.game[i, ::-1])))
                     for i in range(self.game.shape[0])]
            self.game = numpy.array(lines)
        elif direction == 3:
            lines = [list(reversed(Game2048.process_line(self.game[::-1, i])))
                     for i in range(self.game.shape[1])]
            self.game = numpy.array(lines).T

    def best_move(self):
        """
        Selects the best move knowing the current game.
        By default, selects a random direction.
        This function must not modify the game.
        """
        return random.randint(0, 3)

    def score(self):
        "Returns the maximum values."
        return numpy.max(self.game)

    def evaluate_strategy(self, ntries=10):
        """
        Applies method *best_move* until gameover
        starting from the current position. Repeats *ntries* times
        and the maximum number in every try.
        """
        for i in range(0, ntries):
            g = self.copy()
            while True:
                try:
                    g.next_turn()
                except GameOverException:
                    break
                d = g.best_move()
                g.play(d)
            yield g.score()
