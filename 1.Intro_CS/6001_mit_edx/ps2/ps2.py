
# Problem 1 - Paying Debt off in a Year

# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# monthlyInterestRate = annualInterestRate / 12.0

# month = 0
# while month < 12:
#     month += 1
#     minMonthlyPayment = balance * monthlyPaymentRate
#     monthlyUnpaidPaymemt = balance - minMonthlyPayment
#     interest = monthlyUnpaidPaymemt * monthlyInterestRate
#     balance = round(monthlyUnpaidPaymemt + interest, 2)
    
# print("Remaining balance:", balance)



# Problem 2 - Paying Debt Off in a Year

# balance = 3329
# annualInterestRate = 0.2

# monthlyInterestRate = annualInterestRate / 12.0

# monthlyPayment = 0

# check_balance = 0

# while check_balance < balance:
#     monthlyPayment += 10
#     check_balance = 0
#     month = 0
#     while month < 12:
#         month += 1
#         check_balance += monthlyPayment - check_balance * monthlyInterestRate
    
# print(monthlyPayment)



# Problem 3 - Using Bisection Search to Make the Program Faster

balance = 320000
annualInterestRate = 0.2

left = balance / 12
right = (balance * (1 + annualInterestRate / 12.0)**12) / 12.0
monthlyPayment = (left + right) / 2
epsilon = 0.01
attempt = balance

while abs(attempt) >= epsilon:
    attempt = balance
    month = 1    
    while month <= 12:
        unpaid_balance = attempt - monthlyPayment
        attempt = unpaid_balance + (annualInterestRate / 12.0) * unpaid_balance
        month += 1

    if attempt > 0:
        left = monthlyPayment
    else:
        right = monthlyPayment
    monthlyPayment = (left + right) / 2

print("Lowest payment: " + str(round(monthlyPayment, 2)))
