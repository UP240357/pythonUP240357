#level 03

""" 1
Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list"""
import random

def shuffle_list(list):
    shuffled_copy = list[:]
    random.shuffle(shuffled_copy)
    return shuffled_copy

print()
print(shuffle_list([1,2,3,4,5]))

""" 2
Write a function which returns an array of seven random numbers in a range of 0-9. 
All the numbers must be unique."""
print()
def generate_unique_seven_numbers():
    population = list(range(10))
    unique_nums = random.sample(population, 7)
    return unique_nums

print(generate_unique_seven_numbers())