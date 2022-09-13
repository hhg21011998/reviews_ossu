<<<<<<< HEAD

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
annual_interest_rate = 0.2

monthly_interest_rate = (annual_interest_rate) / 12.0

monthly_payment_lower_bound = balance / 12
monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0

monthly_payment = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2

epsilon = 0.01

attempt = balance

while abs(attempt) >= epsilon :
    
    attempt = balance
    month = 0
    
    while month < 12:
        month += 1
        unpaid_balance = attempt - monthly_payment
        interest = unpaid_balance * monthly_interest_rate
        attempt = unpaid_balance + interest

    if attempt < 0:
        monthly_payment_upper_bound = monthly_payment
    else:
        monthly_payment_lower_bound = monthly_payment
    
    mid_payment = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2
    
print(mid_payment)

=======
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0

month = 0
while month < 12:
    month += 1
    minMonthlyPayment = balance * monthlyPaymentRate
    monthlyUnpaidPaymemt = balance - minMonthlyPayment
    interest = monthlyUnpaidPaymemt * monthlyInterestRate
    balance = round(monthlyUnpaidPaymemt + interest, 2)
    
print("Remaining balance:", balance)
>>>>>>> parent of 60edbd1 (Done ps2 edx)
