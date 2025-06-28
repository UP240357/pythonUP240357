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

#lvl 2

print(f"A: {A}")
print(f"B: {B}")

""" 1
Join A and B
"""
Join = A.union(B)
print(Join)

""" 2
Find A intersection B
"""
print(A.intersection(B))

""" 3
Is A subset of B
"""
print(A.issubset(B))

""" 4
Are A and B disjoint sets
"""
print(A.isdisjoint(B))

""" 5
Join A with B and B with A
"""
A.update(B)
B.update(A)

print(f"A: {A}")
print(f"B: {B}")

""" 6
What is the symmetric difference between A and B
"""
print(A.symmetric_difference(B))

""" 7
Delete the sets completely
"""
del A
del B

print("---------------------------------------------------------------------------------------------------------------------")

#lvl 3

"""
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
"""
st_ages = set(age)
print(len(age))
print(len(st_ages))

"""
Explain the difference between the following data types: string, list, tuple and set

string: es una cadena de caracteres que almacena texto y es inmodificable.
list: es un conjunto de elementos que pueden ser de diferentes tipos y se pueden modificar y utiliza [].
tuple: es simlar a una lista pero es inmodificable y se utiliza ().
set: es un conjunto de elementos únicos y no ordenados, se utiliza {}.
"""

"""
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
"""
oracion = "I am a teacher and I love to inspire and teach people"
palabras = oracion.split()
palabras_unicas = set(palabras)
print(palabras_unicas)
print(len(palabras_unicas))