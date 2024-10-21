"""
Sets are collections of items with a similar definition to that of "sets" in mathematics.

Sets store only _unique_ items and it is possible to identify the following metrics of two (or more) sets: union, intersection, difference, symmetric difference, subset, super set, and disjoint
"""

# Make a set
ex_set = set()
print(type(ex_set))

# Can also coerce a list to a set using the "set" function
ex_list = [1, 2, 3, 4]
ex_set = set(ex_list)
print(ex_set)

# Can also create sets via curly braces
fruits_set = {"banana", "orange", "lemon", "mango"}
print(fruits_set)

# Can use the length function to find the number of items
print(len(fruits_set))

"""Accessing Set Contents"""

# Just like elsewhere, can check contents of a set
print("Is 'mango' in our fruit example set? ", "mango" in fruits_set)

# While we can't change items in a set, we can add items with the "add" method
fruits_set.add("lime")
print(fruits_set)

# Can add multiple items with the "update" method (which accepts a list of new items)
fruits_set.update(["tomato", "watermelon", "tangerine"])
print(fruits_set)

# The "remove" method lets us rem,ove an item
fruits_set.remove("tomato")
print(fruits_set)

# The "pop" method removes a random item and returns that item
ex_set = {1, 2, 3, 4, 5}
rm_item = ex_set.pop()
print("Removed ", rm_item, ". Leaving set with contents: ", ex_set)

# Can also clear/empty a set with the "clear" method
print("Cleared example set leaving contents: ", ex_set.clear())

# As with tuples, the "del" operator fully deletes the set
del ex_set

""" Set Operations """



