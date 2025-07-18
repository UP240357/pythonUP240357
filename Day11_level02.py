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
They should calculate_mean, calculate_median, 
calculate_mode, calculate_range, calculate_variance, 
calculate_std (standard deviation)."""
def calculate_mean(list):
    total = 0
    for number in list:
        total += number
    mean = total/(len(list))
    return mean

def calculate_median(list):
    sorted_list = sorted(list)
    n = len(sorted_list)
    if n % 2 == 1:
        median = sorted_list[n//2]
    else:
        mid1 = sorted_list[n//2-1]
        mid2 = sorted_list[n//2]
        median = (mid1+mid2)/2
    return median

def calculate_mode(list):
    counts = {}
    if not list:
        return "Error: La lista no puede estar vacía para calcular la moda."
    for item in list:
        counts[item] = counts.get(item,0)+1
    max_count = 0
    if counts:
        max_count = max(counts.values())
    modes = []
    for item, count in counts.items():
        if count == max_count:
            modes.append(item)
    if max_count == 1 and len(modes) == len(list):
        return "Fashion doesn't exist"
    return modes

def calculate_range(list):
    min_val = list[0]
    max_val = list[0]
    for number in list:
        if number < min_val:
            min_val = number
        if number > max_val:
            max_val = number
    range_val = max_val - min_val
    return range_val

def calculate_variance(list):
    mean_val = calculate_mean(list)
    if isinstance(mean_val, str):
        return mean_val
    squared_dif_sum = 0
    for number in list:
        squared_dif_sum += (number - mean_val)**2
    variance = squared_dif_sum/(len(list))
    return variance

def calculate_std(list):
    variance = calculate_variance(list)
    if isinstance(variance,str):
        return variance
    std_dev = variance**0.5
    return std_dev

print(f"\nmean of [1,2,3,4,5] is {calculate_mean([1,2,3,4,5])}")

print(f"\nmedian of [1,5,2,4,3] is {calculate_median([1,5,2,4,3])}")

print(f"\nmode of [1,5,2,4,3,5,5,6] is {calculate_mode([1,5,2,4,3,5,5,6])}")

print(f"\nrenge of [1,5,2,4,3] is {calculate_range([1,5,2,4,3])}")

print(f"\nvariance of [1,2,3,4,5] is {calculate_variance([1,2,3,4,5])}")

print(f"\nstd of [1,2,3,4,5] is {calculate_std([1,2,3,4,5])}")