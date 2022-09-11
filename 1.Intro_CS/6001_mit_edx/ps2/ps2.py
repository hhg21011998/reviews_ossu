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
