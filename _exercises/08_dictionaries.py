# Exercises

## 1. Create  an empty dictionary called dog
dog = dict()
print("1: ", type(dog))

## 2. Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Spot"
dog["color"] = "white"
dog["breed"] = "Australian Shepherd"
dog["legs"] = 3
dog["age"] = 4
print("2: ", dog)

## 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name":"Doe", "last_name":"Jane", "gender":"NB", "age":33, "marital_status":"married", "skills":["Python", "SQL", "R"], "country":"USA", "city":"Santa Barbara", "address":"123 Fake St."}
print("3: ", student)

## 4. Get the length of the student dictionary
print("4: ", "The 'student' dictionary has length ", len(student))

## 5. Get the value of skills and check the data type, it should be a list
print("5: ", "The 'student' dictionary contains a 'skills' item of type ", type(student.get
("skills")))

## 6. Modify the skills values by adding one or two skills
student["skills"].append("Quarto")
print("6: ", student.get("skills"))

## 7. Get the dictionary keys as a list
print("7: ", student.keys())

## 8. Get the dictionary values as a list
print("8: ", student.values())

## 9. Change the dictionary to a list of tuples using _items()_ method
student_tup = student.items()
print("9: ", student_tup)

## 10. Delete one of the items in the dictionary
student.pop("address")
print("10: ", student)

## 11. Delete one of the dictionaries
del student
