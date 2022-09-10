import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
# You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.


# Exercise 2: Change your socket program so that it counts the number of characters it has received
# and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document
# and count the total number of characters
# and display the count of the number of characters at the end of the document.

# url = input("Enter - ")
# try:
#     urlComp = url.split("/")
#     host = urlComp[2]
# except:
#     print("Error url, we need the protocol http/https!")
#     exit()
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((host, 80))
# cmd = ("GET %s HTTP/1.0\r\n\r\n" % url).encode()
# mysock.send(cmd)
#
# total = 0
# document = ""
#
# while True:
#     data = mysock.recv(512)
#     total += len(data)
#     if len(data) < 1:
#         break
#     document += data.decode()
#
# print(document[:3001])
# print("Total:", total)
#
# mysock.close()


# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document.
# Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

# url = input("Enter - ")
# fhand = urllib.request.urlopen(url)
# newLine = ""
# for line in fhand:
#     newLine += line.decode()
#
# print(newLine[:3001])
# print("Total", len(newLine))


# Exercise 4: Change the urllinks.py program to extract and
# count paragraph (p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program.
# Do not display the paragraph text, only count them.
# Test your program on several small web pages as well as some larger web pages.

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('p')
# total = 0
# for tag in tags:
#     total += 1
#     print("1:", tag)
#
# print(total)

# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers
# and a blank line have been received.
# Remember that recv receives characters (newlines and all), not lines.

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

document = ""

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    document += data.decode()

posBlankLine = document.find("\r\n\r\n")

print(document[posBlankLine+1:])
mysock.close()
