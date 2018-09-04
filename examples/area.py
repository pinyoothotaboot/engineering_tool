import sys
sys.path.append("..")

from engineering_tool.areas import *

def Area_All():

    radius = 15.6  
    base   = 20
    wide   = 30
    height = 40

    circle = Area.circle(radius)
    rectangle = Area.rectangle(base,height)
    square = Area.square(base)
    triangle = Area.triangle(base,height)
    parallelogram = Area.parallelogram(wide,height)
    trapezoid = Area.trapezoid(base,wide,height)

    print("Areas.....")
    print("Circle = %.3f"%circle)
    print("Rectangle = %.3f"%rectangle)
    print("Square = %.3f"%square)
    print("Triangle = %.3f"%triangle)
    print("Parallelogram = %.3f"%parallelogram)
    print("Trapezoid = %.3f"%trapezoid)


Area_All()


