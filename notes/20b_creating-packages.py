"""
Creating a Package

We can create our own packages by creating a folder with some conserved formatting elements. We'll create those below before demonstrating how to use that package.
"""

# Load needed packages
import os

# Define package name
pkg_name = "my_package"

# Make package folder (if it doesn't exist already)
if os.path.exists(path = pkg_name) == False:
    os.mkdir(pkg_name)
    print("Created folder '", pkg_name, "'.")
else:
    print("Folder '", pkg_name, "' already exists")

# Make the needed file(s)
file_init = open(file = os.path.join(pkg_name, "init.py"), mode = "w")
file_init.close()

# Creating scripts (i.e., modules) manually
## arithmetic.py
## greet.py

# Can then import as normal
from my_package import arithmetic

# And use the functions contained there!
arithmetic.subtract(5, 3)

