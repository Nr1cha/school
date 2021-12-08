import math

# Write a program to compute the areas of three different shapes. 
# Prompt for the necessary information, then compute and display the area, as follows:
# Make sure that your program can appropriately handle decimal values as well as whole numbers.

# 01 Square—The area is the length of a side squared.
# 02 Rectangle—The area is the length multiplied by the width.
# 03 Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.


#square stuff
def compute_area_square():
    square_length = int(input("What is the length of a side of the square? "))
    area_of_square = square_length ** square_length
    return square_length


#rectangle stuff
def compute_area_rectangle():
    rectangle_length = int(input("What is the length of a side of the rectangle? "))
    rectangle_width = int(input("what is the width of the rectangle? "))
    area_of_rectangle = rectangle_length * rectangle_width
    return rectangle_length, rectangle_width


#circle stuff
def compute_area_circle():
    radius = int(input("What is the radius of the circle? "))
    area_of_circle = math.pi * (radius * radius)
    return radius




#===============================
#float items
#===============================

#square stuff
square_length = float(input("What is the length of a side of the square? (in cm) "))
area_of_square = square_length ** square_length
print(f"The area of the square is: ",area_of_square,"cm^2",'\n')


#rectangle stuff
rectangle_length = float(input("What is the length of a side of the rectangle? (in cm) "))
rectangle_width = float(input("what is the width of the rectangle? (in cm) "))
area_of_rectangle = rectangle_length * rectangle_width
print(f"The area of the rectangle is: ",area_of_rectangle,"cm^2",'\n')


#circle stuff
radius = float(input("What is the radius of the circle? (in cm) "))
area_of_circle = math.pi * (radius * radius)
print(f"The area of the circle is:",area_of_circle,"cm^2",'\n')


#===============================
#4outputs from 1 input
#===============================
print('==============================================')
print('last section')
print('==============================================','\n')

value = float(input('give me a number...'))

area_for_square = value * value
area_for_circle = math.pi * (value * value)
volume_of_cube = value ** 3
volume_of_sphere = (4 / 3) * math.pi * (value ** 3)



#square stuff
print(f"The area of the square is: ",area_for_square,"cm^2",'\n')

#circle stuff
print(f"The area of the square is: ",area_for_circle,"cm^2",'\n')

#cube stuff
print(f"The area of the square is: ",volume_of_cube,"cm^2",'\n')

#sphere stuff
print(f"The area of the square is: ",volume_of_sphere,"cm^2",'\n')
