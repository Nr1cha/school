# If the first number is greater than the second, 
# print "The first number is greater". 
# Otherwise, print "The first number is not greater".



# If the two numbers are equal 
# print "The numbers are equal". 
# Otherwise, print "The numbers are not equal".



# If the second number is greater than the first. 
# print "The second number is greater". 
# Otherwise, print "The second number is not greater".


first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

#FIRST PART
if first_number > second_number:
    print("The first number is greater",first_number,"\n")
else: 
    print ("The first number is not greater", first_number, "<", second_number,"\n")



#SECOND PART
if first_number == second_number:
    print("The numbers are equal.", first_number, "==", second_number,"\n")
else:
    print("The numbers are not equal.",first_number,"!==", second_number,"\n")


#THIRD PART
if second_number > first_number:
    print("The second number is greater.", second_number, ">", first_number,"\n")
else:
    print("The second number is not greater.",second_number,"<",first_number,"\n")


#=============================
favorite_color = input("What is your favorite color? ")
if favorite_color.lower() == "blue":
    print("That's awesome! My favorite color is also", favorite_color)
else:
    print(favorite_color, "is not my favorite color")