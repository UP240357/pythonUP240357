# Day 5 lvl 1 - Lists  in Python
# Ruiz Clemente Jorge Alberto

""" 1
Declare an empty list
""" 
empty_list = list()
print(f"empty list = {empty_list}")

""" 2
Declare a list with more than 5 items
"""
new_list_games = ["Fortnite", "GTA V", "Street fighter", "God of war", "Borderlands", "Fallout"]
print(f"new list = {new_list_games}")

""" 3
Find the length of your list
"""
print(f"length of games list = {len(new_list_games)}")

""" 4
Get the first item, the middle item and the last item of the list
"""
print(f"firts item = {new_list_games[0]}")
print(f"last item = {new_list_games[-1]}")
middle = (len(new_list_games)+1)//2
print(f"middle item = {new_list_games[middle]}")

""" 5
Declare a list called mixed_data_types, put your(name, age, height, 
marital status, address)
"""
mixed_data_types = ["Jorge", 20, 1.69, "single", "Aguascalientes"]
print(f"\nmixed data types = {mixed_data_types}")

""" 6
Declare a list variable named it_companies and assign initial values 
Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

""" 7
Print the list using print()
"""
print(f"\ncomanies list = {it_companies}")

""" 8
Print the number of companies in the list
"""
print(f"length of companies list = {len(it_companies)}")

""" 9
Print the first, middle and last company
"""
print(f"firts item = {it_companies[0]}")
print(f"last item = {it_companies[-1]}")
middle = (len(it_companies)+1)//2
print(f"middle item = {it_companies[middle]}")

""" 10
Print the list after modifying one of the companies
"""
it_companies[1] = "Gugle"
print(f"\nchange in companies list\n= {it_companies}")

""" 11
Add an IT company to it_companies
"""
it_companies.append("Linux")
print(f"\nadd an IT company (Linux)\n= {it_companies}")

""" 12
Insert an IT company in the middle of the companies list
"""
middle = len(it_companies)//2
it_companies.insert(middle,"Android")
print(f"\ninsert an IT company in the middle\n= {it_companies}")

""" 13
Change one of the it_companies names to uppercase (IBM excluded!)
"""
it_companies[4] = it_companies[4].upper()
print(f"\nchange one name to uppercase\n= {it_companies}")

""" 14
Join the it_companies with a string '#;  '
"""
print(f"\njoin the hash at the companies list")
print("= ","#; ".join(it_companies))

""" 15
Check if a certain company exists in the it_companies list.
"""
print("\nis IBm in the companies list?")
print("IBM" in it_companies)
print("is Google in the companies list?")
print("Google" in it_companies)

""" 16
Sort the list using sort() method
"""
it_companies.sort()
print(f"\ncompanies list sort\n= {it_companies}")

""" 17
Reverse the list in descending order using reverse() method
"""
it_companies.reverse()
print(f"\nreverse companies list\n= {it_companies}")

""" 18
Slice out the first 3 companies from the list
"""
first_3 = it_companies[:3]
print(f"\nthe first companies are\n= {first_3}")

""" 19
Slice out the last 3 companies from the list
"""
last_3 = it_companies[-3:]
print(f"\nthe last companies are\n= {last_3}")

""" 20
Slice out the middle IT company or companies from the list
"""
middle = (len(it_companies)+1)//2
print(f"\nthe comany or companies in the middle are\n= {it_companies[middle:middle+1]}")

""" 21
Remove the first IT company from the list
"""
del it_companies[0]
print(f"\nremove the firts item in companies list\n= {it_companies}")

""" 22
Remove the middle IT company or companies from the list
"""
middle = len(it_companies)//2
del it_companies [middle:middle+1]
print(f"\nremove the middle item in companies list\n= {it_companies}")

""" 23
Remove the last IT company from the list
"""
del it_companies[-1]
print(f"\nremove the last item in companies list\n= {it_companies}")

""" 24
Remove all IT companies from the list
"""
del it_companies[:]
print(f"\nremove al items in companies list\n= {it_companies}")

""" 25
Destroy the IT companies list
"""
del it_companies
print(f"\ndestroy the companies list")

""" 26
Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join = front_end + back_end
print(f"\njoin {front_end} + {back_end}\n= {join}")

""" 27
After joining the lists in question 26. Copy the joined list and 
assign it to a variable full_stack, then insert Python and SQL 
after Redux.
"""
full_stack = join
redux = full_stack.index("Redux")
position = redux+1
full_stack[position:position] = ["Python", "SQL"]
print(f"\njoin Python and SQL after Redux\n={full_stack}")