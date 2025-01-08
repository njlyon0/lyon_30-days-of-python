"""
Pandas Module

The pandas module is a powerful way of working tabular data in python. Specific tools include those aimed at changing data shape, merging separate data tables, sorting data, slicing data, and aggregating data to name a few.

Pandas is based on "DataFrames" and "Series"

- Series = a single column
- DataFrame = data object containing multiple columns
"""

# Import pandas
import pandas as pd
import numpy as np
import os

# Demo data objects
ex_list = [1, 2, 3, 4, 5]
ex_dict = { "name":"Nick", "country":"USA", "languages":["R", "Python"]}
ex_multilist = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]

""" Creating Series & DataFrames """

# Series can be created from a list
ex_ser = pd.Series(data = ex_list)
ex_ser
type(ex_ser)

# Or from a dictionary
ex_ser2 = pd.Series(data = ex_dict)
ex_ser2
type(ex_ser2)

# A DataFrame can be created directly from a list of list
ex_df = pd.DataFrame(data = ex_multilist, columns = ["Name", "Country", "City"])
ex_df
type(ex_df)

""" Pandas + CSVs """

# Can read data from a CSV file into python with Pandas
ex_df2 = pd.read_csv(os.path.join("ancillary", "weight_height.csv"))
ex_df2

# Can then check out the first or last few rows (i.e., the "head"/"tail" of the data respectively)
ex_df2.head(5)
ex_df2.tail(2)

# The "shape" attribute identifies the number of rows/columns
ex_df2.shape

# The "columns" attribute returns a list of column names
ex_df2.columns

# Specific columns can be accessed via their name
## Note this converts them to a series
ex_df2["Height"]
type(ex_df2["Weight"])

# The "describe" method returns simple summary statistics for float/integer columns
ex_df2.describe()

""" Working with DataFrames """

# Let's convert a list of dictionaries to a DataFrame
dict_list = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}
]
df = pd.DataFrame(data = dict_list)
print(df)

# We can add columns by accessing a column that doesn't (yet) exist and assigning a list with as many items as there are rows
df["Weight"] = [74, 78, 69]
df["Height"] = [173, 175, 169]
df

# Once columns exist, we can edit them and overwrite their original state
df["Height"] = df["Height"] * 0.01
df

# And calculate new columns from existing ones
df["BMI"] = round(df["Weight"] / (df["Height"] ** 2), ndigits = 2)
df

# Let's add some more new columns
df["Birth Year"] = [1969, 1985, 1990]
df["Current Year"] = 2025
df["Age"] = df["Current Year"] - df["Birth Year"]
df

# We can access the "dtype" attribute of a series (or "dtypes" for a DataFrame) to identify the type of data in each column
df.dtypes
df["Current Year"].dtype

# And we can coerce a series to a different type with the "astype" method
df["Weight"].dtype
df["Weight"] = df["Weight"].astype(dtype = "float")
df["Weight"].dtype

# We can also filter the data to only rows that meet certain criteria
## This is also known as "boolean indexing"
df[df["Age"] <= 40]
df[df["Name"] != "John"]
