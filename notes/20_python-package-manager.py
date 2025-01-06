"""
Python Package Manager

PIP (Preferred Installer Program) is used to install Python packages. These packages consist of one or more modules that can be imported into relevant scripts. This allows fundamental operations to be loaded from an existing package rather than defined by every programmer every time they write a new script.

Can check the version of PIP with the command line snippet `pip --version`
"""

# Install the "numpy" package
## python3 -m pip install numpy

# Once installed, can import the relevant module(s) and use their tools
import numpy

## Check version
numpy.version.version

## Some demo operations
ex_list = [1, 2, 3, 4, 5]
np_array = numpy.array(ex_list)
np_array * 2
np_array + 4

# Another important package is "pandas"
## python3 -m pip install pandas

# Import it
import pandas as pd

# The "webbrowser" module is built in to Python3 (i.e., doesn't need to be installed) and allows operations with websites
import webbrowser

## Make list of URLs
url_list = [
    "https://github.com/njlyon0",
    "https://www.linkedin.com/in/nicholasjlyon/"
]

## Loop across list items and open in a new tab
for site in url_list:
    webbrowser.open_new_tab(url = site)

""" Uninstalling Packages """

# Can uninstall unwanted packages via the following command line snippet:
## python3 -m pip uninstall PACKAGENAME

""" Listing Packages """

# Can list installed packages with this snippet:
## python3 -m pip list

""" Package Information """

# Get some critical information about a given package like so:
## python3 -m pip show --verbose PACKAGENAME

""" PIP Freeze """

# To get a list of installed packages and their versions in a format suitable for a "requirements.txt" file use this snippet:
## python3 -m pip freeze

"""
Reading From URL

Sometimes we want to read data from a website or via an API (Application Program Interface). We can use the "requests" package to get some useful tools for this. Many of its operations return JSON-style data that we can implement CRUD operations (create, read, update, delete).
"""

# Install via command line
## python3 -m pip install requests

# Import it
import requests as rq
## Note their is a warning about this module when used on MacOS
## See the following GH issue for more info: https://github.com/urllib3/urllib3/issues/3020

# Access a URL
url = "https://github.com/njlyon0/lyon_30-days-of-python"
url_response = rq.get(url = url)

# Check out various bits of returned information
print(url_response)
print(url_response.status_code)
print(url_response.headers)
print(url_response.text)
