import os 
os.system("clear")
import random


user_choice = int(input("How many meal options would you like to choose from? "))


mylist = ['Stir Fry',
'Breakfast',
'Enchiladas',
'Sausage and Potatos',
'Tacos',
'Burgers and fries',
'Pulled Pork',
'BBQ Chicken',
'Spaghetti',
'Curry',
'Jambalaya',
'Chili',
'Ramen',
'Salmon',
'Veggie Kebabs',
'Pork Chops',
'Chicken Noodle Soup',
'Tuscan Chicken Soup',
'Random Recipe from Cookbook',
'Big Salad']
random.shuffle(mylist)
# random_index = random.randrange(len(mylist))

# for number in range(1, user_choice + 1):

result = random.sample(mylist, user_choice)
print("\nYour choices are:\n")
print(f"\n".join(result))




