numbers = [42, 25, 18, 83, 23, 85, 38, 2]

largest_number_so_far = numbers[0]

for number in numbers:
    if number > largest_number_so_far:
        largest_number_so_far = number
print(f"The largest number is: {largest_number_so_far}")