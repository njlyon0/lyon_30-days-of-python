"""
Modules are files containing groups of functions so that they can be easily imported to an application. Such files may include anything from a single variable all the way to a large codebase

Modules can be easily created by saving the desired module content as a .py file
"""

# Existing modules can be loaded with the 'import' keyword
## To keep my directories clean I put 'demo_module.py' in a folder named 'ancillary'
from ancillary import demo_module as demo

# Then the content they include can be invoked my namespacing the module name
print(demo.generate_full_name("Nick", "Lyon"))

# Can use multiple variables defined in the same module!
print(demo.sum_two_nums(1, 2))
print("Gravity constant defined as ", demo.gravity)
print(demo.person["firstname"])

# Can alias components of a module during the import phase if the module isn't in a subdirectory(?)
## E.g., `from demo_module import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g`

# Some formal Python modules/packages exist and can be loaded for easy access to the tools that they contain

# OS (Operating System) module
import os
os.getcwd()

# The 'sys' module affects the Python runtime environment
import sys
sys.version

# The 'statistics' module includes fundamental mathematical operations
## Import all bits of that module
import statistics as stats

## Make an integer list
num_list = [1, 2, 3, 4, 5]

## Summarize it in various ways
print(stats.stdev(num_list))
print(stats.median(num_list))

# The 'math' module includes mathematical operations and constants
import math
print(math.pi)
print(math.sqrt(4))

# The 'string' module has nice methods for working with strings
import string
print(string.ascii_letters)

# The 'random' module allows for rando number generation
import random
print(random.random()) # random float between 0 and 0.9999 repeating
print(random.randint(1, 5))
