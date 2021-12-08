import brick
import ball
import bar

import core
from pygame.math import Vector2


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [800, 600]


    print("Setup END---------")

def run():

    print(core.getkeyPressValue())


    """1073741904 clique gauche"""
    """1073741903 clique droit"""

core.main(setup, run)