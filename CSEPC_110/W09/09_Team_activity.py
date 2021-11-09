list_of_numbers = []
print("Enter a list of numbers, type 0 when finished. ")
Enter_number = "Enter a number: "
Number = None
#loop stuff
while Number != 0:
    Number = int(input(Enter_number))
    if Number != 0:
        list_of_numbers.append(Number)
print()
print("your numbers are: ")
for numbers in list_of_numbers:
    print(numbers)
