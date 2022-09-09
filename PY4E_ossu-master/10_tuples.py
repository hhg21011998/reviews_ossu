# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

# fname = input("Enter a file name: ")
#
# try:
#     fhand = open(fname)
# except:
#     print("Error file name!")
#     exit()
#
# addressDict = dict()
#
# for line in fhand:
#     line = line.rstrip()
#     line = line.split()
#     if len(line) > 0 and line[0] == "From":
#         address = line[1]
#         addressDict[address] = addressDict.get(address, 0) + 1
#
# addressList = list()
#
# for key in addressDict:
#     addressList.append((addressDict[key], key))
#
# addressList.sort(reverse = True)
# a, b = addressList[0]
#
# print(b, a)

# Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the “From” line by finding the time string and
# then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

# fname = input("Enter a file name: ")
#
# try:
#     fhand = open(fname)
# except:
#     print("Error file name!")
#     exit()
#
# hourDict = dict()
#
# for line in fhand:
#     line = line.rstrip()
#     line = line.split()
#     if len(line) > 0 and line[0] == "From":
#         time = line[5]
#         time = time.split(":")
#         hour = time[0]
#         hourDict[hour] = hourDict.get(hour, 0) + 1
#
# hourList = list()
#
# for key in hourDict:
#     hourList.append((key, hourDict[key]))
#
# hourList.sort()
#
# for a, b in hourList:
#     print(a, b)

# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and see how letter frequency varies between languages.
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("Error file name!")
    exit()

letterDict = dict()

for line in fhand:
    line = line.strip()
    line = line.lower()
    if len(line) > 0:
        for letter in line:
            if letter.isalpha():
                letterDict[letter] = letterDict.get(letter, 0) + 1

letterList = list(letterDict.items())
letterList.sort()
print(letterList)
