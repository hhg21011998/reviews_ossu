myName = ["Ha", "Hoang", "Giang", "Vip", "Pro"]

# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def chop(t):
    del t[0]
    del t[len(t) - 1]

chop(myName)

def middle(arr):
    arr.pop()
    del arr[0]
    return arr

a = middle(myName)

for item in a:
    print(item)

# Exercise 2: Figure out which line of the above program is still not properly guarded.
# See if you can construct a text file which causes the program to fail and
# then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 :
        continue
    if words[0] != 'From' :
         continue
    print(words[2])

# Exercise 3: Rewrite the guardian code in the above example without two if statements.
# Instead, use a compound logical expression using the or logical operator with a single if statement.

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0  or words[0] != 'From' :
        continue
    print(words[2])

# Exercise 4: Find all unique words in a file
#
# Shakespeare used over 20,000 words in his works. But how would you determine that? How would you produce the list of all the words that Shakespeare used? Would you download all his work, read it and track all unique words by hand?
#
# Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.
#
# To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.

uniqueWords = []

inp = input("Enter file name: ")
fhand = open(inp)

for line in fhand:
    wordsInLine = line.split()
    for word in wordsInLine:
        if not(word in uniqueWords):
            uniqueWords.append(word)
uniqueWords.sort()
print(uniqueWords)

# Exercise 5: Minimalist Email Client.

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)
count = 0

for line in fhand:
    if line.startswith("From") and not(line.startswith("From:")):
        listOfWord = line.split()
        print(listOfWord[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")

# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”.
# Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

listOfNumber = []

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    listOfNumber.append(int(inp))

print("Min:", min(listOfNumber))
print("Max:", max(listOfNumber))
