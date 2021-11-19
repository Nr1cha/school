import os 
os.system("clear")
bank_accounts = []
balances = []

account_name = None

print("Enter the bank_accounts and balances of bank accounts (type: quit when done) ")

# Build the lists
while account_name != "quit":
    account_name = input("What is the name of this account? ")

    if account_name != "quit":
        balance = float(input("What is the balance? "))

        bank_accounts.append(account_name)
        balances.append(balance)

# Display all of the accounts with their balances
# Compute the total at the same time.
Total = 0

print(f"\nAccount Information: ")
for i in range(len(bank_accounts)):
    print(f"{i}. {bank_accounts[i]} - ${balances[i]}")

    Total += balances[i]

average = Total / len(balances)
print()
print(f"Total: ${Total:.2f}")
print(f"Average: ${average:.2f}")



#STRETCH PORTION

# Find the highest balance:
highest_name = None
highest_balance = -1

for i in range(len(bank_accounts)):
    name = bank_accounts[i]
    balance = balances[i]

    if balance > highest_balance:
        # We have a new highest!
        highest_balance = balance
        highest_name = name

print(f"Highest balance: {highest_name} - ${highest_balance:.2f}")

change_account = "yes"

while change_account == "yes":
    change_account = input("\nDo you want to update an account? ")

    if change_account == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))

        balances[index] = new_amount
    
    # Now print the balances
    print("\nAccount Information:")
    for i in range(len(bank_accounts)):
        print(f"{i}. {bank_accounts[i]} - ${balances[i]:.2f}")