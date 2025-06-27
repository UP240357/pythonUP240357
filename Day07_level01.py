# Day 7 lvl 1 - Sets
# Ruiz Clemente Jorge Alberto

#lvl 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

"""
Find the length of the set it_companies
"""
print(len(it_companies))

"""
Add 'Twitter' to it_companies
"""
it_companies.add("Twitter")
print(it_companies)

"""
Insert multiple IT companies at once to the set it_companies
"""
it_companies.update(["YouTube","Android","Lenovo"])
print(it_companies)

"""
Remove one of the companies from the set it_companies
"""
it_companies.remove("Apple")
print(it_companies)

"""
What is the difference between remove and discard

La diferencia es que remove manda un error si el elemento a eliminar no existe, en cambio remove si te genera un error
"""

print("---------------------------------------------------------------------------------------------------------------------")

#lvl 2

"""
Join A and B
"""
Join = A.union(B)
print(A)

"""
Find A intersection B
"""
"""
Is A subset of B
"""
"""
Are A and B disjoint sets
"""
"""
Join A with B and B with A
"""
"""
What is the symmetric difference between A and B
"""
"""
Delete the sets completely
"""

#lvl 3

"""

"""