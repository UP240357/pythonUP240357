#level 02
""" 1
Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F"""
score = int(input("Enter your score: "))

if 80 <= score <= 100:      # ncantidad <= varible <= ncantidad --- esto es un rango, y vemos si el valor que tiene esta en ese rango
    print("Grade: A")  
elif 70 <= score < 80:
    print("Grade: B")
elif 60 <= score < 70:
    print("Grade: C")
elif 50 <= score < 60:
    print("Grade: D")
elif 0 <= score < 50:
    print("Grade: F")

""" 2
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
"""
month = input("Enter the name of a month: ")

if month in ["September", "October", "November"]:   #usamos "in" que ya lo habiamos visto, y nos ayuda a ver si el valor de una variable esta en una lista
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:  #las listas contienen los meses de cada estacion
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("That is not a valid month.")             #si se escribe algo que no sea un mes, se imprime este mensaje

""" 3
The following list contains some fruits:

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
If the fruit exists print('That fruit already exist in the list')"""
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ")

if fruit not in fruits:
    print(fruit, "is not in the list")      #mensaje de que la fruta no esta en la lista
    print("Adding fruit to the list")       #mensaje que se agregara la fruta a la lista
    fruits.append(fruit)                    #comando para agregar la fruta
    print("Modified list:", fruits)         #imprime la lista modificada
else:
    print("That fruit already exist in the list")

