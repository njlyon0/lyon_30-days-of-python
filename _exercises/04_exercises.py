# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
ex_string = ["Thirty", "Days", "Of", "Python"]
print("1:", " ".join(ex_string))

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
ex_string = ["Coding", "For", "All"]
print("2:", " ".join(ex_string))

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print("4:", company)

# 5. Print the length of the company string using len() method and print().
print("5:", len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print("6:", company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print("7:", company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print("8A:", company.capitalize())
print("8B:", company.title())
print("8C:", company.swapcase())

# 9. Cut (slice) out the first word of Coding For All string.
print("9:", company[0:7])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("10:", company.lower().startswith("coding"))

# 11. Replace the word 'coding' in the string 'Coding For All' to Python.
print("11:", company.replace("Coding", "Python"))

# 12. Change 'Python for Everyone' to 'Python for All' using the replace method or other methods.
print("12:", "Python for Everyone".replace("Everyone", "All"))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print("13: ", company.split(" "))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("14: ", "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))

# 15. What is the character at index 0 in the string Coding For All.
print("15: ", company[0:1]) # "C"

# 16. What is the last index of the string Coding For All.
print("16: ", company[::-1][0:1]) # "l"

# 17. What character is at index 10 in "Coding For All" string.
print("17: ", company[10:11]) # " "

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("18: ", "Python for Everyone".replace("Python for Everyone", "PfE"))

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
print("19: ", "Coding For All".replace("Coding For All", "CfA"))

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print("20: ", company.find("C"))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print("21: ", company.find("F"))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("22: ", company.rfind("l"))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
ex_string = "You cannot end a sentence with because because because is a conjunction"
print("23: ", ex_string.find("because"))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("24: ", ex_string.rindex("because"))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("25: ", ex_string.replace("because ", ""))

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""Skipping; duplicate of 23"""

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""Skipping; duplicate of 25"""

# 28. Does ''Coding For All' start with a substring Coding?
print("28: ", company.lower().startswith("coding"))

# 29. Does 'Coding For All' end with a substring coding?
print("29: ", company.lower().endswith("coding"))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("30: ", "   Coding For All      ".strip(" "))

# 31. Which one of the following variables return True when we use the method isidentifier():
## 30DaysOfPython
## thirty_days_of_python
print("31A: ", "30DaysOfPython".isidentifier()) # False - begins with number
print("31B: ", "thirty_days_of_python".isidentifier()) # True - okay variable name

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print("32: ", " # ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33. Use the new line escape sequence to separate the following sentences.
## I am enjoying this challenge.
## I just wonder what is next.
print("33: \nI am enjoying this challenge.\nI just wonder what is next.")

# 34. Use a tab escape sequence to write the following lines.
## Name      Age     Country   City
## Asabeneh  250     Finland   Helsinki
print("34: \nName\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 35. Use the string formatting method to display the following:
## radius = 10
## area = 3.14 * radius ** 2
## The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * (radius ** 2)
print("35: ", "The area of a circle with radius {} meters is {} meters square.".format(radius, area))

# 36. Make the following using string formatting methods:
## 8 + 6 = 14
## 8 - 6 = 2
## 8 * 6 = 48
## 8 / 6 = 1.33
## 8 % 6 = 2
## 8 // 6 = 1
## 8 ** 6 = 262144
a, b = 8, 6
print("36A: ", "{} + {} = {}".format(a, b, a + b))
print("36B: ", "{} - {} = {}".format(a, b, a - b))
print("36C: ", "{} * {} = {}".format(a, b, a * b))
print("36D: ", "%d / %d = %.2f" %(a, b, a / b)) # Doing a different way to round result
print("36E: ", "{} % {} = {}".format(a, b, a % b))
print("36F: ", "{} // {} = {}".format(a, b, a // b))
print("36G: ", "{} ** {} = {}".format(a, b, a ** b))
