# Exercises - Regular Expressions

# Import needed module
import re

## Exercises: Level 1
###  1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Find words in paragraph
matches = re.findall(pattern = r"[A-Za-z]+", string = paragraph)

# List for storing loop outputs
done = list()

# Set some useful starting positions
max_word = ""
max_ct = 0

# Loop across words numbers
for word_num in range(len(matches)):

    # Find word at that index position
    word = matches[word_num]

    # Skip if already counted
    if word in done: continue

    # Otherwise...
    else: 

        # Count instances of that word
        word_ct = matches.count(word)

        # If this word occurs more than prior words:
        if word_ct > max_ct:

            # Update the max word & max count!
            max_word = word
            max_ct = word_ct

        # Add to 'done' list
        done.append(word)

# Identify answer
print("1-1: ", "The most used word is '", max_word, "' and it was used", max_ct, "times.")

### 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']

# List for storing outputs
points_vals = list()

# Loop across points
for pt in range(len(points)):
    points_vals.append(int(points[pt]))

# Identify distance between furthest points
max_pt = max(points_vals)
min_pt = min(points_vals)

# Calculate distance
pt_dist = max_pt - min_pt

# Give answer
print("1-2: ", "The distance between the max/min point (", max_pt, " and ", min_pt, ") is ", pt_dist)

## Exercises: Level 2
### 1. Write a pattern which identifies if a string is a valid python variable

# Define function
def is_valid_variable(name):

    # Identify regex patterns that make invalid variable names
    bad = len(re.findall(pattern = "\d.+|-| |\?", string = name))

    # Pass the appropriate boolean back to the user
    if bad > 0: return False
    else: return True

# Invoke it
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

## Exercises: Level 3
### 1. Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Clean sentence
clean_text = re.sub(pattern = "%|@|#|&|;|\$", repl = "", string = sentence)
clean_text

# Find words in sentence
matches = re.findall(pattern = r"[A-Za-z]+", string = clean_text)
matches

# Lists for storing loop outputs
done = list()
match_cts = list()

# Loop across words numbers
for word_num in range(len(matches)):

    # Find word at that index position
    word = matches[word_num]

    # Skip if already counted
    if word in done:
        continue

    # Otherwise...
    else: 

        # Count instances of that word
        word_ct = matches.count(word)

        # Add to 'done' lists
        match_cts.append([word, word_ct])
        done.append(word)

# See output list
match_cts

# Identify answer
print("3-1:", "The ost common word is 'I' and occurs 3 times")
