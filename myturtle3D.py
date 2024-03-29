from turtle import *
cornerlist = []

def shapemaker(length, sides):
    sidecount = 0
    while sidecount < sides:
        forward(length)
        henryright(sides)
        sidecount += 1

# compute the interior angle of a regular polygon with
# 'sides' sides
def interiorangle(sides):
    return ((sides - 2)*180)/sides

def henryright(sides):
    x, y = pos()
    cornerlist.append((x,y))
    right(180 - interiorangle(sides))

def prismmaker(length, depth, sides):
    shapemaker(length, sides)
    for corner in cornerlist:
        penup()
        goto(corner)
        pendown()
        seth(45)
        forward(depth)
    pendown()
    seth(0)
    shapemaker(length, sides)

#Argument 1 is the length of each side of the face, argument 2 is how far out the prism goes
#argument 3 is how many sides the face has.
prismmaker(50, 150, 21)