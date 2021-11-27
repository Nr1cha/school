import os 
os.system("clear")

user_choice = None
max_life_expectancy = None
max_life_expectancy_year = None
max_life_expectancy_entity = None
min_life_expectancy = None
min_life_expectancy_year = None
min_life_expectancy_entity = None




min_expectancy = None
min_country1 = None
max_expectancy = None
max_country2 = None




array_expectancy = []

with open("life-expectancy.csv") as life_expectency_file:
    user_choice = input("Enter the year of interest:")
    for line in life_expectency_file:
        if line.startswith("Entity"): continue;
        clean_line = line.split(",")

        entity = clean_line[0]
        code = clean_line[1]
        year = clean_line[2]
        expectency = clean_line[3]

        if user_choice == year:
            array_expectancy.append(float(expectency))





        if user_choice == year and (min_expectancy == None or expectency < min_expectancy):
            min_expectancy = expectency
            min_country1 = entity

        # if user_choice == year and expectency > max_expectancy:
            
        #     max_expectancy = expectency
        #     max_country2 = entity




        if min_life_expectancy == None or expectency < min_life_expectancy:
            min_life_expectancy = expectency
            min_life_expectancy_year = year
            min_country = entity
        
        if max_life_expectancy == None or expectency > max_life_expectancy:
            max_life_expectancy = expectency 
            max_life_expectancy_year = year
            max_country = entity

    life_average_age = sum(array_expectancy) / len(array_expectancy)

    print(f"The overall min life expectancy is: {min_life_expectancy} from {min_country} in {min_life_expectancy_year}")
    print(f"The overall max life expectancy is: {max_life_expectancy} from {max_country} in {max_life_expectancy_year}")
    print()
    print(f"For the year {user_choice}:")
    print(f"The average life expectancy across all countries was {life_average_age:.2f}")




    print(f"The max life expectancy was in {max_country2} with {max_expectancy}")
    print(f"The min life expectancy was in {min_country1} with {min_expectancy}")
