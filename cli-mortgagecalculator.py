import math

def calculate_monthly_payment(principal, interest_rate, num_terms):
    n = num_terms * 12
    r = interest_rate / 12 / 100
    monthly_payment = principal * (r / (1 - math.pow(1 + r, -n)))
    return monthly_payment

def calculate_total_interest_and_amount_paid(principal, monthly_payment, num_terms):
    n = num_terms * 12
    total_amount_paid = monthly_payment * n
    total_interest_paid = total_amount_paid - principal
    return total_interest_paid, total_amount_paid

def main():
    print("Mortgage Calculator v0.01")
    principal = float(input("Enter the principal amount of the loan: "))
    interest_rate = float(input("Enter the annual interest rate in percentage: "))
    num_terms = int(input("Enter the number of terms (years): "))

    monthly_payment = calculate_monthly_payment(principal, interest_rate, num_terms)
    total_interest_paid, total_amount_paid = calculate_total_interest_and_amount_paid(principal, monthly_payment, num_terms)

    print(f"Monthly Payment: ${monthly_payment:,.2f}")
    print(f"Total Interest Paid: ${total_interest_paid:,.2f}")
    print(f"Total Amount Paid: ${total_amount_paid:,.2f}")

if __name__ == "__main__":
    main()

