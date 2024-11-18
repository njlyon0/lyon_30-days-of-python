"""
Type Errors

Python--like many coding languages--can signal failure to run code via "errors". Understanding these is a key component to debugging code (i.e., resolving errors so the code can run)
"""

"""Syntax Error"""
# >>> print "hello"
#   File "<stdin>", line 1
#     print "hello"
#     ^^^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("hello")


"""Name Error"""
# >>> print(age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'age' is not defined
age = 30
print(age)

"""Index Error"""
# >>> numbers = [1, 2, 3]
# >>> numbers[4]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
numbers = [1, 2, 3]
numbers[2]

"""Module Not Found Error"""
# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
import math

"""Attribute Error"""
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
import math
math.pi

"""Key Error"""
# >>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
# >>> users["home"]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'home'
users = {'name':'Asab', 'age':250, 'country':'Finland'}
users["country"]

"""Type Error"""
# >>> 4 + "3"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
"4" + "3"
4 + 3

"""Import Error"""
# >>> from math import power
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'power' from 'math' (/Users/lyon/anaconda3/lib/python3.11/lib-dynload/math.cpython-311-darwin.so)
from math import pow

"""Value Error"""
# >>> int("1o")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '1o'
int("10")

"""Zero Division Error"""
# >>> 1/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
