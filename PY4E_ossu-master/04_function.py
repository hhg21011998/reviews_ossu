# import math
# print(math)

# Exercise 1: Run the program on your system and see what numbers you get. 
# Run the program more than once and see what numbers you get.
# import random

# for i in range(10):
#     x = random.random()
#     print(x)

# print(random.randint(1, 3))

# Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. 
# Run the program and see what error message you get.

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# def print_lyrics():
#     print("I'm a lumberjack, and I'm OK.")
#     print("I sleep all night and I work all day.")

# repeat_lyrics()

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and 
# create a function called computepay which takes two parameters (hours and rate).

def computepay(hour, rate):
    if hour > 40:
        newHour = hour - 40
        hour = 40 + newHour * 1.5
    return hour * rate

hour = input("Enter hours: ")
rate = input("Enter rate: ")

try:
    print("Pay:",computepay(float(hour), float(rate)))
except:
    print("Error, please enter numeric input")

# Exercise 7: Rewrite the grade program from the previous chapter 
# using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def takeScore(score):
    if score < 0 or score > 1:
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
    else:
        print("Bad score")

yourScore = input("Enter your score: ")
try:
    takeScore(float(yourScore))
except:
    print("Bad score")