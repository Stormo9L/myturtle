from turtle import *
def drawaxis():
    tracer(0, 0)
    forward(250)
    home()
    left(90)
    forward(250)
    home()
    right(90)
    forward(250)
    home()
    right(180)
    forward(250)
    home()
def findpoint(slope, yintercept):
    penup()
    forward(500)
    if 1 / slope > 0:
        left(90)
        forward(slope * 500)
    else:
        right(90)
        forward(abs(slope) * 500)
    pendown()
    goto(0, yintercept)

def drawline(yintercept, slope):
    goto(0, yintercept)
    seth(180)
    findpoint(slope, yintercept)
    seth(0)
    findpoint(slope, yintercept)
    update()

drawaxis()
drawline(50, -5)
mainloop()