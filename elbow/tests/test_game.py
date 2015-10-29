"""Test for the generic game class"""
from unittest import TestCase
from elbow import Game


class TestGame(TestCase):
    """Generic test class"""
    game = Game
    prompt = "No prompt"

    def test_init(self):
        self.assertTrue(self.game().answer)
        self.assertEqual(self.game().prompt, self.prompt)
