monthly_income = int(input("Enter your monthly income: "))  # monthly_income
monthly_expense = int(
    input("Enter your total monthly expense: ")
)  # total_monthly_expense
monthly_savings = monthly_income - monthly_expense  # monthly savings
rate = 0.05  # simple annual interest rate of 5%
projection = monthly_savings * 12 + (monthly_savings * 12 * rate)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest is: ${int(projection)}.")
