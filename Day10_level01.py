# Day 10 - Loops
# Ruiz Clemente Jorge Alberto

#level 01

""" 1
Iterate 0 to 10 using for loop, do the same using while loop."""
x = 0
print("\nIterating from 0 to 10 using for loop:")
for i in range(11): #se genera un rango desde 0 hasta 10 (se pone 11 pero no se incluye el 11 en el rango)
    print(i)

print("\nIterating from 0 to 10 using while loop:")
while x <= 10:  #mientras que x sea menor o igual a 10 se imprime x y se suma 1
    print(x)
    x += 1

""" 2
Iterate 10 to 0 using for loop, do the same using while loop."""
x = 10
print("\nIterating from 10 to 0 using for loop:")
for i in range(10, -1, -1): #la variable i toma el valor de 10, luego se va restando 1 (con el -1) hasta llegar a 0 (se utiliza -1 pero no se incluye en el rango)
    print(i)

print("\nIterating from 10 to 0 using while loop:")
while x >= 0:   #mientras que x sea mayor o igual a 0 se imprime x y se resta 1
    print(x)
    x -= 1

""" 3
Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#
##
###
####
#####
######
#######
"""
x = 1
print()
while x <= 7:  #mientras que x sea menor o igual a 10 se imprime x y se suma 1
    print(x*"#")
    x += 1

""" 4
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
x = 0
print()
while x < 8:
    print("# " * 8)
    x+= 1

x = 0
print()
while x < 8:
    y = 0
    while y < 8:
        print("#", end=" ")
        y+= 1
    print()
    x+= 1

""" 5
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""


""" 6
Iterate through the list, 
['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items."""


""" 7
Use for loop to iterate from 0 to 100 and print only even numbers"""


""" 8
Use for loop to iterate from 0 to 100 and print only odd numbers"""


#level 02
""" 1
Use for loop to iterate from 0 to 100 and print the sum of all numbers.

The sum of all numbers is 5050."""


""" 2
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500."""


#level 03
""" 1
Go to the data folder and use the countries.py file. 
Loop through the countries and extract all the countries containing the word land."""


""" 2
This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop."""


""" 3
Go to the data folder and use the countries_data.py file."""
"""    What are the total number of languages in the data   """    
"""    Find the ten most spoken languages from the data     """
"""    Find the 10 most populated countries in the world    """