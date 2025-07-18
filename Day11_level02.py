# level 03

""" 1
Declare a function named evens_and_odds. 
It takes a positive integer as parameter and it counts number of evens and odds in the number.
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51."""
print()
def evens_and_odds(n):
    total_evens = 0
    total_odds = 0
    for i in range(n):
        if n % 2 == 0:
            total_evens += 1
        else:
            total_odds += 1
        n -= 1
    return f"total of evens: {total_evens}\ntotal of odds: {total_odds}"

print(evens_and_odds(1))

""" 1
Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number"""
print()
def factorial(n):
    i = 1
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

print(factorial(5))

""" 2
Call your function is_empty, it takes a parameter and it checks if it is empty or not"""
print()
def is_empty(param):
    if param:
        return False
    else:
        return True

print(is_empty([]))

""" 3
Write different functions which take lists. 
They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation)."""
print()
def calculate_mean(list):
    total = 0
    for number in list:
        total += number
    mean = total/(len(list))
    return mean

#def calculate_median(list):
