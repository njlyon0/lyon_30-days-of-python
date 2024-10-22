# Exercises: Level 1

## 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

### Gather user age (as an integer)
user_age = int(input("Enter your age: "))

### Respond conditional on user input
if user_age >= 18:
    print("You are old enough to learn to drive")
else: 
    print("You must wait ", 18 - user_age, " years before you can learn to drive")

## 2. Compare the values of my_age and your_age using if/else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 

### Identify "my age"
my_age = 31

### Gather user age
your_age = int(input("Enter your age: "))

### Respond conditional on user input
if my_age == your_age:
    print("We are the same age!")
elif my_age < your_age:
    if your_age - my_age == 1:
        print("You are 1 year older than me")
    else: 
        print("You are ", your_age - my_age, " years older than me")
else: 
    if my_age - your_age == 1:
        print("I am 1 year older than you")
    else: 
        print("I am ", my_age - your_age, " years older than you")

## 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

### Gather numbers
a = int(input("Enter a number (A): "))
b = int(input("Enter another number (B): "))

### Respond conditionally
if a == b:
    print("A and B are equal")
elif a > b:
    print("A is greater than B")
else:
    print("B is greater than A")

# Exercises: Level 2

## 1. Write a code which gives grade to students according to theirs scores:

### Define a grade
grade = 83

if grade >= 90:
    print("You have earned an A with your score of ", grade)
elif grade >= 80 and grade < 90:
    print("You have earned a B with your score of ", grade)
elif grade >= 70 and grade < 80:
    print("You have earned a C with your score of ", grade)
elif grade >= 60 and grade < 70:
    print("You have earned a D with your score of ", grade)
elif grade >= 50 and grade < 60:
    print("You have earned a F with your score of ", grade)

## 2. Check if the season is Autumn, Winter, Spring or Summer.

### Identify a month
month = "January"

### Conditionally handle that
if month in "September October November".split():
    print("The season is Autumn")
elif month in "December January February".split():
    print("The season is Winter")
elif month in "March April May".split():
    print("The season is Spring")
elif month in "June July August".split():
    print("The season is Summer")
else: 
    print("Unrecognized month!")

## 3. The following list contains some fruits: `fruits = ['banana', 'orange', 'mango', 'lemon']` If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print 'That fruit already exist in the list'. 

### Generate the list
fruits = ['banana', 'orange', 'mango', 'lemon']

### Identify a new fruit
new_fruit = "lime"

### Do specified conditional
if new_fruit in fruits:
    print("That fruit already exists in the list")
else: 
    fruits.append(new_fruit)
    print("Fruits list is now: ", fruits)

# Exercises: Level 3

## 1. Here we have a person dictionary. Feel free to modify it!
person = {'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
        }

### A. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person.keys():
    print("3-A:", "Following skills found: ", person.get("skills"))
else:
    print("3-A:", "No 'skills' key found in supplied dictionary")

### B. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person.keys():
    # Identify skills list
    found_skills = person.get("skills")

    # Check whether Python is in that list
    if "Python" in found_skills:
        print("3-B: ", person.get("first_name"), " is skilled in Python")
    else: 
        print("3-B: ", person.get("first_name"), " is _not_ skilled in Python")
else:
    print("3-B:", "No 'skills' key found in supplied dictionary")

### C. If a person skills has only JavaScript and React, print('He is a front end developer'), if the person has skills in Node, Python, MongoDB, print('He is a backend developer'), if the person has skills in React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

### Strip out skills
person_skills = person.get("skills")

### Conditionally identify the type of developer they are
if all([item in person_skills for item in "React Node MongoDB".split()]):
    print("This person is a fullstack developer")
elif all([item in person_skills for item in "Node Python MongoDB".split()]):
    print("This person is a frontend developer")
elif all([item in person_skills for item in "JavaScript React".split()]):
    print("This person is a frontend developer")
else:
    print("This person is some other type of developer")

### D. If the person is married and if he lives in Finland, print the information in the following format:
print(person.get("first_name"), person.get("last_name"), "lives in Finland and is married") if person.get("country") == "Finland" and person.get("is_married") == True else print(person.get("first_name"), person.get("last_name"), "does not live in Finland and/or is not married")
