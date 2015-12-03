"""Base class for a game"""
import shlex

class Game(object):
    """
    Base class for a game from which other games inherit. Inheriting games must
    override the following attributes/methods:

    Attributes:

       - answer: The player must enter this to "win"
       - prompt: This will be displayed to the player when prompting for
                 input - tell them what to do!

    Methods:

       - give_hint: This method takes the players, current guess and must return
                    a string (even if its empty) giving them a clue on how to improve
                    an incorrect answer.


    """

    # Attributes
    answer = True
    prompt = "No prompt"

    # "Public" methods - inheriting classes should override these to define their game
    def give_hint(self, answer):
        """
        This function should be overidden by inheriting classes to give feedback
        to the user about how they can improve their answer.

        Returns a String.
        """
        return ""

    def check_answer(self, guess):
        """
        If this method isn't the overloaded for more complex game types
        then we just look to see if guess = answer
        """
        if guess == str(self.answer):
            return "Congratulations you win!"
        else:
            return "Incorrect\n%s" % self.give_hint(guess)

    # "Private" methods - inheriting classes shouldn't touch these

class GameRunner(object):
    """
    Base game runner class this should be inherited by other game runner classes.

    It is responsible for managing the commands that are associated with a game
    and handling user input etc.
    """

    def __init__(self, game):
        self.game = game
        self.commands = {}
        self.add_command("check_answer", game.check_answer)

    def add_command(self, name, func):
        """
        This adds commands to the runner, these will be available as commands
        to the user when they play the game
        """
        self.commands[name] = func

    def run(self, line):
        """
        Given a line to execute this method parses it and looks to see if the command is
        defined, if so execute it.
        """
        tokens = shlex.split(line)
        command, args = tokens[0], tokens[1:]

        # Assume any non-command is a guess
        if command not in self.commands:
            result = self.commands['check_answer'](command)
        else:
            result = self.commands[name](*args)

        if result is not None:
            print(result)
