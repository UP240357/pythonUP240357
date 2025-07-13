# Day 8 lvl 1 - Dictionaries
# Ruiz Clemente Jorge Alberto

""" 1
Create an empty dictionary called dog
"""
dog = {}

""" 2
Add name, color, breed, legs, age to the dog dictionary
"""
dog = {"name": "Nicky", "color": "White", "breed": "Schnauzer", "legs": 4, "age": 5}
print(f"Dog = {dog}")

""" 3
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country,
city and address as keys for the dictionary
"""
student = {"first_name": "Jorge A", "last_name": "Ruiz Clemente", "gender": "M", "age": 20, "marital_status": "single", "skills": "programming", "country": "Mexico", "city": "Aguascalientes", "address": "Av. Universidad 1234"}
print(f"\nstudent = {student}")

""" 4
Get the length of the student dictionary
"""
print(f"\nlength of student dictionary = {len(student)}")

""" 5
Get the value of skills and check the data type, it should be a list
"""
print(f"\nskills = {student['skills']}")

""" 6
Modify the skills values by adding one or two skills
"""
student["skills"] = ["programming","Python"]
print(f"\nModified skills = {student['skills']}")

""" 7
Get the dictionary keys as a list
"""
print(f"\nKeys of student dictionary = {list(student.keys())}")

""" 8
Get the dictionary values as a list
"""
print(f"\nValues of student dictionary = {list(student.values())}")

""" 9
Change the dictionary to a list of tuples using items() method
"""
student_items = list(student.items())
print(f"\nStudent items as list of tuples = {student_items}")

""" 10
Delete one of the items in the dictionary
"""
del student["marital_status"]
print(f"\nStudent dictionary after deletion = {student}")

"""" 11
Delete one of the dictionaries
"""
del dog
print("\nDog dictionary has been deleted.")