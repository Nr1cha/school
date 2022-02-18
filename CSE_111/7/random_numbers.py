import random

numbers_list = [16.2, 75.1, 52.3]

def main():
    append_random_number(numbers_list, 67)
    print(f"list of numbers {numbers_list}")


def append_random_number(number_list, quantity = 1): 
    for _ in range (quantity): 
        random_number = random.uniform(0, 100) 
        rounding = round(random_number, 1) 
        number_list.append(rounding)



if __name__ == "__main__":
    main()