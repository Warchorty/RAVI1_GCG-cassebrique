import pygame
from pygame.math import Vector2
import random
import core



class Brick:
    def __init__(self,largeur=400,hauteur=400):
        self.position = Vector2(random.randint(0,largeur),random.randint(0,hauteur))
        self.dimension = Vector2(5,10)
        self.couleur = (0,0,0)


    def show(self, screen):
        pygame.draw.rect(screen,self.couleur,self.position,self.dimension)