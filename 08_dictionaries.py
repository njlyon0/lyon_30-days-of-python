"""
Dictionaries are a type of data that is editable, is not ordered, and contains paired (key/value) information.
"""

# Creating a dictionary can use the `dict` function
ex_dict = dict()
print(type(ex_dict))

# They can also be created with curly braces (like sets) so long as keys and values are both supplied
ex_dict = {"key1":"value1", "key2":"value2"}
print(type(ex_dict))
## Like lists, the values part of dictionaries can be any type (including additional dictionaries)

# The `len` function identifies the number of key/value pairs
print(len(ex_dict))

# Bracket notation can be used to extract the value associated with the named key
print(ex_dict["key2"])

# This approach raises an error if the specified key does not exist so we can instead use the ".get" method which returns "None" if the key doesn't exist
print(ex_dict.get("key1"))
print(ex_dict.get("fake_key"))

# Items can be added to a dictionary with bracket notation for the new key name via simple assignment
ex_dict["key3"] = "value3"
print(ex_dict)

# Items can be modified via simple assignment to an existing key name
ex_dict["key1"] = "first_value"
print(ex_dict)

# As with other data types, dictionaries support the `in` operator for identifying whether a specified key is found in the dictionary
print("key5" in ex_dict)
print("key2" in ex_dict)

# Items can be removed by the ".pop" method--with specified key name--, with ".popitem" for the last key/value pair, or via the `del` operator--again, with specified key name
## Delete with 'pop'
ex_dict.pop("key1")
print(ex_dict)

## Re-add
ex_dict["key1"] = "value1"

## Delete with popitem
ex_dict.popitem()
print(ex_dict)

## Re-add
ex_dict["key1"] = "value1"

## Delete with `del`
del ex_dict["key1"]
print(ex_dict)

## Re-add
ex_dict["key1"] = "value1"

# Can change a dictionary's contents to a list of tuples with the ".items" method
ex_dict_tup = ex_dict.items()
print(ex_dict_tup)

# Like sets, the ".clear" method empties the specified dictionary
print(ex_dict.clear())

# Dictionaries can be copied with the ".copy" method
ex_dict = {"key1":"value1", "key2":"value2", "key3":"value3"}
ex_dict_copy = ex_dict.copy()
print(ex_dict_copy)

# Or deleted via the `del` operator
del ex_dict_copy

# Key names can be extracted with the "keys" method and returned as a list
ex_keys = ex_dict.keys()
print(type(ex_keys))
print(ex_keys)

# You can do the converse operation--i.e., extract values only as a list--with the "values" method
ex_vals = ex_dict.values()
print(type(ex_vals))
print(ex_vals)
