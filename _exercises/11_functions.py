# Exercises: Level 1

## 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b

add_two_numbers(a = 1, b = 1)

## 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
def area_of_circle(r):
    pi = 3.14
    return pi * r * r

area_of_circle(r = 1)

## 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for x in nums:
        total += x
    return total

add_all_nums(1, 2, 3)

## 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
def convert_celsius_to_fahrenheit(c):
    f = (c * (9/5)) + 32
    return f

convert_celsius_to_fahrenheit(c = 0)

## 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):

    month_low = month.lower()

    if month_low in "September October November".lower().split():
        return "autumn"
    elif month_low in "December January February".lower().split():
        return "winter"
    elif month_low in "March April May".lower().split():
        return "spring"
    elif month_low in "June July August".lower().split():
        return "summer"
    else: 
        return "Unrecognized month!"

check_season(month = "JANUARY")
check_season("july")

## 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

calculate_slope(x1 = 0, y1 = 0, x2 = 1, y2 = 1)

## 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
"""This is not a test of function comprehension -- skipping"""

## 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for item in list:
        print(item)

print_list(list = [1, 2, 3])

## 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lt):
    rev_list = list()
    for index in reversed(range(len(lt))):
        item = lt[index]
        rev_list.append(item)
    return(rev_list)

reverse_list(lt = [1, 2, 3, 4, 5])
reverse_list(lt = ["A", "B", "C"])

## 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lt):
    upper_list = list()
    for index in range(len(lt)):
        item = lt[index]
        upper_list.append(item.upper())
    return upper_list

capitalize_list_items(lt = ["hello", "bye bye"])

## 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lt, item):
    lt.append(item)
    return lt

add_item(lt = ['Potato', 'Tomato', 'Mango', 'Milk'], item = 'Meat')
add_item(lt = [1, 2, 3], item = 4)

## 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lt, item):
    lt.remove(item)
    return lt

remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango')
remove_item([2, 3, 7, 9], 3)

## 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(max_num):
    total = 0
    for val in range(max_num + 1):
        total += val
    return total

sum_of_numbers(5)
sum_of_numbers(100)

## 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(max_num):
    total_odds = 0
    for val in range(max_num + 1):
        if val % 2 != 0:
            total_odds += val
    return total_odds

sum_of_odds(5)

## 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
"""Redundant with question 14 -- skipping"""

# Exercises: Level 2

## 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(max_num):
    even_list = list()
    odd_list = list()
    for val in range(max_num + 1):
        if val % 2 == 0:
            even_list.append(val)
        else: 
            odd_list.append(val)
    even_ct = len(even_list)
    odd_ct = len(odd_list)
    return even_ct, odd_ct

evens_and_odds(max_num = 100)

## 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(x):
    result = 1
    while x > 1:
        result = result * (x * (x - 1))
        x -= 2
    return result

factorial(x = 5)
factorial(x = 3)

## 3. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
def is_empty(var):
    if len(var) == 0:
        return True
    return False

is_empty(var = list())
is_empty(var = "hello")

## 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
"""Again, not a test of function comprehension -- skipping."""

# Exercises: Level 3

## 1. Write a function called is_prime, which checks if a number is prime.


## 2. Write a functions which checks if all items are unique in the list.


## 3. Write a function which checks if all the items of the list are of the same data type.


## 4. Write a function which check if provided variable is a valid python variable


## 5. Go to the data folder and access the countries-data.py file.

# - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

