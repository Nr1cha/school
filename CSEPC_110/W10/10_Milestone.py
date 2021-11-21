import os
os.system("clear")
shopping_cart = []
choices = [1,2,3,4,5]
user_choice = None
prices = []
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
        item_cost = float(input(f"What is the price of '{item}'? "))
        prices.append(item_cost)
        shopping_cart.append(item)
        print(f"{item} has been added to the cart.")


    if user_choice == 2:
        print(f"The contents of the shopping cart are: ")
        for i in range(len(shopping_cart)):
            print(f"{i+1}. {shopping_cart[i]} - ${prices[i]:.2f}")


    if user_choice == 3:
        for i in range(len(shopping_cart)):
            print(f"{i+1}. {shopping_cart[i]}")

        choice_remove = int(input("Which item would you like to remove? "))

        if choice_remove > len(shopping_cart) or choice_remove <= 0:
            print("Sorry, that is not a valid item number. ")
            
        else:
            last_item = shopping_cart[choice_remove - 1]
            shopping_cart.pop(choice_remove - 1)
            prices.pop(choice_remove -1)
            print(f"{last_item} removed.")


    if user_choice == 4:
        total = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total}")


print("Thank you. Goodbye.")