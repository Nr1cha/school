from calendar import c, week
import math
from datetime import datetime
import os
from statistics import mode 
os.system("clear")
current_date = datetime.now()

print("this program will calculate the volume of your tire.")
print()
user_choice = None
with open("volumes.txt", mode="at") as volumes:

# nest the program in a while loop
    while user_choice != "n":    # get width, aspect, and diameter from the user.

        os.system("clear")
        width = int(input("Enter the width of the tire in mm (ex 205): "))
        aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
        diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
        # current_date = datetime.now()
        
        # compute the volume of the tire
        tire_volume = (math.pi * width**2 * aspect * (width * aspect + 2540 * diameter)) / 10000000000
        # round to the 2nd decimal place
        tire_volume = round(tire_volume, 2)
        
        #output
        print(current_date.strftime("%Y-%m-%d"), width, aspect, diameter, tire_volume, sep=", ", file=volumes)
        user_choice = input("would you like to run the program? (y/n)")

    print(f"thanks for testing my program")
