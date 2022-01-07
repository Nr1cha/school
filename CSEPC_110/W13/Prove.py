import os
os.system("clear")

#instructions for creating a function
#1 IDENTIFY THE INPUTS
#2 IDENTIFY THE OUTPUTS
#3 FIND A NAME THAT RELATES TO THE I/O

def Calculate_wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed**0.16) + 0.4275 * temperature * (wind_speed**0.16)

    return wind_chill


def C_to_F_Conversion(Celsius):
    Fahrenheit = (Celsius * (9 / 5)) + 32

    return Fahrenheit

#PRINT QUESTIONS
user_temp = float(input("What is the temperature? "))
temp_type = input("Fahrenheit or Celsius (F/C)? ")

#WHILE LOOP
for windspeed in range(5,65,5):
    #STATEMENTS
    if temp_type.lower() == "f":
        print(f"At temperature {user_temp}F, and windspeed {windspeed} mph, the windchill is: {Calculate_wind_chill(user_temp,windspeed):.2f}F")
    elif temp_type.lower() == "c":
        Temperature_Fah = C_to_F_Conversion(user_temp)
        print(f"At temperature {Temperature_Fah:.1f}F, and windspeed {windspeed} mph, the windchill is: {Calculate_wind_chill(Temperature_Fah,windspeed):.2f}F")
