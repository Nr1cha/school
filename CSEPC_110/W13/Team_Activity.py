import os 
os.system("clear")
import math

#==============
#FUNCTIONS
#==============
def compute_area_square(side): #CIRCLE FUNCTION
    return side * side

def compute_area_rectangle(length, width): #CIRCLE FUNCTION
    return length * width 

def compute_area_circle(radius): #CIRCLE FUNCTION
    return math.pi * radius * radius

def compute_area(shape, value1, value2=0):
    area = -1

    if shape == "square":
        area = compute_area_square(value1)
    elif shape == "circle":
        area = compute_area_circle(value1)
    elif shape == "rectangle":
        area = compute_area_rectangle(value1, value2)

    return area

#=============
#LOOP
#=============

shape = ""
while shape != "quit":
    shape = input("What shape do you have? \nSquare, Rectangle or Circle.\n")
    print()
    shape = shape.lower() #CONVERT TO LOWER

    if shape == "square": #SQUARE
        side = float(input("What is the length of the side? "))
        area = compute_area_square(side)
        print(f"The area of your square is {area}")
        print()

    elif shape == "rectangle": # RECTANGLE
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area_rectangle(length, width)
        print(f"The area of your rectangle is {area}")
        print()
            
    elif shape == "circle": #CIRCLE
        radius = float(input("What is the radius? "))
        area = compute_area_circle(radius)
        print(f"The area of your circle is {area}")
        print()

