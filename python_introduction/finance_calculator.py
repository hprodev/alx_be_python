income = int(input("Enter your monthly income: "))  # monthly_income
expense = int(input("Enter your total monthly expense: "))  # total_monthly_expense
savings = income - expense  # monthly savings
rate = 0.05  # simple annual interest rate of 5%
projection = savings * 12 + (savings * 12 * rate)

print(f"Your monthly savings are ${savings}")
print(f"Projected savings after one year, with interest is: ${int(projection)}.")
