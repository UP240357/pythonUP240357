# Day 5 lvl 1 - Lists  in Python
# Ruiz Clemente Jorge Alberto

""" 1
Declare an empty list
""" 
empty_list = list()
print(empty_list)

""" 2
Declare a list with more than 5 items
"""
new_list_games = ["Fortnite", "GTA V", "Street fighter", "God of war", "Borderlands", "Fallout"]

""" 3
Find the length of your list
"""
print(len(new_list_games))

""" 4
Get the first item, the middle item and the last item of the list
"""
print(new_list_games[0])
print(new_list_games[-1])
middle = len(new_list_games)//2
print(new_list_games[middle])

""" 5
Declare a list called mixed_data_types, put your(name, age, height, 
marital status, address)
"""
mixed_data_types = ["Jorge", 20, 1.69, "single", "Aguascalientes"]

""" 6
Declare a list variable named it_companies and assign initial values 
Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

""" 7
Print the list using print()
"""
print(it_companies)

""" 8
Print the number of companies in the list
"""
print(len(it_companies))

""" 9
Print the first, middle and last company
"""
print(it_companies[0])
print(it_companies[-1])
middle = len(it_companies)//2
print(it_companies[middle])

""" 10
Print the list after modifying one of the companies
"""
it_companies[1] = "Gugle"
print(it_companies)

""" 11
Add an IT company to it_companies
"""
it_companies.append("Linux")
print(it_companies)

""" 12
Insert an IT company in the middle of the companies list
"""
middle = len(it_companies)//2
it_companies.insert(middle,"Android")
print(it_companies)

""" 13
Change one of the it_companies names to uppercase (IBM excluded!)
"""
it_companies[4] = it_companies[4].upper()
print(it_companies)

""" 14
Join the it_companies with a string '#;  '
"""

""" 15
Check if a certain company exists in the it_companies list.
"""

""" 16
Sort the list using sort() method
"""

""" 17
Reverse the list in descending order using reverse() method
"""

""" 18
Slice out the first 3 companies from the list
"""

""" 19
Slice out the last 3 companies from the list
"""

""" 20
Slice out the middle IT company or companies from the list
"""

""" 21
Remove the first IT company from the list
"""

""" 22
Remove the middle IT company or companies from the list
"""

""" 23
Remove the last IT company from the list
"""

""" 24
Remove all IT companies from the list
"""

""" 25
Destroy the IT companies list
"""

""" 26
Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""

""" 27
After joining the lists in question 26. Copy the joined list and 
assign it to a variable full_stack, then insert Python and SQL 
after Redux.
"""