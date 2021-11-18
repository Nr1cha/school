import os
os.system("clear")
shopping_cart = []
choices = [1,2,3,4,5]
user_choice = None
print("Welcome to the Shopping Cart Program!")


while user_choice != 5:
    print()
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    print()
    user_choice = int(input("Please enter an option: "))
    if user_choice == 1:
        item = input("What item would you like to add? ")
        shopping_cart.append(item)
        print(f"{item} has been added to the cart.")
    if user_choice == 2:
        print("\n".join(shopping_cart))
print("Thank you. Goodbye.")
