import os
os.system("clear")


#instructions for creating a function
#1 IDENTIFY THE INPUTS
#2 IDENTIFY THE OUTPUTS
#3 FIND A NAME THAT RELATES TO THE I/O

#01 
#Write a function to calculate and return the wind chill based on a given temperature and wind speed.
def Calculate_wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed**0.16) + 0.4275 * temperature * (wind_speed**0.16)
    
    return wind_chill

input_temperature = 8
input_windspeed = 5
output = Calculate_wind_chill(input_temperature, input_windspeed)

print(f"At temperature {input_temperature}F, and windspeed {input_windspeed} mph, the windchill is:  {output:.2f}F")




def C_to_F_Conversion(Celsius):
    Fahrenheit = (Celsius * (9 / 5)) + 32

    return Fahrenheit




# celcius_input = 79
# Temp_output = C_to_F_Conversion(celcius_input)
# print(f"{celcius_input} degrees celcius is {Temp_output:.2f} degrees Fahrenheit")



#PRINT QUESTIONS
user_temp = float(input("What is the temperature? "))
temp_type = input("Fahrenheit or Celsius (F/C)? ")

if temp_type.lower() == "f":
    print(f"the temperature is: {user_temp} Degrees Fahrenheit.") #INPUT Fahrenheit DATA
elif temp_type.lower() == "c":
    Temperature_Fah = C_to_F_Conversion(user_temp)
    print(f"the new temperature is: {Temperature_Fah} Degrees Fahrenheit.")
