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
company_python = company.replace("Coding","Python")    #remplazamos una palabra
print(company_python)                                  #primero busca y luego cambia

""" 12
Change Python for Everyone to Python for All using the replace 
method or other methods.
"""
print(company_python.replace("All", "Everyone"))

""" 13
Split the string 'Coding For All' using space 
as the separator (split()) .
"""
print(company.split())

""" 14
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
split the string at the comma.
"""
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))

""" 15
What is the character at index 0 in the string Coding For All.
"""
print(company[0])

""" 16
What is the last index of the string Coding For All.
"""
last_leter_company = len(company)-1
print(company[last_leter_company])

print(company[-1])  #otra forma de encontrar la ultima letra

""" 17
What character is at index 10 in "Coding For All" string.
"""
print(company[10])

""" 18
Create an acronym or an abbreviation for the name 
'Python For Everyone'.
"""
