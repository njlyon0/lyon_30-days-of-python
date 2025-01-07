# 1. Declare your age as integer variable
age = 30
print(type(age))

# 2. Declare your height as a float variable
height = 5.9
print(type(height))

# 3. Declare a variable that store a complex number
complex_num = 4j
print(type(complex_num))

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
"""
## Accept inputs (and coerce to floating points)
tri_base = float(input("Enter the length of the base of the triangle"))
tri_height = float(input("Enter the height of the triangle"))

## Do math
tri_area = tri_base * tri_height * 0.5

## Return result
print("The area of the specified triangle is", tri_area)
"""

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
"""
## Accept inputs / coerce to correct type
tri_side_one = float(input("Enter the length of the first side: "))
tri_side_two = float(input("Enter the length of the second side: "))
tri_side_three = float(input("Enter the length of the third side: "))

## Do math
tri_perim = tri_side_one + tri_side_two + tri_side_three

## Return result
print("The perimeter of that triangle is", tri_perim)
"""

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""
rect_len = float(input("Enter the length of the rectangle: "))
rect_wid = float(input("Enter the width of the rectangle: "))
rect_perim = 2 * (rect_len + rect_wid)
print("The specified rectangle has a perimeter of: ", rect_perim)
"""

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
"""
circle_rad = float(input("Enter the radius of the circle: "))
pi = 3.14
circle_circum = 2 * pi * circle_rad
circle_area = pi * (circle_rad ** 2)
print("The area of the circle is ", circle_area, 
      " and its circumference is ", circle_circum)
"""

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
"""
Slope is 2
y-intercept is -2
x-intercept is 1

Not sure how we'd 'calculate' that in Python
"""

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope = (10 - 2) / (6 - 2)
import math
euc_dist = math.sqrt( ((2 - 6) ** 2) + ((2 - 10) ** 2) )
print("Slope is ", slope, " and Euclidean distance is ", euc_dist)

# 10. Compare the slopes in tasks 8 and 9.
"""
Same slope!
"""

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
"""
Skipping (seems like a math question more than really a coding challenge)
"""

# 12. Find the length of 'python' and 'dragon' and make a false comparison statement.
print(len("python") != len("dragon"))

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

# 14. "I hope this course is not full of jargon". Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")

# 15. There is no 'on' in both dragon and python
print("on" not in "python" and "on" not in "dragon")

# 16. Find the length of the text python and convert the value to float and convert it to string
test_len = len("python")
test_float = float(test_len),
test_str = str(test_float)
print(type(test_str))

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
my_num = 6
print(my_num, "is even: ", ((my_num % 2) == 0))

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 / 3)
print(int(2.7))
print((7 / 3) == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print(type("10") == type(10))

# 20. Check if int('9.8') is equal to 10
print(int(9.8) == 10)

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""
person_hour = float(input("Enter your weekly hours: "))
person_pay = float(input("Enter your hourly pay: "))
person_wage = person_hour * person_pay
print("Your weekly earning is: $", person_wage)
"""

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
"""
person_age = float(input("Enter the number of years you've lived: "))
person_life_yr = 100 - person_age
person_life_sec = person_life_yr * 60 * 60
print("You have ", person_life_sec, " seconds remaining in your life (likely)")
"""

# 23. Write a Python script that displays the following table
"""
I don't think we know how to do this at this point...
"""