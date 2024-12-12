"""
Python comes with certain built-in functions.
These can be used without importing/configuring libraries

For an exhaustive list of these, see here: 
https://docs.python.org/3.9/library/functions.html
"""

# The 'print' function simply prints to the Terminal
print("Hello!")

# The 'len' function counts the number of characters (including spaces)
print(len("Hello!"))

# Functions also exist that coerce data to a particular type
print(type(str(10)))
print(type(int("10")))
print(type(float(10)))

# The 'input' function can be used to interactively gather user inputs
# input("Type your name:")

# The 'help' function gets some high-level information about a particular function
# print(help(str))
## Help files can be escaped by typing "q"

# We can also do simple arithmetic/numeric options on integer/float lists
print(min([1, 2, 3, 4, 5]))
print(max([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5]))
