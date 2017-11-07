"""
Introduction to Python
DATE - 9 Nov 2017
Instructor - Nathan Danielsen @nate_somewhere
https://github.com/ndanielsen/beginning-python/
"""

print('hello world')

# Comments in python use a '#'

# Exercise: Comments
# print('uncomment me')

# BASIC DATA TYPES

# Numbers
# https://docs.python.org/3/tutorial/introduction.html#numbers

5  # Integer
5.0  # Float (decimal)
x = 5  # creates an object

type(x)  # check the type: int (not declared explicitly)
type(5)  # assigning it to a variable is not required
type(5.0)  # float
type(True)  # bool

### Exercise: Checking Data Type
text = 'What type of data type am I?'

# math operations

1 + 2  # Addition
7 - 5  # Division
5 * 7  # Multiplication
10 / 3  # Division
10 / 3.0  # Floor division
16 % 5  # Modulo (remainder)
2**10  # Exponent

# variable assignment
a = 1
b = 2
c = 6

### Exercise: A little math
#1 Assign a variable 'd' that equals 'a' plus 'b' minus 'c'
#2 What value is d?
#3 Assign a variable 'e' that is 'd' divided by 6.0
#4 what is the value of e?

# STRINGS
# https://docs.python.org/2/tutorial/introduction.html#strings

s = str(42)
s  # convert another data type into a string (casting)
s = 'I like cookies'

# examine a string
s[0]  # returns 'I'
len(s)  # returns 10

# string slicing like lists
s[0:7]  # returns 'I like'
s[6:]  # returns 'cookies'
s[-1]  # returns 'u'

# EXERCISE: Book Titles (Part 1)
# 1) Extract the book title from the string
# 2) Save each book title to a variable (ie book1_title)
# 3) How many characters/elements are in each title?

book1 = "Beyond the Door by Dick, Philip K., 1928-1982"

book2 = "The Variable Man by Dick, Philip K., 1928-1982"

book3 = "The Skull by Dick, Philip K., 1928-1982"

################

# split a string into a list of substrings separated by a delimiter

s = 'I like cookies'
s.split(' ')  # returns ['I','like','cookies']
s.split()  # same thing

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4  # returns 'The meaning of life is 42'
s3 + ' ' + str(42)  # same thing

# EXERCISE: Book Titles (Part 2)
# 1. How words are in the title of book1?
# BONUS: Comparison:  Does book1_title have more words then book3_title?
# HINT: https://docs.python.org/3/library/stdtypes.html#comparisons
book1_title = "Beyond the Door"
book3_title = "The Skull"

# FUNCTIONS - Part I

# let's create a function to save us some work of adding numbers together

def adder(x, y): # def declares that it is a function, the two inputs between the parens
    total = x + y
    return total

# total = adder(9, 5)
# print(total)

# EXERCISE:
# 1. Adapt the function `doing_good_job` to take an input called friend_name and
# have it print out "Hang in there, {friend_name}"
# HINTS: Look at the function adder and "concatenate strings" above

def doing_good_job():
    print("Programming is hard!")
    print("You're doing a great job so far!")
    print("Hang in there, friend!")


# FUNCTIONS - Part II
# Now that have some basic tools, let's do something interesting

#
# https://www.nationaljournal.com/md/656032/urban-forestry-washington-d-c
# Look at the data source:
# http://opendata.dc.gov/datasets/urban-forestry-street-trees?

import requests
# https://opendata.arcgis.com/datasets/f6c3c04113944f23a7993f2e603abaf2_23.csv

# response =  requests.get('https://opendata.arcgis.com/datasets/f6c3c04113944f23a7993f2e603abaf2_23.csv')
# with open('./Urban_Forestry_Street_Trees.csv', 'wb') as f:
#     f.write(response.content)
