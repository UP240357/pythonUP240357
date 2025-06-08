# Day 3 lvl 1 - Operators in Python
# Ruiz Clemente Jorge Alberto

age = (20)
height = (1.70)

#area de un triangulo
print("Area de un triangulo")
BASE_Triangulo = float(input("dame la base del triangulo:"))
ALTURA_Triang = float(input("dame el area del triangulo:"))

Area_triangulo = 0.5*BASE_Triangulo*ALTURA_Triang
print("el area es:",Area_triangulo)

#perimetro de un triangulo
print("Perimetro de un triangulo")
side_a = float(input("dame el lado a del triangulo:"))
side_b = float(input("dame el lado b del triangulo:"))
side_c = float(input("dame el lado c del triangulo:"))

Perimetro_triangulo = side_a+side_b+side_c
print("el perimetro es ",Perimetro_triangulo)

#area y perimetro de un rectangulo
print("Area y Perimetro de un rectangulo")
Ancho_rectangulo = float(input("Dame el ancho del rectangulo:"))
Alto_rectangulo = float(input("Dame el alto  del rectangulo:"))

Area_rectangulo = Ancho_rectangulo*Alto_rectangulo
Perimetro_rectangulo = 2*(Ancho_rectangulo+Alto_rectangulo)
print("el area es :",Area_rectangulo,"y el perimetro es:",Perimetro_rectangulo)

#area y circunferencia de un circulo
Radio_circulo = float(input("Dame el radio del circulo :"))

Area_circulo = 3.14*(Radio_circulo**2)
circunferencia_circulo = 2*3.14*Radio_circulo

print("el area del ciruclo es:",Area_circulo,"y su circunferencia es:",circunferencia_circulo)

#Intersecciones de X y Y en y = 2x - 2
print("Intersecciones de X y Y")
    #datos de la formula mx + b
m_1 = 2
b = -2

    # Calculo de la interseccion en X (y = 0)
interseccion_X = -b/m_1

print("La pendiente es:",m_1)
print("se interseca y en (0,",b")")
print("se intersecta x en (",interseccion_X,",0)")

#encontrar pendiente y distancia eucladiana
print("Pendiente")
x1,y1 = 2, 2
x2,y2 = 6,10
m_2 = (y2-y1)/(x2-x1)
dist_eucladiana = ((x2-x1)**2+(y2-y1)**2)**0.5

print("La pendiente es:",m_2)
print("La distancia eucladiana es:",dist_eucladiana)

#comparacion de pendientes
if m_1==m_2:
    print("Son iguales")
elif m_1>m_2:
    print("La primer pendiente es mas grande")
else:
    print("La segunda pendientes es mas grande")

#calcular el valor de y en (y= x^2 + 6x + 9)
print("Encontrar el valor de y en una ecuacion")
x_Valor_dado = float(input("Dame el valor de x:"))
y_ecuacion1 = x_Valor_dado**2 + 6*x_Valor_dado + 9
print("El valor de y cuando x vale",x_Valor_dado, "es:",y_ecuacion1)

#longitud y comparacion falsa de "python" y "dragon"
print("longitud y comparacion falsa de python y dragon")
print("Longitud de python :",len("python"))
print("Longitud de gragon :",len("dragon"))
comparacion_falsa = len("python") > len("dragon")
print("comparacion:")
print("¿son diferentes?",comparacion_falsa)

#busqueda de la palbra "on" en las dos palabras
print("busqueda de la palbra on en las dos palabras")
busqueda_on = ("on" in "python")and("on" in "dragon")
print("Se encuentra on en ambas palabras?",busqueda_on)

#buscar "jargon" en una sentencia
print("buscar jargon en una sentencia")
busqueda_jargon = ("jargon" in "I hope this course is not full of jargon")
print("Se encuentra la palabra jargon en la sentencia?",busqueda_jargon)

#busqueda de la palbra "on" no debe estar en las dos palabras
print("busqueda de la palbra on no debe estar en las dos palabras")
busqueda_on_not = ("on" not in "python")and("on" not in "dragon")
print("No se encuentra on en ambas palabras?",busqueda_on_not)

#longitud de la palabra python y hacerla string
print("longitud de la palabra python y hacerla string")
longitu_python = len("python")
longitu_python_float = float(longitu_python)
longitu_python_string = str(longitu_python)

print("el ancho de python es:",longitu_python)
print("en float:",longitu_python_float)
print("en string:",longitu_python_string)

#modulo de 2
print("Modulo de 2")
Valor_evaluable = float(input("Dame el valor a evaluar:"))
if (Valor_evaluable % 2) == 0:
    print(Valor_evaluable,"es par")
else:
    print(Valor_evaluable,"es impar")

#floor division 7/3 igual a int 2.7
print("floor division 7/3 igual a int 2.7")
floor_division = 7//3
Valor = int(2.7)

print("¿Son iguales?",floor_division==Valor)

#comparacion de tipos de datos "10" y 10
print("comparacion de tipos de datos 10 y 10")
print("son iguales?",type("10")==type(10))

#comparacion de int(9.8) y 10
print("comparacion de int(9.8) y 10")
print("son iguales?",int(float("9.8"))==10) #primero se hace float por que int no le acepta de una vez los valores con punto decimal,
                                            #ya despues podemos usar int para el redondeo

#calcula el pago por horas de una persona
print("calcula el pago por horas de una persona")
Horas_trabajadas = float(input("¿Cuantas horas trabajo esta semana?:"))
Pago_horas = float(input("¿Cuanto le pagan por hora?:"))

Pago_Total = Horas_trabajadas*Pago_horas
print("su pago den la semana sera de: $",Pago_Total)

#segundos que ha vivido una persona basada en los años introducidos
print("calculo de los segundos que ha vivido una persona basada en los años introducidos")
años_vividos = int(input("¿Cuanto años ha vivido?"))
segundos_vividos = años_vividos*31536000

print("usted ha vivido:",segundos_vividos,"segundos")

#tabla dada por la instruccion
print("tabla dada por la instruccion")
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)

