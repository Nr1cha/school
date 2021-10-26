import random

number = random.randint(1, 100)
# print(number)


#VARIABLES
# magicNumber = int(input("what is the magic number? "))
userGuess = int(input("what is your guess? "))

#LOGIC PORTION
while userGuess != number:
    if userGuess < number:
        print("Higher")
        userGuess = int(input("please guess a higher number ")) 
    elif userGuess > number:
        print("Lower")
        userGuess = int(input("please guess a lower number ")) 
print(f"you guessed correct {number}, CONGRATS!! ")
