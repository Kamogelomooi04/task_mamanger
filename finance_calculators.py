#the import math at the top of the program helps us use mathematical functions in python.
import math

#some information here to inform the user on what to do.
#As well as some options for the user to choose from.
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print()
print("investment      - to calculate the amount of interest youl'll earn on interest.")
print("bond            - to calculate the amount you'll have to pay on a home loan.")
print()

calculation_type = input(": ")
print()

#This is the beginning of the conditional satements.
#Depending on the option the user picks the program will decide on a path to follow.
#After the program decides on a path it will ask the user a series of questions related to the option chosen.
#We use the input() funtion to take in the user input.
#The user input is then stored in the varibales below.
if calculation_type == "investment" or calculation_type  == "Investment" or calculation_type == "INVESTMENT":
    investment_p = float(input("What is the amount of money that you are depositing?  \nR"))
    investment_r = float(input("Enter the interest rate (as a percentage). Just enter the number.: \n"))
    investment_r2 = ((investment_r)/ 100)
    investment_r = investment_r2
    investment_t = int(input("Enter the number of years you plan on investing for.: \n"))
    interest = input("Enter whether you'd like 'simple' or 'compound' interest.: \n")

#Here we have a conditional statement inside of another conditional statement.
#Here once again we give the program the chance to decide on a path for us depending on the option the user chooses.
#We use conditional statements to achieve this.    
#If the user  chooses 'simple', the program will calculate the total amount using the simple interest formula.
#If the user chooses 'compound', the program will calculate the total amount using the compound interest formula.
#The program will then display the results of the calculation to the user.    
    if interest == "Simple" or interest == "simple" or interest == "SIMPLE":
        simple_interest = investment_p *(1 + investment_r * investment_t)
        print("The Total amount once the interest has been applied is R{}".format(format(simple_interest, ".2f")))

    elif interest ==  "Compound" or interest == "compound" or interest == "COMPOUND":
        compound_interest = investment_p* math.pow((1 + investment_r),investment_t)
        print("The total amount once the interest has been applied is R{}".format(format(compound_interest, ".2f")))

    else:
        print("Please make sure you have entered the correct option. Either 'simple' or 'compound'.")
        
#Here is another conditional statement linked to the main one at the top on the program.
#Here depending on which option the user chose at the top the program will ask th user these series of questions.
#The input() function is put into use here again as we do need to get some user input.
#The user input is then stored in the virables named below.
#The program will execute a calculation using the user input.
#Then the program will display the results of the calculation to the user.        
elif calculation_type == "bond" or calculation_type == "Bond" or calculation_type == "BOND":
    present_value_of_house = float(input("Eenter the present value of the house.: \nR"))
    bond_interest = float(input("Enter the interest rate (as a percentage). Just enter the number.: \n"))
    bond_interest2 = ((bond_interest)/ 12)
    bond_interest = bond_interest2
    bond_months = int(input("Enter the number of months you plan on taking to repay the bond.: \n"))
    bond_repayment = (bond_interest* present_value_of_house)/ (1- (1+ bond_interest)**(-bond_months))
    print("You will have to repay R{} each month.".format(format(bond_repayment, ".2f")))

else:
    print("Please make sure you have entered the correct option. Either 'investment' or 'bond'.")
    
