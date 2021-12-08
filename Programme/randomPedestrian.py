import random
import pygame
from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    core.memory("origine", Vector2(200, 400))
    core.memory("positionVecteur",Vector2(0,0))
    core.memory("monVecteur",Vector2(0,200))
    core.memory("magnitude",core.memory("monVecteur").magnitude())
    print("Setup END-----------")


def run():

    core.cleanScreen()

    if core.getKeyPressList(276) and core.memory("positionVecteur").x>-190:
        core.memory("positionVecteur", Vector2(core.memory("positionVecteur").x-5, core.memory("positionVecteur").y))
    if core.getKeyPressList(275) and core.memory("positionVecteur").x<190:
        core.memory("positionVecteur", Vector2(core.memory("positionVecteur").x+5, core.memory("positionVecteur").y))

    if core.getKeyPressList(273) and core.memory("positionVecteur").y>-190:
        core.memory("positionVecteur", Vector2(core.memory("positionVecteur").x, core.memory("positionVecteur").y-5))
    if core.getKeyPressList(274) and core.memory("positionVecteur").y<190:
        core.memory("positionVecteur", Vector2(core.memory("positionVecteur").x, core.memory("positionVecteur").y+5))


    pygame.draw.line(core.screen,(255,255,255),core.memory("origine")+core.memory("positionVecteur"),core.memory("origine")+ core.memory("positionVecteur")+Vector2(core.memory("monVecteur").x,-core.memory("monVecteur").y))

core.main(setup, run)