import matplotlib.pyplot as plot 
import numpy, random


def graphType():
    pass 

def makeHistogram():
    pass

def makeBar():
    # Number of Data Points
    print("+=+=+=+ Bar Graph +=+=+=+\n")    
    print("This program requires an equal number of X and Y data points to plot correctly.\n")
    numPts = int(input("How many data points will you need to plot?  Type an integer value and press enter.\n"))
    count = 0 

    # Title 
    myTitle = input("\nPlease type the TITLE of your scatter plot and press enter.\n")
    plot.title(myTitle)

    # x Related
    labelX = input("\nPlease type the X-AXIS LABEL of your scatter plot and press enter.\n")
    plot.xlabel(labelX)
    xVals = []

    # y Related
    labelY = input("\nPlease type the Y-AXIS LABEL of your scatter plot and press enter.\n")
    plot.ylabel(labelY)
    yVals = []

    # Data Point Entry
    print()    
    print("+=+=+=+ DATA ENTRY +=+=+=+\n")    
    print("\nPlease type the X and Y values for the data points.\nFormat as x, y and then press enter!\n")
    while count < numPts: 
        count += 1
        newVals = input(f"\nType the X and Y values for Data Point {count} and press ENTER.\n").split(',')
        xVals.append(newVals[0])
        yVals.append(newVals[1])
        
    x = numpy.array(xVals)
    y = numpy.array(yVals)

    plot.scatter(x, y, marker="*")
    plot.show()

def makeScatter():
    # Number of Data Points
    print("+=+=+=+ Scatter Plot +=+=+=+\n")    
    print("This program requires an equal number of X and Y data points to plot correctly.\n")
    numPts = int(input("How many data points will you need to plot?  Type an integer value and press enter.\n"))
    count = 0 

    # Title 
    myTitle = input("\nPlease type the TITLE of your scatter plot and press enter.\n")
    plot.title(myTitle)

    # x Related
    labelX = input("\nPlease type the X-AXIS LABEL of your scatter plot and press enter.\n")
    plot.xlabel(labelX)
    xVals = []

    # y Related
    labelY = input("\nPlease type the Y-AXIS LABEL of your scatter plot and press enter.\n")
    plot.ylabel(labelY)
    yVals = []

    # Data Point Entry
    print()    
    print("+=+=+=+ DATA ENTRY +=+=+=+\n")    
    print("\nPlease type the X and Y values for the data points.\nFormat as x, y and then press enter!\n")
    while count < numPts: 
        count += 1
        newVals = input(f"\nType the X and Y values for Data Point {count} and press ENTER.\n").split(',')
        xVals.append(newVals[0])
        yVals.append(newVals[1])
        
    x = numpy.array(xVals)
    y = numpy.array(yVals)

    plot.scatter(x, y, marker="*")
    plot.show()