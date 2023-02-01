# Memory Game, Ryan Kelley, v0.8 -- based on a project by Al Sweigart.  

import pygame, sys, random
from pygame.locals import *

# Game Constants 
FPS = 30 # Set to 30 FPS. 
WINDOWWIDTH = 640 # Measured in Pixels 
WINDOWHEIGHT = 480 # Measured in Pixels 
REVEALSPEED = 8 # How fast the boxes slide to reveal picture. 
BOXSIZE = 40 # Size of box height and width, in pixels. 
GAPSIZE = 10 # Gap between boxes, in pixels. 
BOARDWIDTH = 10 # Number of Columns in Game Board 
BOARDHEIGHT = 7 # Number of Rows in Game Board 
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board must be an even number of boxes for matched pairs.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
