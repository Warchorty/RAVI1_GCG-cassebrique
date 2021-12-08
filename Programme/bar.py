import pygame
from pygame.math import Vector2
import random
import core


class Bar:
    def __init__(self,largeur=400,hauteur=400):
        self.position = Vector2(800,300)
        self.dimension = Vector2(5, 10)
        self.couleur = (0, 250, 250)
        self.acc = Vector2()


    def show(self, screen):
        pygame.draw.rect(screen,self.couleur,self.position,self.dimension)


    def deplacement(self,target):