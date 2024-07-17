"""
Lists are a fundamental type of data in Python
They are ordered but changeable and they allow duplicate items as well as items of different types themselves

They differ importantly from tuples, sets, and dictionaries (see days 6, 7, and 8 respectively)
"""

# Lists can be created in one of two ways
## 1. Via square brackets
test_list1 = []
print(type(test_list1))

## 2. With the list function
test_list2 = list()
print(type(test_list2))

# As stated above, lists can contain separate data types
test_list3 = [33, "hello", ("a", "b", "c")]
print(test_list3)

# Lists can then be worked with in similar ways to how we work with strings (see day 4)
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)

# The 'len' function can still be used but now it refers to the number of list items (rather than the number of characters as it does in strings)
print("There are {} fruits".format(len(fruits)))

# The index position of a list is similarly changed: it refers to the item at that index position rather than the character within a string
print("The second fruit in our list is: ", fruits[1])

# We can still use negative indexing too to find items from the back to the front
## Note that the first 'reverse index' is "-1" *not* 0 as it is in regular indexing
print("The penultimate fruit in our list is: ", fruits[-2])

















