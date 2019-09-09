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
def drawline(slope, yintercept):
    for i in range(2):
        goto(0, yintercept)
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
        if 1 / slope > 0:
            right(270) 
        else:
            right(90)
        update()

drawaxis()
drawline(4, 70)
mainloop()