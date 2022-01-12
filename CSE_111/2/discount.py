import math
from datetime import datetime

now = datetime.now() 
current_time = now.strftime("%H:%M")
day = now.day
month = now.month
year = now.year
print(f"Current Time = {current_time}" )
print(f"Current date = {month}/{day}/{year}" )




#gather data from user
# input("Please enter the subtotal: {}")
# input("Sales tax amount: {}")


# #output
# print(f"Total: {}")
