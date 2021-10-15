# You need to have at least three levels of scenarios with possible choices.

# At least one of your scenarios must have more than two possible choices.

# In each prompt, write the choices in ALL CAPS, so that the user knows which words are possible responses to choose.

# When checking the users responses, you should match on the keyword, 
# regardless of the uppercase/lowercase used in the response (e.g., "match", "MATCH", "Match" should all work).

# Making different choices should take you to different scenarios. (You shouldn't have the same result for different choices.)

# Choices should only work for the correct question.

# In other words, if one scenario resulted in choices of Run/Hide, 
# but another resulted in choices Follow/Look, you should not be able to respond with "Follow" to the question that asked for Run/Hide.

# A good way to accomplish this is to have a series of nested if statements. 
# (That is, the print and then the next if statement will be within the body/block of the first if statement.)

# For each question, you should provide an "else" clause to handle the case that the user tries to type something other than the possible choices. 
# It is up to you how to handle this case.
#==========================================


#questions
begin = input("Ready to begin? ")
user_name = input("What is your name? ")
user_color1 = input("what is your first favorite color? ")
user_color2 = input("what is your second favorite color? ")
input(f"you see two doors, door number 1 has the color {user_color1} on it, door number 2 has {user_color2} on it, which one do you choose? ")
door_color1 = input("what door will you go through? ")
door_color2 = input("")


#steps
step2 = input("what step will you take? ")
step3 = input("what step will you take? ")
step4 = input("what step will you take? ")
step5 = input("what step will you take? ")
step6 = input("what step will you take? ")
