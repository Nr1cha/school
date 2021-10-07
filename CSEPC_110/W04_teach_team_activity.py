import math
# Prompt the user for each of the variables described above.

# Compute the value for the inner value c which is computed as:

# c = (1 / 2) * p * A * C

# Display the value c to three decimal places.

# Compute and display the overall velocity. Display the value to three decimal places.`

#WELCOME
print("Welcome to the velocity calculator. Please enter the following: ","\n")

#GATHER INPUT
Mass = int(input("Mass (in kg): "))
Gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
Time = int(input("Time (in seconds): "))
Density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water):  "))
Cross_sectional_Area = float(input("Cross sectional area (in m^2): "))
Drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "),"\n")

#RESULT
inner_value_of_c = float(input("The inner value of c is: "))
velocity = float(input("The velocity after 10.0 seconds is: ", "m/s"))
#
#
#
#MATH STUFF
m = Mass

g = Gravity

t = Time

p = Density

A = Cross_sectional_Area

C = Drag_constant

c = (1/2) * p * A * C

exp = the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).

sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).