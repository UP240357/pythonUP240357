# Day 4 lvl 1 - Strings  in Python
# Ruiz Clemente Jorge Alberto 

""" 1
Concatenate the string 'Thirty', 'Days', 'Of', 
'Python' to a single string, 'Thirty Days Of Python'.
"""
single_string = "Thirty "+"Days "+"Of "+"Python"
print(f"Thirty + Days + Of + Python ={single_string}")

""" 2
Concatenate the string 'Coding', 'For' , 'All' 
to a single string, 'Coding For All'.
"""
single_string_2 = "Coding "+"For "+"All"
print(f"\nCoding + For + All = {single_string_2}")

""" 3
Declare a variable named company and assign it 
to an initial value "Coding For All".
"""
company = "Coding For All"

""" 4
Print the variable company using print().
"""
print(f"\nVariable company = {company}")

""" 5
Print the length of the company string using 
len() method and print().
"""
print(f"\nlength of company = {len(company)}")

""" 6
Change all the characters to uppercase letters 
using upper() method.
"""
print(f"\nuppercase of company = {company.upper()}")  #hace todo mayusculas

""" 7
Change all the characters to lowercase letters 
using lower() method.
"""
print(f"\nlowercase of company = {company.lower()}")  #hace todo minusculas

""" 8
Use capitalize(), title(), swapcase() methods to 
format the value of the string Coding For All.
"""
print(f"\ncapitalize of company = {company.capitalize()}") #mayuscula a la primera palabra
print(f"\ntitle of company = {company.title()}")      #mayuscula cada palabra
print(f"\nswapcase of company = {company.swapcase()}")   #los extremos minusculas y lo de enmedio mayusculas

""" 9
Cut(slice) out the first word of Coding For All string.
"""
#separar las palabras y
#con [] seleccionamos la palabra a imprimir
print(f"\ncut out the first word of coding for all = {company.split()[0]}")

""" 10
Check if Coding For All string contains a word Coding 
using the method index, find or other methods.
"""
word_coding_position = company.find("Coding")
print(f"\nposition of Coding = {word_coding_position}")  #arroja la posicion en la que se encuentra la oración

""" 11
Replace the word coding in the string 'Coding For All' to Python.
"""
company_python = company.replace("Coding","Python")    #remplazamos una palabra
print(f"\nreplace the word coding for Python = {company_python}") #primero busca y luego cambia

""" 12
Change Python for Everyone to Python for All using the replace 
method or other methods.
"""
company_python = company_python.replace("All", "Everyone")
print(f"\nreplace the word all for veryone = {company_python}")

""" 13
Split the string 'Coding For All' using space 
as the separator (split()) .
"""
print(f"\nsplit coding for all = {company.split()}")

""" 14
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
split the string at the comma.
"""
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(f"\nVariable companies = {companies}")
companies_split = companies.split(", ")
print(f"\nVariable companies with comma = {companies_split}")

""" 15
What is the character at index 0 in the string Coding For All.
"""
print(f"\nthe first character of Coding For All is = {company[0]}")

""" 16
What is the last index of the string Coding For All.
"""
print(f"\nthe last character of Coding For All is  = {company[-1]}")

""" 17
What character is at index 10 in "Coding For All" string.
"""
print(f"\nthe 10th character of Coding For All is  = {company[-1]}")
print(company[10])

""" 18
Create an acronym or an abbreviation for the name 
'Python For Everyone'.
"""
company_python_split = company_python.split()

Primera = company_python_split[0][0]
Segunda = company_python_split[1][0]
Tercera = company_python_split[2][0]

print(f"the acronym of Python For Everyone is = {Primera+Segunda+Tercera}")

""" 19
reate an acronym or an abbreviation for the name 
'Coding For All'.
"""
company_split = company.split()

Primera = company_split[0][0]
Segunda = company_split[1][0]
Tercera = company_split[2][0]

print(f"\nthe acronym of Coding For All is = {Primera+Segunda+Tercera}")

""" 20
Use index to determine the position of the first 
occurrence of C in Coding For All.
"""
position_C = company.find("C")
print(f"\nfirst ocurrence of C in Coding For All = {position_C}")

""" 21
Use index to determine the position of the first 
occurrence of F in Coding For All.
"""
position_F = company.find("F")
print(f"\nfirst ocurrence of F in Coding For All = {position_F}")

""" 22
Use rfind to determine the position of the last 
occurrence of l in Coding For All People.
"""
single_string_3 = company+" People"
position_l = single_string_3.rfind("l")

print(f"\nlast occurrence of l in Coding For All People = {position_l}")

"""23
Use index or find to find the position of the first 
occurrence of the word 'because' in the following sentence: 
'You cannot end a sentence with because because because is a 
conjunction'
"""
single_string_4 = "You cannot end a sentence with because because because is a conjunction"
print(f"\noriginal text:\n{single_string_4}")
position_because = single_string_4.find("because")
print(f"\nfirst occurrence of because in the sentence = {position_because}")

""" 24
Use rindex to find the position of the last occurrence of 
the word because in the following sentence: 'You cannot end a 
sentence with because because because is a conjunction'
"""
position_because = single_string_4.rfind("because")
print(f"\nlast occurrence of because in the sentence = {position_because}")

""" 25
Slice out the phrase 'because because because' in the 
following sentence: 'You cannot end a sentence with because 
because because is a conjunction'
"""
print("\ntext whiuot because :")
print(single_string_4[:31]+single_string_4[55:])   #imprime desde hasta, (concatena), desde hasta
#dejarlos vacios significa [:31] = del inicio hasta 31 y [55:] = del 48 hasta el final

""" 26
Find the position of the first occurrence of the word 'because' 
in the following sentence: 'You cannot end a sentence with because 
because because is a conjunction'
"""
position_because = single_string_4.find("because")
print(f"\nfirst occurrence of because in the sentence = {position_because}")

""" 27
Slice out the phrase 'because because because' in the following 
sentence: 'You cannot end a sentence with because because because 
is a conjunction'
"""
print("\ntext whiuot because :")
print(single_string_4[:31]+single_string_4[55:])

""" 28
Does ''Coding For All' start with a substring Coding?
"""
question_1 = company.startswith("Coding")
print(f"\nDoes ''Coding For All' start with a substring Coding? R: {question_1}")

""" 29
Does 'Coding For All' end with a substring coding?
"""
question_2 = company.endswith("coding")
print(f"\nDoes ''Coding For All' end with a substring Coding? R: {question_2}")

""" 30
'   Coding For All      '  , remove the left and right 
trailing spaces in the given string.
"""
single_string_5 = '   Coding For All      '
print("\nleft and right trailing spaces of '   Coding For All      '")
print(single_string_5.strip())


""" 31
Which one of the following variables return True when we use the 
method isidentifier():
    30DaysOfPython
    thirty_days_of_python
"""
print("\n30DaysOfPython whit isidentifier is")
print("30DaysOfPython".isidentifier())
print("\nthirty_days_of_python with isidentifier is")
print("thirty_days_of_python".isidentifier())

""" 32
The following list contains the names of some of python libraries: 
['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list 
with a hash with space string.
"""
print("\nlist: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']")
print("\nJoin the list with a hash with space string")
print(" # ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

""" 33
Use the new line escape sequence to separate the following sentences.
    I am enjoying this challenge.
    I just wonder what is next.
"""
print("\nI am enjoying this challenge.\nI just wonder what is next.")

""" 34
Use a tab escape sequence to write the following lines.
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
"""
print("\nName     \tAge   \tCountry   \tCity")
print("Asabeneh \t250   \tFinland   \tHelsinki")

""" 35
Use the string formatting method to display the following:
    radius = 10
    area = 3.14 * radius ** 2
    The area of a circle with radius 10 is 314 meters square.
"""
radius = 10
area = 3.14 * radius ** 2
print(f"\nThe area of a circle with radius {radius} is {area} meters square.")

print("The area of a circle with radius {} is {} meters square.".format(radius, area))

""" 36
Make the following using string formatting methods:
    8 + 6 = 14
    8 - 6 = 2
    8 * 6 = 48
    8 / 6 = 1.33
    8 % 6 = 2
    8 // 6 = 1
    8 ** 6 = 262144
"""
a, b = 8, 6
print(f"\n{a} + {b} = {a+b}\n{a} - {b} = {a-b}\n{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}\n{a} % {b} = {a%b}\n{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")