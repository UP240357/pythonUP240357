#lvl 3

""" 1
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
"""
st_ages = set(age)
print(len(age))
print(len(st_ages))

""" 2
Explain the difference between the following data types: string, list, tuple and set

string: es una cadena de caracteres que almacena texto y es inmodificable.
list: es un conjunto de elementos que pueden ser de diferentes tipos y se pueden modificar y utiliza [].
tuple: es simlar a una lista pero es inmodificable y se utiliza ().
set: es un conjunto de elementos únicos y no ordenados, se utiliza {}.
"""

""" 3
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
"""
oracion = "I am a teacher and I love to inspire and teach people"
palabras = oracion.split()
palabras_unicas = set(palabras)
print(palabras_unicas)
print(len(palabras_unicas))