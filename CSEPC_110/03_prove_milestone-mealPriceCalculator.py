# Determine the meal's subtotal (before adding sales tax)
# by 
# multiplying the number of children by the price of their meal,
# and 
# multiplying the number of adults by the price of their meal 
# and 
# adding those two values together.
#------------
#Compute and display the sales tax, 
# by 
# multiplying the subtotal by the sales tax rate divided by 100.
#------------
#Compute and display the total price of the meal 
# by 
# adding the subtotal and the sales tax.



#INPUT PORTION
childs_meal_float = float(input("what is the price of a child's meal? "))
adults_meal_float = float(input("The price of an adult's meal? "))
number_of_children = int(input("The number of children? "))
number_of_adults = int(input("The number of adults? "))
sales_tax_rate = float(input("what is the sales tax rate? "))



#MATH LOGIC
#-----------------
subtotal = number_of_children * childs_meal_float + number_of_adults * adults_meal_float
sales_tax = subtotal * sales_tax_rate / 100
total_price_of_meal = subtotal + sales_tax
#-----------------

# OUTPUT
print("childs meal subtotal$",number_of_children * childs_meal_float)
print("adult meal subtotal$",number_of_adults * adults_meal_float)
print("Subtotal: $",subtotal)
print("sales tax$",sales_tax )
print("meals total including sales tax$",total_price_of_meal)

user_input_amount = float(input("what is the payment amount? "))
print("change: $", user_input_amount - total_price_of_meal)