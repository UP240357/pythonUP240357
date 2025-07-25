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
while x <= 7:  #mientras que x sea menor o igual a 7 se imprime x veces el caracter "#"
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
#metodo sin anidados
x = 0
print()
while x < 8:
    print("# " * 8)
    x+= 1

#metodo con anidados
x = 0
print()
while x < 8:
    y = 0
    while y < 8:
        print("#", end=" ")
        y+= 1
    print() #se imrpime un salto de linea
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
x = 0
y = 0
print()
while x <=10:                   #mientras que x sea menor o igual a 10
    print(f"{x} x {y} = {x*y}") #imprime el valor de x, y y su multiplicacion
    x += 1
    y += 1

""" 6
Iterate through the list, 
['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items."""
lista = ['Python', 'Numpy','Pandas','Django', 'Flask']  #iteracion: tomar cada elemento e imprimirlo
print()
for element in lista:   #por cada elemento en la lista
    print(element)      #imprime el elemento

""" 7
Use for loop to iterate from 0 to 100 and print only even numbers"""
x = 0
print()
while x <= 100:         #hacemos el ciclo mientras que x sea menor o igual a 100
    if x % 2 == 0:      #para saber si un numero es par, se utiliza el modulo (%), usando x % 2 == (igual) 0
        print(x)        #imprime ese numero
    x += 1

""" 8
Use for loop to iterate from 0 to 100 and print only odd numbers"""
x = 0
print()
while x <= 100:         #un bucle exactamente igual que el anterior
    if x % 2 != 0:      #usando el modulo (%), como x % 2 != (diferente) 0
        print(x)
    x += 1
