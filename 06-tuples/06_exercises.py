# Exercises: Level 1

## 1. Create an empty tuple
empty_tup = tuple()

## 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brother_tup = ("bro 1", "bro 2", "bro 3")
sister_tup = ("sis 1", "sis 2", "sis 3")

## 3. Join brothers and sisters tuples and assign it to siblings
siblings_tup = brother_tup + sister_tup

## 4. How many siblings do you have?
print("1-4: I have {} siblings".format(len(siblings_tup)))

## 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_tup = ("parent 1", "parent 2") + siblings_tup
print("1-5: My family consists of: ", family_tup)

# Exercises: Level 2

## 1. Unpack siblings and parents from family_members
par1_tup, par2_tup, *siblings_tup2 = family_tup
parent_tup = par1_tup + par2_tup
print("2-1: Parents are: ", parent_tup, " and siblings are: ", tuple(siblings_tup2))

## 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("mango", "lemon")
vegetables = ("celery", "broccoli")
animal_prods = ("milk", "egg")
food_stuff_tp = fruits + vegetables + animal_prods
print("2-2: ", food_stuff_tp)

## 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("2-3: ", type(food_stuff_lt))

## 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print("2-4: ", food_stuff_lt[len(food_stuff_lt) // 2])

## 5. Slice out the first three items and the last three items from food_staff_lt list
print("2-5a: ", food_stuff_lt[0:3])
print("2-5b: ", food_stuff_lt[-3:])

## 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

## 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

### Check if 'Estonia' is a nordic country
print("2-7a: ", "Estonia" in nordic_countries)

### Check if 'Iceland' is a nordic country
print("2-7b: ", "Iceland" in nordic_countries)
