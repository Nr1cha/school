
print("This program is an implementation of the Rosenberg")
print("Self-Esteem Scale. This program will show you ten")
print("statements that you could possibly apply to yourself.")
print("Please rate how much you agree with each of the")
print("statements by responding with one of these four letters:")
print()
print("D means you strongly disagree with the statement.")
print("d means you disagree with the statement.")
print("a means you agree with the statement.")
print("A means you strongly agree with the statement.")

Q1 = input(f"I feel that I am a person of worth, at least on anequal plane with others Enter D, d, a, or, A:")
Q2 = input(f"I feel that I have a number of good qualities.Enter D, d, a, or A:")
Q3 = input(f"All in all, I am inclined to feel that I am a failure.Enter D, d, a, or A:")
Q4 = input(f"I am able to do things as well as most other people.Enter D, d, a, or A:")
Q5 = input(f"I feel I do not have much to be proud of.Enter D, d, a, or A:")
Q6 = input(f"I take a positive attitude toward myself.Enter D, d, a, or A:")
Q7 = input(f"On the whole, I am satisfied with myself.Enter D, d, a, or A:")
Q8 = input(f"I wish I could have more respect for myself.Enter D, d, a, or A:")
Q9 = input(f"I certainly feel useless at times.Enter D, d, a, or A:")
Q10 = input(f"At times I think I am no good at all.Enter D, d, a, or A:")

def add_user_input(): 
    
    print()

print(f"Your score is")
print(f"A score below 15 may indicate problematic low self-esteem.")