

    
                        

import math
# Request user input

menu = input("Choose either 'investment' or 'bond' from the menu below to proceed:\n" "investment - to calculate the amount of interest you'll earn on interest\n" "bond - to calculate the amount you'll have to pay on a homeloan \n")

if menu == "Investment".lower() or menu == "Investment".upper():

# Request investment's inputs for calculations
    deposit = int(input("Enter the deposit amount: "))
    interest_rate = float(input("Enter the interest rate: "))
    period = int(input("Enter the investment period: "))
    interest = input("simple or compound: ")


# Investment's simple interest calculation
    if interest.lower() == "simple":
        simple_interest = deposit*(1+interest_rate*period)
        print("The total investment will be : ",simple_interest)

# Investment's compound interest calculation
    elif interest.lower() == "compound":
        compound_interest = deposit*(1+(interest_rate))**period
        print("The total investment will be : ", compound_interest)
    print("Thank you")

elif menu == "Bond".lower() or menu == "Bond".upper():
 
# Request bond's inputs for calculations
    present_value = int(input("Enter the present value: "))
    interest_rate = float(input("Enter the interest rate: "))
    period = int(input("Enter the number of months to repay the bond: "))

# Bond's monthly repayment calculation
    repayment = (interest_rate*present_value)/(1-(1+interest_rate)**(-period))
    print("Bond monthly repayment will be :", repayment)

    print("Thank you")

                    
elif menu != "Investment" and menu != "Bond":
    print("You have entered an invalid input. Please enter the valid entry")






















               
    
