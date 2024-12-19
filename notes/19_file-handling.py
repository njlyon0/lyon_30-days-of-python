"""
File Handling

Data are typically stored in non-Python file types. These can however be 'read into' Python environments and then operated on using the principles covered in other scripts in this repo.
"""

# Load 'os' library
import os

# "open" function allows simple interactions with data objects
produce_csv = open(file = os.path.join("ancillary", "produce.csv"), mode = "r")
produce_csv
## Mode can be any of the following:
## 'r' (read - default - error if doesn't exist)
## 'a' (append - creates file if doesn't exist)
## 'w' (write - creates if doesn't exist)
## 'x' (create - error if already exists)
## 't' (text mode - default)
## 'b' (binary mode - e.g., images)

# Once opened, must be read to access
produce = produce_csv.read()
produce

# Then closed when done
produce_csv.close()

# Variables assigned while the file was open persist!
produce

## The "readline" method reads only the first line
produce_csv = open(file = os.path.join("ancillary", "produce.csv"), mode = "r")
produce_csv.readline()
produce_csv.close()

## "readlines" (plural) returns a list of lines
produce_csv = open(file = os.path.join("ancillary", "produce.csv"), mode = "r")
produce_csv.readlines()
produce_csv.close()

## Danger in forgetting to close a file
## Can use "with" to make that automatic
with open(file = os.path.join("ancillary", "produce.csv"), mode = "r") as ex_file:
    ex_lines = ex_file.read().splitlines()
    print(type(ex_lines))
    print(ex_lines)

# The "write" method allows for adding lines to files
with open(file = os.path.join("ancillary", "test.txt"), mode = "w") as demo_file:
    demo_file.write("First line of a new file!")

# And the "remove" function (from the 'os' module) allows for deletion of a file
os.remove(os.path.join("ancillary", "test.txt"))

# If the file doesn't exist the above will raise an error so smart to nest it in a conditional
if os.path.exists(os.path.join("ancillary", "test.txt")):
    os.remove(os.path.join("ancillary", "test.txt"))
    print("File 'test.txt' deleted")
else: 
    print("File 'test.txt' not found")

"""
JSON Files 

JSON (JavaScript Object Notation) files contain key-value pairs -- not unlike a Python dictionary!
"""

# Import "json" library
import json

# Make a demo dictionary as a **docstring**
person_docstr = '''{
    "name" : "Nick",
    "country" : "USA",
    "skills" : ["R", "Quarto", "Python"]
}'''
type(person_docstr)

# Use the "loads" method to make it a true dictionary
person_dict = json.loads(s = person_docstr)
type(person_dict)
print(person_dict)

# Can use the "dumps" method to change a dictionary to a JSON (technically type 'str' but has special indenting / formatting)
person_json = json.dumps(obj = person_dict, indent = 4)
print(person_json)

# Finally, we can export to a JSON file that can be read in / used elsewhere
with open(file = os.path.join("ancillary", "test.json"), mode = "w", encoding = 'utf-8') as ex_json:
    json.dump(obj = person_json, fp = ex_json, ensure_ascii = False, indent = 4)

# Now remove it so it won't get committed on accident
if os.path.exists(os.path.join("ancillary", "test.json")):
    os.remove(os.path.join("ancillary", "test.json"))
    print("File 'test.json' deleted")
else: 
    print("File 'test.json' not found")

"""
CSV Files

CSV (Comma Separated Values) files are a common format for tabular (i.e., 'table-like' with rows/columns) information. While we _can_ read these files in with the built-in "open" function, we can use more purpose-built tools from the "csv" library
"""

# Load needed library
import csv

# Open example produce file
with open(file = os.path.join("ancillary", "produce.csv"), mode = "r") as ex_csv:

    # Read and assign to a variable
    csv_reader = csv.reader(ex_csv, delimiter = ",")

  # Identify column names (i.e., contents of first row)
    for row in csv_reader:
        print(f'Row contents are :{", ".join(row)}')

"""
XLSX Files

Microsoft Excel files can be opened using the same syntax / pattern
"""

# Install relevant library (if not already installed)
## Need to use command line for following code
## python3 -m pip install xlrd

# Import relevant library
import xlrd

# Syntax is as follows:
## excel_book = xlrd.workbook("test.xlsx")
## print(excel_book.nsheets)
## print(excel_book.sheet_names)

"""
XML Files

Extensible Markup Files (XML) look like HTML files in that they are composed of nested 'tags' containing various pieces of information
"""

# Import just the parth of the 'xml' library that we need
import xml.etree.ElementTree as xml_et

# Syntax is as follows:
## xml_tree = xml_et.parse("test.xml")
## xml_root = xml_tree.getroot()
## print("Root tag: ", xml_root.tag)
## print("Attribute: ", xml_root.attrib)
## for xml_child in xml_root:
##     print('Field: ', xml_child.tag)
