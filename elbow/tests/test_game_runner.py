"""Tests for the generic GameRunner class """
from unittest import TestCase
from elbow import Game, GameRunner

class TestGameRunner(TestCase):
    """ Generic game runner test class """

    game = Game

    def test_init(self):
        self.assertEqual(GameRunner(Game).game, self.game)
        self.assertDictEqual(GameRunner(Game).commands,
                                        {'check_answer' : self.game.check_answer})
