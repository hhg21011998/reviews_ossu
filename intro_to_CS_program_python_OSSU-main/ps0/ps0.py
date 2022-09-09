import math

# Assignment:
#   Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”. 

x = input("Enter number x: ")
y = input("Enter number y: ")
x = int(x)
y = int(y)

print(x**y)
print(math.log(x, 2))