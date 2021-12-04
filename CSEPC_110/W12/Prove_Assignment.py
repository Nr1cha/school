# //TODO
#Allow the user to type in a country #*DONE
#then #*DONE
#show the minimum, maximum, and average life expectancy for that country.

import os 
os.system("clear")

u = "\033[4m"
b = "\033[1m"
Green = "\u001b[32m"
Blue = "\u001b[34m"
Cyan = "\u001b[36m"
Reset = "\u001b[0m"

array_life_expectancy = []
list_of_countries = [] # list of all country entries
#1ST SET OF VARIABLES
user_choice = None
max_life_expectancy = None
max_life_expectancy_year = None
max_life_expectancy_entity = None
min_life_expectancy = None
min_life_expectancy_year = None
min_life_expectancy_entity = None
#2ND SET OF DATA
min_expectancy = None
min_country1 = None
max_expectancy = None
max_country2 = None


#========================
#SECOND LOOP VARIABLES
#========================

#1ST SET OF DATA
user_choice = None
max_life_expectancy = None
max_life_expectancy_year = None
max_life_expectancy_entity = None
min_life_expectancy = None
min_life_expectancy_year = None
min_life_expectancy_entity = None
#2ND SET OF DATA
min_expectancy = None
min_country1 = None
max_expectancy = None
max_country2 = None


with open("../W11/life-expectancy.csv") as life_expectency_file:
    user_choice = input("Enter the year of interest: ")
    for line in life_expectency_file:
        if line.startswith("Entity"): continue;
        clean_line = line.split(",")
#establishing data
        country = clean_line[0]
        list_of_countries.append(country)
        code = clean_line[1]
        year = clean_line[2]
        life_expectency = float(clean_line[3])
#if statements
        if user_choice == year:
            array_life_expectancy.append(float(life_expectency)) # adding life_expectency to array outside of loop

        if user_choice == year and (min_expectancy == None or life_expectency < min_expectancy):
            min_expectancy = life_expectency
            min_country1 = country

        if user_choice == year and (max_expectancy == None or life_expectency > max_expectancy):
            max_expectancy = life_expectency
            max_country2 = country


    #!min portion
        if min_life_expectancy == None or life_expectency < min_life_expectancy:
            min_life_expectancy = life_expectency
            min_life_expectancy_year = year
            min_country = country
    #!max portion        
        if max_life_expectancy == None or life_expectency > max_life_expectancy:
            max_life_expectancy = life_expectency 
            max_life_expectancy_year = year
            max_country = country




    #=========================================
    display_of_countries = list(set(list_of_countries)) #this takes and sorts out into just unique items
    #=========================================
    print(f"Below are the countries to select from:")
    print(f"{display_of_countries}")
    select_country = input("Please select a country from the list: ")
    print()
#SECOND LOOP
    for line in life_expectency_file:
        if line.startswith("Entity"): continue;
        clean_line = line.split(",")
#positions
        country = clean_line[0]
        code = clean_line[1]
        year = clean_line[2]
        life_expectency = float(clean_line[3])
#if statements
        if user_choice == year:
            array_life_expectancy.append(float(life_expectency)) # adding life_expectency to array outside of loop
# LOGIC STUFF
        if user_choice == year and (min_expectancy == None or life_expectency < min_expectancy):
            min_expectancy = life_expectency
            min_country1 = country

        if user_choice == year and (max_expectancy == None or life_expectency > max_expectancy):
            max_expectancy = life_expectency
            max_country2 = country

        if min_life_expectancy == None or life_expectency < min_life_expectancy:
            min_life_expectancy = life_expectency
            min_life_expectancy_year = year
            min_country = country
        
        if max_life_expectancy == None or life_expectency > max_life_expectancy:
            max_life_expectancy = life_expectency 
            max_life_expectancy_year = year
            max_country = country






    life_average_age = sum(array_life_expectancy) / len(array_life_expectancy)

    print(f"The overall min life expectancy is: {Green}{min_life_expectancy}{Reset} from {u}{min_country}{Reset} in {Cyan}{min_life_expectancy_year}{Reset}")
    print(f"The overall max life expectancy is: {Green}{max_life_expectancy}{Reset} from {u}{max_country}{Reset} in {Cyan}{max_life_expectancy_year}{Reset}")
    print("")
    print(f"For the year {Cyan}{user_choice}{Reset}:")
    print(f"The average life expectancy across all countries was {Green}{life_average_age:.2f}{Reset}")
    print(f"The max life expectancy was in {u}{max_country2}{Reset} with {Green}{max_expectancy:.2f}{Reset}")
    print(f"The min life expectancy was in {u}{min_country1}{Reset} with {Green}{min_expectancy:.2f}{Reset}")


    print(f"For the country {select_country}")
    print(f"The average life expectancy for {select_country} is {Green}{life_average_age:.2f}{Reset}")
    print(f"The max life expectancy  ")
    print(f"The min life expectancy ")
