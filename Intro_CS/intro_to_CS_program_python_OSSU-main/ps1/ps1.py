# Part A: House Hunting

# annual_salary = int(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary, as a decimal: "))
# total_cost = int(input("Enter the cost of your dream home: "))

# portion_down_payment = 0.25
# total_cost = total_cost * portion_down_payment
# current_savings = 0
# r = 0.04
# month_salary = annual_salary / 12
# month_savings = month_salary * portion_saved

# number_of_months = 0

# while current_savings < total_cost:
#     number_of_months += 1
#     current_savings += current_savings * r / 12
#     current_savings += month_savings
    
# print("Number of months:", number_of_months)



# Part B: Saving, with a raise

# annual_salary = int(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary, as a decimal: "))
# total_cost = int(input("Enter the cost of your dream home: "))
# semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

# portion_down_payment = 0.25
# total_cost = total_cost * portion_down_payment
# current_savings = 0
# return_annual = 0.04
# month_salary = annual_salary / 12
# month_savings = month_salary * portion_saved

# number_of_months = 0

# while current_savings < total_cost:
#     number_of_months += 1
#     current_savings += current_savings * return_annual / 12
#     current_savings += month_savings
#     if number_of_months > 0 and number_of_months % 6 == 0:
#         annual_salary = annual_salary + (annual_salary * semi_annual_raise)
#         month_salary = annual_salary / 12
#         month_savings = month_salary * portion_saved
    
# print("Number of months:", number_of_months)



# Part C: Finding the right amount to save away

semi_annual_raise = 0.07 
return_annual = 0.04
down_payment_house = 250000
starting_salary = int(input("Enter the starting salary: "))

lower = 0
higher = 10000
epsilon = 100

step_biSearch = 0
possible = True

while True:
    step_biSearch += 1
    annual_salary = starting_salary
    portion_saved = (lower + higher) / 2 / 10000
    month_salary = annual_salary / 12
    month_savings = month_salary * portion_saved
    
    current_savings = 0
    three_years = 0
    
    while three_years <= 36:
        three_years += 1
        current_savings += current_savings * return_annual / 12
        current_savings += month_savings
        
        if three_years % 6 == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)
            month_salary = annual_salary / 12
            month_savings = month_salary * portion_saved
            
    print("curent saving:", current_savings)
            
    if abs(current_savings - down_payment_house) <= epsilon:
        break
    
    if current_savings > down_payment_house:
        higher = portion_saved * 10000
        print("High:", higher)
    else:
        lower = portion_saved * 10000
        print("Lower:", lower)
    if lower >= higher:
        possible = False
        break

if possible:
    print("Step of Bisection:", step_biSearch)
    print("Portion Saving:", portion_saved)
else:
    print("It's impossible")