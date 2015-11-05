"""
This module contains the REPL. It is repsonsible for

    - TODO: Choose a random game to play
    - TODO: Prompt the user for their input
    - TODO: Pass user input and replies to/from the currently loaded game class
"""
from elbow.games import GuessMyNumber, GameRunner
from sys import exit, stdin
import code


class REPL(object):
    """
    This class implements the REPL for Project Elbow
    """
    def __init__(self, game_runner):
        self.game_runner = game_runner

    def run_game(self, file_d):
        """
        Given a file descriptor file_d for a given input stream,
        for each line in that input stream, pass that comand to the game and
        run it.
        """
        for line in file_d:
            self.game_runner.run(line)

    def interact(self, locals=None):
        class LambdaConsole(code.InteractiveConsole):
            def runsource(code_console, source, filename=None, symbol=None):
                try:
                    self.game_runner.run(source)
                except SystemExit:
                    raise
                except:
                    code_console.showtraceback()

        try:
            import readline; readline
        except ImportError:
            pass

        LambdaConsole(locals=locals, filename="<repl>").interact(banner='')

    def run_repl(self, file_d=None, interact=False):
        if file_d is None:
            file_d = stdin

        if file_d.isatty():
            self.interact()

        self.run_game(file_d)



def main(file_d = None):
    """
    Get everything going, eventually this is where the random game selection will come
    from.
    """
    game = GuessMyNumber()
    game_runner = GameRunner(game)
    return REPL(game_runner).run_repl(file_d)

if __name__ == '__main__':
    exit(main())
