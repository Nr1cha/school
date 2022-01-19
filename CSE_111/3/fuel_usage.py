def main():
    # Get an odometer value in U.S. miles from the user.

    # Get another odometer value in U.S. miles from the user.

    # Get a fuel amount in U.S. gallons from the user.

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.

    # Display the results for the user to see.


    first_reading = float(input("Enter the first odometer reading (miles): " ))
    second_reading = float(input("Enter the second odometer reading (miles): " ))
    fuel_used = float(input("Enter the amount of fuel used (gallons): " ))

    #output
    mpg = miles_per_gallon(first_reading,second_reading,fuel_used)
    lp100k = lp100k_from_mpg(mpg)
    print(f"{mpg:.2f} miles per gallon. ")
    print(f"{lp100k:.2f} liters per 100 kilometers. ")

#words that are in the parameters of a function, must be used later int he function body
def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg = abs(end_miles - start_miles) / amount_gallons

    return mpg

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """

    liters_per100k = 235.215 / mpg

    return liters_per100k
# Call the main function so that
# this program will start executing.
main()


