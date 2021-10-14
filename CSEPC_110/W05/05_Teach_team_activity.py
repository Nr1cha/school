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

a = A
b = B
c = C
d = D
f = F

grade_percentage = int(input("What is your grade percentage? "))

#SCORE OF 90
if grade_percentage >= 90:
    print("Congradulations, you passed with your score of", grade_percentage,"your grade is", a)
else:
    print("your score was", grade_percentage, "with a bit more practice you can get a passing grade.","\n")

#SCORE OF 80
if grade_percentage >= 80:
    print("Congradulations, you passed with your score of", grade_percentage,"your grade is", b)
else:
    print("your score was", grade_percentage, "with a bit more practice you can get a passing grade.","\n")


#SCORE OF 70
if grade_percentage >= 70:
    print("Congradulations, you passed with your score of", grade_percentage,"your grade is", c)
else:
    print("your score was", grade_percentage, "with a bit more practice you can get a passing grade.","\n")
