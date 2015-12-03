from elbow.games import Game, GameRunner
from random import randint

class GuessMyNumber(Game):
    """
    A simple guess my number game, chooses a number between 1-100 asks the player
    to guess what number it is thinking of. The player wins when the correct number
    has been guessed.
    """
    answer = randint(1,100)
    prompt = "I am thinking of a number bewtween 1 and 100, what is it? "

    def give_hint(self, answer):
        """
        This function gives feedback to the player saying if their answer was too
        low or too high.
        """
        if int(answer) < self.answer:
            return "Your guess was too low"
        else:
            return "Your guess was too high."
