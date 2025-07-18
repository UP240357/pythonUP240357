# Day 11 - Modules
# Ruiz Clemente Jorge Alberto

#level 01

""" 1
Writ a function which generates a six digit/character random_user_id.
  print(random_user_id());
  '1ee33d'"""
import random
def random_user_id():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    user_id = ''.join(random.choice(characters) for i in range(6))
    return user_id

print(f"\n{random_user_id()}")

""" 2
Modify the previous task. 
Declare a function named user_id_gen_by_user. 
It doesn’t take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr"""
import random

def user_id_gen_by_user():
    try:
        num_characters = int(input("\nEnter the number of characters per ID: "))
        num_ids_to_generate = int(input("Enter the number of IDs to generate: "))
    except ValueError:
        print("\nInvalid input. Please enter whole numbers.")
        return
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for _ in range(num_ids_to_generate):
        user_id = "".join(random.choice(characters) for i in range(num_characters))
        print(user_id)

user_id_gen_by_user()


""" 3
Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form"""
def rgb_color_gen():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    rgb_string = f"\nrgb({red},{green},{blue})"
    return rgb_string

print(rgb_color_gen())