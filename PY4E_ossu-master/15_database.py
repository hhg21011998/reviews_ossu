import sqlite3
import urllib.request, urllib.parse, urllib.error
import ssl
import re
import xml.etree.ElementTree as ET
import json

# conn = sqlite3.connect("music.db")
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Tracks')
# cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

# cur.execute("INSERT INTO Tracks (title, plays) VALUES (?, ?)", ("Thunfer Suck", 20))
# cur.execute("INSERT INTO Tracks (title, plays) VALUES (?, ?)", ("My way", 15))
# conn.commit()
#
# print("Tracks: ")
#
# rows = cur.execute("SELECT title, plays FROM Tracks").fetchall()
#
# print(rows)
#
# cur.execute("DELETE FROM Tracks where plays < 100")
# conn.commit()
#
# conn.close()

# Autograder: Counting Email in a Database

# fhand = open("mbox.txt")
# conn = sqlite3.connect("count_org.sqlite")
# cur = conn.cursor()
#
# cur.execute("DROP TABLE IF EXISTS Counts")
# cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
#
# cur.execute("DELETE FROM Counts")
# conn.commit()
#
# ct = 0
# d = dict()
#
# for line in fhand:
#     line = line.strip()
#     if re.search("From ", line):
#         line = line.split()
#         mailAdd = line[1].split("@")
#         if len(mailAdd) > 1:
#             org = mailAdd[1]
#             d[org] = d.get(org, 0) + 1
#
# for key in d:
#     cur.execute(f"INSERT INTO Counts (org, count) VALUES (?, ?)", (key, d[key]))
#     conn.commit()



# Autograder: Multi-Table Database - Tracks

# conn = sqlite3.connect("trackdb.sqlite")
# cur = conn.cursor()
#
# cur.executescript("""
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Genre;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;
#
# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );
#
# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );
# """)
#
# def lookup(d, key):
#     found = False
#     for child in d:
#         if found: return child.text
#         if child.tag == "key" and child.text == key:
#             found = True
#     return None
#
# fname = open("Library.xml")
#
# stuff = ET.parse(fname) # tra ve <xml.etree.ElementTree.ElementTree object at 0x000001BA95C58A30>
#
# all = stuff.findall("dict/dict/dict") # tra ve 1 bien all la 1 mang chua cac dict
# a = 0
# for entry in all:
#     if ( lookup(entry, 'Track ID') is None ) : continue
#
#     name = lookup(entry, 'Name')
#     artist = lookup(entry, 'Artist')
#     genre = lookup(entry, "Genre")
#     album = lookup(entry, 'Album')
#     rating = lookup(entry, 'Rating')
#     length = lookup(entry, 'Total Time')
#     count = lookup(entry, 'Play Count')
#
#     if name is None or artist is None or album is None or genre is None : # đề phòng trường hợp file xml bị thiếu giá trị thì mình sẽ không fetchone được.
#         continue
#     # print(name, artist, album, count, rating, length)
#
#     cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist,))
#     cur.execute("SELECT id FROM Artist where name = ?", (artist,))
#     artist_id = cur.fetchone()[0] #tra ve 1 tuple chua cac gia tri trong row
#
#     cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre,))
#     cur.execute("SELECT id FROM Genre where name = ?", (genre,))
#     genre_id = cur.fetchone()[0]
#
#     cur.execute("INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)", (artist_id, album,))
#     cur.execute("SELECT id FROM Album where title = ?", (album,))
#     album_id = cur.fetchone()[0]
#
#     cur.execute("INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)",
#     (name, album_id, genre_id, length, rating, count,))
#
#     conn.commit()



# Autograder: Many Students in Many Courses

conn = sqlite3.connect("rosterdb.sqlite")
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fhand = open("roster_data.json")
data = json.load(fhand)

for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]
    print(user_id)

    cur.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)", (title, ))
    cur.execute("SELECT id FROM Course where title = ?", (title, ))
    course_id = cur.fetchone()[0]
    print(course_id)

    cur.execute("INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)", (user_id, course_id, role, ))

    conn.commit()
