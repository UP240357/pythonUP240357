
#lvl 2

print(f"A: {A}")
print(f"B: {B}")

""" 1
Join A and B
"""
Join = A.union(B)
print(Join)

""" 2
Find A intersection B
"""
print(A.intersection(B))

""" 3
Is A subset of B
"""
print(A.issubset(B))

""" 4
Are A and B disjoint sets
"""
print(A.isdisjoint(B))

""" 5
Join A with B and B with A
"""
A.update(B)
B.update(A)

print(f"A: {A}")
print(f"B: {B}")

""" 6
What is the symmetric difference between A and B
"""
print(A.symmetric_difference(B))

""" 7
Delete the sets completely
"""
del A
del B

print("---------------------------------------------------------------------------------------------------------------------")
