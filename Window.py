import turtle


def drawASquare(xCoordinate, yCoordinate, lengthOfSide):
    turtle.penup()
    turtle.goto(xCoordinate, yCoordinate)
    turtle.pendown()
    turtle.pensize(7)
    turtle.pencolor('yellow')
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(lengthOfSide)
        turtle.right(90)
    turtle.end_fill()

def drawAWindow(xCoordinate, yCoordinate, lengthOfSide):
    sides_of_window = 4
    for i in range(sides_of_window):
        drawASquare(xCoordinate, yCoordinate, lengthOfSide)
        turtle.left(90)

drawAWindow(0,0,100)
drawAWindow(250,100,100)
drawAWindow(-250,100,100)

def isEven(side):
    return side % 2 == 0

def drawADoor(xCoordinate, yCoordinate, widthOfDoor, heightOfDoor):
    turtle.penup()
    turtle.goto(xCoordinate, yCoordinate)
    turtle.pendown()
    turtle.pensize(4)
    turtle.pencolor('white')
    turtle.fillcolor('red')
    turtle.begin_fill()
    number_of_sides = 4
    for side in range(number_of_sides):
        if isEven(side):
            turtle.forward(widthOfDoor)
        else:
            turtle.forward(heightOfDoor)
            turtle.right(90)

drawADoor(-100,-50,50,100)
turtle.mainloop()

def moveATurtle(xCoordinate, yCoordinate):
    turtle.penup()
    turtle.goto(xCoordinate, yCoordinate)
    turtle.pendown()

def drawAFacade(xCoordinate, yCoordinate, breadth, height):
    turtle.penup()
    moveATurtle(xCoordinate, yCoordinate)
    turtle.pensize(5)
    turtle.pencolor('red')
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    number_of_sides = 4
    for side in range(number_of_sides):
        if isEven(side):
            turtle.forward(breadth)
        else:
            turtle.forward(height)

        turtle.right(90)

turtle.end_fill()

drawAFacade(-300,300,200,400)

def drawABuilding(facadeX, facadeY, facadeBreadth, facadeHeight):
    drawAFacade(facadeX, facadeY, facadeBreadth, facadeHeight)

    facadeMargin = facadeBreadth/10
    doorBreadth = facadeBreadth/4
    doorHeight = facadeHeight/4
    drawADoor(facadeX + facadeMargin, facadeY,
    facadeHeight + doorHeight, doorBreadth, doorHeight)
    
    drawABuilding(-500,300,300,600)
