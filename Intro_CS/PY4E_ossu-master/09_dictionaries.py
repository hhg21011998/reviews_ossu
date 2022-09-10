# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn’t matter what the values are.
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

# fhand = open("words.txt")
# dictWords = dict()
#
# for line in fhand:
#     flist = line.split()
#     if len(flist) > 0:
#         for word in flist:
#             dictWords[word] = 1
#
# print("and" in dictWords)

# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and
# keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).

# fname = input("Enter a file name: ")
# try:
#     fhand = open(fname)
# except:
#     print("Error file name %s" %fname)
#
# countsDay = dict()
#
# for line in fhand:
#     line = line.strip()
#     lineList = line.split()
#     if len(lineList) > 0 and lineList[0] == "From":
#         countsDay[lineList[2]] = countsDay.get(lineList[2], 0) + 1
#
# print(countsDay)

# Exercise 3: Write a program to read through a mail log,
# build a histogram using a dictionary to count how many messages have come from each email address,
# and print the dictionary.

# fname = input("Enter a file name: ")
# try:
#     fhand = open(fname)
# except:
#     print("Error file name %s" %fname)
#
# countsMail = dict()
#
# for line in fhand:
#     line = line.strip()
#     lineList = line.split()
#     if len(lineList) > 0 and lineList[0] == "From":
#         countsMail[lineList[1]] = countsMail.get(lineList[1], 0) + 1
#
# print(countsMail)

# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created,
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
# to find who has the most messages and print how many messages the person has.

# fname = input("Enter a file name: ")
# try:
#     fhand = open(fname)
# except:
#     print("Error file name %s" %fname)
#
# countsMail = dict()
#
# for line in fhand:
#     line = line.strip()
#     lineList = line.split()
#     if len(lineList) > 0 and lineList[0] == "From":
#         countsMail[lineList[1]] = countsMail.get(lineList[1], 0) + 1
#
# checkMax = None
# mailMax = ""
#
# for mail in countsMail:
#     if checkMax is None or countsMail[mail] > checkMax:
#         checkMax = countsMail[mail]
#         mailMax = mail
#
# print(mailMax, checkMax)

# Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

# fname = input("Enter a file name: ")
# try:
#     fhand = open(fname)
# except:
#     print("Error file name %s" %fname)
#
# countsDomain = dict()
# domain = ""
#
# for line in fhand:
#     line = line.strip()
#     lineList = line.split()
#     if len(lineList) > 0 and lineList[0] == "From":
#         address = lineList[1]
#         positionAtSign = address.find("@")
#         domain = address[positionAtSign + 1 : len(address)]
#         countsDomain[domain] = countsDomain.get(domain, 0) + 1
# 
# print(countsDomain)
