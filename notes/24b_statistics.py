"""
Statistics

"Statistics" is a very broad term that encapsulates a lot of territory but generally contains many tools built to summarize or compare data. These tools are prerequisite to both data science generally and machine learning approaches more specifically.

Python includes a "statistics" module for doing simple mathematical statistics on numeric data. It can be valuable but is not meant to compete with either more nuanced Python packages (e.g., NumPy, SciPy, MatPlotLib, etc.) or standalone non-Python statistical languages (e.g., R, SAS, Matlab, etc.).

These notes are mostly focused on the "numpy" module but delve into the "statistics" module as needed.
"""

# Import needed module(s)
import statistics
import numpy as np
import matplotlib as mpl
import seaborn as sb
import scipy

# Sample an array of values from a normal distribution
ex_normal = np.random.normal(100, 15, size = (3, 2))
ex_normal

""" Simple Summary Statistics """

# Can get various summary statistics from an array using relevant methods
ex_normal.min()
ex_normal.max()
ex_normal.mean()
ex_normal.std()

# Median requires a function rather than a method
np.median(a = ex_normal)

# A multi-dimensional array can easily be summarized by column or by row
ex_normal
## By row
np.min(a = ex_normal, axis = 1)
## By column
np.amax(a = ex_normal, axis = 0)

# Some non-numpy packages are also useful
scipy.stats.mode(ex_normal)

""" Linear Algebra """

# Two simple arrays to demonstrate the following
a1 = np.array(object = [1, 2, 3])
a2 = np.array(object = [4, 5, 6])

# Calculate dot product (of two arrays)
np.dot(a = a1, b = a2)

# Create two simple matrix-like arrays too
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[1, 2], [3, 4]])
m1
m2

# Can perform matrix multiplication too
np.matmul(m1, m2)
