#lvl 2

""" 1
Unpack siblings and parents from family_members
"""
brothers = family_members[:2]
parents = family_members[-2:]
print(f"{brothers}\n{parents}")

""" 2
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
"""
fruits = ("Banana","Coconut","Pineapple")
vegetables = ("Onion","Corn","Potato")
animal_products = ("Milk","Cheese","Butter")
food_stuff_tp = fruits+vegetables+animal_products
print(f"{fruits}\n{vegetables}\n{animal_products}")
print(food_stuff_tp)

""" 3
Change the about food_stuff_tp tuple to a food_stuff_lt list
"""
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

""" 4
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
"""
middle = len(food_stuff_lt)//2
print(food_stuff_lt[middle])

""" 5
Slice out the first three items and the last three items from food_staff_lt list
"""
print(f"{food_stuff_lt[0]}, {food_stuff_lt[1]}, {food_stuff_lt[3]}")

""" 6
Delete the food_staff_tp tuple completely
"""
del food_stuff_tp

""" 7
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country
"""
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
check = "Estonia" in nordic_countries
print(check)
check = "Iceland" in nordic_countries
print(check)