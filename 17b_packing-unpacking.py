""" Packing & Unpacking"""

"""Unpacking"""

# We can unpack a list to pass all values for a function as a single variable (when normally the function has several parameters)

# Simple function
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

# Example list
ex_nums = [1, 2, 3, 4, 5]

# Unlist with "*" and run function
sum_of_five_nums(*ex_nums)

# Can also unlist into existing functions
ex_nums = [2, 7]
num_range = range(*ex_nums)
print(list(num_range))

# Can do partial unpacking and assignent to multiple variables if desired
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)

# Though it matters where the "*" is used!
ex_nums = [1, 2, 3, 4, 5, 6, 7]
first, *mid, last = ex_nums
print(first, mid, last)

# Dictionaries can be unpacked with "**"
## Example function
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

## Define dictionary
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}

## Unpack dictionary into function
print(unpacking_person_info(**dct))

"""Packing"""

# While unpacking was useful when we know how many elements we are passing to the function, packing is nice when we don't know how many values to expect (or want to keep our expectations flexible)
## Example function
def sum_all(*vals):
    total = 0
    for k in vals:
        total += k
    return total

## Invoke example function in two different contexts
sum_all(1, 2, 3)
sum_all(1, 2, 3, 4, 5, 6, 7)

# Can also pack dictionaries with the "**" (just like unpacking!)
def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

ex_dict = packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250)
ex_dict

"""Spreading"""

# Can 'spread' lists into a combined list of the same depth
list_one = [1, 2, 3]
list_two = [4, 5, 6, 7]
ex_list = [0, *list_one, *list_two]
ex_list

"""Enumerating"""

# Can 'enumerate' lists to get index positions for each item
for index, item in enumerate(["a", "b", "c"]):
    print(f"{item} is at position {index}")

# Or can identify the index value for a particular list item
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

"""Zip"""

# Lists can be combined while looping across them with "zip"
## Example lists
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

## Empty list for storing output
fruits_and_veges = []

## Loop across both
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

## Which leaves you with...
fruits_and_veges
