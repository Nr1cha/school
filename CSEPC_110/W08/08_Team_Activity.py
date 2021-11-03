
user_table = int(input("How many columns and rows do you want in your multiplication table? "))

for number in range(0, user_table):
    print(number + 1, end=" ")
    for number in range(0, user_table):
        print(number + 1)