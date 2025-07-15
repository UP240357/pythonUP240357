# Day 9 - Conditionals
# Ruiz Clemente Jorge Alberto

#level 01
""" 1
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive."""
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_needed = 18 - age
    print(f"You need {years_needed} more years to learn to drive.")

""" 2
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me."""
my_age = 25                                 #use ese valor, por el ejemplo que me dieron, pero puede ser cualquier otro
your_age = int(input("Enter your age: "))

if your_age > my_age:
    age_difference = your_age - my_age
    year_text = "year" if age_difference == 1 else "years"
    print(f"You are {age_difference} {year_text} older than me.")
elif your_age == my_age:
    print("We are the same age.")
else:
    age_difference = my_age - your_age
    year_text = "year" if age_difference == 1 else "years"
    print(f"I am {age_difference} {year_text} older than you.")

""" 3
Get two numbers from the user using input prompt. 
If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3"""
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

#level 02
""" 1
Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F"""
score = int(input("Enter your score: "))

if 80 <= score <= 100:      # ncantidad <= varible <= ncantidad --- esto es un rango, y vemos si el valor que tiene esta en ese rango
    print("Grade: A")  
elif 70 <= score < 80:
    print("Grade: B")
elif 60 <= score < 70:
    print("Grade: C")
elif 50 <= score < 60:
    print("Grade: D")
elif 0 <= score < 50:
    print("Grade: F")

""" 2
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
"""
month = input("Enter the name of a month: ")

if month in ["September", "October", "November"]:   #usamos "in" que ya lo habiamos visto, y nos ayuda a ver si el valor de una variable esta en una lista
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:  #las listas contienen los meses de cada estacion
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("That is not a valid month.")             #si se escribe algo que no sea un mes, se imprime este mensaje

""" 3
The following list contains some fruits:

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
If the fruit exists print('That fruit already exist in the list')"""
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ")

if fruit not in fruits:
    print(fruit, "is not in the list")      #mensaje de que la fruta no esta en la lista
    print("Adding fruit to the list")       #mensaje que se agregara la fruta a la lista
    fruits.append(fruit)                    #comando para agregar la fruta
    print("Modified list:", fruits)         #imprime la lista modificada
else:
    print("That fruit already exist in the list")

#level 03
""" 1
Here we have a person dictionary. Feel free to modify it!
    person={
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }

Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
If a person skills has only JavaScript and React, print('He is a front end developer'),
    if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
    if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
    else print('unknown title') - for more accurate results more conditions can be nested!
If the person is married and if he lives in Finland, print the information in the following format:
Asabeneh Yetayeh lives in Finland. He is married."""
person={
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }

if "skills" in person:
    skills = person["skills"]
    if len(skills) > 0:
        middle_skills = skills[len(skills) // 2]
        print("Middle skills are:", middle_skills)

    if "Python" in skills:
        print("The person has Python skill")

    if ("JavaScript" in skills and "React" in skills) and len(skills) == 2:
        print("He is a front end developer")
    elif ("Node" in skills and "Python" in skills and "MongoDB") and len(skills) == 3:
        print("He is a backend developer")
    elif ("Node" in skills and "React" in skills and "MongoDB") and len(skills) == 3:
        print("He is a fullstack developer")
    else:
        print("unknown title")
    
    if person["is_marred"] and person["country"] == "Finland":
        print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")