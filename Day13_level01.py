# Day 13 - List Comprehension
# Ruiz Clemente Jorge Alberto

#level 01

""" 1
Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]"""
print()
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filter_numbers = [num for num in numbers if num <= 0]
print(filter_numbers)

""" 2
Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]"""
print()
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [number for sublist1 in list_of_lists for sublist2 in sublist1 for number in sublist2]
print(flattened_list)

""" 3
Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]"""
print()
list_of_tuples = [
    (i, i**0, i**1, i**2, i**3, i**4, i**5) 
    for i in range(11)
]

for tpl in list_of_tuples:
    print(tpl)

""" 4
Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]"""
print()
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

transformed_countries = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for sublist in countries  
    for country, capital in sublist 
]
print(transformed_countries)

""" 5
Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]"""
print()
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

transfor_countries = [
    {'country': country.upper(), 'city': capital.upper()}
    for sublist in countries  
    for country, capital in sublist 
]

print(transfor_countries)

""" 6
Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']"""
print()
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = [
    f"{first_name} {last_name}"
    for sublist in names  
    for first_name, last_name in sublist 
]
print(full_names)

""" 7
Write a lambda function which can solve a slope or y-intercept of linear functions."""
print()
calculate_slope = lambda p1, p2: (p2[1] - p1[1]) / (p2[0] - p1[0])
calculate_y_intercept = lambda point, slope: point[1] - slope * point[0]
point1 = (2, 4)
point2 = (4, 8)
slope = calculate_slope(point1, point2)
print(slope)