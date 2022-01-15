"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python
program named boxes.py that asks the user for two integers:  1) the
number of manufactured items and 2) the number of items that the user
will pack per box. Your program must compute and print the number of
boxes necessary to hold the items. This must be a whole number. Note
that the last box may be packed with fewer items than the other boxes.
"""
import math
import os 
os.system("clear")

#ask the user for numbers
items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

#math portion
num_boxes = math.ceil(items / items_per_box)

#output
print()
print(f"For {items} items, packing {items_per_box} items in each box, you will need {num_boxes} boxes.")
