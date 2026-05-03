# Create a module called shapes.py with functions to calculate the area of a circle (with radius),
# rectangle(with length and width) and triangle(with length and width). Based on user input,
# determine and show the area of shapes using the user defined module

import math

def circle_area(radius):
    return math.pi*radius*radius

def rectangle_area(length, breadth):
    return length*breadth

def triangle_area(length, width):
    return 0.5*length*width
