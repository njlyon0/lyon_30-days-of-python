"""
Python data can include different categories of information.
This is referred to as the "type" of the data.

Examples include:
"""

# Integer
print(type(5))

# Float (non-integer numbers)
print(type(3.14))

# String (characters wrapped with single/double quotes)
print(type("hello"))
print(type("52"))

# Booleans (logical values)
## Capitalization **does** matter!
print(type(True))

"""
Python can also store multiple separate values as a "list"
This is a different "type" of variable.

Lists are defined by square brackets where each "item" in the list is separated by a comma
Lists are _inherently ordered_
"""

# Demo a list
print(type([1, 2, 3, 4]))

# Note that lists can support multiple data types
print(type(["hello", "goodbye", 4000]))

"""
Another type of variable is a "dictionary"
They support data in 'key-value pair' format

Dictionaries are defined by curly braces where each key-value pair is separated from the others by a comma.
Within each key-value pair the key is on the left and is separated from the value by a comma
"""

# Demo a dictionary
print(type(
    {
        "first_name": "Nick",
        "last_name": "Lyon",
        "is_having_fun": True,
        "skills": ["R (advanced)", "Python (beginner)"]
    }
))

"""
Python also supports "tuples" ([TWO-pull])
They are defined with parentheses and each item is separated by a comma
Similar to a list in that they are ordered but **they are not editable after they are created**
"""

# Demo a tuple
print(type(
    (
        "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"
    )
))

"""
Finally (for now), are "sets"
A set is not ordered and is created with curly braces (similar to a dictionary).

A set can only store unique values
"""

# Demo a set
print(type(
    {2, 3, 4}
))