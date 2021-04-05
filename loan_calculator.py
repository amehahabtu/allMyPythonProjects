'''
Date : 4/4/2021
Programmer Name : Ameha Habtu
Description: This prorgams accepts the loan amount , annual interest rate in percent, monthly installment payment, 
number of the months and return the loan details on monthly basis.
'''
def loan_calculator():      
    principal =float(input("Enter the loan amount: "))
    annual_interest_rate=float(input("Enter annual interest rate in percentage: ")) 
    payment = float(input("Enter your monthly payment to be paid: "))
    months=int(input("Enter the number of months you would like to see the results: ")) 
    monthly_interestrate=annual_interest_rate/100/12
    print("Month\tMonthlyPMT\t\tInterestPaid\t\tPaid_To_Principal       LoanBalance\n")
    for i in range(months):
        interest_paid=principal*monthly_interestrate
        principal=principal+interest_paid   
        if (principal+interest_paid < payment):
            print("The final payment due $",format(principal+interest_paid,',.2f'),end="")
            print("You cleared loan payments in",i+1)
            break
        principal= principal-payment
        print(str(i+1),"\t",format(payment,',.2f'),"\t\t",format(interest_paid,',.2f'),"\t\t",format(payment-interest_paid,',.2f'),"\t\t",format(principal,',.2f'))
def main():
    print("Welcome to LOAN CALCULATOR Application!")
    name=input("Enter your name: ").title()
    print(f'Hello {name}.Please enter the following fields to see your results.')
    answer="Y"
    while(answer=="Y"):
        loan_calculator()
        answer=input("Do you want to do more loan calculation...?(Y/N)").upper()
    print(f'{name},Thank you for using LOAN CALCULATOR program!!!')
main()
