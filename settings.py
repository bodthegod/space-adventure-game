"""
Settings file to allow game to work correctly
"""
import sys
import time


def slowprint(strings):
    """
    Creates slowprint for gameplay aspect
    """
    for text_c in strings + '\n \n':
        sys.stdout.write(text_c)
        sys.stdout.flush()
        time.sleep(1./20)


def won_game():
    """
    Quits game with message to display game is won
    """
    slowprint("You Won \n"
              "To restart, click the orange Run Program button. \n"
              "Quitting...")
    sys.exit()


def exit_game():
    """
    Exits game if user loses and displays loss message
    """
    slowprint("You Lose \n"
              "To try again, click the orange Run Program button. \n"
              "Quitting...")
    sys.exit()
