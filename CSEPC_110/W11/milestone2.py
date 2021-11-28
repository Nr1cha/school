import os 
os.system("clear")

u = "\033[4m"
b = "\033[1m"
i = "\033[3m"
Black = "\u001b[30m"
Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Reset = "\u001b[0m"


user_choice = None
max_life_expectancy = None
max_life_expectancy_year = None
max_life_expectancy_entity = None
min_life_expectancy = None
min_life_expectancy_year = None
min_life_expectancy_entity = None
#2nd data
min_expectancy = None
min_country1 = None
max_expectancy = None
max_country2 = None
#array
array_expectancy = []

with open("life-expectancy.csv") as life_expectency_file:
    user_choice = input("Enter the year of interest: ")
    for line in life_expectency_file:
        if line.startswith("Entity"): continue;
        clean_line = line.split(",")
#positions
        entity = clean_line[0]
        code = clean_line[1]
        year = clean_line[2]
        expectency = float(clean_line[3])
#if statements
        if user_choice == year:
            array_expectancy.append(float(expectency)) # adding expectency to array outside of loop
# LOGIC STUFF
        if user_choice == year and (min_expectancy == None or expectency < min_expectancy):
            min_expectancy = expectency
            min_country1 = entity

        if user_choice == year and (max_expectancy == None or expectency > max_expectancy):
            max_expectancy = expectency
            max_country2 = entity

        if min_life_expectancy == None or expectency < min_life_expectancy:
            min_life_expectancy = expectency
            min_life_expectancy_year = year
            min_country = entity
        
        if max_life_expectancy == None or expectency > max_life_expectancy:
            max_life_expectancy = expectency 
            max_life_expectancy_year = year
            max_country = entity

    life_average_age = sum(array_expectancy) / len(array_expectancy)

    print(f"The overall min life expectancy is: {Green}{min_life_expectancy}{Reset} from {u}{min_country}{Reset} in {Cyan}{min_life_expectancy_year}{Reset}")
    print(f"The overall max life expectancy is: {Green}{max_life_expectancy}{Reset} from {u}{max_country}{Reset} in {Cyan}{max_life_expectancy_year}{Reset}")
    print("")
    print(f"For the year {Cyan}{user_choice}{Reset}:")
    print(f"The average life expectancy across all countries was {Green}{life_average_age:.2f}{Reset}")
    print(f"The max life expectancy was in {u}{max_country2}{Reset} with {Green}{max_expectancy:.2f}{Reset}")
    print(f"The min life expectancy was in {u}{min_country1}{Reset} with {Green}{min_expectancy:.2f}{Reset}")
