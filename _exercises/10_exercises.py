# Exercises: Level 1

## 1. Iterate 0 to 10 using for loop, do the same using while loop.
### For loop
for i in range(11):
    print("1-1A: ", i)
### While loop
i = 0
while i <= 10:
    print("1-1B: ", i)
    i = i + 1

## 2. Iterate 10 to 0 using for loop, do the same using while loop.
### For loop
for i in reversed(range(11)):
    print("1-2A: ", i)
### While loop
i = 10
while i >= 0:
    print("1-2B: ", i)
    i = i - 1

## 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
##    ```py
##      #
##      ##
##      ###
##      ####
##      #####
##      ######
##      #######
##    ```

for i in range(8):
    if i == 1:
        print("1-3: ", "#")
    elif i == 2:
        print("1-3: ", "##")
    elif i == 3:
        print("1-3: ", "###")
    elif i == 4:
        print("1-3: ", "####")
    elif i == 5:
        print("1-3: ", "#####")
    elif i == 6:
        print("1-3: ", "######")
    elif i == 7:
        print("1-3: ", "#######")

# 4. Use nested loops to create the following:
##    ```py
##    # # # # # # # #
##    # # # # # # # #
##    # # # # # # # #
##    # # # # # # # #
##    # # # # # # # #
##    # # # # # # # #
##    # # # # # # # #
##    # # # # # # # #
##    ```
for i in range(9):
    print("1-4: ", "# # # # # # # #")

## 5. Print the following pattern:
##    ```py
##    0 x 0 = 0
##    1 x 1 = 1
##    2 x 2 = 4
##    3 x 3 = 9
##    4 x 4 = 16
##    5 x 5 = 25
##    6 x 6 = 36
##    7 x 7 = 49
##    8 x 8 = 64
##    9 x 9 = 81
##    10 x 10 = 100
##    ```
for i in range(11):
    print("1-5: ", i, " x ", i, " = ", i**2)

## 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lang_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in lang_list:
    print("1-6: ", language)

## 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print("1-7: ", i)
    else: 
        continue

## 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print("1-8: ", i)
    else: 
        continue

# Exercises: Level 2
    
## 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.
n = 0
for i in range(101):
    n = n + i
    if i == 100:
        print("2-1: ", "The sum of all numbers from 0 to 100 is ", n)

## 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
e = 0
o = 0
for i in range(101):
    if i % 2 == 0:
        e = e + i
    elif i % 2 != 0:
        o = o + i
    if i == 100:
        print("2-2: ", "The sum of all even numbers from 0 to 100 is ", e, ". The sum of all odds is ", o)

# Exercises: Level 3

## 1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
import os
exec(open(os.path.join("ancillary", "countries-list.py")).read())
for nation in countries: # type: ignore (warning is incorrect because of above line)
    if "land" in nation:
        print("3-1: ", nation)

## 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_rev = list()
for f in [3, 2, 1, 0]:
    fruits_rev.append(fruits[f])
print("3-2: ", fruits, " reversed is ", fruits_rev)

## 3. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file.

"""
This is an interesting problem but because I don't know how to actually read in the giant dictionary in "countries-data.py" I cannot attempt to solve it.

My work around for the first question of this level of exercises doesn't work for this one for some reason.

It does seem like an interesting problem though so I'm taking a subset of the dictionary and adding it directly to this script.
"""

country_dict = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    }
]

### 1. What are the total number of languages in the data
lang_list = list()

for nation_i in range(len(country_dict)):
    if "languages" in country_dict[1].keys():
        lang_list.append(country_dict[nation_i].get("languages").values())
    else: 
        continue

print("3-1: ",  lang_list)

"""
Close but would need to figure out nestedness of resulting list to coerce to a set (for removing non-unique elements).

An answer key would be a big help right around now...
"""

### 2. Find the ten most spoken languages from the data
### 3. Find the 10 most populated countries in the world

"""
Skipping 2 and 3 (for now at least) because they are kind of a nest of interrelated concepts that are badly explained in the day's contents (i.e., assume a much higher level of background knowledge than is provided in the markdown file)
"""
