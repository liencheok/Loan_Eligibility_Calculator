import os
import sys
os.system('cls') 

# List to store loan calculations
loan_calculations = []

def calculate_monthly_installment(principal, annual_interest_rate, loan_term):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = loan_term * 12
    monthly_installment = (
        principal * monthly_interest_rate
    ) / (1 - (1 + monthly_interest_rate) ** -num_payments)
    return monthly_installment

def calculate_total_amount_payable(monthly_installment, loan_term):
    return monthly_installment * loan_term * 12

def calculate_dsr(monthly_income, monthly_commitments):
    return (sum(monthly_commitments) / monthly_income) * 100

def main_menu():
    print("\n1. Calculate a new loan")
    print("2. Display all previous loan calculations")
    print("3. Exit")

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def input_positive_float(prompt):
    while True:
        value = input_float(prompt)
        if value > 0:
            return value
        else:
            print("Please enter a positive number.")

def calculate_loan():
    print("\nCalculate a new loan:")
    principal = input_positive_float("Enter the principal loan amount: RM")
    annual_interest_rate = input_positive_float("Enter the annual interest rate (%): ")
    loan_term = input_positive_float("Enter the loan term in years: ")
    monthly_income = input_positive_float("Enter the applicant's monthly income: RM")

    # Additional monthly financial commitments
    other_commitments = input_positive_float("Enter any other monthly financial commitments: RM")
    total_monthly_commitments = [other_commitments]

    monthly_installment = calculate_monthly_installment(principal, annual_interest_rate, loan_term)
    total_amount_payable = calculate_total_amount_payable(monthly_installment, loan_term)
    
    print(f"\nMonthly Instalment: RM{monthly_installment:.2f}")
    print(f"Total Amount Payable: RM{total_amount_payable:.2f}")

    # Calculate DSR
    total_monthly_commitments.append(monthly_installment)
    dsr = calculate_dsr(monthly_income, total_monthly_commitments)

    print(f"Debt Service Ratio (DSR): {dsr:.2f}%")

    # Check eligibility based on DSR
    if dsr <= 70:
        print("Loan Eligibility: Approved")
    else:
        print("Loan Eligibility: Denied")

    # Store loan details in the list
    loan_calculations.append({
        'Principal RM:': principal,
        'Interest Rate (%):': annual_interest_rate,
        'Loan Term (in years)': loan_term,
        'Monthly Income RM': monthly_income,
        'Monthly Instalment RM': monthly_installment,
        'Total Amount Payable RM': total_amount_payable,
        'DSR: (%)': dsr,
    })

def display_previous_calculations():
    print("\nDisplaying all previous loan calculations:")
    for idx, loan in enumerate(loan_calculations, start=1):
        print(f"\nCalculation {idx}:")
        for key, value in loan.items():
            print(f"{key}: {value}")
            

def main():
    while True:
        main_menu()
        choice = input("\nEnter your choice (1, 2, or 3): ")

        if choice == '1':
            calculate_loan()
        elif choice == '2':
            display_previous_calculations()
        elif choice == '3':
            print("Thank you for using this program. See you next time!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
