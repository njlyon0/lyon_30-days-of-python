"""
Strings are essentially any characters, typically wrapped in apostrophes, quotes, or triple variants of either (like this comment!)

Strings can be manipulated +/- easily in Python
"""

# String concatenation
print("hello" + " ", "world")

# Escape sequences in strings
## New line
print("Line one\nLine two")

## Tab (8 spaces)
print("Antici...\tpation")

## Escape a backslash (to show it) by escaping it with a different one!
print("This is a backslash: \\")

## Can also escape apostrophes/quotes inside of a string
print("So then I said \'what do you mean you don\'t \"get\" strings?\'")


"""Old-style string formatting"""

# You can also strip elements from a tuple for inclusion in a string
## Define variables
first_name = "Nick"
last_name = "Lyon"
language = "Python"

## Use a tuple to format the string
print("I am %s %s. I am learning %s" %(first_name, last_name, language))

## Similar syntax can be used with integers (%d), floating points (%f), and floating points with fixed precision (%.<number of digits>f)
circle_area = 3.14 * (9 ** 2)
print("The area of a circle with a radius of 10 is %.3f." %(circle_area))

"""New-style string formatting"""

# Python 3 enables a different mode of string formatting using the 'format' method (for string type data)
print("I am {} {}. I am learning {}".format(first_name, last_name, language))

# We can also do simple math in this way
a, b = 4, 3
print("{} + {} = {}".format(a, b, a + b))

# Python 3.6+ also supports 'f-strings'
print(f'{a} * {b} = {a * b}')

"""Strings as sequences of characters"""

# At its simplest, we can "unpack" a sequence of characters into separate variables
p, q, r, s, t, u = "Python"
print(p)
print(q)

# Instead we could use the index of the character (index starts at 0)
print("The first index position of \'Python\' is ", "Python"[0])

# You could also "slice" substrings by specifying multiple boundary positions
print("The first through third position of \'Python is\' ", "Python"[0:3])

# Python also allows reversing strings
print("The reverse of \'Python is\' ", "Python"[::-1])

# We can skip characters too (in the below code we're skipping every second character)
print("Python"[0:6:2])

"""String Methods"""

challenge_text = "thirty days of python"

# We can use the various methods available to string type data to perform operations
print(challenge_text.capitalize())
print(challenge_text.count("t"))
print(challenge_text.endswith("on"))
print(challenge_text.find("y")) ## Returns *only FIRST* instance of supplied character
print(challenge_text.rfind("y")) ## Returns *only LAST* instance of supplied character


