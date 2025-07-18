#level 02

""" 1
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. 
Check the task 6 for output examples)."""
import random

print()
def list_of_hexa_colors(n_colors = 1):
    hex_characters = "0123456789abcdef"
    generated_colors = []
    for _ in range(n_colors):
        hex_code = "#"
        for _ in range(6):
            hex_code += random.choice(hex_characters)
        generated_colors.append(hex_code)
    return generated_colors

print(list_of_hexa_colors())

""" 2
Write a function list_of_rgb_colors which returns any number of RGB colors in an array."""
print()
def list_of_rgb_colors(n_colors = 1):
    generated_colors = []
    for _ in range(n_colors):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        rgb_stri = f"rgb({red},{green},{blue})"
        generated_colors.append(rgb_stri)
    return generated_colors

print(list_of_rgb_colors())


""" 3
Write a function generate_colors which can generate any number of hexa or rgb colors.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']"""
def generate_colors(color_type, n_colors):
    generated_list = []
    if color_type == "hexa":
        for _ in range(n_colors):
            generated_list.append(list_of_hexa_colors())
    elif color_type == "rgb":
        for _ in range(n_colors):
            generated_list.append(list_of_rgb_colors())
    return generated_list

print()
print(generate_colors("hexa",2))

