# Day 11 - Functions
# Ruiz Clemente Jorge Alberto

#level 01
""" 1
Declare a function add_two_numbers. It takes two parameters and it returns a sum."""
print()
def add_two_numbers(a,b):
    return a + b

print(add_two_numbers(3, 5))

""" 2
Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle."""
print()
def area_of_circle(r):
    return 3.1416 * r * r
print(area_of_circle(4))

""" 3
Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
Check if all the list items are number types. If not do give a reasonable feedback."""
print()
def add_all_nums(*args):                                        #definir la funcion con un numero arbitrario de argumentos
    if not all(isinstance(arg, (int, float)) for arg in args):  #verificar si todos los argumentos son numeros
        return "All arguments must be numbers."                 #si no lo son, retornar un mensaje
    total = 0                                                   #variable para guardar la suma total
    for arg in args:                                            #para cada argumento (arg) en args
        total += arg                                            #se suma ese argumento a total
    return total                                                #retur = regresar
print(add_all_nums(2, 3, 5))                                    #le decimos cuales son las variables

""" 4
Temperature in °C can be converted to °F using this formula: 
°F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit."""
print()
def convert_celsius_to_fahrenheit(c):
    return(c * 9/5) + 32
print(convert_celsius_to_fahrenheit(50))

""" 5
Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer."""
print()
def check_season(month):

    if month in ["September", "October", "November"]:
        print("The season is Autumn.")
    elif month in ["December", "January", "February"]:
        print("The season is Winter.")
    elif month in ["March", "April", "May"]:
        print("The season is Spring.")
    elif month in ["June", "July", "August"]:
        print("The season is Summer.")
    else:
        print("That is not a valid month.")

check_season("March")

""" 6
Write a function called calculate_slope which return the slope of a linear equation"""
print()
def calculate_slope(x1,y1,x2,y2):
    rest_y = y2 - y1
    rest_x = x2 - x1
    if rest_x == 0:
        return "slope is undef."
    else:
        return rest_y / rest_x

print(calculate_slope(2,3,4,5))

""" 7
Quadratic equation is calculated as follows: ax² + bx + c = 0.
Write a function which calculates solution set of a quadratic equation,
solve_quadratic_eqn."""
print()
def solve_quadratic_eqn(a,b,c):
    if a == 0:
        return "a cannot be a zero"
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "no real solution"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"one solution: x = {x}"
    else:
        sqrt_discriminant = discriminant**0.5
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return f"two solutions: x_1 = {x1}, x_2 = {x2}"

print(solve_quadratic_eqn(1,-3,2))

""" 8
Declare a function named print_list.
It takes a list as a parameter and it prints out each element of the list."""
print()
def print_list(list):
    for item in list:
        print(item)

print_list([1,2,3,4,5,6])

""" 9
Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]"""
print()
def reverse_list (list):
    reverse_elems = []
    for i in range(len(list)-1,-1,-1):
        reverse_elems.append(list[i])
    return reverse_elems

print(reverse_list([1, 2, 3, 4, 5, 6]))

""" 10
Declare a function named capitalize_list_items.
It takes a list as a parameter and it returns a capitalized list of items"""
print()
def capitalize_list_items(list):
    capt_items = []
    for item in list:
        if isinstance(item, str):
            capt_items.append(item.capitalize())
    else:
        try:
            str_item = str(item)
            capt_items.append(str_item.capitalize())
        except Exception as e:
            capt_items.append("error")
    return capt_items

print(capitalize_list_items(["hola","konnichiwa","rArO"]))

""" 11
Declare a function named add_item. 
It takes a list and an item parameters.
It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     
# ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      
# [2, 3, 7, 9, 5]"""
print()
def add_item(list, item_to_add):
    new_list = list[:]
    new_list.append(item_to_add)
    return new_list

print(add_item([1,2,3,4,5], 6))

""" 12
Declare a function named remove_item. It takes a list and an item parameters.
It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]"""
print()
def remove_item(list,item_remove):
    new_list = list[:]
    try:
        new_list.remove(item_remove)
        return new_list
    except ValueError:
        return "dont found elemnt"

print(remove_item([1,2,3,4,5],4))

""" 13
Declare a function named sum_of_numbers. 
It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050"""
print()
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

print(sum_of_numbers(100))

""" 14
Declare a function named sum_of_odds. 
It takes a number parameter and it adds all the odd numbers in that range."""
print()
def sum_of_odds(n):
    total = 0
    for i in range(n+1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(5))

""" 15
Declare a function named sum_of_even. 
It takes a number parameter and it adds all the even numbers in that - range."""
print()
def sum_of_even(n):
    total = 0
    for i in range(n+1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(5))