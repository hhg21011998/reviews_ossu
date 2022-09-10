print("hello world")

# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
total = 0
count = 0
average = 0

while True:
    userInput = input("Enter a number: ")
    try:
        if userInput == "done":
            break
        else:
            total += int(userInput)
            count += 1
            average = total / count
    except:
        print("Invalid input")
print(total, count, average)

# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
myMax = None
myMin = None

while True:
    userInput = input("Enter a number: ")

    try:
        if userInput == "done":
            break
        else:
            intInput = int(userInput)
            if myMax is None or myMax < intInput:
                myMax = intInput
            if myMin is None or myMin > intInput:
                myMin = intInput
    except:
        print("Invalid input")
print("My min =", myMin, "My max =", myMax)
