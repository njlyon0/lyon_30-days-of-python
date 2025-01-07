# Exercises - Higher Order Functions

## Assign neded demo variables
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Exercises: Level 1

# 1. Explain the difference between map, filter, and reduce.
"""
All three accept a function and an interable. Map returns an iterable of the same length as the input, filter returns only those items that evalue to `True`, and reduce returns a single value
"""

# 2. Explain the difference between higher order function, closure and decorator
"""
Higher order functions (HOFs) are those that can accept functions as inputs or return a function as an output. Closures and decorators are types of HOFs. Closures are nested functions where the 'inner' function can access the variables declared in the 'outer' function. Decorators add functionality to existing functions but don't modify the fundamental structure of those functions
"""

# 3. Define a call function before map, filter or reduce, see examples.
"""This is not sufficiently explained for 'call function' to mean something specific to me"""

# 4. Use for loop to print each country in the countries list.
for nation in countries:
    print(nation)

# 5. Use for to print each name in the names list.
for nm in names:
    print(nm)

# 6. Use for to print each number in the numbers list.
for val in numbers:
    print(val)

## Exercises: Level 2

# 1. Use map to create a new list by changing each country to uppercase in the countries list
result = list(map(lambda k: k.upper(), countries))
print("2-1: ", result)

# 2. Use map to create a new list by changing each number to its square in the numbers list
result = list(map(lambda n: n ** 2, numbers))
print("2-2: ", result)

# 3. Use map to change each name to uppercase in the names list
result = list(map(lambda k: k.upper(), names))
print("2-3: ", result)

# 4. Use filter to filter out countries containing 'land'.
result = list(filter(lambda j: not "land" in j, countries))
print("2-4: ", result)

# 5. Use filter to filter out countries having exactly six characters.
result = list(filter(lambda l: len(l) != 6, countries))
print("2-5: ", result)

# 6. Use filter to filter out countries containing six letters and more in the country list.
result = list(filter(lambda l: len(l) < 6, countries))
print("2-6: ", result)

# 7. Use filter to filter out countries starting with an 'E'
result = list(filter(lambda o: not o[0] == "E", countries))
print("2-7: ", result)

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))


# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.


# 10. Use reduce to sum all the numbers in the numbers list.
import functools
result = functools.reduce(lambda x, y: int(x) + int(y), numbers)
print("2-10: ", result)

# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries


# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js. (eg 'land', 'ia', 'island', 'stan')).


# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.


# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.


# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

# ### Exercises: Level 3

# 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#    - Sort countries by name, by capital, by population
#    - Sort out the ten most spoken languages by location.
#    - Sort out the ten most populated countries.


