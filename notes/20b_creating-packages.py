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




