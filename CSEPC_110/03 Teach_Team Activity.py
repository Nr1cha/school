import math

# Write a program to compute the areas of three different shapes. 
# Prompt for the necessary information, then compute and display the area, as follows:
# Make sure that your program can appropriately handle decimal values as well as whole numbers.

# 01 Square—The area is the length of a side squared.
# 02 Rectangle—The area is the length multiplied by the width.
# 03 Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.


#square stuff
square_length = int(input("What is the length of a side of the square? "))
area_of_square = square_length ** square_length
print(f"The area of the square is: ",area_of_square,'\n')


#rectangle stuff
rectangle_length = int(input("What is the length of a side of the rectangle? "))
rectangle_width = int(input("what is the width of the rectangle? "))
area_of_rectangle = rectangle_length * rectangle_width
print(f"The area of the rectangle is: ",area_of_rectangle,'\n')


#circle stuff
radius = int(input("What is the radius of the circle? "))
area_of_circle = math.pi * (radius * radius)
print(f"The area of the circle is:",area_of_circle,'\n')




#===============================
#float items
#===============================
print('==============================================')
print('this is going to be the results as a decimal')
print('==============================================','\n')

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
#float items
#===============================


print('==============================================')
print('this is going to be the results as a decimal')
print('==============================================','\n')


#cube stuff
square_length = float(input("What is the length of a side of the square? (in cm) "))
area_of_square = square_length ** 3
print(f"The area of the square is: ",area_of_square,"cm^2",'\n')