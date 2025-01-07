"""
NumPy Module

The "numpy" module is broadly useful for a lot of statistical tools. Below is a quick review of some of the core operations in this package with a strong emphasis on the "array" data type.
"""

# Import needed module(s)
import numpy as np

""" NumPy Array Fundamentals """

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

# Remind self about the 2D array structure
ex_2d_array

# Can access particular rows in an array
ex_2d_array[0,:]
ex_2d_array[1,:]
ex_2d_array[2,:]

# Or access particular columns
ex_2d_array[:,0]

# Or even particular cell coordinates (i.e., row / column combinations)
ex_2d_array[1, 1]

# A number by itself (without a comma) is implicitly a column number
ex_2d_array[1]

""" Reshaping Arrays """

# Can reshape arrays with "reshape" method by specifying the desired number of rows/columns
## Note that the new shape still needs to have the same size as the starting shape
ex_2d_array
ex_2d_array_v2 = ex_2d_array.reshape(2, 3)
ex_2d_array_v2

# You can also simply use the "flatten" method to collapse a multi-dimensional array into a flat one
ex_array_flat = ex_2d_array.flatten()
ex_array_flat

""" Combining Arrays """

# Can combine arrays relatively easily, let's make two demo arrays to show this
ar1 = np.array([1, 2, 3])
ar2 = np.array([4, 5, 6])

# Arithmetic is performed element by element while conserving shape and size
ar1 + ar2
ar1 / ar2

# Stacking horizontally is done with the "hstack" function
## Though you do need to make a tuple containing the arrays to combine
np.hstack(tup = (ar1, ar2))

# Can also stack vertically by the "vstack" function
np.vstack(tup = (ar1, ar2))

""" Random Numbers """

# Can generate one or more random floats
np.random.random(size = 1)
np.random.random(size = 3)

# Or generate one or more random integers within a specified range
## Note that the 'low' number *is* included but the 'high' end of the range *is not*
np.random.randint(low = 0, high = 10)
np.random.randint(low = 1, high = 3, size = 5)

# And if you specify the size as a tuple, the set of random values are returned as an array
np.random.randint(low = 0, high = 2, size = (2, 2))

# Can grab random values from a known normal distribution as well
## Syntax is `...normal(mean, variance, size)`
np.random.normal(50, 12, size = 15)

""" NumPy Matrices """

# Make a matrix of values
ex_matrix = np.matrix(data = np.ones(shape = (4, 4), dtype = "float"))
ex_matrix

# Can make the matrix into an array with the "asarray" function
ex_array = np.asarray(a = ex_matrix)
ex_array
