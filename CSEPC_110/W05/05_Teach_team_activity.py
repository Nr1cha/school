# A >= 90
# B >= 80
# C >= 70
# D >= 60
# F < 60

# Ask the user for their grade percentage, 
# then 
# write a series of if-elif-else statements to print out the appropriate letter grade. 
# (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)

# Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out. 
# Add a separate if statement to determine if the user passed the course
# if so 
# display a message to congratulate them. 
# If not 
# display a different message to encourage them for next time.

# Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block, 
# instead 
# create a new variable called letter and 
# then 
# in each block, set this variable to the appropriate value. 
# Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once

grade_percentage = int(input("What is your grade percentage? "))
letter = ""
sign = ""
last_digit = grade_percentage % 10

if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"
print(f"Your grade is: {letter}")

#=======================

if grade_percentage >= 70:
    print("Congrats, you passed the course!")
else:
    print("keep going, you got this")

# stretch challenge 1

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

# Stretch Challenge 2
if grade_percentage >= 93:
    sign = ""

# Stretch Challenge 3
if letter == "F":
    sign = ""

print(f"Your letter grade is: {letter}{sign}")

if grade_percentage >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Keep going, you got this")
