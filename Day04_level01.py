# Day 4 lvl 1 - Strings  in Python
# Ruiz Clemente Jorge Alberto 

""" 1
Concatenate the string 'Thirty', 'Days', 'Of', 
'Python' to a single string, 'Thirty Days Of Python'.
"""
single_string = "Thirty "+"Days "+"Of "+"Python"
print(single_string)

""" 2
Concatenate the string 'Coding', 'For' , 'All' 
to a single string, 'Coding For All'.
"""
single_string_2 = "Coding "+"For "+"All"
print(single_string_2)

""" 3
Declare a variable named company and assign it 
to an initial value "Coding For All".
"""
company = "Coding For All"

""" 4
Print the variable company using print().
"""
print(company)

""" 5
Print the length of the company string using 
len() method and print().
"""
print(len(company))

""" 6
Change all the characters to uppercase letters 
using upper() method.
"""
print(company.upper())  #hace todo mayusculas

""" 7
Change all the characters to lowercase letters 
using lower() method.
"""
print(company.lower())  #hace todo minusculas

""" 8
Use capitalize(), title(), swapcase() methods to 
format the value of the string Coding For All.
"""
print(company.capitalize()) #mayuscula a la primera palabra
print(company.title())      #mayuscula cada palabra
print(company.swapcase())   #los extremos minusculas y lo de enmedio mayusculas

""" 9
Cut(slice) out the first word of Coding For All string.
"""
print(company.split()[0])   #separar las palabras y
                            #con [] seleccionamos la palabra a imprimir

""" 10
Check if Coding For All string contains a word Coding 
using the method index, find or other methods.
"""
print(company.index("Coding"))  #arroja la posicion en la que se encuentra la oración

""" 11
Replace the word coding in the string 'Coding For All' to Python.
"""
company_python = company.replace("Python", "coding")    #remplazamos una palabra
print(company_python)                                   #primero el cambio y luego la que cambia

""" 12
Change Python for Everyone to Python for All using the replace 
method or other methods.
"""
print(company_python.replace("All", "Everyone"))