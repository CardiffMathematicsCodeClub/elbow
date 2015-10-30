from elbow.games import Game
from random import randint

class GuessMyNumber(Game):
    """
    A simple guess my number game, chooses a number between 1-100 asks the player
    to guess what number it is thinking of. The player wins when the correct number
    has been guessed.
    """
    answer = randint(1,100)
    prompt = "I am thinking of a number bewtween 1 and 100, what is it? "
