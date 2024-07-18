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

# We can also "unpack" list items similarly to how we'd assign several list items on the same row
first_fruit, *other_fruits = fruits
print(first_fruit, type(first_fruit))
print(other_fruits, type(other_fruits))

## Another example
num_list = [1, 2, 3, 4, 5, 6]
first_num, *mid_nums, last_num = num_list
print(first_num)
print(mid_nums)
print(last_num)

"""Slicing"""
# Lists can be sliced like strings
## A particular index position
print(fruits[2])

## From one position to another
print(fruits[1:3])

## From one position onwards
print(fruits[1:])

## Every nth item
print(fruits[::2])

"""Modifying"""
# Can tweak existing lists via index positions
## Replace the second fruit
fruits[1] = "tomato"
print(fruits)

# Can also check what's in a list
print("tomato" in fruits)

# Items can be added with the 'append' method (available to list type data) 
## Note that this method lets us skip assigning a new variable (automatically edits the existing list variable)
fruits.append("lime")
print("append 'lime': ", fruits)

# Items can also be inserted between existing items with the 'insert' method
fruits.insert(2, "apple")
print("insert 'apple': ", fruits)

# Or items can be removed with the eponymous method
fruits.remove("tomato")
print("remove 'tomato': ", fruits)

# We can also use the 'pop' method to remove an item by its index (rather than naming it specifically with 'remove')
fruits.pop(-2)
print("pop second-to-last index position: ", fruits)

# We can delete lists entirely with the 'del' keyword
## Note that keywords are not the same as functions/methods/etc.
ex_list = [1, 2, 3]
del ex_list

# Or we can keep the list variable declared but remove everything from it with the 'clear' method
ex_list = [1, 2, 3]
ex_list.clear()
print("Cleared list: ", ex_list)

"""
**Copying**

You may have noticed the assigning an existing list to a new variable does not work as you may expect
Doing so and editing the second variable *still affects the first variable*

To truly create a copy of a variable we need to use the 'copy' method
"""

# Demo copying
ex_list = [1, 2, 3]
ex_list2 = ex_list.copy()
ex_list2.pop(0)
print(ex_list2)

"""Joining/Concatenating"""

# You can concatenate lists with the '+' operator
ex_listA = [1, 2, 3]
ex_listB = [4, 5, 6]
ex_listAB = ex_listA + ex_listB
print(ex_listAB)

# You can also do this the the 'extend' method on the first list
## Note this does change the first list rather than making a new combo list
ex_listAA = ex_listA.copy()
ex_listAA.extend(ex_listB)
print(ex_listAA)

"""Counting & Finding"""

# We can count the number of times an item appears in a list with the 'count' method
fruits = ["orange", "orange", "orange", "banana"]
print(fruits.count("orange"))

# Or the 'index' method finds the first item in a list that matches the provided value
print(fruits.index("banana"))

"""Ordering"""

# Reverse list order with the 'reverse' method
ex_list3 = [1, 2, 3]
ex_list3.reverse()
print(ex_list3)

# Sort with the 'sort' method
rand_list = [5, 1, 6, 3, 4, 2]
rand_list.sort()
print(rand_list)

# Specifying descending with the 'reverse' argument
rand_list.sort(reverse = True)
print(rand_list)

# The 'sorted' function shows the sorted list without actually changing the order
rand_list = [5, 1, 6, 3, 4, 2]
print(sorted(rand_list))
