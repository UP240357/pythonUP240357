# Day 3 lvl 1 - Operators in Python
# Ruiz Clemente Jorge Alberto

age = (20)
height = (1.70)

#area de un triangulo
print("Area de un triangulo")
BASE_Triangulo = float(input("dame la base :"))
ALTURA_Triang = float(input("dame el area :"))

area = 0.5*BASE_Triangulo*ALTURA_Triang
print(area)

#area de un triangulo
print("Perimetro de un triangulo")
side_a = float(input("dame el lado a :"))
side_b = float(input("dame el lado b :"))
side_c = float(input("dame el lado c :"))

perimetro = side_a+side_b+side_c
print("el perimetro es ",perimetro)

#area y perimetro de un rectangulo
print("Area y Perimetro de un rectangulo")
Ancho_rectangulo = float(input("Dame el ancho :"))
Alto_rectangulo = float(input("Dame el alto :"))

Area_rectangulo = Ancho_rectangulo*Alto_rectangulo
Perimetro_rectangulo = 2*(Ancho_rectangulo+Alto_rectangulo)
print("el area es :",int(Area_rectangulo),"y el perimetro es:",int(Perimetro_rectangulo))