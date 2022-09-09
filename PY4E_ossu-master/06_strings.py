# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

# myString = input("Enter a string: ")
# myIndex = len(myString) - 1
#
# while myIndex >= 0:
#     print("\n", myString[myIndex])
#     myIndex -= 1
#
# print(dir(myString))



# Exercise 2: Given that fruit is a string, what does fruit[:] mean?

# fruit = "banana"
# print(fruit)



# Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

# myWord = input("Enter a word: ")
# myCharacter = input("Enter a character: ")
#
# def count(word, character):
#     count = 0
#     for letter in word:
#         if letter == character:
#             count = count + 1
#     return count
#
# print("Character", myCharacter, "in", myWord, "=", count(myWord, myCharacter))



# Exercise 4: There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at:
# https://docs.python.org/library/stdtypes.html#string-methods
# Write an invocation that counts the number of times the letter a occurs in “banana”.

# word = "banana"
# counting = word.count("a")
# print(counting)



# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475 '
# Use find and string slicing to extract the portion of the string after the colon character and
# then use the float function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475 '
findindColon = str.find(":")
strWeNeed = str[findindColon+1 : ]
stripingStr = strWeNeed.strip()
print(type(stripingStr))
print(stripingStr)
floatWeNeed = float(stripingStr)
print(type(floatWeNeed))
print(floatWeNeed)
