from cgitb import reset
from datetime import datetime



def main():
    # Formatting
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


    gender = input('What is your gender: (f / m): ')
    birth_str = input('What is your brithday in this format: YYYY-MM-DD: ')
    pounds = float(input('What is your weight in pounds? '))
    height = float(input('What is your height in inches? '))

    # Call the compute_age function to
    # compute the user's age in years.
    years = compute_age(birth_str)

    # Call the kg_from_lb function to
    # convert from pounds to kilograms.
    kilograms = kg_from_lb(pounds)

    # Call the cm_from_in function to
    # convert from inches to centimeters.
    centimeters = cm_from_in(height)

    # Call the body_mass_index function.
    bmi = body_mass_index(kilograms, centimeters)

    # Call the basal_metabolic_rate function.
    bmr = int(basal_metabolic_rate(gender, kilograms, centimeters, years))

    print(f"Age (years): {b}{years}{Reset}")
    print(f'Weight (kg): {Blue}{kilograms:.2f}{Reset}')
    print(f'Height (cm): {Blue}{centimeters:.1f}{Reset}')
    print(f'Body mass index: {Green}{bmi:.1f}{Reset}')
    print(f'Basal metabolic rate (kcal/day): {Green}{bmr}{Reset}')
    

def compute_age(birth_str):
    # Convert a person's birthdate from a string to a date object
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(weight):
    #Convert lbs to kilograms
    kilograms = weight * 0.45359237
    return kilograms

def cm_from_in(height):
    #convert inches to centimeters
    centimeters = height * 2.54
    return centimeters

def body_mass_index(weight, height):
    #compute BMI
    bmi = weight / (height ** 2) * 10000
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    #conpute BMR
    if gender.lower() == "f":
        bmr =  447.593 + 9.247  * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 13.397 * weight + 4.799 * height - 5.677 * age + 88.362
    return bmr
main()