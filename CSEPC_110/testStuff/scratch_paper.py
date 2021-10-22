# user_age = int(input("what is your age? "))
# can_drive = False


# if user_age >= 16:
#     can_drive = True
#     print("nice, you can drive")
# elif user_age == 13:
#     can_drive = True
#     print("you slick cheater. good on ya")
# else:
#     can_drive = False 
#     print("you need to grow up more.")





# Python3 code to demonstrate working of
# Converting String to binary
# Using join() + ord() + format()
  
# initializing string 
test_str = input("what is the text you want to convert to binary? ")
  
# printing original string 
print("The original string is : " + str(test_str))
  
# using join() + ord() + format()
# Converting String to binary
res = ''.join(format(ord(i), '08b') for i in test_str)
  
# printing result 
print("The string after binary conversion : " + str(res))
