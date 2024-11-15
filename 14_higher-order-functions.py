"""
Higher Order Functions

Functions can accept one or more functions as parameters and/or they can return a function.

They can also be edited and assigned to variables
"""

""" Functions as Parameters """
# Define a higher order function
def ex_hof(_f, _list):
    result = _f(_list)
    return result

# Invoke it
ex_hof(sum, [1, 2, 3, 4])

""" Returning Functions from Functions """
# Define some helper functions
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x < 0:
        val = x * -1
    else: 
        val = x
    return val

# Define another HOF
def ex_hof2(operation):
    if operation == "square":
        return square
    elif operation == "cube":
        return cube
    elif operation == "absolute":
        return absolute

# Invoke it a few ways
new_fxn = ex_hof2("square")
print(new_fxn(-2))
new_fxn = ex_hof2("cube")
print(new_fxn(-2))
new_fxn = ex_hof2("absolute")
print(new_fxn(-2))

""" Python Closures & Decorators """

# Closures are created by defining a function inside of another and returning the nested one
def add_ten():
    def add(num):
        return num + 10
    return add

# Invoke higher order function
closure_fxn = add_ten()

# Use the closure function
print(closure_fxn(5))

# Decorators allow users to _add_ functionality to an existing variable without modifying its structure
def greeting():
    return "Welcome!"

def uppercase_decorator(fxn):
    def wrapper():
        func = fxn()
        to_upper = func.upper()
        return to_upper
    return wrapper

# Add decorator
upper_greeting = uppercase_decorator(greeting)

# Demonstrate its changed behavior
print(greeting())
print(upper_greeting())

# Create another decorator
def split_string_decorator(fxn):
    def wrapper():
        func = fxn()
        split_string = func.split()
        return split_string
    return wrapper

# Split greeting
split_greeting = split_string_decorator(greeting)

# Add both decorators
split_upper_greeting = split_string_decorator(uppercase_decorator(greeting))

# Invoke it
print(greeting())
print(split_greeting())
print(split_upper_greeting())

""" Built-In HOFs """

# The "map" function is a built-in HOF that accepts a function and an iterable as parameters
def square(x):
    return x ** 2

nums = [1, 2, 3, 4, 5, 6]
result = list(map(square, nums))
print(result)

# Can also do this with lambda functions to write fewer lines
result = list(map(lambda n: n ** 2, nums))
print(result)

# The "filter" function returns only items in the iterable that return `True` for the provided conditional
result = list(filter(lambda i: i % 2 == 0, nums))
print(result)

# The "reduce" function from the "functools" module is also an HOF
## It returns a single value rather than another iterable (as with "map" and "reduce")
import functools

result = functools.reduce(lambda j, k: int(j) + int(k), ["1", "2", "3", "4"])
print(result)
