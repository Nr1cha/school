#1 Defining Functions
def print_message():
    #code here
    print("hello Nick!")

#2 Calling Functions
print_message()

#calling function again
print_message()

#3 Passing Parameters to Functions
def print_double(value):
    double_value = value * 2
    print(double_value)

print_double(16) #calling the function

#4 Returning Values (this doesn't print anything to the screen)
def get_double(value):
    double_the_value = value * 2
    return double_the_value

#5 Variable Scope
def print_the_message(the_message):
    the_message = "Message 1"
    print_the_message(the_message)
    user_message = "message 2"
    print_the_message(user_message)

    print_the_message()