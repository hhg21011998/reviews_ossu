# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours
from re import S

try: 
    hour = int(input("Enter hours: "))
    if hour < 40:
        rate  = 1
        print("Pay: " + str(hour * rate))
    else:
        rate = 1.5 
        print("Pay: " + str(hour * rate))
except:
    print("Please enter a number")
    
# Exercise 2: Rewrite your pay program using try and except 
# so that your program handles non-numeric input gracefully by printing a message and exiting the program.

# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
try:
    score = float(input("Enter a score: "))
    if score < 0.0 or score > 1.0:
        print("Bad score")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
except:
    print("Please enter a number from 0.0 to 1.0")