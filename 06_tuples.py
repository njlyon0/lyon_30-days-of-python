"""
Tuples are an important data type in Python
They are ordered and unchangeable (i.e., immutable)

Tuples are created with parentheses and, once created, cannot be changed
Unlike lists (see day 5), we can't use add, insert, or remove methods
"""

# Make a tuple
ex_tup = (1, 2, 3, 4)
print(type(ex_tup))

# Make another using the 'tuple' function
ex_tup = tuple([1, 2, 3, 4])
print(ex_tup, type(ex_tup))

# Assess the length of the tuple
print(len(ex_tup))

# Positive and negative indexing work on tuples (like lists)
print(ex_tup[0])
print(ex_tup[-2])

# Make another demo tuple
fruits = ("banana", "orange", "mango", "lemon")
print(fruits[len(fruits) - 1])

"""Slicing"""

# Can slice out a sub-tuple using range of indices
print(fruits[0:2])
print(fruits[0:3:2])
print(fruits[2:])

"""Tuple Conversion"""

# Can convert tuples into lists with the 'list' function
fruit_list = list(fruits)
print(type(fruit_list))

"""Finding Items in Tuples"""

# Can look for specific info in a tuple
print("mango" in fruits)

"""Joining Tuples"""

# Can join tuples with the '+' operator
tup_one = (1, 2, 3)
tup_two = (4, 5, 6)
tup_three = tup_one + tup_two
print(tup_three)

"""Deleting Tuples"""

# The 'del' keyword works on tuple variables too
del tup_three
