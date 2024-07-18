## Exercises: Level 1

# 1. Declare an empty list
empty_list = []
print("1: ", empty_list)

# 2. Declare a list with more than 5 items
big_list = [1, 2, 3, 4, 5, 6, 7]
print("2: ", big_list)

# 3. Find the length of your list
print("3: ", len(big_list))

# 4. Get the first item, the middle item and the last item of the list
print("4: ", big_list[::3])
print("4: ", big_list[0], big_list[3], big_list[6])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["NL", 30, 5.9, False, "xxx"]
print("5: ", type(mixed_data_types))

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("6: ", it_companies)

# 7. Print the list using _print()_
print("7: ", it_companies)

# 8. Print the number of companies in the list
print("8: ", len(it_companies))

# 9. Print the first, middle and last company
print("9: ", it_companies[0], it_companies[int(len(it_companies)/2)], it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = "Meta"
print("10: ", it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Fake Co")
print("11: ", it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(3, "Faux Inc")
print("12: ", it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()
print("13: ", it_companies)

# 14. Join the it_companies with a string '#;&nbsp; '
joined_str = ' / '.join(it_companies)
print("14: ", joined_str)

# 15. Check if a certain company exists in the it_companies list.
print("15: ", "Google" in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print("16: ", it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print("17: ", it_companies)
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
it_short = it_companies.copy()
it_short = it_short[3:len(it_short)]
print("18: ", it_short)

# 19. Slice out the last 3 companies from the list
it_short = it_companies.copy()
it_short = it_short[0:len(it_short) - 3]
print("19: ", it_short)

# 20. Slice out the middle IT company or companies from the list
it_short = it_companies.copy()
it_short.pop(int(len(it_short) / 2))
print("20: ", it_short)

# 21. Remove the first IT company from the list
it_short = it_companies.copy()
it_short.pop(0)
print("21: ", it_short)

# 22. Remove the middle IT company or companies from the list
it_short = it_companies.copy()
it_short.remove("Google")
print("22: ", it_short)

# 23. Remove the last IT company from the list
it_short = it_companies.copy()
it_short.pop(len(it_short) - 1)
print("23: ", it_short)

# 24. Remove all IT companies from the list
it_empty = it_companies.copy()
it_empty.clear()
print("24: ", it_empty)

# 25. Destroy the IT companies list
it_del = it_companies.copy()
del it_del

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
both_ends = front_end + back_end
print("26: ", both_ends)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = both_ends.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print("27: ", full_stack)

## Exercises: Level 2

# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Sort the list and find the min and max age
ages.sort()
print("1A: ", "min age is ", ages[0], "; max age is ", ages[-1])

# - Add the min age and the max age again to the list
ages.insert(0, ages[0])
ages.append(ages[-1])
print("1B: ", ages)

# - Find the median age (one middle item or two middle items divided by two)
median_age = (ages[5] + ages[6]) / 2
print("1C: ", median_age)

# - Find the average age (sum of all items divided by their number )
mean_age = sum(ages) / len(ages)
print("1D: ", mean_age)

# - Find the range of the ages (max minus min)
ages.sort()
age_range = ages[-1] - ages[0]
print("1E: ", age_range)

# - Compare the value of (min - average) and (max - average), use _abs()_ method
age_min_mean_diff = ages[0] - mean_age
age_max_mean_diff = ages[-1] - mean_age
print("1F: ", abs(age_min_mean_diff), abs(age_max_mean_diff))

# 2. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
countries = ["orange", "apple", "banana", "lemon", "lime"]
print("2: ", countries[int(len(countries) / 2)])

# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
"""Skipping. Conditionals not covered until day 9"""

# 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = countries
print("4: ", scandic)
