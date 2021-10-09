# Write a program to convert from Fahrenheit to Celsius. 
# Display the result to one decimal place of precision.

# To convert degrees in Fahrenheit to Celsius you need to 
# subtract 32 from the Fahrenheit amount 
# then 
# multiply it by the fraction 5/9.


user_input = int(input("what is the temperature in Fahrenheit? "))
step1 = user_input - 32
temperature = step1 * 5 / 9

print(f"the temperature in Celsius is",round(temperature,1),"degrees")

