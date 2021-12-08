import pygame
from pygame.math import Vector2
import random
import core



class Ball:
    def __init__(self,largeur=400,hauteur=400):
        self.position = Vector2(400, 200)
        self.rayon = 5
        self.couleur = (255, 0, 0)
        self.vel = Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
        self.acc = Vector2()



    def show(self, screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.taille)