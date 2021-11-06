import os
import math
os.system("clear")


user_input = int(input("how many columns and rows do you want in your multiplication table? "))
max_number = user_input * user_input
digits = int(math.log(max_number)) + 1


range_size = user_input + 1

for row_number in range(1, range_size):
    for col_number in range(1, range_size):
        number = row_number * col_number
        print(f"{number:{digits}}", end=" ")
    print()
