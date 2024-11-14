"""
List comprehension in Python is a compact way of creating a list from a sequence of operations. It creates a list and is dramatically faster than a typical loop (see '10_loops.py' for information on standard loops)

Syntax is as follows:
`[i for i in iterable if expression]`
"""

# Let's look at an example
language = "Python"

# Turn it into a list via function(s)
lang_list = list(language)
print(lang_list)

# Turn it into a list via list comprehension
lang_list = [i for i in language]
print(lang_list)

# Can use this to generate a list of numbers
nums = [k for k in range(10)]
print(nums)

# Can also do math on each value
squares = [g * g for g in range(5)]
print(squares)

# List comprehension can be expanded to also handle conditionals
evens = [j for j in range(10) if j % 2 == 0]
print(evens)

# Can flatten arrays this way
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [val for row in array for val in row]
print(flat_list)

"""
Lambda Functions

These are small, often nameless functions that can take any number of arguments but only have one expression. Similar to "anonymous" functions in JavaScript
"""

# Define one using the 'lambda' keyword
fxn = lambda param1, param2, param3: param1 + param2 + param3

# Use it
result = fxn(1, 2, 3)

# Print the outcome
print(result)

# Check type
print(type(fxn))
## Displays as just a 'function'

# Lambda functions can be defined inside of another function
## Define
def power(x):
    return lambda n: x ** n

## Invoke
### Second set of parentheses is 'n' accepted by internal lambda function
cube = power(2)(3)
print(cube)

