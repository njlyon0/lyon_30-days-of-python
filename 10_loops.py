"""
Loops are for repetitive tasks.

Python provides two primary types:

1. 'while' loops that repeat as long as the initial condition is met
2. 'for' loops that repeat a known number of times
"""

""" While Loops """

# Example while loop
i = 1
while i < 5:
    print(i)
    i = i + 1

# We can add an "else" operator to run some other code when the while loop ends
i = 1
while i < 5:
    print(i)
    i = i + 1
else:
    print(i)

# Alternately, we can use the "break" operator to stop the while loop based on some condition
## Note the indentation of both "if" and "break" relative to "while"
i = 0
while i < 5:
    print(i)
    i = i + 1
    if i == 3:
        break

# We can also use the "continue" operator to skip an iteration based on some conditional
## Here we are skipping the print step when i is 3
i = 0
while i < 5:
    if i == 3:
        i = i + 1
        continue
    print(i)
    i = i + 1

""" For Loops """

# Example for loop
my_nums = [1, 2, 3, 4]
for k in my_nums:
    print(k)

# Can also loop across characters in a string
for char in "Python":
    print(char)

# Or loop across index positions
for g in range(len("Python")):
    print("Python"[g])

# Can also loop across tuples, sets, and dictionaries (in addition to lists & strings)

# Default behavior of dictionary loops is to gather only the keys but can affect this with the ".item" method
ex_dict = {"key1":"value1", "key2":"value2"}
for key, value in ex_dict.items():
    print(key, value)

# The range function lists numbers
## We used it earlier in one of the string + for loop examples
print(range(5))

# Default is from 0 to specified number by increments of 1 but we can mess with that
## Order is start (inclusive), stop (exclusive), and increment
print(list(range(0, 10, 2)))
## Note that "10" is excluded because the end of the range is not included

# For loops can be nested and the for loop supports an "else" operator for a final set of code execution

# For loops also support the "pass" operator for skipping execution entirely (typically to avoid errors)
for l in range(2):
    pass
