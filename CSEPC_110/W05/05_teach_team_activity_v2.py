story = ""
yes_no = ""
user_response = input("Would you like to play a short game? ")

if user_response.lower().strip() == "yes":
    user_response = input("you reach")
    story = "your in a deep forest"
elif user_response.lower() == "no":
    story = "ok, goodby"
else:
    story = "please type (yes/no)"
# print(f"Your grade is: {letter}")

#=======================

# print(f"Your letter grade is: {letter}")

# if grade_percentage >= 70:
#     print("Congratulations! You passed the class!")
# else:
#     print("Keep going, you got this")
