# Memory Game, Ryan Kelley, v1.4 -- based on a project by Al Sweigart.  

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

# Colors 
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

# Define Shapes 
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for number of shapes/colors defined."

def main(): 
    global FPSCLOCK, DISPLAYSURF # global keyword allows the variable to be accessed by any other function. 
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    # Mouse Cursor Location 
    mousex = 0 
    mousey = 0 

    # Game Caption 
    pygame.display.set_caption('Memory Game')

    # Board Setup 
    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None # Store the (x, y) coordinates of the first box that is clicked. 

    # Fill in Board Background and Start Animation 
    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True: 
        mouseClicked = False # Tracks whether mouse has been clicked. 

        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION: # Scan for motion of the mouse. 
                mousex, mousey = event.pos 
            elif event.type == MOUSEBUTTONUP: 
                mousex, mousey = event.pos
                mouseClicked = True 
        
        boxx, boxy = getBoxAtPixel(mousex, mousey) # Determine location of the box that was clicked. 
        if boxx != None and boxy != None: # If both are None, there was a box under the mouse. 
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked: 
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True # Mark the box as being revelead. 
                if firstSelection == None: # Check if this the first box to be clicked. 
                    firstSelection = (boxx, boxy)
                else: # The current box is the second box if we get to the else: block. 
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color: # Check for shape and color matches. 
                        pygame.time.wait(1000) # Value is in milliseconds. 
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1], (boxx, boxy))])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False 
                    elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        # Reset the Board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        # Reveal the Board for 1 Second
                        drawBoard(mainboard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Replay Star Game Animation 
                        starGameAnimation(mainBoard)
                    firstSelection = None
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generateReaveledBoxesData(val): 
    revealedBoxes = [] # Create an empty list of revealed boxes. 
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes

def generateRandomizedBoard():
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape, color))

    random.shuffle(icons) # Randomize, aka shuffle, the list of icons. 
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # Calculate number of icons needed. 
    icons = icons[:numIconsUsed] * 2 # Create two of each icon used. 

    # Create the Board and Randomly Place Icons 
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] # Remove icon after adding, so we don't double up. 
        board.append(column)
    return board 


    
