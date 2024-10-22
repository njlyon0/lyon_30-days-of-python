"""
Generally, Python scripts are executed line-by-line from the top to the bottom.

However, by using conditionals--statements that return either "True" or "False"--we can write code that skips or runs a chunk depending on a conditional (i.e., is executed conditionally) and we can write chunks that run _as long as_ the conditional returns "True".

Note also that Python is sensitive to indentation and that is how statements "inside of" a conditional chunk are delineated from lines not in that chunk.
"""

# The `if` operator runs specified code only _if the statement is True_
x = 0
if x == 0:
    print("X is equal to 0")

# We can additionally invoke the `else` operator to allow for multiple possibilities
x = 2
if x == 0:
    print("X is equal to 0")
else: 
    print("X is not equal to 0")

# While yes/no pairs are useful, we can support more options with the `elif` operator
x = -3
if x == 0: 
    print("X is equal to 0")
elif x > 0:
    print("X is positive")
else: 
    print("X is negative")

# While this is--arguably--more readable in the multi-line format we could also condense conditionals into a single line by modifying the syntax
## Syntax is: code if condition else code
x = 2
print("X is positive") if x > 0 else print("X is not positive")

# We can also nest conditionals if we want a separate set of conditions to only apply once some initial condition has been met
## Note how we are doubly indented for the nest conditional
x = 7
if x == 0:
    print("X is equal to 0")
else: 
    if x % 2 == 0:
        print("X is an even number")
    else: 
        print("X is an odd number")

# We can use the `and` operator for evaluating multiple conditions at the same time
x = 2
if x > 0 and x % 2 == 0:
    print("X is positive and even")
else: 
    print("X is not positive and/or odd")

# Similarly, we can use `or` to execute if either condition returns "True"
x = 0
if x > 0 or x < 0:
    print("X is not zero")
else: 
    print("X is zero")
