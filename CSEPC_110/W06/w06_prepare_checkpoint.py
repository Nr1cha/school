#1 - 10
print("for each of the following questions, provide a 1-10 rating:","\n")
loan_size = float(input("how large is the loan? "))
credit_history = float(input("how good is your credit history? "))
income = float(input("how high is your income? "))
down_payment = float(input("how large is your down payment? "))
should_loan = False

#create a boolean variable
if loan_size >= 5:
    if credit_history and income >= 7:
        should_loan = True
    elif credit_history or income >= 7:
        if down_payment >= 5: 
            should_loan = True
        else:
            should_loan = False 
    else:
        should_loan = False
            
else:
#the otherwise part
    if credit_history < 4:
        should_loan = False
    else:
        if income or down_payment >= 7:
            should_loan = True
        elif income and down_payment >=4:
            should_loan = True
        else:
            should_loan = False
if should_loan:
    print("the decision is yes. this is a good loan.")
else:
    print("the decision is no. you should not loan this money.")