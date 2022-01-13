import math
from datetime import datetime

discount_percent = 0.1
sales_tax_percent = 0.06

current_date = datetime.now()
weekday = current_date.weekday()
subtotal = 0
price = None

while price != 0:
    price = float(input("Enter the price: "))
    if price != 0:
        item_num = int(input("Enter the amount of items: "))
        subtotal += price * item_num


if weekday == 1 or weekday == 2:
    if subtotal < 50:
        missing = 50 - subtotal
        print(f"if you would like a discount, buy {missing} worth of items or more.")
    else:
        discount = round(subtotal * discount_percent)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount

sales_tax= round(subtotal * sales_tax_percent, 2)
print(f"Sales tax amount: {sales_tax}")

total = subtotal + sales_tax
print(f"total: {total:.2f}")

# #output
# print(f"Total: {}")
