# Day 7 lvl 1 - Sets
# Ruiz Clemente Jorge Alberto

#lvl 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f"It companies: {it_companies}")

""" 1
Create an empty set
Find the length of the set it_companies
"""
print(len(it_companies))

""" 2
Add 'Twitter' to it_companies
"""
it_companies.add("Twitter")
print(it_companies)

""" 3
Insert multiple IT companies at once to the set it_companies
"""
it_companies.update(["YouTube","Android","Lenovo"])
print(it_companies)

""" 4
Remove one of the companies from the set it_companies
"""
it_companies.remove("Apple")
print(it_companies)

""" 5
What is the difference between remove and discard

La diferencia es que remove lanza un error si el elemento a eliminar no existe, 
mientras que discard no lanza error si el elemento no está presente.
"""

print("---------------------------------------------------------------------------------------------------------------------")
