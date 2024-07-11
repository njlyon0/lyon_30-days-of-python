# Exercise: Level 1

## Check the python version you are using
import sys
print(sys.version)

## Open the python interactive shell and do the following operations. Use the operands 3 and 4.
### addition(+)
print(3 + 4)
### subtraction(-)
print(3 - 4)
### multiplication(*)
print(3 * 4)
### modulus(%)
print(3 % 4)
### division(/)
print(3 / 4)
### exponential(**)
print(3 ** 4)
### floor division operator(//)
print(3 // 4)

## Write strings on the python interactive shell. The strings are the following:
### Your name
print("Nick")
### Your family name
print("Lyon")
### Your country
print("USA")
### I am enjoying 30 days of python
print("I'm enjoying 30 days of python")

## Check the data types of the following data:

### 10
print(type(10))
### 9.8
print(type(9.8))
### 3.14
print(type(3.14))
### 4 - 4j
print(type(4 - 4j))
### ['Asabeneh', 'Python', 'Finland']
print(type(["x", "y", "z"]))
### Your name
print(type("Nick"))
### Your family name
print(type("Lyon"))
### Your country
print(type("I'm enjoying 30 days of python"))

# Exercise: Level 2

## Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

"""
I understand the theory of this but I don't want to make that folder so I'm skipping this exercise.
"""

# Exercise: Level 3

## Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

### Float example
print(type(6.66))

### String example
print(type("goodbye"))

### Boolean example
print(type(False))

### List example
print(type(
    [1, 2, 3]
))

### Tuple example
print(type(
    (1, 2, 3)
))

### Set example
print(type(
    {1, 2, 3}
))

### Dictionary Example
print(type(
    {
        "first": 1,
        "second": 2,
        "third": 3
    }
))

## Find an Euclidian distance between (2, 3) and (10, 8)
"""
Formula is:
Square root of (p1 - q1)^2 + (p2 - q2)^2
"""

# Import needed library
import math

# Use square root function
print( math.sqrt( ((2 - 10) ** 2) + ((3 - 8) ** 2) ) )