# Exercises - List Comprehension

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_nums = [i for i in numbers if i <= 0]
print("1: ", filter_nums)

# 2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
unnest_list = [num for row in list_of_lists for num in row]
flat_list = [num for row in unnest_list for num in row]
print("2: ", flat_list)

# 3. Using list comprehension create the following list of tuples:
# Output: [(0, 1, 0, 0, 0, 0, 0),
#    (1, 1, 1, 1, 1, 1, 1),
#    (2, 1, 2, 4, 8, 16, 32),
#    (3, 1, 3, 9, 27, 81, 243),
#    (4, 1, 4, 16, 64, 256, 1024),
#    (5, 1, 5, 25, 125, 625, 3125),
#    (6, 1, 6, 36, 216, 1296, 7776),
#    (7, 1, 7, 49, 343, 2401, 16807),
#    (8, 1, 8, 64, 512, 4096, 32768),
#    (9, 1, 9, 81, 729, 6561, 59049),
#    (10, 1, 10, 100, 1000, 10000, 100000)]
"""My hangup is I'm not immediately sure how these tuples are related to one another so the expression to generate all of them is unclear to me (rather than generating a list of tuples being the hard bit)"""
tups = [(i, i, i, i, i, i, i ** i) for i in range(7)]
print("3:", tups)

# 4. Flatten the following list to a new list.
## Output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [list(nation) for tup in countries for nation in tup]
print("4: ", flat_countries)

# 5. Change the following list to a list of dictionaries.
## Output: [{'country': 'FINLAND', 'city': 'HELSINKI'},
#    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#    {'country': 'NORWAY', 'city': 'OSLO'}]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [dict(nation) for tup in countries for nation in tup]
print("5: ", dict_countries)

# 6. Change the following list of lists to a list of concatenated strings.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Hello', 'Goodbye')], [('Bill', 'Gates')]]
unnest_names = [list(nation) for tup in countries for nation in tup]
flat_names = [nation for list in unnest_names for nation in list]
print("6: ", flat_names)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.


