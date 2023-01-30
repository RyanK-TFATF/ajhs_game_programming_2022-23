# Primitive Drawing, Ryan Kelley, v0.5
import pygame, sys
from pygame.locals import *

pygame.init() 

# Setup Window 
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Primitive Drawing')

# Color Setup 
# COLORNAME = (RedValue, GreenValue, BlueValue) 0 = No Value, 255 = Max Value 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


