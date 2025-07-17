#level 02
""" 1
Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050."""
x = 0
suma = 0
print()
while x <= 100:
    suma += x   #significa: suma = suma + x
    x += 1
print(f"the sum of all numbers of 0 to 100 is {suma}")

""" 2
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
The sum of all evens is 2550. And the sum of all odds is 2500."""
x = 0
suma_par = 0
suma_impar = 0
print()
while x <= 100:             #ciclo mientras que compara si la variable x es menor o igual a 100
    if x % 2 == 0:          #usamos el modulo (%) con if para comprobar si es par
        suma_par += x       #si es par, se suma a la variable suma_par
    else:
        suma_impar += x     #si no es par, se sabe que es impar y se suma a la variable suma_impar
    
    x += 1
print(f"the sum of all evens numbers of 0 to 100 is {suma_par}")        #impresion de los resultados
print(f"the sum of all odds numbers of 0 to 100 is {suma_impar}")