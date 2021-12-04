#Allow the user to type in a country #*DONE
#then #*DONE
#show the minimum, maximum, and average life expectancy for that country.

import os
import cmd
os.system("clear")
cli = cmd.Cmd()
size = os.get_terminal_size()

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
min_life_expectancy = None
max_life_expectancy = None
min_life_expectancy_year = None
max_life_expectancy_year = None
#2ND SET OF DATA
min_expectancy = None
max_expectancy = None
min_country1 = None
max_country2 = None
#3RD SET OF DATA
selected_min_expectancy = None
selected_max_expectancy = None


#========================
#FIRST LOOP
#========================
with open("life-expectancy.csv", encoding="utf-8") as life_expectency_file:
    user_choice = input("Enter the year of interest: ")
    for line in life_expectency_file:
        if line.startswith("Entity"): continue
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

        if user_choice == year and (min_expectancy is None or life_expectency < min_expectancy):
            min_expectancy = life_expectency
            min_country1 = country

        if user_choice == year and (max_expectancy is None or life_expectency > max_expectancy):
            max_expectancy = life_expectency
            max_country2 = country

        #!min portion
        if min_life_expectancy is None or life_expectency < min_life_expectancy:
            min_life_expectancy = life_expectency
            min_life_expectancy_year = year
            min_country = country

        #!max portion
        if max_life_expectancy is None or life_expectency > max_life_expectancy:
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

    print()

    #=========================================
    display_of_countries = list(set(list_of_countries)) #this takes and sorts out into just unique items
    #=========================================
    print("Below are the countries to select from:")

    cli.columnize(display_of_countries, displaywidth=size[0])
    select_country = input("Please select a country from the list: ")
    print()
    array_life_expectancy = []

#========================
#SECOND LOOP
#========================
#if statements
with open("life-expectancy.csv", encoding="utf-8") as life_expectency_file:
    for line in life_expectency_file:
        if line.startswith("Entity"): continue
        clean_line = line.split(",")
        #establishing data
        country = clean_line[0]
        list_of_countries.append(country)
        code = clean_line[1]
        year = clean_line[2]
        life_expectency = float(clean_line[3])

        #user choice stuff
        if select_country == country:
            array_life_expectancy.append(float(life_expectency)) # adding life_expectency to array outside of loop
        # LOGIC STUFF
        if select_country == country and (selected_min_expectancy is None or life_expectency < selected_min_expectancy):
            selected_min_expectancy = life_expectency

        if select_country == country and (selected_max_expectancy is None or life_expectency > selected_max_expectancy):
            selected_max_expectancy = life_expectency

    country_average_age = sum(array_life_expectancy) / len(array_life_expectancy)

    print(f"For the country {select_country}")
    print(f"The average life expectancy for {select_country} is {country_average_age:.2f} ")
    print(f"The max life expectancy is {selected_max_expectancy}")
    print(f"The min life expectancy {selected_min_expectancy}")
