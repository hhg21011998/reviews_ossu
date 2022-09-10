import re

# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

# typing = input("Enter a regex: ")
# fhand = open("mbox.txt")
# count = 0
#
# for line in fhand:
#     if re.search("%s" %typing, line):
#         count += 1
#
# print("mbox.txt had %d lines that matched %s" %(count, typing))



# Exercise 2: Write a program to look for lines of the form:
#
# New Revision: 39772
#
# Extract the number from each of the lines using a regular expression and the findall() method.
#  Compute the average of the numbers and print out the average as an integer.
# fname = input("Enter file: ")
#
# try:
#     fhand = open(fname)
# except:
#     print("Error file name!")
#     exit()
#
# listX = list()
# for line in fhand:
#     line = line.strip()
#     x = re.findall("^New\sRevision: ([0-9]*)", line)
#     if len(x) > 0:
#         for item in x:
#             listX.append(int(item))
# result = int(sum(listX)/len(listX))
# print(result)



# Autograder: Regular Expressions
fhand = open("regex_sum_1456357.txt")
sum = 0

for line in fhand:
    # line = line.strip()
    x = re.findall("[0-9]*", line)
    for item in x:
        if item != "":
            sum += int(item)

print(sum)
