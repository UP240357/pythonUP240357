# Day 6 lvl 1 y 2 - Tuples
# Ruiz Clemente Jorge Alberto

""" 1
Create an empty tuple
"""
empty_tuple = ()

""" 2
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
"""
Names_M = ("Alex","Jorge",)
Names_F = ("Michelle","Diana")
print(f"{Names_M}\n{Names_F}")

""" 3
Join brothers and sisters tuples and assign it to siblings
"""
Names = Names_M+Names_F
print(Names)

""" 4
How many siblings do you have?
"""
brothers = ("Alex","Jorge")
print(brothers)

""" 5
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
"""
parents = ("Jorge","Norma")
print(parents)
familly = brothers+parents
print(familly)