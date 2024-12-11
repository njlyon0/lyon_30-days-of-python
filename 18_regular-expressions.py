"""
Regular Expressions

Regular expressions are special text strings that can be used to find/interact with patterns in data
"""

# Import relevant module
import re

# Make simple text demo
ex_text = """I love teaching python and R.
I enjoy working on the 30 day challenge"""

# "match" function searches the *beginning* of a string and returns either the matched characters or `None`
print(re.match(pattern = "I love", string = ex_text))
print(re.match(pattern = "I enjoy", string = ex_text))

# "search" returns a match if any is found at any point in even a multi-line string
print(re.search(pattern = "I love", string = ex_text))
print(re.search(pattern = "I enjoy", string = ex_text))

# "findall" returns a list containing all matches
print(re.findall(pattern = "I love", string = ex_text))
print(re.findall(pattern = "I enjoy", string = ex_text))

# "split" accepts a string and splits it at the match points (returns as a list)
## Note that it *removes* the matched part
print(re.split(pattern = "I enjoy", string = ex_text))
print(re.split(pattern = "\n", string = ex_text))

# "sub" replaces one/many matches within a string
print(re.sub(pattern = "I love", repl = "I LOVE", string = ex_text))

# Can retrieve the coordinates of a match with the "span" method
ex_match = re.search(pattern = "I enjoy", string = ex_text)
ex_span = ex_match.span()
ex_start, ex_end = ex_span
ex_text[ex_start:ex_end]

# Multiple matches can be searched for at the same time
re.findall(pattern = "love|enjoy", string = ex_text)

# These matching functions *are case sensistive*!
ex_text2 = "Python is a fun language, but 'python' is not always capitalized"
re.findall(pattern = "Python", string = ex_text2)

# Can handle differences in casing like so
## If not naming parameters, can use the "I" attribute of the "re" module
re.findall("Python", ex_text2, re.I)
## Can also fully write out both options
re.findall(pattern = "Python|python", string = ex_text2)
## Can also put square brackets around the character(s) that differ
re.findall(pattern = "[Pp]ython", string = ex_text2)

""" Regex Patterns """

# Can declare a RegEx variable with "r" followed by a string
ex_text3 = "Apples and bananas are fruits. An old cliche says 'an apple a day keeps the doctor away' has been replaced by 'a banana a day keeps the doctor far far away'."

regex_apple = r"[Aa]pple"

re.findall(pattern = regex_apple, string = ex_text3)
re.split(pattern = regex_apple, string = ex_text3)

# There are many special facets of regex syntax we can leverage:
## Can look for all letters between two specified letters
r"[a-g]" 
## Or the same for numbers
r"[0-3]"
## Or even multiple separate ranges of characters
r"[A-F5-7g-j]"
## Can use certain special characters if escaped with a backslash
r"\d" ### match all digits (0-9)
r"\D" ### match all *non-* digits
## Find any character expect a newline
r"[a]." ### finds groups of two characters where the first is "a"
## Can find substrings
r"^start" ### substring at start of a line
r"end$" ### substring that ends a line
## Can find replicates
r"[x]+" ### one or more times
r"[y]*" ### zero or more times
r"[z]?" ### zero or one time
### Can specify how any characters specifically
r"[x]{3}" ### exactly three "x"s
r"[y]{5,}" ### at least 5 "y"s
r"[z]{1,6}" ### 1 to 6 "z"s

# Let's practice finding all digits in the following string
ex_text4 = "I am working on this lesson on December 11, 2024 and began this challenge more than 30 days ago"

## Find all digits doesn't return exactly what we want
re.findall(pattern = r"\d", string = ex_text4)

## Can add a plus to keep groups of numbers together
re.findall(pattern = r"\d+", string = ex_text4)

# More practice on matches some number of times
ex_text5 = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.
I am confident that it is not "e---mail" though.'''

## "-?" means that only instances with one or zero hyphens are found (and not the "e---mail" at the end)
re.findall(pattern = r"[Ee]-?mail", string = ex_text5)
