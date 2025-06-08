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
