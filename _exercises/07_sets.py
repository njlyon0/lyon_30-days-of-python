# Exercises: Level 1

# Make the needed example set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

## 1. Find the length of the set it_companies
print("1-1: ", len(it_companies))

## 2. Add 'Twitter' to it_companiesit_companies
it_companies.add("Twitter")
print("1-2: ", it_companies) 

## 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["co 1", "co 2", "co 3"])
print("1-3: ", it_companies)

## 4. Remove one of the companies from the set it_companies
it_companies.remove("co 1")
print("1-4: ", it_companies)

## 5. What is the difference between remove and discard
print("1-5: ", "The `.discard` method doesn't raise an error if the item is not in the set while the `.remove` method does")

### Exercises: Level 2

# Make the needed example sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

## 1. Join A and B
A_join_B = A.union(B)
print("2-1: ", A_join_B)

## 2. Find A intersection B
A_intersect_B = A.intersection(B)
print("2-2: ", A_intersect_B)

## 3. Is A subset of B
print("2-3: ", "'A is a subset of B' is a ", A.issubset(B), " statement.")

## 4. Are A and B disjoint sets
print("2-4: ", "'A and B are isjoint sets' is a ", A.isdisjoint(B), " statement.")

## 5. Join A with B and B with A
B_join_A = B.union(A)
print("2-5i: ", "A joined with B is: ", A_join_B)
print("2-5ii: ", "B joined with A is: ", B_join_A)

## 6. What is the symmetric difference between A and B
AB_symdiff = A.symmetric_difference(B)
print("2-6: ", "The symmetric difference of A and B is ", AB_symdiff)

## 7. Delete the sets completely
del A
del B
print("2-7: ", "Sets are deleted with the `del` operator")

### Exercises: Level 3

# Make the needed example list
age = [22, 19, 24, 25, 26, 24, 25, 24]

## 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print("3-1: ", "The length of the list is ", len(age), " while the length of the set version of the same contents is ", len(age_set), "\n", "This is because sets can only contain _unique_ items")

## 2. Explain the difference between the following data types: string, list, tuple and set
print("3-2: ", "Strings are a type of value (either a non-number or a number that isn't evaluated in code like a number).", "\n", "Lists are ordered and editable. They allow non-unique items and the items they contain need not be the same type themselves.", "\n", "Tuples are ordered (like lists) but are _not_ editable (unlike lists).", "\n", "Sets can only contain unique items and are editable.")

## 3. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
### The `.split` method is only available to strings
teach_list = "I am a teacher and I love to inspire and teach people".split()
teach_set = set(teach_list)
print("3-3: ", "The sentence 'I am a teacher and I love to inspire and teach people', contains ", len(teach_set), " unique words.")
