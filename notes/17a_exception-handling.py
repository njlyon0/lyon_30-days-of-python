"""
Exception Handling

Errors can be handled with "try" and "except" to handle errors 'gracefully'. This means an error condition is detected but the code is exited in a controlled manner. Syntax is:

try:
    # run this code
except: 
    # execute this code when there *is* an exception
else:
    # execute this code when there *is not* an exception
finally:
    # always run this code
"""

# Example
try:
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')

# Can include more informative / multiple "except" clauses
try:
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('Zero division error occured')

# Can also add more code after the exception handling chunk(s)
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

# Exception handling can be simplfied like so:
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
