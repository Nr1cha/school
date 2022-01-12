'''
Write a Python program named tire_volume.py 
that reads from the keyboard the three numbers for a tire 
and 
computes 
and 
outputs the volume of space inside that tire.
'''
# Import that math module
import math
import os
os.system("clear")

# print description of what this program is going to do. 
print("this program will calculate the volume of your tire.")
print()
user_choice = None
# user_choice = input("would you like to run the program? (y/n)")
# nest the program in an if statement
while user_choice != "n":
    # get width, aspect, and diameter from the user.
    os.system("clear")
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    # compute the volume of the tire
    tire_volume = (math.pi * width**2 * aspect * (width * aspect + 2540 * diameter)) / 10000000000
    # round to the 2nd decimal place
    tire_volume = round(tire_volume, 2)
    #output the result
    print(f"The approximate volume is {tire_volume} liters")
    user_choice = input("would you like to run the program? (y/n)")

    # if user_choice == "y"
print("thanks for testing my program")
