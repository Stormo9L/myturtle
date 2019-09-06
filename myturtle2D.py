from turtle import *
from colorsys import *
from time import *

#Majority of color programming done by dad

def drawsquare(length):
    sidesquare = 0
    while sidesquare < 4:
        forward(length)
        right(90)
        sidesquare += 1

def draweqtriangle(length):
        sidetriangle = 0
        while sidetriangle < 3:
                forward(length)
                right(120)
                sidetriangle += 1

def drawhexagon(length):
        sidehexagon = 0
        while sidehexagon < 6:
                forward(length)
                right(60)
                sidehexagon += 1

def drawfunkysquare(iterations):
        for i in range(iterations):
                drawsquare(100)
                pencolor(hls_to_rgb(i/iterations, .5, .7))
                left(360/iterations)

def drawstar(length, point):
        x = 0
        if (point % 2) == 0:
                raise ValueError("Even Numbers not allowed")
        while x < point:
                forward(length)
                right(180 - (180/point))
                x += 1

def drawfunkystar(length, points, iterations):    
        for i in range(iterations):
                pencolor(hls_to_rgb(i/iterations, .5, .7))
                drawstar(length, points)
                right(360/iterations)
speed(0)
drawfunkystar(200, 4, 17)
sleep(5)