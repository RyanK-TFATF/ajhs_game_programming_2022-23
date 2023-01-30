# Hello World with PyGame, Ryan Kelley, v0.2

import pygame, sys 
from pygame.locals import * 

pygame.init() # .init() is short for INITIALIZE.  
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello, World!')

