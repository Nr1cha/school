import os
os.system("clear")
list_of_numbers = []
print("Enter a list of numbers, type 0 when finished. ")
Enter_number = "Enter a number: "
Number = None
#loop stuff
while Number != 0:
    Number = float(input(Enter_number))
    if Number != 0:
        list_of_numbers.append(Number)

#variables
total = sum(list_of_numbers)
average = sum(list_of_numbers) / len(list_of_numbers)
largest = max(list_of_numbers)
string_ints = [str(int) for int in list_of_numbers]
sorted_list = sorted(list_of_numbers)
sorted_string = [str(int) for int in sorted_list]

#output
print()
print("your sorted list is:\n","\n""".join(sorted_string))
print(f"your numbers are: {total:2}")
print(f"your average is: {average:2}")
print(f"your max number you entered is: {largest:2}")

# for numbers in list_of_numbers:
#     print(numbers)
# list_of_numbers.sort()
# print(list_of_numbers)


#==========================================================
# Have the user 
# enter both positive and negative numbers
# then 
# find the smallest positive number (the positive number that is closest to zero).

# Sort the numbers in the list
# and 
# display the new, sorted list. 
# Hint: There are python libraries that can help you here, try searching the internet for them.