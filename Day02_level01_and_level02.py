# Day 2 lvl 1 - Variables in Python
# Ruiz Clemente Jorge Alberto

first_name = 'Jorge'
last_name = 'Ruiz'
full_name = 'Jorge Alberto Ruiz Clemente'
country = 'Mexico'
city = 'Aguascalientes'
age = 20
year = 2025
is_married = False
is_true = True
is_light_on = True
language, university, tacos = 'spanish', 'UPA', 5

# Day 2 lvl 2 - Variables in Python
# Ruiz Clemente Jorge Alberto

first_name = 'Jorge'
last_name = 'Ruiz'
full_name = 'Jorge Alberto Ruiz Clemente'
country = 'Mexico'
city = 'Aguascalientes'
age = 20
year = 2025
is_married = False
is_true = True
is_light_on = True
language, university, tacos = 'spanish', 'UPA', 5


#primera parte
#Check the data type of all your variables using type() built-in function# type = saber el tipo de dato
# type = saber el tipo de dato
# type = know the data type

print(type(first_name))                     #first_name
print(type(last_name))                      #last_name
print(type(full_name))                      #full_name
print(type(country))                        #country
print(type(city))                           #city
print(type(age))                            #age
print(type(year))                           #year
print(type(is_married))                     #is_married
print(type(is_true))                        #is_true
print(type(is_light_on))                    #is_lights_on
print(type(language), type(university), type(tacos))    #lenguage, university, tacos

print('my first name has:', len(first_name), 'letters')
print('my last name has:', len(last_name), 'letters')


#segunda parte
'''1. Using the _len()_ built-in function, find the length of your first name
1. Compare the length of your first name and your last name
1. Declare 5 as num_one and 4 as num_two
1. Add num_one and num_two and assign the value to a variable total
1. Subtract num_two from num_one and assign the value to a variable diff
1. Multiply num_two and num_one and assign the value to a variable product
1. Divide num_one by num_two and assign the value to a variable division
1. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
1. Calculate num_one to the power of num_two and assign the value to a variable exp
1. Find floor division of num_one by num_two and assign the value to a variable floor_division'''

num_one = 5
num_two = 4

total = num_one+num_two
diff = num_two-num_one
product = num_two*num_one
division = num_one/num_two
remainder = num_two%num_one
exp = num_one**num_two
floor_division = num_one//num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)


#tercera parte
'''The radius of a circle is 30 meters.
    1. Calculate the area of a circle and assign the value to a variable name of 
    area_of_circle
    2. Calculate the circumference of a circle and assign the value to a variable 
    name of circum_of_circle
    3. Take radius as user input and calculate the area.'''

area_of_circle = (3.1416*(30**2))
print(area_of_circle)

circum_of_circle = (2*3.1416*30)
print(circum_of_circle)

rad = float(input('give the radius: '))

new_area_of_circle = (3.1416*(rad**2))
print(new_area_of_circle)

new_circum_of_circle = (2*3.1416*rad)
print(new_circum_of_circle)

#cuarta parte
'''Use the built-in input function to get first name, last name, country and 
age from a user and store the value to their corresponding variable names'''

given_first_name = input('Enter your first name :')
print(f'"{given_first_name}" is of type: {type(given_first_name)}')

given_last_name = input('Enter your last name :')
print(f'"{given_last_name}" is of type: {type(given_last_name)}')

given_country = input('Enter your country :')
print(f'"{given_country}" is of type: {type(given_country)}')

given_age = int(input('Enter your age :'))
print('are a ',type(given_age),'type')
