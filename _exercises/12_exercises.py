# Exercises: Level 1

## 1. Write a function which generates a six digit/character random_user_id.
def random_user_id():
    # Get needed module(s)
    import random
    import string
    
    # Start the ID
    id = ""

    # While ID is not long enough, add components
    while len(id) < 6:

        # Flip a coin
        coin = random.randint(1, 2)

        # Use that to decide between letters or numbers
        if coin == 1:
            val = str(random.randint(0, 9))
        else:
            val = string.ascii_lowercase[random.randint(0, 25)]

        # Once found, add it to the growing ID
        id = id + val

    return id

# Invoke function
random_user_id()

## 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated. 
def user_id_gen_by_user():
    # Get needed module(s)
    import random
    import string
    
    # Gather needed inputs from user
    nuser = int(input("How many users should unique IDs be generated for? "))
    nchar = int(input("How many characters should be in each unique ID? "))

    # Define a list for user IDs
    user_list = []

    # Loop across desired number of users
    for focal_user in range(nuser):
            
        # Start one ID
        id = ""

        # While ID is not long enough, add components
        while len(id) < nchar:

            # Flip a coin
            coin = random.randint(1, 2)

            # Use that to decide between letters or numbers
            if coin == 1:
                val = str(random.randint(0, 9))
            else:
                val = string.ascii_lowercase[random.randint(0, 25)]

            # Once found, add it to the growing ID
            id = id + val

        # Attach ID to list
        user_list.append(id)

    # Return the list
    return user_list

# Invoke function
user_id_gen_by_user()

## 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    # Import needed module
    import random

    # Generate needed colors
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Assemble into a list
    color = [r, g, b]

    # Return
    return color

# Invoke function
rgb_color_gen()

# Exercises: Level 2

## 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(ncolors = 1):
    # Import needed modules
    import random
    import string

    # Assemble hexadecimal characters
    hexchars = string.ascii_letters[0:6] + "0123456789"

    # Make a list for storing outputs
    color_list = []

    # Loop across desired number of colors
    for k in range(ncolors):

        # Start the hexcode
        hex = ""

        # While it's not long enough, add to it
        while len(hex) < 6:
            hex = hex + hexchars[random.randint(0, 15)]

        # Add a leading hashtag
        hex = "#" + hex

        # Once identified, add to list
        color_list.append(hex)

    # Return the list
    return color_list

# Invoke function
list_of_hexa_colors()
list_of_hexa_colors(3)

## 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(ncolors = 1):

    # Make list
    color_list = []

    # Loop across desired number of colors
    for k in range(ncolors):
        
        # Grab color
        color = rgb_color_gen()

        # Add to list
        color_list.append(color)
    
    # Return colors
    return color_list

# Invoke function
list_of_rgb_colors(1)
list_of_rgb_colors(4)

## 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(type = "hexa", ncolors = 1):

    # Make desired type of colors
    if type == "hexa":
        color_list = list_of_hexa_colors(ncolors)
    elif type == "rgb":
        color_list = list_of_rgb_colors(ncolors)
    else: print("Unrecognized value for 'type'")

    # Return colors
    return color_list

# Invoke the function
generate_colors("hexa", 5)
generate_colors("rgb")

# Exercises: Level 3

## 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(list):
    # Import needed module(s)
    import random

    # Make list(s) for output(s)
    mix = []
    coords = []

    # Loop across list coords
    while not len(coords) == len(list):

        # Identify random number
        rand = random.randint(0, len(list) - 1)

        # If it's not already in coords:
        if not rand in coords:
            
            # Add it to our records
            coords.append(rand)

            # Slice out that bit of the original list
            item = list[rand]

            # Add it to the mixed list
            mix.append(item)

        # Otherwise, try again
        else: 
            continue

    # Return that mixed list
    return mix

# Invoke function
fruits = ["mango", "banana", "pineapple", "lemon", "apple"]
shuffle_list(fruits)

## 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def rand_seven():

    # Import module(s)
    import random

    # Empty output lists
    vals = []

    # Loop across desired values
    while not len(vals) == 7:

        # Grab random number
        new_val = random.randint(0, 7)

        # Add it to the list if it's not there already
        if not new_val in vals:
            vals.append(new_val)
        else:
            continue

    # Return finished values when done
    return vals

# Invoke function
rand_seven()

