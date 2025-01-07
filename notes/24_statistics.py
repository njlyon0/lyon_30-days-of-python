"""
Statistics

"Statistics" is a very broad term that encapsulates a lot of territory but generally contains many tools built to summarize or compare data. These tools are prerequisite to both data science generally and machine learning approaches more specifically.

Python includes a "statistics" module for doing simple mathematical statistics on numeric data. It can be valuable but is not meant to compete with either more nuanced Python packages (e.g., NumPy, SciPy, MatPlotLib, etc.) or standalone non-Python statistical languages (e.g., R, SAS, Matlab, etc.).

These notes are mostly focused on the "numpy" module but delve into the "statistics" module as needed.
"""

# Import needed module(s)
import statistics
import numpy as np

""" NumPy Arrays """

# Make a standard list and convert it to a NumPy "array"
ex_list = [1, 2, 3, 4]
ex_array = np.array(ex_list)
print(ex_array)
print(type(ex_array))

# Demonstrate with a "2D" list too
ex_2d_list = [[0, 1], [2, 3], [4, 5]]
ex_2d_array = np.array(ex_2d_list)
print(ex_2d_array)
print(type(ex_2d_array))

# While coercing to an array, we can change the data type
## To float
print(np.array(ex_list, dtype = float))

## To boolean
print(np.array([1, 0, -1, 0], dtype = bool))

# You can also use the "astype" method to change the type of the data after creating the array
ex_array.astype(dtype = "str")

# The "tolist" method converts NumPy arrays into lists
new_list = ex_array.tolist()
print(type(new_list))
print(new_list)

# The "shape" attribute specifies the dimensionality of a NumPy array
## First number is "rows", second is "column"
ex_2d_array
ex_2d_array.shape

# The "dtype" attribute identifies the data type stored in the array
ex_2d_array.dtype

# The "size" attribute tells us the number of items contained in the array
ex_2d_array.size

""" Arithmetic on NumPy Arrays """

# Basic arithmetic operations are supported on arrays
ex_array + 10
ex_array - 8
ex_array * 3
ex_array / 4
ex_array % 2
ex_array ** 2

""" Accessing Items in Arrays """




