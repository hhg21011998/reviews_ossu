# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
yourName = input("Enter your name: ")
print("Welcome" + yourName)

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
hour = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
print("Pay: " + str(hour * rate))

# Exercise 4: Assume that we execute the following assignment statements:
width = 17
height = 12.0

print(type(width//2))
print(type(width/2.0))
print(type(height/3))
print(type(1 + 2 * 5))

# Exercise 5: Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the converted temperature.
c = int(input("Enter a Celsius: "))
print(c * 9/5 + 32)
