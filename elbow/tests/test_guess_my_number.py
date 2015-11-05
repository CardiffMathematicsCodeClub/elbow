""" Tests for the GuessMyNumber game"""
from .test_game import TestGame
from elbow.games import GuessMyNumber

class TestGuessMyNumber(TestGame):

    game = GuessMyNumber
    prompt = "I am thinking of a number bewtween 1 and 100, what is it? "
