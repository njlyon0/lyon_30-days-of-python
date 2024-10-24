"""
Functions can be either built-in (see prior scripts) or can be custom built by users

This is a nice way of reducing duplication in code as repeated operations can be condensed into a single function that is then invoked as needed
"""

# Defining a function requires the "def" operator
# Functions can be defined with or without parameters
# The "return" keyword can be used to make the function return some value to the user
## Without specifying this bit, the value returned is "None"
# Parameters are interpreted based on their position or by the parameter name (if supplied by the user)

# Simple example function
## Define
def plus(a, b):
    return a + b

## Invoke
plus(a=1, b=1)

# The "return" operator stops execution (similar to "break")
def is_even(n):
    if n % 2 == 0:
        print(n, " is even")
        return True
    print(n, " is not even")
    return False

## Test it
is_even(n = 3)
is_even(n = 4)

# Default values can be set when defining a function
def add_ten(x = 1):
    return x + 10

add_ten()

# We can allow the user to supply an arbitrary number of arguments with an asterisk in the definition phase
def sum_all_nums(*nums):
    total = 0
    for val in nums:
        total += val
    return(total)

sum_all_nums(3, 4, 5, 6, 7)
sum_all_nums(1, 1)

# We can also pass a function as a parameter to another function
## In R this would be called a "functional" or "function operator" (depending on whether it returns a value or another function respectively)
def square_num(n):
    return n * n

def do_function(f, x):
    return f(x)

do_function(f = square_num, x = 5)
