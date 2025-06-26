"""base = 20
altura = 10
# Tu código aquí
area = (base*altura)/2
print(area)

nombre = "Carlos"
apellido = "Ramirez"
# Tu código aquí
nombre_completo = nombre+" "+apellido
print(nombre_completo)

# Tu código aquí
ask_python = "on" in "python"
print(ask_python)
ask_dragon = "on" in "dragon"
print(ask_dragon)

texto = "Coding For All"
nombre = "Carlos"
# Tu código aquí
print(texto.replace("Coding",nombre))

num = 10
# Tu código aquí
num_flot = float(num)
print(num_flot)
num_strg = str(num)
print(num_strg)

a = 2
b = 3
c = 5
d = 7
e = 11
# Tu código aquí
suma = sum([a,b,c,d,e])
producto = a*b*c*d*e
cantidad = len([a,b,c,d,e])
print(f"{suma} {producto} {cantidad}")

texto = "Thirty Days Of Python"
# Tu código aquí
print(texto.split())

cadena = "I hope this course is not full of jargon"
# Tu código aquí
print(len(cadena))

n = 4
# Tu código aquí
prueba = (n%2==0 and n%2==0)
print(bool(prueba))

peso = 70  # en kilogramos
altura = 1.75  # en metros
# Tu código aquí
Imc = peso / (altura * altura)
print(round(Imc))"""


# examen.py
# Examen basado en los Días 1 al 4 del repositorio 30 Days of Python
# Las entradas están definidas directamente en el código.
# IMPORTANTE:
# 1. Debes usar la función print() para mostrar la salida de cada ejercicio.
# 2. No modifiques ni elimines las condiciones que seleccionan el problema.
# 3. Escribe tu código exactamente debajo del comentario '# Tu código aquí',
#    con la misma tabulación que se muestra en el ejemplo.
# 4. No uses estructuras que aún no se han visto en clase.

problema = int(input("Número del problema (1-10): "))

if problema == 1:
    # Problema 1: Calcular el área de un triángulo de base 20 y altura 10.
    base = 20
    altura = 10
    # Tu código aquí
    area = (base*altura)/2
    print(area)

elif problema == 2:
    # Problema 2: Concatena el nombre y apellido y muéstralo en una sola línea
    # con un espacio entre nombre y apellido.
    nombre = "Carlos"
    apellido = "Ramirez"
    # Tu código aquí
    nombre_completo = nombre+" "+apellido
    print(nombre_completo)


elif problema == 3:
    # Problema 3: Verifica si 'on' está en 'python' y en 'dragon'.
    # Tu código aquí
    ask_python = "on" in "python"
    print(ask_python)
    ask_dragon = "on" in "dragon"
    print(ask_dragon)

elif problema == 4:
    # Problema 4: Reemplaza 'Coding' por el nombre dado en el string.
    texto = "Coding For All"
    nombre = "Carlos"
    # Tu código aquí
    print(texto.replace("Coding",nombre))

elif problema == 5:
    # Problema 5: Convertir el entero 10 a float y string.
    num = 10
    # Tu código aquí
    num_flot = float(num)
    print(num_flot)
    num_strg = str(num)
    print(num_strg)

elif problema == 6:
    # Problema 6: Suma, producto y cantidad de cinco números conocidos,
    # el resultado en una sola línea separados por un espacio.
    a = 2
    b = 3
    c = 5
    d = 7
    e = 11
    # Tu código aquí
    suma = sum([a,b,c,d,e])
    producto = a*b*c*d*e
    cantidad = len([a,b,c,d,e])
    print(f"{suma} {producto} {cantidad}")

elif problema == 7:
    # Problema 7: Divide el string en una lista de palabras.
    texto = "Thirty Days Of Python"
    # Tu código aquí
    print(texto.split())

elif problema == 8:
    # Problema 8: Calcula la longitud de la cadena dada.
    cadena = "I hope this course is not full of jargon"
    # Tu código aquí
    print(len(cadena))

elif problema == 9:
    # Problema 9: Determina si un número es par usando %.
    n = 4
    # Tu código aquí
    prueba = (n%2==0 and n%2==0)
    print(prueba)

elif problema == 10:
    # Problema 10: Calcula el Índice de Masa Corporal (IMC).
    # Fórmula: IMC = peso / (altura * altura)
    peso = 70  # en kilogramos
    altura = 1.75  # en metros
    # Tu código aquí
    Imc = peso / (altura * altura)
    print(round(Imc))

else:
    print("Por favor, ingresa un número entre 1 y 10 para seleccionar un ejercicio.")